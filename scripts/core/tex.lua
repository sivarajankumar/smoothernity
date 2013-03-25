local M = {}

local cfg = require 'config'
local util = require 'core.util'

local shelves = {}

local function make_shelf(size)
    local self = {}
    self.count = 0
    self.left = 0
    self.left_min = 0
    self.allocs = 0
    self.frees = 0
    self.size = size
    self.chunks = {}
    return self
end

local function make_tex(shelf, id, unit, layer)
    local self = {}
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
    function self.size()
        return shelf.size
    end
    function self.unit()
        return unit
    end
    function self.layer()
        return layer
    end
    return self
end

function M.sizes_layers()
    local t = {}
    for _, s in ipairs(util.sorted(util.keys(cfg.TEX_POOL))) do
        table.insert(t, s)
        table.insert(t, cfg.TEX_POOL[s])
    end
    return unpack(t)
end

function M.init()
    local id = 0
    for k, size in ipairs(util.sorted(util.keys(cfg.TEX_POOL))) do
        local layers = cfg.TEX_POOL[size]
        local unit = k - 1
        if shelves[size] == nil then
            shelves[size] = make_shelf(size)
        end
        local shelf = shelves[size]
        for layer = 0, layers - 1 do
            id = id + 1
            shelf.chunks[id] = make_tex(shelf, id, unit, layer)
            shelf.count = shelf.count + 1
            shelf.left = shelf.left + 1
            shelf.left_min = shelf.left_min + 1
        end
    end
end

function M.done()
    for _, s in ipairs(util.sorted(util.keys(cfg.TEX_POOL))) do
        local shelf = shelves[s]
        io.write(string.format('Textures pool %i chunks usage: %i/%i, allocs/frees: %i/%i\n',
            s, shelf.count - shelf.left_min, shelf.count, shelf.allocs, shelf.frees))
    end
end

function M.alloc(size)
    local shelf = shelves[size]
    assert(shelf ~= nil)
    assert(shelf.left > 0)
    for k, v in pairs(shelf.chunks) do
        shelf.chunks[k] = nil
        v.alloc()
        return v
    end
end

return M
