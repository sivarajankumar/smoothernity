local M = {}

local cfg = require 'config'
local util = require 'util'
local blinker = require 'blinker'
local cubes = require 'cubes'
local vehicle = require 'vehicle'
local camcord = require 'camera.cord'
local camdev = require 'camera.dev'
local camswitch = require 'camera.switcher'
local world = require 'world'

local blink, wld, cbs, car, camc, camd, camsw, mproj
local pressed = 0

local START_X = 0
local START_Y = 0
local START_Z = 0

local PROJ_Z_NEAR = 1
local PROJ_Z_FAR = 1024
local PROJ_FOV = 60 * math.pi / 360

local function make_mproj()
    mproj = api_matrix_alloc()
    local vbounds = api_vector_alloc()
    local vz = api_vector_alloc()

    local ymax = PROJ_Z_NEAR * math.tan(PROJ_FOV)
    local xmax = ymax * cfg.DISPLAY_WIDTH / cfg.DISPLAY_HEIGHT

    api_vector_const(vbounds, -xmax, xmax, -ymax, ymax)
    api_vector_const(vz, PROJ_Z_NEAR, PROJ_Z_FAR, 0, 0)

    api_matrix_frustum(mproj, vbounds, vz, 0, 1)
    api_matrix_update(mproj)
    api_matrix_stop(mproj)
    api_display_proj(mproj)
    api_vector_free(vbounds)
    api_vector_free(vz)
end

function M.init()
    util.set_gravity(0, -10, 0)
    blink = blinker.alloc()
    wld = world.alloc(START_X, START_Y, START_Z)
    cbs = cubes.alloc(START_X, START_Y + 15, START_Z - 5)
    car = vehicle.alloc(START_X, START_Y + 10, START_Z + 5)
    camc = camcord.alloc(START_X, START_Y + 10, START_Z + 10)
    camd = camdev.alloc(START_X, START_Y, START_Z)
    camsw = camswitch.alloc(camc, camd)
    camc.attach(car.mchassis)
    wld.attach(car.mchassis)
    make_mproj()
end

function M.done()
    blink.free()
    wld.free()
    cbs.free()
    car.free()
    camc.free()
    camd.free()
    api_matrix_free(mproj)
end

function M.control(mach)
    if pressed == 0 then
        if api_input_key(API_INPUT_KEY_F10) == 1 then
            pressed = 1
            cbs.free()
            cbs = cubes.alloc(START_X, START_Y + 15, START_Z - 5)
            car.free()
            car = vehicle.alloc(START_X, START_Y + 10, START_Z + 5)
            camc.attach(car.mchassis)
            wld.attach(car.mchassis)
        end
    elseif pressed == 1 then
        if api_input_key(API_INPUT_KEY_F10) == 0 then
            pressed = 0
        end
    end
    car.update()
    camd.update()
    camsw.update()
    wld.move(car, camc)
end

function M.work(mach)
    wld.generate(mach)
end

return M
