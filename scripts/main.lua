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
    local frame_time = api_main_time()
    while api_main_machines_running()
    do
        local logic_time = api_main_time()
        do
            local t = api_main_time()
            api_physics_update(cfg.FRAME_TIME)
            prf.sample('physics', api_main_time() - t)
        end
        do
            local t = api_main_time()
            api_input_update()
            prf.sample('input', api_main_time() - t)
        end
        do
            local t = api_main_time()
            api_main_gc_step(GC_STEP)
            prf.sample('gc', api_main_time() - t)
        end
        do
            local t = api_main_time()
            api_main_machines_update(LOGIC_TIME - (api_main_time() - logic_time))
            prf.sample('machines', api_main_time() - t)
        end
        do
            local t = api_main_time()
            render.update()
            prf.sample('rupdate', api_main_time() - t)
        end
        do
            local t = api_main_time()
            render.draw()
            prf.sample('rdraw', api_main_time() - t)
        end
        prf.sample('frame', api_main_time() - frame_time)
        prf.update()
        gui.frame_time(api_main_time() - frame_time)
        frame_time = api_main_time()
    end
    prf.free()
    game.done()
end

function control(mach)
    game_started = true
    while not quit.requested()
    do
        game.control(mach)
        quit.control()
        ddraw.update()
        api_machine_yield(mach)
    end
    while not work_finished do
        api_machine_yield(mach)
    end
end

function work(mach)
    while not quit.requested()
    do
        if game_started then
            game.work(mach)
        end
        api_machine_sleep(mach)
    end
    work_finished = true
end
