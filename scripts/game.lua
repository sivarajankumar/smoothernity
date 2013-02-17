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
local key = require 'key'
local shader = require 'shader.shader'
local poolbuf = require 'pool.buf'
local poolibuf = require 'pool.ibuf'
local poolvbuf = require 'pool.vbuf'

local LOGIC_TIME = 0.013
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
        api_main_gc_step(GC_STEP)
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

function M.run()
    poolbuf.init()
    poolibuf.init(render)
    poolvbuf.init(render)
    shader.init()
    pwld.init()
    render.init()

    local wld, cbs, car, camc, camd, camsw
    local created = false
    local generated = false

    util.set_gravity(0, -10, 0)
    render.engage(render.visual)

    local control = coroutine.create(
        function()
            while not created do
                coroutine.yield(true)
            end
            while not quit.requested()
            do
                quit.control()
                ddraw.update()
                car.update()
                camd.update()
                camsw.update()
                wld.move(car, camc)
                wld.showhide()
                if generated then
                    pause.control()
                end
                coroutine.yield(true)
            end
        end)

    local slowpok = coroutine.create(
        function()
            while not created do
                coroutine.yield(true)
            end
            while not quit.requested()
            do
                gui.gen_progress(wld.gen_progress())
                local edist = wld.edge_dist()
                gui.edge_dist(edist)
                car.restrain(edist)
                coroutine.yield(true)
            end
        end)

    local work = coroutine.create(
        function()
            local blink = blinker.alloc()
            gui.init()
            gui.wait_show()
            api_physics_wld_tscale(pwld.wld, 0)
            render.timescale(0)
            wld = world.alloc('world', START_X, START_Y, START_Z)
            local sx, sy, sz = start_pos(wld)
            cbs = cubes.alloc(sx, sy, sz - 5)
            car = vehicle.alloc('car', sx, sy, sz + 5)
            camc = camcord.alloc('camera', car.mchassis, sx, sy, sz + 10)
            camd = camdev.alloc(sx, sy, sz)
            camsw = camswitch.alloc(camc, camd)
            wld.attach(car.mchassis)
            created = true
            wld.generate()
            api_physics_wld_tscale(pwld.wld, 1)
            render.timescale(1)
            gui.wait_hide()
            generated = true
            while not quit.requested()
            do
                wld.generate()
                coroutine.yield(true)
            end
            while coroutine.status(control) ~= 'dead'
               or coroutine.status(slowpok) ~= 'dead'
            do
                coroutine.yield(true)
            end
            gui.wait_show()
            api_physics_wld_tscale(pwld.wld, 0)
            render.timescale(0)
            car.save(wld)
            camc.save()
            wld.save()
            render.camera_stop()
            camc.free()
            camd.free()
            car.free()
            cbs.free()
            wld.free()
            gui.done()
            blink.free()
        end)

    while coroutine.status(control) ~= 'dead'
       or coroutine.status(slowpok) ~= 'dead'
       or coroutine.status(work) ~= 'dead'
    do
        local logic_time = api_timer()
        local core_time = logic_time
        api_physics_update(cfg.FRAME_TIME)
        api_input_update()
        api_main_gc_step(GC_STEP)
        api_storage_update()

        local control_time = api_timer()
        run_co(control, logic_time, 0)

        local slowpok_time = api_timer()
        run_co(slowpok, logic_time, 0)

        local work_time = api_timer()
        run_co(work, logic_time, LOGIC_TIME)

        local rupdate_time = api_timer()
        render.update()

        local rdraw_time = api_timer()
        render.draw()

        core_time = control_time - core_time
        control_time = slowpok_time - control_time
        slowpok_time = work_time - slowpok_time
        work_time = rupdate_time - work_time
        rupdate_time = rdraw_time - rupdate_time
        rdraw_time = api_timer() - rdraw_time - render.clear_time - render.swap_time
        gui.cpu_times(core_time, control_time, slowpok_time, work_time, rupdate_time,
                      render.clear_time, rdraw_time, render.swap_time)
    end

    render.done()
    pwld.done()
    shader.done()
    poolvbuf.done()
    poolibuf.done()
    poolbuf.done()
end

return M
