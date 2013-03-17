local M = {}

function M.alloc(title, res_size, res_start, res_count, pool_dims,
                 res_set, res_map, res_unmap, res_copy, res_waiting)
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
        local chunk = {}
        local shelf = shelves[size]
        chunk.size = 0
        chunk.start = start
        chunk.res = r
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
        function chunk.map()
            res_map(chunk.res, chunk.start, chunk.size)
            while res_waiting(chunk.res) do
                coroutine.yield(true)
            end
        end
        function chunk.unmap()
            res_unmap(chunk.res)
            while res_waiting(chunk.res) do
                coroutine.yield(true)
            end
        end
        function chunk.copy(chunk_to)
            res_copy(chunk.res, chunk_to.res, chunk.start, chunk_to.start, chunk_to.size)
            while res_waiting(chunk.res) do
                coroutine.yield(true)
            end
        end
        function chunk.set(i, ...)
            res_set(chunk.res, chunk.start + i, ...)
        end
        return chunk
    end

    function self.free()
        local sizes = {}
        for s in pairs(shelves) do table.insert(sizes, s) end
        table.sort(sizes)
        io.write(string.format('%s largest requested chunk: %i\n', title, largest_size))
        for si, s in ipairs(sizes) do
            local shelf = shelves[s]
            io.write(string.format('%s pool %i chunks usage: %i/%i, allocs/frees: %i/%i\n',
                title, s, shelf.count - shelf.left_min, shelf.count, shelf.allocs, shelf.frees))
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
