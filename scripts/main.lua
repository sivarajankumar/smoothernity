local ddraw = require 'ddraw'
local perf = require 'perf'
local util = require 'util'
local blinker = require 'blinker'
local land = require 'land'
local cubes = require 'cubes'
local vehicle = require 'vehicle'
local camcord = require 'camera.cord'
local camdev = require 'camera.dev'
local camswitch = require 'camera.switcher'

local quit = false
local machwork = nil

function configure()
    return {['mpool_sizes'] = function() return    100, 1000, 10000, 100000, 1000000, 10000000 end,
            ['mpool_counts'] = function() return 10000, 1000,   100,     10,       1,        1 end,
            ['frame_time'] = 1 / 60,
            ['logic_time'] = 0.01,
            ['gc_step'] = 10,
            ['display_width'] = 1920,
            ['display_height'] = 1080,
            ['mesh_count'] = 100,
            ['vbuf_size'] = 10000,
            ['vbuf_count'] = 100,
            ['ibuf_size'] = 10000,
            ['ibuf_count'] = 100,
            ['text_size'] = 100,
            ['text_count'] = 100,
            ['vector_count'] = 100,
            ['vector_nesting'] = 10,
            ['matrix_count'] = 100,
            ['matrix_nesting'] = 10,
            ['colshape_count'] = 100,
            ['rigidbody_count'] = 100,
            ['vehicle_count'] = 10,
            ['buf_size'] = 10000,
            ['buf_count'] = 10}
end

function control(mach)
    while machwork == nil do
        api_machine_yield(mach)
    end
    local prf = perf.alloc(mach, machwork)
    while not quit
    do
        if api_input_key(API_INPUT_KEY_ESCAPE) == 1 then
            quit = true
        end
        ddraw.update()
        prf.update()
        api_machine_yield(mach)
    end
    prf.free()
end

function work(mach)
    machwork = mach
    util.set_gravity(0, -10, 0)
    local blink = blinker.alloc()
    local lnd = land.alloc(0, -15, -3)
    local cbs = cubes.alloc(0, 0, -5)
    local car = vehicle.alloc(0, -10, 5)
    local camc = camcord.alloc(0, -10, 20)
    local camd = camdev.alloc(0, -10, 20)
    local camsw = camswitch.alloc(camc, camd)
    camc.attach(car.mchassis)
    while not quit
    do
        if api_input_key(API_INPUT_KEY_F10) == 1 then
            cbs.free()
            cbs = cubes.alloc(0, 0, -5)
            car.free()
            car = vehicle.alloc(0, -10, 5)
            camc.attach(car.mchassis)
            while api_input_key(API_INPUT_KEY_F10) == 1 do
                api_machine_sleep(mach)
            end
        end
        car.update()
        camd.update()
        camsw.update()
        api_machine_sleep(mach)
    end
    blink.free()
    lnd.free()
    cbs.free()
    car.free()
    camc.free()
    camd.free()
end
