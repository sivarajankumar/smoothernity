local M = {}

local cfg = require 'config'
local util = require 'core.util'
local log = require 'core.log'

local worlds = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_world(wi)
    local self = {}
    local tscl = 1
    function self.alloc()
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        worlds[wi] = self
    end
    function self.id()
        return wi
    end
    function self.gravity(x, y, z)
        local grav = util.vector_const(x, y, z, 0)
        api_physics_wld_gravity(wi, grav.id())
        grav.free()
    end
    function self.ddraw()
        api_physics_wld_ddraw(wi)
    end
    function self.ddraw_mode(mode)
        api_physics_wld_ddraw_mode(wi, mode)
    end
    function self.tscale(t)
        tscl = t
    end
    function self.move(dv)
        api_physics_wld_move(wi, dv.id())
    end
    function self.update(dt)
        if tscl > 0 then
            api_physics_wld_update(wi, dt * tscl)
        end
    end
    return self
end

function M.init()
    for wi = 0, cfg.WORLD_COUNT - 1 do
        worlds[wi] = make_world(wi)
    end
    left = cfg.WORLD_COUNT
    left_min = cfg.WORLD_COUNT
end

function M.done()
    log.info('Worlds usage: %i/%i, allocs/frees: %i/%i',
             cfg.WORLD_COUNT - left_min, cfg.WORLD_COUNT, allocs, frees)
    if allocs ~= frees then
        error('Allocs/frees mismatch')
    end
end

function M.alloc()
    if left == 0 then
        error('out of worlds')
    end
    for wi, w in pairs(worlds) do
        worlds[wi] = nil
        w.alloc()
        return w
    end
end

return M

