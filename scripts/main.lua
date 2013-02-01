local ddraw = require 'ddraw'
local perf = require 'perf'
local game = require 'game'
local cfg = require 'config'
local render = require 'render'
local pwld = require 'physwld'
local quit = require 'quit'
local gui = require 'gui.gui'

local work_finished = false
local game_started = false

local LOGIC_TIME = 0.01
local GC_STEP = 10

function configure()
    return {mpool_sizes = function() return    100, 1000, 10000, 100000, 1000000, 5000000 end,
            mpool_counts = function() return 10000, 1000,  1000,      2,       2,       2 end,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            mesh_count = 1000,
            vbuf_size = 10000,
            vbuf_count = 1000,
            ibuf_size = 100000,
            ibuf_count = 1000,
            text_size = 100,
            text_count = 100,
            vector_count = 100,
            vector_nesting = 20,
            matrix_count = 1000,
            matrix_nesting = 20,
            world_count = 2,
            colshape_count = 100,
            rigidbody_count = 100,
            vehicle_count = 10,
            buf_size = 10000,
            buf_count = 100,
            rop_count = 100,
            storage_size = 100000,
            storage_count = 1}
end

function run()
    game.init()
    local prf = perf.alloc()
    local frame_time = api_timer()
    local control, work
    control = coroutine.create(
        function()
            while not quit.requested()
            do
                game.control()
                quit.control()
                ddraw.update()
                coroutine.yield(true)
            end
            control = nil
        end)
    work = coroutine.create(
        function()
            while not quit.requested()
            do
                game.work()
                coroutine.yield(true)
            end
            work = nil
        end)
    while control ~= nil and work ~= nil
    do
        local logic_time = api_timer()
        do
            local t = api_timer()
            api_physics_update(cfg.FRAME_TIME)
            prf.sample('physics', api_timer() - t)
        end
        do
            local t = api_timer()
            api_input_update()
            prf.sample('input', api_timer() - t)
        end
        do
            local t = api_timer()
            api_main_gc_step(GC_STEP)
            prf.sample('gc', api_timer() - t)
        end
        do
            local t = api_timer()
            if control ~= nil then
                local res, arg = coroutine.resume(control)
                if not res then
                    error(arg)
                end
            end
            prf.sample('control', api_timer() - t)
        end
        do
            local t = api_timer()
            if work == nil then
                io.write('work is nil\n')
            end
            while work ~= nil do
                local res, arg = coroutine.resume(work)
                if res and arg then
                    break
                elseif not res then
                    error(arg)
                end
                if api_timer() - logic_time > LOGIC_TIME then
                    break
                end
            end
            prf.sample('work', api_timer() - t)
        end
        do
            local t = api_timer()
            render.update()
            prf.sample('rupdate', api_timer() - t)
        end
        do
            local t = api_timer()
            render.draw()
            prf.sample('rdraw', api_timer() - t)
        end
        prf.sample('frame', api_timer() - frame_time)
        prf.update()
        gui.frame_time(api_timer() - frame_time)
        frame_time = api_timer()
    end
    prf.free()
    game.done()
end
