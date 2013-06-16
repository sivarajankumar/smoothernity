local M = {}

local cfg = require 'config'
local log = require 'core.log'

local colshapes = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_colshape(csi)
    local self = {}
    function self.alloc()
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        colshapes[csi] = self
        api_physics_cs_free(csi)
    end
    function self.alloc_box(size)
        api_physics_cs_alloc_box(csi, size.id())
    end
    function self.alloc_sphere(r)
        api_physics_cs_alloc_sphere(csi, r)
    end
    function self.alloc_hmap(buf, width, length, hmin, hmax, scale)
        api_physics_cs_alloc_hmap(csi, buf.start, width, length, hmin, hmax, scale.id())
    end
    function self.alloc_comp()
        api_physics_cs_alloc_comp(csi)
    end
    function self.comp_add(tm, child)
        api_physics_cs_comp_add(csi, tm.id(), child.id())
    end
    function self.id()
        return csi
    end
    return self
end

function M.init()
    for csi = 0, cfg.COLSHAPE_COUNT - 1 do
        colshapes[csi] = make_colshape(csi)
    end
    left = cfg.COLSHAPE_COUNT
    left_min = cfg.COLSHAPE_COUNT
end

function M.done()
    log.info('Collision shapes usage: %i/%i, allocs/frees: %i/%i',
             cfg.COLSHAPE_COUNT - left_min, cfg.COLSHAPE_COUNT,
             allocs, frees)
    if allocs ~= frees then
        error('Allocs/frees mismatch')
    end
end

local function alloc()
    if left == 0 then
        error('out of colshapes')
    end
    for csi, cs in pairs(colshapes) do
        colshapes[csi] = nil
        cs.alloc()
        return cs
    end
end

function M.alloc_box(size)
    local cs = alloc()
    cs.alloc_box(size)
    return cs
end

function M.alloc_sphere(r)
    local cs = alloc()
    cs.alloc_sphere(r)
    return cs
end

function M.alloc_hmap(start, width, length, hmin, hmax, scale)
    local cs = alloc()
    cs.alloc_hmap(start, width, length, hmin, hmax, scale)
    return cs
end

function M.alloc_comp()
    local cs = alloc()
    cs.alloc_comp()
    return cs
end

return M
