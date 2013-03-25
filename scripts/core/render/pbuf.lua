local M = {}

local cfg = require 'config'
local util = require 'core.util'

local shelves = {}

function M.sizes()
    local t = {}
    local size = math.max(unpack(util.keys(cfg.TEX_POOL)))
    while size > 0 do
        for i = 1, cfg.COPIES do
            table.insert(t, size * size)
        end
        size = math.floor(size / 2)
    end
    return unpack(t)
end

local function make_shelf(size)
    local self = {}
    self.size = size
    self.allocs = 0
    self.frees = 0
    self.left = 0
    self.left_min = 0
    self.count = 0
    self.chunks = {}
    return self
end

local function make_base_pbuf(size, id)
    local self = {}
    local side = math.sqrt(shelf.size)
    function self.set(x, y, ...)
        api_pbuf_set(id, x + y*side, ...)
    end
    function self.id()
        return id
    end
    function self.side()
        return side
    end
    function self.store()
        return string.format("{%i, %i}", size, id)
    end
    return self
end

local function make_pbuf(shelf, id)
    local self = make_base_pbuf(shelf.size, id)
    function self.alloc()
        shelf.allocs = shelf.allocs + 1
        shelf.left = shelf.left - 1
        shelf.left_min = math.min(shelf.left, shelf.left_min)
        shelf.chunks[id] = nil
    end
    function self.free()
        shelf.frees = shelf.frees + 1
        shelf.left = shelf.left + 1
        shelf.chunks[id] = self
    end
    return self
end

function M.restore(state)
    local size, id = unpack(state)
    return make_base_pbuf(size, id)
end

function M.init()
    for id, size in ipairs({M.sizes()}) do
        if shelves[size] == nil then
            shelves[size] = make_shelf(size)
        end
        local shelf = shelves[size]
        shelf.chunks[id] = make_pbuf(shelf, id)
        shelf.count = shelf.count + 1
        shelf.left = shelf.left + 1
        shelf.left_min = shelf.left_min + 1
    end
end

function M.done()
    for _, s in ipairs(util.sorted(util.keys(shelves))) do
        local shelf = shelves[s]
        io.write(string.format('Pixel buffers pool %i chunks usage: %i/%i, allocs/frees: %i/%i\n',
            s, shelf.count - shelf.left_min, shelf.count, shelf.allocs, shelf.frees))
    end
end

function M.alloc(size)
    local shelf = shelves[size]
    assert(shelf ~= nil)
    assert(shelf.left > 0)
    for k, v in pairs(shelf.chunks) do
        v.alloc()
        return v
    end
end

return M
