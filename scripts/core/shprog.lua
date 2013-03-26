local M = {}

local cfg = require 'config'

local shprogs = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_shprog(si)
    local self = {}
    function self.alloc()
        api_shprog_alloc(si)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        shprogs[si] = self
        api_shprog_free(si)
    end
    function self.attach_frag(data)
        api_shprog_attach(si, API_SHPROG_FRAGMENT, data)
    end
    function self.attach_vertex(data)
        api_shprog_attach(si, API_SHPROG_VERTEX, data)
    end
    function self.link()
        api_shprog_link(si)
    end
    function self.id()
        return si
    end
    return self
end

function M.init()
    for si = 0, cfg.SHPROG_COUNT - 1 do
        shprogs[si] = make_shprog(si)
    end
    left = cfg.SHPROG_COUNT
    left_min = cfg.SHPROG_COUNT
end

function M.done()
    io.write(string.format('Shader programs usage: %i/%i, allocs/frees: %i/%i\n',
                           cfg.SHPROG_COUNT - left_min, cfg.SHPROG_COUNT,
                           allocs, frees))
end

function M.alloc()
    if left == 0 then
        error('out of shprogs')
    end
    for si, s in pairs(shprogs) do
        shprogs[si] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        s.alloc()
        return s
    end
end

return M
