local M = {}

local cfg = require 'config'

local shunis = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_shuni(si)
    local self = {}
    function self.alloc_vector(shprog, mesh, name, vec)
        api_shuni_alloc_vector(si, shprog.id(), mesh.id(), name, vec.id())
    end
    function self.alloc_int(shprog, mesh, name, int)
        api_shuni_alloc_int(si, shprog.id(), mesh.id(), name, int)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        shunis[si] = self
        api_shuni_free(si)
    end
    function self.id()
        return si
    end
    return self
end

function M.init()
    for si = 0, cfg.SHUNI_COUNT - 1 do
        shunis[si] = make_shuni(si)
    end
    left = cfg.SHUNI_COUNT
    left_min = cfg.SHUNI_COUNT
end

function M.done()
    io.write(string.format('Shader uniforms usage: %i/%i, allocs/frees: %i/%i\n',
                           cfg.SHUNI_COUNT - left_min, cfg.SHUNI_COUNT,
                           allocs, frees))
end

local function alloc()
    if left == 0 then
        error('out of shunis')
    end
    for si, s in pairs(shunis) do
        shunis[si] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        return s
    end
end

function M.alloc_vector(shprog, mesh, name, vec)
    local s = alloc()
    s.alloc_vector(shprog, mesh, name, vec)
    return s
end

function M.alloc_int(shprog, mesh, name, int)
    local s = alloc()
    s.alloc_int(shprog, mesh, name, int)
    return s
end

return M
