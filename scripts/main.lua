local ddraw = require 'ddraw'
local perf = require 'perf'
local game = require 'game'
local cfg = require 'config'
local render = require 'render'
local pwld = require 'physwld'
local quit = require 'quit'

local machwork = nil
local work_finished = false
local game_started = false

function configure()
    return {['mpool_sizes'] = function() return    100, 1000, 10000, 100000, 1000000, 5000000 end,
            ['mpool_counts'] = function() return 10000, 1000,  1000,      2,       2,       2 end,
            ['frame_time'] = cfg.FRAME_TIME,
            ['logic_time'] = 0.01,
            ['gc_step'] = 10,
            ['screen_width'] = cfg.SCREEN_WIDTH,
            ['screen_height'] = cfg.SCREEN_HEIGHT,
            ['mesh_count'] = 1000,
            ['vbuf_size'] = 10000,
            ['vbuf_count'] = 1000,
            ['ibuf_size'] = 100000,
            ['ibuf_count'] = 1000,
            ['text_size'] = 100,
            ['text_count'] = 100,
            ['vector_count'] = 100,
            ['vector_nesting'] = 20,
            ['matrix_count'] = 1000,
            ['matrix_nesting'] = 20,
            ['world_count'] = 2,
            ['colshape_count'] = 100,
            ['rigidbody_count'] = 100,
            ['vehicle_count'] = 10,
            ['buf_size'] = 10000,
            ['buf_count'] = 100,
            ['rop_count'] = 100}
end

function control(mach)
    while machwork == nil do
        api_machine_yield(mach)
    end
    game.init()
    game_started = true
    local prf = perf.alloc(mach, machwork)
    while not quit.requested()
    do
        game.control(mach)
        quit.control()
        ddraw.update()
        prf.update()
        api_machine_yield(mach)
    end
    while not work_finished do
        api_machine_yield(mach)
    end
    prf.free()
    game.done()
end

function work(mach)
    machwork = mach
    while not quit.requested()
    do
        if game_started then
            game.work(mach)
        end
        api_machine_sleep(mach)
    end
    work_finished = true
end
