local M = {}

local cfg = require 'config'
local log = require 'core.log'

local rigidbodies = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_rigidbody(ri)
    local self = {}
    function self.alloc(wld, cs, tm, mass, frict, roll_frict)
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        api_physics_rb_alloc(ri, wld.id(), cs.id(), tm.id(),
                             mass, frict, roll_frict)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        rigidbodies[ri] = self
        api_physics_rb_free(ri)
    end
    function self.id()
        return ri
    end
    return self
end

function M.init()
    for ri = 0, cfg.RIGIDBODY_COUNT - 1 do
        rigidbodies[ri] = make_rigidbody(ri)
    end
    left = cfg.RIGIDBODY_COUNT
    left_min = cfg.RIGIDBODY_COUNT
end

function M.done()
    log.info('Rigid bodies usage: %i/%i, allocs/frees: %i/%i',
             cfg.RIGIDBODY_COUNT - left_min, cfg.RIGIDBODY_COUNT, allocs, frees)
    if allocs ~= frees then
        error('Allocs/frees mismatch')
    end
end

function M.alloc(wld, cs, tm, mass, frict, roll_frict)
    if left == 0 then
        error('out of rigidbodies')
    end
    for ri, r in pairs(rigidbodies) do
        rigidbodies[ri] = nil
        r.alloc(wld, cs, tm, mass, frict, roll_frict)
        return r
    end
end

return M

