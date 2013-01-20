local ddraw = require 'ddraw'
local perf = require 'perf'
local util = require 'util'
local blinker = require 'blinker'
local cubes = require 'cubes'
local vehicle = require 'vehicle'
local camcord = require 'camera.cord'
local camdev = require 'camera.dev'
local camswitch = require 'camera.switcher'
local world = require 'world'

local quit = false
local machwork = nil

function configure()
    return {['mpool_sizes'] = function() return    100, 1000, 10000, 100000, 1000000, 10000000 end,
            ['mpool_counts'] = function() return 10000, 1000,  1000,     10,       1,        1 end,
            ['frame_time'] = 1 / 60,
            ['logic_time'] = 0.01,
            ['gc_step'] = 10,
            ['display_width'] = 1920,
            ['display_height'] = 1080,
            ['mesh_count'] = 100,
            ['vbuf_size'] = 10000,
            ['vbuf_count'] = 100,
            ['ibuf_size'] = 100000,
            ['ibuf_count'] = 100,
            ['text_size'] = 100,
            ['text_count'] = 100,
            ['vector_count'] = 100,
            ['vector_nesting'] = 10,
            ['matrix_count'] = 200,
            ['matrix_nesting'] = 10,
            ['colshape_count'] = 100,
            ['rigidbody_count'] = 100,
            ['vehicle_count'] = 10,
            ['buf_size'] = 10000,
            ['buf_count'] = 100}
end

local game = {}

function control(mach)
    while machwork == nil do
        api_machine_yield(mach)
    end
    local prf = perf.alloc(mach, machwork)
    util.set_gravity(0, -10, 0)
    game.blink = blinker.alloc()
    game.wld = world.alloc(machwork, 0, -15, -3)
    game.cbs = cubes.alloc(0, 0, -5)
    game.car = vehicle.alloc(0, -5, 5)
    game.camc = camcord.alloc(0, -5, 20)
    game.camd = camdev.alloc(0, -5, 20)
    game.camsw = camswitch.alloc(game.camc, game.camd)

    game.camc.attach(game.car.mchassis)
    game.wld.attach(game.car.mchassis)
    local pressed = 0
    while not quit
    do
        if api_input_key(API_INPUT_KEY_ESCAPE) == 1 then
            quit = true
        end
        if pressed == 0 then
            if api_input_key(API_INPUT_KEY_F10) == 1 then
                pressed = 1
                game.cbs.free()
                game.cbs = cubes.alloc(0, 0, -5)
                game.car.free()
                game.car = vehicle.alloc(0, -5, 5)
                game.camc.attach(game.car.mchassis)
                game.wld.attach(game.car.mchassis)
            end
        elseif pressed == 1 then
            if api_input_key(API_INPUT_KEY_F10) == 0 then
                pressed = 0
            end
        end
        game.car.update()
        game.camd.update()
        game.camsw.update()
        ddraw.update()
        prf.update()
        api_machine_yield(mach)
    end
    prf.free()
    game.blink.free()
    game.wld.free()
    game.cbs.free()
    game.car.free()
    game.camc.free()
    game.camd.free()
end

function work(mach)
    machwork = mach
    while not quit
    do
        if game.wld ~= nil then
            game.wld.update()
        end
        api_machine_sleep(mach)
    end
end
