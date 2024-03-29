local M = {}

local cfg = require 'config'
local log = require 'core.log'

local vehicles = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_vehicle(vehi)
    local self = {}
    function self.alloc(wld, ch_cs, ch_inert, tm, ...)
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        api_physics_veh_alloc(vehi, wld.id(), ch_cs.id(), ch_inert.id(), tm.id(), ...)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        vehicles[vehi] = self
        api_physics_veh_free(vehi)
    end
    function self.transform(tm)
        api_physics_veh_transform(vehi, tm.id())
    end
    function self.add_wheel(pos, dir, axl, sus_rest, roll, radius, front)
        local wheel = {}
        local wheeli = api_physics_veh_add_wheel(vehi, pos.id(), dir.id(), axl.id(),
                                                 sus_rest, roll, radius, front)
        function wheel.set(engine, brake, steer)
            api_physics_veh_set_wheel(vehi, wheeli, engine, brake, steer)
        end
        function wheel.contact()
            return api_physics_veh_wheel_contact(vehi, wheeli)
        end
        function wheel.id()
            return wheeli
        end
        function wheel.veh_id()
            return vehi
        end
        return wheel
    end
    function self.id()
        return vehi
    end
    return self
end

function M.init()
    for vehi = 0, cfg.VEHICLE_COUNT - 1 do
        vehicles[vehi] = make_vehicle(vehi)
    end
    left = cfg.VEHICLE_COUNT
    left_min = cfg.VEHICLE_COUNT
end

function M.done()
    log.info('Vehicles usage: %i/%i, allocs/frees: %i/%i',
             cfg.VEHICLE_COUNT - left_min, cfg.VEHICLE_COUNT, allocs, frees)
    if allocs ~= frees then
        error('Allocs/frees mismatch')
    end
end

function M.alloc(wld, ch_cs, ch_inert, tm, mass, ch_frict, ch_roll_frict,
                 sus_stif, sus_comp, sus_damp, sus_trav, sus_force, slip_frict)
    if left == 0 then
        error('out of vehicles')
    end
    for vehi, veh in pairs(vehicles) do
        vehicles[vehi] = nil
        veh.alloc(wld, ch_cs, ch_inert, tm, mass, ch_frict, ch_roll_frict,
                  sus_stif, sus_comp, sus_damp, sus_trav, sus_force, slip_frict)
        return veh
    end
end

return M
