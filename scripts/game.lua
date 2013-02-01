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
local quit = require 'quit'
local ddraw = require 'ddraw'
local perf = require 'perf'
local key = require 'key'

local LOGIC_TIME = 0.015
local GC_STEP = 10
local START_X = 0
local START_Y = 0
local START_Z = 0

local function start_pos(wld)
    local wx, wy, wz = wld.scene_to_world(START_X, 0, START_Z)
    wy = wld.height(wz, wx) + 10
    return wld.world_to_scene(wx, wy, wz)
end

local function run_co(co, start_time, max_time)
    while coroutine.status(co) ~= 'dead' do
        local res, arg = coroutine.resume(co)
        if res and arg then
            break
        elseif not res then
            io.write('Coroutine\n', debug.traceback(co), '\n')
            error(arg)
        end
        if api_timer() - start_time > max_time then
            break
        end
    end
end

local function tick(f)
    local t = api_timer()
    f()
    return api_timer() - t
end 

function M.run()
    pwld.init()
    render.init()
    gui.init()

    local prf = perf.alloc()
    local frame_time = api_timer()
    local blink = blinker.alloc()
    local wld = world.alloc(START_X, START_Y, START_Z)
    local sx, sy, sz = start_pos(wld)
    local cbs = cubes.alloc(sx, sy, sz - 5)
    local car = vehicle.alloc(sx, sy, sz + 5)
    local camc = camcord.alloc(sx, sy, sz + 10)
    local camd = camdev.alloc(sx, sy, sz)
    local camsw = camswitch.alloc(camc, camd)
    local keyctl = key.alloc(function() return API_INPUT_KEY_F10 end,
        function()
            local sx, sy, sz = start_pos(wld)
            cbs.free()
            cbs = cubes.alloc(sx, sy, sz - 5)
            car.free()
            car = vehicle.alloc(sx, sy, sz + 5)
            camc.attach(car.mchassis)
            wld.attach(car.mchassis)
        end, function() end)

    camc.attach(car.mchassis)
    wld.attach(car.mchassis)
    util.set_gravity(0, -10, 0)
    render.visual.engage()

    local control = coroutine.create(
        function()
            while not quit.requested()
            do
                quit.control()
                ddraw.update()
                keyctl.update()
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
                coroutine.yield(true)
            end
        end)

    local work = coroutine.create(
        function()
            while not quit.requested()
            do
                wld.generate()
                coroutine.yield(true)
            end
        end)

    while coroutine.status(control) ~= 'dead'
       or coroutine.status(work) ~= 'dead'
    do
        local logic_time = api_timer()
        prf.sample('physics', tick(function() api_physics_update(cfg.FRAME_TIME) end))
        prf.sample('input', tick(function() api_input_update() end))
        prf.sample('gc', tick(function() api_main_gc_step(GC_STEP) end))
        prf.sample('control', tick(function() run_co(control, logic_time, 0) end))
        prf.sample('work', tick(function() run_co(work, logic_time, LOGIC_TIME) end))
        prf.sample('rupdate', tick(function() render.update() end))
        prf.sample('rdraw', tick(function() render.draw() end))
        prf.sample('frame', api_timer() - frame_time)
        prf.update()
        gui.frame_time(api_timer() - frame_time)
        frame_time = api_timer()
    end

    prf.free()
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

return M
