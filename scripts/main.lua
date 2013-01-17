dofile('demo.lua')
dofile('perf.lua')
dofile('api.lua')

quit = false

function configure()
    return {["mpool_sizes"] = function() return    100, 1000, 10000, 100000, 1000000, 10000000 end,
            ["mpool_counts"] = function() return 10000, 1000,   100,     10,       1,        1 end,
            ["frame_time"] = 1 / 60,
            ["logic_time"] = 0.01,
            ["gc_step"] = 10,
            ["display_width"] = 1920,
            ["display_height"] = 1080,
            ["mesh_count"] = 100,
            ["vbuf_size"] = 10000,
            ["vbuf_count"] = 100,
            ["ibuf_size"] = 10000,
            ["ibuf_count"] = 100,
            ["text_size"] = 100,
            ["text_count"] = 100,
            ["vector_count"] = 100,
            ["vector_nesting"] = 10,
            ["matrix_count"] = 100,
            ["matrix_nesting"] = 10,
            ["colshape_count"] = 100,
            ["rigidbody_count"] = 100,
            ["vehicle_count"] = 10,
            ["buf_size"] = 10000,
            ["buf_count"] = 10}
end

function control(machine)
    demo.control_machine = machine
    local ds = demo.ddraw_switcher_create()
    local prf = perf.create()
    while not quit
    do
        if api_input_key(API_INPUT_KEY_ESCAPE) == 1 then
            quit = true
        end
        ds:update()
        prf:update()
        api_machine_yield(machine)
    end
    prf:destruct()
end

function work(machine)
    demo.work_machine = machine
    demo.set_gravity(0, -10, 0)
    local blink = demo.blinker_create()
    local land = demo.landscape_create(0, -15, -3)
    local sweet = demo.sweet_pair_create(0, 0, -5)
    local car = demo.vehicle_create(0, -10, 5)
    local camera = demo.cord_camera_create(0, -10, 20, car.mchassis)
    while not quit
    do
        if api_input_key(API_INPUT_KEY_F10) == 1 then
            sweet:destruct()
            sweet = demo.sweet_pair_create(0, 0, -5)
            car:destruct()
            car = demo.vehicle_create(0, -10, 5)
            camera:destruct()
            camera = demo.cord_camera_create(0, -10, 20, car.mchassis)
            while api_input_key(API_INPUT_KEY_F10) == 1 do
                api_machine_sleep(machine)
            end
        end
        car:update()
        api_machine_sleep(machine)
    end
    blink:destruct()
    land:destruct()
    sweet:destruct()
    car:destruct()
    camera:destruct()
end
