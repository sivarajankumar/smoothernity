local M = {}

local cfg = require 'config'

local meshes = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_mesh(mi)
    local self = {}
    function self.alloc(...)
        api_mesh_alloc(mi, ...)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        api_mesh_free(mi)
    end
    function self.group(g)
        api_mesh_group(mi, g)
    end
    function self.id()
        return mi
    end
    return self
end

function M.init()
    for mi = 0, cfg.MESH_COUNT - 1 do
        meshes[mi] = make_mesh(mi)
    end
    left = cfg.MESH_COUNT
    left_min = cfg.MESH_COUNT
end

function M.done()
    io.write(string.format('Meshes usage: %i/%i, allocs/frees: %i/%i\n',
                           cfg.MESH_COUNT - left_min, cfg.MESH_COUNT,
                           allocs, frees))
end

function M.alloc(group, kind, vbuf, ibuf, shprog, matrix, ioffset, icount)
    if left == 0 then
        error('out of meshes')
    end
    for mi, m in pairs(meshes) do
        meshes[mi] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        m.alloc(group, kind, vbuf, ibuf, shprog, matrix, ioffset, icount)
        return m
    end
end

return M
