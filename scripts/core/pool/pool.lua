local log = require 'core.log'

local M = {}

local function make_base_chunk(size, start, res)
    local self = {}
    self.size = size
    self.start = start
    self.res = res
    function self.store()
        return string.format("{%i, %i, %i}", size, start, res)
    end
    return self
end

function M.restore_chunk(state)
    local size, start, res = unpack(state)
    return make_base_chunk(size, start, res)
end

function M.size(pool_dims)
    local size = 0
    for k, v in pairs(pool_dims) do
        size = size + k * v
    end
    return size
end

function M.alloc(title, res_size, res_start, res_count, pool_dims)
    local self = {}
    local shelves = {}
    local res = {}
    local largest_size = 0

    local function find_shelf(size)
        local min_size
        for s in pairs(shelves) do
            if s >= size then
                if min_size == nil or s < min_size then
                    min_size = s
                end
            end
        end
        if min_size == nil then
            error(string.format('No shelf for size %i.\n', size))
        end
        return shelves[min_size]
    end

    local function ensure_shelf(size)
        local shelf
        if shelves[size] == nil then
            shelf = {}
            shelf.size = size
            shelf.count = 0
            shelf.left = 0
            shelf.left_min = 0
            shelf.allocs = 0
            shelf.frees = 0
            shelf.chunks = {}
            shelves[size] = shelf
        else
            shelf = shelves[size]
        end
        return shelf
    end

    local function make_chunk(size, start, r)
        local chunk = make_base_chunk(size, start, r)
        local shelf = shelves[size]
        chunk.id = shelf.left
        function chunk.free()
            if shelf.chunks[chunk.id] ~= nil then
                error(string.format('Chunk with id %i already exists in shelf %i.\n',
                                    chunk.id, shelf.size))
            end
            chunk.size = 0
            shelf.frees = shelf.frees + 1
            shelf.left = shelf.left + 1
            shelf.chunks[chunk.id] = chunk
        end
        return chunk
    end

    function self.free()
        local sizes = {}
        for s in pairs(shelves) do table.insert(sizes, s) end
        table.sort(sizes)
        log.info('%s largest requested chunk: %i', title, largest_size)
        for si, s in ipairs(sizes) do
            local shelf = shelves[s]
            log.info('%s pool %i chunks usage: %i/%i, allocs/frees: %i/%i',
                     title, s, shelf.count - shelf.left_min, shelf.count,
                     shelf.allocs, shelf.frees)
            if shelf.allocs ~= shelf.frees then
                error('Allocs/frees mismatch')
            end
        end
    end

    function self.left(size)
        return find_shelf(size).left
    end

    function self.alloc(size)
        local shelf = find_shelf(size)
        if shelf.left == 0 then
            error(string.format('Out of chunks in shelf %i.\n', shelf.size))
        end
        if size > largest_size then
            largest_size = size
        end
        shelf.allocs = shelf.allocs + 1
        shelf.left = shelf.left - 1
        if shelf.left < shelf.left_min then
            shelf.left_min = shelf.left
        end
        for i, chunk in pairs(shelf.chunks) do
            shelf.chunks[i] = nil
            chunk.size = size
            return chunk
        end
    end

    do
        local left = {}
        local sizes = {}
        for s, c in pairs(pool_dims) do left[s] = c end
        for s in pairs(pool_dims) do table.insert(sizes, s) end
        table.sort(sizes, function(x, y) return x > y end)
        for ri = 0, res_count - 1 do
            res[ri] = ri + res_start
            local start = 0
            for si, size in ipairs(sizes) do
                while start + size <= res_size and left[size] > 0 do
                    local shelf = ensure_shelf(size)
                    local chunk = make_chunk(size, start, res[ri])
                    shelf.chunks[chunk.id] = chunk
                    shelf.count = shelf.count + 1
                    shelf.left = shelf.left + 1
                    shelf.left_min = shelf.left
                    left[size] = left[size] - 1
                    start = start + size
                end
            end
            if start ~= res_size then
                error(string.format('Invalid pool size: %i.\n', start))
            end
        end
    end

    return self
end

return M
