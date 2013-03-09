local M = {}

local cfg = require 'config'
local util = require 'core.util'
local blinker = require 'game.blinker'
local cubes = require 'game.cubes'
local vehicle = require 'game.vehicle'
local camcord = require 'game.camera.cord'
local camdev = require 'game.camera.dev'
local camswitch = require 'game.camera.switcher'
local world = require 'game.world'
local corewld = require 'core.world'
local render = require 'game.render'
local pwld = require 'game.physwld'
local pause = require 'game.pause'
local gui = require 'game.gui.gui'
local quit = require 'game.quit'
local query = require 'core.query'
local mesh = require 'core.mesh'
local shprog = require 'core.shprog'
local shuni = require 'core.shuni'
local thread = require 'core.thread'
local ddraw = require 'game.ddraw'
local meshes = require 'game.meshes'
local sync = require 'core.sync'
local key = require 'core.key'
local shader = require 'game.shader'
local poolbuf = require 'core.pool.buf'
local poolpbuf = require 'core.pool.pbuf'
local twinibuf = require 'core.twin.ibuf'
local twinvbuf = require 'core.twin.vbuf'

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
        collectgarbage('step', GC_STEP)
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
    corewld.init()
    shprog.init()
    shuni.init()
    mesh.init()
    query.init()
    sync.init()
    thread.init()
    meshes.init()
    poolbuf.init()
    twinibuf.init()
    twinvbuf.init()
    poolpbuf.init()
    shader.init()
    pwld.init()
    render.init()

    local wld, cbs, car, camc, camd, camsw
    local created = false
    local generated = false

    pwld.wld.gravity(0, -10, 0)
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
            pwld.wld.tscale(0)
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
            pwld.wld.tscale(1)
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
            pwld.wld.tscale(0)
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

    collectgarbage('stop')

    while coroutine.status(control) ~= 'dead'
       or coroutine.status(slowpok) ~= 'dead'
       or coroutine.status(work) ~= 'dead'
    do
        local logic_time = api_timer()
        local core_time = logic_time
        pwld.wld.update(cfg.FRAME_TIME)
        api_input_update()
        collectgarbage('step', GC_STEP)

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
    poolpbuf.done()
    twinvbuf.done()
    twinibuf.done()
    poolbuf.done()
    shprog.done()
    shuni.done()
    query.done()
    mesh.done()
    sync.done()
    thread.done()
    corewld.done()
end

return M
