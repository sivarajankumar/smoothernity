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
local pause = require 'pause'
local gui = require 'gui.gui'

local blink, wld, cbs, car, camc, camd, camsw
local pressed = 0

local START_X = 0
local START_Y = 0
local START_Z = 0

local function start_pos()
    local wx, wy, wz = wld.scene_to_world(START_X, 0, START_Z)
    wy = wld.height(wz, wx) + 10
    return wld.world_to_scene(wx, wy, wz)
end

function M.init()
    pwld.init()
    render.init()
    gui.init()
    util.set_gravity(0, -10, 0)
    blink = blinker.alloc()
    wld = world.alloc(START_X, START_Y, START_Z)

    local sx, sy, sz = start_pos()
    cbs = cubes.alloc(sx, sy, sz - 5)
    car = vehicle.alloc(sx, sy, sz + 5)
    camc = camcord.alloc(sx, sy, sz + 10)
    camd = camdev.alloc(sx, sy, sz)

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
    gui.done()
    render.done()
    pwld.done()
end

function M.control(mach)
    if pressed == 0 then
        if api_input_key(API_INPUT_KEY_F10) == 1 then
            pressed = 1
            local sx, sy, sz = start_pos()
            cbs.free()
            cbs = cubes.alloc(sx, sy, sz - 5)
            car.free()
            car = vehicle.alloc(sx, sy, sz + 5)
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
    wld.showhide()
    pause.control()
    gui.gen_progress(wld.gen_progress())

    local edist = wld.edge_dist()
    gui.edge_dist(edist)
    car.restrain(edist)
    gui.control()
end

function M.work(mach)
    wld.generate(mach)
end

return M
