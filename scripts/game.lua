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
local render = require 'render'
local pwld = require 'physwld'

local blink, wld, cbs, car, camc, camd, camsw
local pressed = 0

local START_X = 0
local START_Y = 0
local START_Z = 0

function M.init()
    pwld.init()
    render.init()
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
    render.visual.engage()
end

function M.done()
    blink.free()
    wld.free()
    cbs.free()
    car.free()
    camc.free()
    camd.free()
    render.done()
    pwld.done()
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
