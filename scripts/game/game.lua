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
local rigidbody = require 'core.rigidbody'
local colshape = require 'core.colshape'
local coreveh = require 'core.vehicle'
local matrix = require 'core.matrix'
local vector = require 'core.vector'
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
local prof = require 'game.prof'

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
    matrix.init()
    vector.init()
    corewld.init()
    coreveh.init()
    colshape.init()
    rigidbody.init()
    shprog.init()
    shuni.init()
    mesh.init()
    query.init()
    sync.init()
    thread.init()
    meshes.init()
    poolbuf.init()
    poolpbuf.init()
    shader.init()
    pwld.init()
    prof.init()
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
            local t = api_timer()
            wld.generate()
            t = api_timer() - t
            io.write(string.format('generation time: %f\n', t))
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
            created = false
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

        prof.gpu.logic.start()

        prof.cpu.core.start()
        if created then
            wld.move(car, camc)
        end
        pwld.wld.update(cfg.FRAME_TIME)
        api_input_update()
        collectgarbage('step', GC_STEP)
        prof.cpu.core.finish()

        prof.cpu.control.start()
        run_co(control, logic_time, 0)
        prof.cpu.control.finish()

        prof.cpu.slowpok.start()
        run_co(slowpok, logic_time, 0)
        prof.cpu.slowpok.finish()

        prof.cpu.work.start()
        run_co(work, logic_time, LOGIC_TIME)
        prof.cpu.work.finish()

        prof.cpu.rupdate.start()
        render.update()
        prof.cpu.rupdate.finish()

        prof.gpu.logic.finish()

        render.draw()

        prof.update()
    end

    render.done()
    prof.done()
    pwld.done()
    shader.done()
    poolpbuf.done()
    poolbuf.done()
    shprog.done()
    shuni.done()
    query.done()
    mesh.done()
    sync.done()
    thread.done()
    rigidbody.done()
    colshape.done()
    coreveh.done()
    corewld.done()
    matrix.done()
    vector.done()
end

return M
