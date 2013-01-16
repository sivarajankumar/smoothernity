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
            ["vbuf_size"] = 1024,
            ["vbuf_count"] = 100,
            ["ibuf_size"] = 1024,
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
    local perf = demo.perf_create()
    while not quit
    do
        if api_input_key(API_INPUT_KEY_ESCAPE) == 1 then
            quit = true
        end
        ds:update()
        perf:update()
        api_machine_yield(machine)
    end
    perf:destruct()
end

function work(machine)
    demo.work_machine = machine
    demo.set_gravity(0, -10, 0)
    local blink = demo.blinker_create()
    local land = demo.landscape_create(0, -15, -3)
    local freecam = demo.free_camera_create(0, -10, 20)
    local sweet = demo.sweet_pair_create(0, 0, -5)
    local car = demo.vehicle_create(0, -10, 5)
    while not quit
    do
        if api_input_key(API_INPUT_KEY_F10) == 1 then
            sweet:destruct()
            sweet = demo.sweet_pair_create(0, 0, -5)
            car:destruct()
            car = demo.vehicle_create(0, -10, 5)
            while api_input_key(API_INPUT_KEY_F10) == 1 do
                api_machine_sleep(machine)
            end
        end
        freecam:update()
        car:update()
        api_machine_sleep(machine)
    end
    blink:destruct()
    freecam:destruct()
    land:destruct()
    sweet:destruct()
    car:destruct()
end

demo = {}

function demo.wait(machine, us)
    local time = api_machine_time(machine)
    while api_machine_time(machine) - time < us
    do
        api_machine_sleep(machine)
    end
end

function demo.set_gravity(x, y, z)
    local grav = api_vector_alloc()
    api_vector_const(grav, x, y, z, 0)
    api_physics_set_gravity(grav)
    api_vector_free(grav)
end

function demo.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, axis, angle)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, px, py, pz, 0)
    api_vector_const(scl, sx, sy, sz, 0)
    api_vector_const(rot, angle, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, axis, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

function demo.matrix_pos_stop(x, y, z)
    return demo.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, API_MATRIX_AXIS_X, 0)
end

function demo.matrix_pos_scl_stop(px, py, pz, sx, sy, sz)
    return demo.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, API_MATRIX_AXIS_X, 0)
end

function demo.matrix_pos_rot_stop(x, y, z, axis, angle)
    return demo.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, axis, angle)
end

function demo.matrix_rot_stop(axis, angle)
    return demo.matrix_pos_scl_rot_stop(0, 0, 0, 1, 1, 1, axis, angle)
end

function demo.matrix_scl_stop(sx, sy, sz)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, 0, 0, 0, 0)
    api_vector_const(scl, sx, sy, sz, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

function demo.matrix_move(m, x, y, z)
    local dm = demo.matrix_pos_stop(x, y, z)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

function demo.matrix_rotate(m, axis, angle)
    local dm = demo.matrix_rot_stop(axis, angle)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

function demo.blinker_create()
    local obj = {}
    obj.v = api_vector_alloc()
    obj.buf = api_buf_alloc()
    function obj.destruct(self)
        api_vector_free(self.v)
        api_buf_free(self.buf)
    end
    api_buf_set(obj.buf, 0,   0,0.05,0,1,1,   0,0,0.05,1,1)
    api_vector_seq(obj.v, obj.buf, 0, 2, 1, API_VECTOR_IPL_SPLINE)
    api_display_clear_color(obj.v)
    return obj
end

function demo.ddraw_switcher_create()
    local obj = {}
    obj.debug = 0
    obj.pressed = 0
    function obj.update(self)
        if self.pressed == 0 then
            if api_input_key(API_INPUT_KEY_F1) == 1 then
                self.pressed = 1
                if self.debug == 0 then
                    self.debug = 1
                    api_physics_set_ddraw(API_PHYSICS_DRAW_WIREFRAME)
                    api_display_draw_scene(0)
                else
                    self.debug = 0
                    api_physics_set_ddraw(API_PHYSICS_NO_DEBUG)
                    api_display_draw_scene(1)
                end
            end
        elseif self.pressed == 1 then
            if api_input_key(API_INPUT_KEY_F1) == 0 then
                self.pressed = 0
            end
        end
    end
    return obj
end

PERF_SHORT_FRAMES = 60
PERF_LONG_FRAMES = 600

function demo.perf_create()
    local obj = {}
    function obj.construct(self)
        self.pressed = 0
    end
    function obj.destruct(self)
        if self.short ~= nil then
            self.short:destruct()
        end
        if self.long ~= nil then
            self.long:destruct()
        end
    end
    function obj.update(self)
        if self.short ~= nil then
            self.short:update()
        end
        if self.long ~= nil then
            self.long:update()
        end
        if self.pressed == 0 then
            if api_input_key(API_INPUT_KEY_F2) == 1 then
                self.pressed = 1
                if self.short == nil and self.long == nil then
                    self.short = demo.perf_looped_create(PERF_SHORT_FRAMES)
                elseif self.short ~= nil then
                    self.short:destruct()
                    self.short = nil
                    self.long = demo.perf_looped_create(PERF_LONG_FRAMES)
                elseif self.long ~= nil then
                    self.long:destruct()
                    self.long = nil
                end
            end
        elseif self.pressed == 1 then
            if api_input_key(API_INPUT_KEY_F2) == 0 then
                self.pressed = 0
            end
        end
    end
    obj:construct()
    return obj
end

function demo.stats_create(count_max)
    local obj = {}
    obj.min = math.huge
    obj.max = 0
    obj.sum = 0
    obj.count = 0
    obj.count_max = count_max
    obj.str = "computing..."
    function obj.sample(self, value)
        if value < self.min then
            self.min = value
        end
        if value > self.max then
            self.max = value
        end
        self.sum = self.sum + value
        self.count = self.count + 1
        if self.count >= self.count_max then
            self.str = string.format("%.3f / %.3f / %.3f", self.min, self.max, self:avg())
            self.min = math.huge
            self.max = 0
            self.sum = 0
            self.count = 0
        end
    end
    function obj.avg(self)
        if self.count > 0 then
            return self.sum / self.count
        else
            return 0
        end
    end
    return obj
end

function demo.perf_looped_create(count_max)
    local obj = {}
    function obj.construct(self, count_max)
        self.prev_time = api_machine_time(demo.control_machine)
        self.stats_physics = demo.stats_create(count_max)
        self.stats_input = demo.stats_create(count_max)
        self.stats_gc = demo.stats_create(count_max)
        self.stats_control = demo.stats_create(count_max)
        self.stats_work = demo.stats_create(count_max)
        self.stats_display = demo.stats_create(count_max)
        self.stats_frame = demo.stats_create(count_max)
        self.samples = 0
        self.count_max = count_max
        self:create_text()
        io.write("Started recording performance every "..tostring(count_max).." frames\n")
    end
    function obj.destruct(self)
        io.write("Finished recording performance\n")
        api_text_free(self.text)
    end
    function obj.create_text(self)
        local str = string.format("Recorded %i samples every %i frames", self.samples, self.count_max)
        self.text = api_text_alloc(str, API_TEXT_FONT_8_BY_13, 20, 20)
    end
    function obj.update(self)
        local time = api_machine_time(demo.control_machine)
        self.stats_physics:sample(api_physics_timing())
        self.stats_input:sample(api_input_timing())
        self.stats_gc:sample(api_main_timing())
        self.stats_control:sample(api_machine_timing(demo.control_machine))
        self.stats_work:sample(api_machine_timing(demo.work_machine))
        self.stats_display:sample(api_display_timing())
        self.stats_frame:sample(time - self.prev_time)
        self.prev_time = time
        if self.stats_frame.count == 0 then
            self.samples = self.samples + 1
            api_text_free(self.text)
            self:create_text()
            io.write("Physics update:  "..self.stats_physics.str.."\n")
            io.write("Input update:    "..self.stats_input.str.."\n")
            io.write("Garbage collect: "..self.stats_gc.str.."\n")
            io.write("Control step:    "..self.stats_control.str.."\n")
            io.write("Work step:       "..self.stats_work.str.."\n")
            io.write("Display update:  "..self.stats_display.str.."\n")
            io.write("Frame time:      "..self.stats_frame.str.."\n")
            io.write("-------------------------------------\n")
        end
    end
    obj:construct(count_max)
    return obj
end

function demo.free_camera_create(x, y, z)
    local obj = {}
    obj.matrix = demo.matrix_pos_stop(x, y, z)
    obj.invmatrix = api_matrix_alloc()
    function obj.destruct(self)
        api_matrix_free(self.matrix)
        api_matrix_free(self.invmatrix)
    end
    function obj.update(self)
        local ofs = 0.25
        local ang = 0.02
        if api_input_key(API_INPUT_KEY_LSHIFT) == 1 then
            ofs = 0.05
            ang = 0.01
        end
    
        if api_input_key(API_INPUT_KEY_E) == 1 then
            demo.matrix_move(self.matrix, 0, 0, -ofs)
        end
        if api_input_key(API_INPUT_KEY_D) == 1 then
            demo.matrix_move(self.matrix, 0, 0, ofs)
        end
        if api_input_key(API_INPUT_KEY_S) == 1 then
            demo.matrix_move(self.matrix, -ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_F) == 1 then
            demo.matrix_move(self.matrix, ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_A) == 1 then
            demo.matrix_move(self.matrix, 0, ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_Z) == 1 then
            demo.matrix_move(self.matrix, 0, -ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_LEFT) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Y, ang)
        end
        if api_input_key(API_INPUT_KEY_RIGHT) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Y, -ang)
        end
        if api_input_key(API_INPUT_KEY_UP) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_X, ang)
        end
        if api_input_key(API_INPUT_KEY_DOWN) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_X, -ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEUP) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Z, ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEDOWN) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Z, -ang)
        end
    end

    api_matrix_inv(obj.invmatrix, obj.matrix)
    api_display_camera(obj.invmatrix)

    return obj
end

function demo.landscape_create(x, y, z)
    local obj = {}

    function obj.construct_vb(self)
        local vb = api_vbuf_alloc()
        for x = 0, self.width - 1 do
            for z = 0, self.length - 1 do
                api_vbuf_set(vb, x + z * self.width,
                             x - 0.5 * (self.width - 1),
                             self.hmap[z + 1][x + 1],
                             z - 0.5 * (self.length - 1),
                             math.random(), math.random(), math.random(), 1,
                             0, 0)
            end
        end
        api_vbuf_bake(vb)
        self.vb = vb
    end

    function obj.construct_ib(self)
        local ib = api_ibuf_alloc()
        for x = 0, self.width - 2 do
            for z = 0, self.length - 2 do
                local i00 = x + z * self.width
                local i01 = x + (z + 1) * self.width
                local i10 = (x + 1) + z * self.width
                local i11 = (x + 1) + (z + 1) * self.width
                local i = (x + z * (self.width - 1)) * 6
                api_ibuf_set(ib, i,  i00,i01,i10,  i10,i01,i11)
            end
        end
        api_ibuf_bake(ib)
        self.ib = ib
    end

    function obj.construct_matrices(self, x, y, z)
        self.mstart = demo.matrix_pos_stop(x, y, z)
        self.mvis = demo.matrix_pos_scl_stop(0,-1,0, self.scalex,self.scaley,self.scalez)
    end

    function obj.construct_physics(self)
        local size = api_vector_alloc()
        api_vector_const(size, self.scalex, self.scaley, self.scalez, 0)
        self.buf = api_buf_alloc()
        for x = 0, self.width - 1 do
            for z = 0, self.length - 1 do
                api_buf_set(self.buf, x + z * self.width, self.hmap[z + 1][x + 1])
            end
        end
        self.cs = api_physics_cs_alloc_hmap(self.buf, 0, self.width, self.length, 0, 1, size)
        self.rb = api_physics_rb_alloc(self.cs, self.mstart, 1, 1)
        api_vector_free(size)
    end

    function obj.construct_visual(self)
        self.mmul = api_matrix_alloc()
        self.mrb = api_matrix_alloc()
        api_matrix_rigid_body(self.mrb, self.rb)
        api_matrix_mul(self.mmul, self.mrb, self.mvis)
        self.mesh = api_mesh_alloc(API_MESH_TRIANGLES, self.vb, self.ib, -1, self.mmul, 0,
                                   6 * (self.width - 1) * (self.length - 1))
    end

    function obj.construct(self, x, y, z)
        sizex = 40
        sizey = 2
        sizez = 40
        self.width = 6
        self.length = 6
        self.scalex = sizex / (self.width - 1)
        self.scaley = sizey
        self.scalez = sizez / (self.length - 1)
        self.hmap = {{1, 1, 1, 1, 1, 1},
                     {1, 0, 0, 0, 0, 1},
                     {1, 0, 1, 1, 0, 1},
                     {1, 0, 1, 1, 0, 1},
                     {1, 0, 0, 0, 0, 1},
                     {1, 1, 1, 1, 1, 1}}
        self:construct_vb()
        self:construct_ib()
        self:construct_matrices(x, y, z)
        self:construct_physics()
        self:construct_visual()
    end

    function obj.destruct(self)
        api_vbuf_free(self.vb)
        api_ibuf_free(self.ib)
        api_matrix_free(self.mstart)
        api_matrix_free(self.mvis)
        api_matrix_free(self.mrb)
        api_matrix_free(self.mmul)
        api_physics_rb_free(self.rb)
        api_physics_cs_free(self.cs)
        api_buf_free(self.buf)
        api_mesh_free(self.mesh)
    end

    obj:construct(x, y, z)
    return obj
end

function demo.sweet_pair_create(x, y, z)
    local obj = {}

    function obj.construct_vb(self)
        local vb = api_vbuf_alloc()
        api_vbuf_set(vb, 0, -1,-1, 1,   1, 0, 0, 1,   0, 0,
                             1,-1, 1,   0, 1, 0, 1,   0, 0,
                             1, 1, 1,   0, 0, 1, 1,   0, 0,
                            -1, 1, 1,   1, 1, 1, 1,   0, 0,
                            -1,-1,-1,   0, 1, 1, 1,   0, 0,
                             1,-1,-1,   0, 0, 0, 1,   0, 0,
                             1, 1,-1,   1, 1, 0, 1,   0, 0,
                            -1, 1,-1,   1, 0, 1, 1,   0, 0)
        api_vbuf_bake(vb)
        self.vb = vb
    end

    function obj.construct_ib(self)
        local ib = api_ibuf_alloc()
        api_ibuf_set(ib, 0,  0,1,2,  0,2,3,
                             1,5,6,  1,6,2,
                             5,4,7,  5,7,6,
                             4,0,3,  4,3,7,
                             3,2,6,  3,6,7,
                             1,0,4,  1,4,5)
        api_ibuf_bake(ib)
        self.ib = ib
    end

    function obj.construct_matrices(self, x, y, z)
        self.mbig = demo.matrix_pos_stop(x, y, z)
        self.mrb = api_matrix_alloc()
        self.mloc = api_matrix_alloc()
        self.msmall = api_matrix_alloc()
        self.brot = api_buf_alloc()
        self.bpos = api_buf_alloc()
        self.vrot = api_vector_alloc()
        self.vpos = api_vector_alloc()
        self.vscl = api_vector_alloc()
        api_buf_set(self.brot, 0,   0,0,0,0,3,   math.pi*2,0,0,0,0)
        api_buf_set(self.bpos, 0,   2,1, 2,0,1,   2,-1,-2,0,1,
                                   -2,1,-2,0,1,  -2,-1, 2,0,1)
        api_vector_seq(self.vrot, self.brot, 0, 2, 1, API_VECTOR_IPL_LINEAR)
        api_vector_seq(self.vpos, self.bpos, 0, 4, 1, API_VECTOR_IPL_SPLINE)
        api_vector_const(self.vscl, 0.5, 0.5, 0.5, 0)
        api_matrix_pos_scl_rot(self.mloc, self.vpos, self.vscl, self.vrot, API_MATRIX_AXIS_Y, 0)
        api_matrix_mul(self.msmall, self.mrb, self.mloc)
    end

    function obj.construct_visual(self)
        self.mesh_big = api_mesh_alloc(API_MESH_TRIANGLES, self.vb, self.ib, -1, self.mrb, 0, 36)
        self.mesh_small = api_mesh_alloc(API_MESH_TRIANGLES, self.vb, self.ib, -1, self.msmall, 0, 36)
    end

    function obj.construct_physics(self)
        local size = api_vector_alloc()
        api_vector_const(size, 1, 1, 1, 0)
        self.cs = api_physics_cs_alloc_box(1000, size)
        self.rb = api_physics_rb_alloc(self.cs, self.mbig, 1, 1)
        api_matrix_rigid_body(self.mrb, self.rb)
        api_vector_free(size)
    end

    function obj.construct(self, x, y, z)
        self:construct_vb()
        self:construct_ib()
        self:construct_matrices(x, y, z)
        self:construct_physics()
        self:construct_visual()
    end

    function obj.destruct(self)
        api_vbuf_free(self.vb)
        api_ibuf_free(self.ib)
        api_matrix_free(self.mrb)
        api_matrix_free(self.mbig)
        api_matrix_free(self.mloc)
        api_matrix_free(self.msmall)
        api_vector_free(self.vrot)
        api_vector_free(self.vpos)
        api_vector_free(self.vscl)
        api_buf_free(self.brot)
        api_buf_free(self.bpos)
        api_mesh_free(self.mesh_big)
        api_mesh_free(self.mesh_small)
        api_physics_rb_free(self.rb)
        api_physics_cs_free(self.cs)
    end

    obj:construct(x, y, z)
    return obj
end

CAR_CH_SIZE_X = 2
CAR_CH_SIZE_Y = 1
CAR_CH_SIZE_Z = 4
CAR_CH_MASS = 800
CAR_CH_FRICT = 0.5
CAR_CH_ROLL_FRICT = 0
CAR_SUS_STIF = 20
CAR_SUS_COMP = 4.4
CAR_SUS_DAMP = 2.3
CAR_SUS_TRAV = 500
CAR_SUS_FORCE = 6000
CAR_SUS_REST = 0.6
CAR_SLIP_FRICT = 1000
CAR_ROLL_INF = 0.1
CAR_WHEEL_RADIUS = 0.5
CAR_WHEEL_POS_X = 0.9
CAR_WHEEL_POS_Y = 0.2
CAR_WHEEL_POS_Z = 1.6
CAR_ACCEL_MAX = 1000
CAR_ACCEL_PUSH = 100
CAR_ACCEL_POP = 100
CAR_BRAKE_MAX = 100
CAR_BRAKE_PUSH = 10
CAR_BRAKE_POP = 10
CAR_STEER_MAX = 0.6
CAR_STEER_PUSH = 0.05
CAR_STEER_POP = 0.05

function demo.vehicle_create(x, y, z)
    local obj = {}
    function obj.construct_vb(self)
        local vb = api_vbuf_alloc()
        api_vbuf_set(vb, 0, -1,-1, 1,   1, 0, 0, 1,   0, 0,
                             1,-1, 1,   0, 1, 0, 1,   0, 0,
                             1, 1, 1,   0, 0, 1, 1,   0, 0,
                            -1, 1, 1,   1, 1, 1, 1,   0, 0,
                            -1,-1,-1,   0, 1, 1, 1,   0, 0,
                             1,-1,-1,   0, 0, 0, 1,   0, 0,
                             1, 1,-1,   1, 1, 0, 1,   0, 0,
                            -1, 1,-1,   1, 0, 1, 1,   0, 0)
        api_vbuf_bake(vb)
        self.vb = vb
    end
    function obj.construct_ib(self)
        local ib = api_ibuf_alloc()
        api_ibuf_set(ib, 0,  0,1,2,  0,2,3,
                             1,5,6,  1,6,2,
                             5,4,7,  5,7,6,
                             4,0,3,  4,3,7,
                             3,2,6,  3,6,7,
                             1,0,4,  1,4,5)
        api_ibuf_bake(ib)
        self.ib = ib
    end
    function obj.construct_cs(self)
        local size = api_vector_alloc()
        api_vector_const(size, 0.5*CAR_CH_SIZE_X, 0.5*CAR_CH_SIZE_Y, 0.5*CAR_CH_SIZE_Z, 0)
        self.cs = api_physics_cs_alloc_box(CAR_CH_MASS, size)
        api_vector_free(size)
    end
    function obj.construct_veh(self, x, y, z)
        local m = demo.matrix_pos_rot_stop(x, y, z, API_MATRIX_AXIS_Y, math.pi)
        self.veh = api_physics_veh_alloc(self.cs, m, CAR_CH_FRICT, CAR_CH_ROLL_FRICT,
                                         CAR_SUS_STIF, CAR_SUS_COMP, CAR_SUS_DAMP,
                                         CAR_SUS_TRAV, CAR_SUS_FORCE, CAR_SLIP_FRICT)
        api_matrix_free(m)
        self.wheel_fr = self:add_wheel( CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y, CAR_WHEEL_POS_Z, 1)
        self.wheel_fl = self:add_wheel(-CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y, CAR_WHEEL_POS_Z, 1)
        self.wheel_br = self:add_wheel( CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y,-CAR_WHEEL_POS_Z, 0)
        self.wheel_bl = self:add_wheel(-CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y,-CAR_WHEEL_POS_Z, 0)
    end
    function obj.add_wheel(self, posx, posy, posz, front)
        local dir = api_vector_alloc()
        local axl = api_vector_alloc()
        local pos = api_vector_alloc()
        api_vector_const(pos, posx, posy, posz, 0)
        api_vector_const(axl, -1, 0, 0, 0)
        api_vector_const(dir, 0, -1, 0, 0)
        local wheel = api_physics_veh_add_wheel(self.veh, pos, dir, axl, CAR_SUS_REST,
                                                CAR_ROLL_INF, CAR_WHEEL_RADIUS, front)
        api_vector_free(pos)
        api_vector_free(dir)
        api_vector_free(axl)
        return wheel
    end
    function obj.construct_matrices(self)
        self.mchassis_local = demo.matrix_scl_stop(0.5*CAR_CH_SIZE_X, 0.5*CAR_CH_SIZE_Y, 0.5*CAR_CH_SIZE_Z)
        self.mchassis_physic = api_matrix_alloc()
        self.mchassis = api_matrix_alloc()
        api_matrix_vehicle_chassis(self.mchassis_physic, self.veh)
        api_matrix_mul(self.mchassis, self.mchassis_physic, self.mchassis_local)
        self.mwheel_local = demo.matrix_scl_stop(CAR_WHEEL_RADIUS, CAR_WHEEL_RADIUS, CAR_WHEEL_RADIUS)
        self.mwheel_physic = {}
        self.mwheel = {}
        for i = 0, 3 do
            self.mwheel_physic[i] = api_matrix_alloc()
            self.mwheel[i] = api_matrix_alloc()
            api_matrix_vehicle_wheel(self.mwheel_physic[i], self.veh, i)
            api_matrix_mul(self.mwheel[i], self.mwheel_physic[i], self.mwheel_local)
        end
    end
    function obj.construct_visual(self)
        self.mesh_chassis = api_mesh_alloc(API_MESH_TRIANGLES, self.vb, self.ib, -1, self.mchassis, 0, 36)
        self.mesh_wheel = {}
        for i = 0, 3 do
            self.mesh_wheel[i] = api_mesh_alloc(API_MESH_TRIANGLES, self.vb, self.ib, -1, self.mwheel[i], 0, 36)
        end
    end
    function obj.construct(self, x, y, z)
        self:construct_ib()
        self:construct_vb()
        self:construct_cs()
        self:construct_veh(x, y, z)
        self:construct_matrices()
        self:construct_visual()
    end
    function obj.destruct(self)
        for i = 0, 3 do
            api_matrix_free(self.mwheel_physic[i])
            api_matrix_free(self.mwheel[i])
            api_mesh_free(self.mesh_wheel[i])
        end
        api_mesh_free(self.mesh_chassis)
        api_matrix_free(self.mwheel_local)
        api_matrix_free(self.mchassis_local)
        api_matrix_free(self.mchassis_physic)
        api_matrix_free(self.mchassis)
        api_vbuf_free(self.vb)
        api_ibuf_free(self.ib)
        api_physics_veh_free(self.veh)
        api_physics_cs_free(self.cs)
    end
    obj.accel = 0
    obj.brake = 0
    obj.steer = 0
    function obj.update(self)
        if api_input_key(API_INPUT_KEY_I) == 1 
        and api_input_key(API_INPUT_KEY_K) == 0 then
            self.accel = self.accel + CAR_ACCEL_PUSH
            if self.accel > CAR_ACCEL_MAX then
                self.accel = CAR_ACCEL_MAX
            end
        elseif api_input_key(API_INPUT_KEY_I) == 0 
        and api_input_key(API_INPUT_KEY_K) == 1 then
            self.accel = self.accel - CAR_ACCEL_PUSH
            if self.accel < -CAR_ACCEL_MAX then
                self.accel = -CAR_ACCEL_MAX
            end
        else
            if self.accel < -CAR_ACCEL_POP then
                self.accel = self.accel + CAR_ACCEL_POP
            elseif self.accel > CAR_ACCEL_POP then
                self.accel = self.accel - CAR_ACCEL_POP
            else
                self.accel = 0
            end
        end
        if api_input_key(API_INPUT_KEY_J) == 1 
        and api_input_key(API_INPUT_KEY_L) == 0 then
            self.steer = self.steer - CAR_STEER_PUSH
            if self.steer < -CAR_STEER_MAX then
                self.steer = -CAR_STEER_MAX
            end
        elseif api_input_key(API_INPUT_KEY_J) == 0 
        and api_input_key(API_INPUT_KEY_L) == 1 then
            self.steer = self.steer + CAR_STEER_PUSH
            if self.steer > CAR_STEER_MAX then
                self.steer = CAR_STEER_MAX
            end
        else
            if self.steer < -CAR_STEER_POP then
                self.steer = self.steer + CAR_STEER_POP
            elseif self.steer > CAR_STEER_POP then
                self.steer = self.steer - CAR_STEER_POP
            else
                self.steer = 0
            end
        end
        if api_input_key(API_INPUT_KEY_SPACE) == 1 then
            self.brake = self.brake + CAR_BRAKE_PUSH
            if self.brake > CAR_BRAKE_MAX then
                self.brake = CAR_BRAKE_MAX
            end
        else
            self.brake = self.brake - CAR_BRAKE_POP
            if self.brake < 0 then
                self.brake = 0
            end
        end
        api_physics_veh_set_wheel(self.veh, self.wheel_fl, self.accel, self.brake, -self.steer)
        api_physics_veh_set_wheel(self.veh, self.wheel_fr, self.accel, self.brake, -self.steer)
        api_physics_veh_set_wheel(self.veh, self.wheel_bl, self.accel, self.brake, 0)
        api_physics_veh_set_wheel(self.veh, self.wheel_br, self.accel, self.brake, 0)
    end
    obj:construct(x, y, z)
    return obj
end

API_INPUT_KEY_ESCAPE = 0
API_INPUT_KEY_UP = 1
API_INPUT_KEY_DOWN = 2
API_INPUT_KEY_LEFT = 3
API_INPUT_KEY_RIGHT = 4
API_INPUT_KEY_PAGEUP = 5
API_INPUT_KEY_PAGEDOWN = 6
API_INPUT_KEY_MINUS = 7
API_INPUT_KEY_EQUALS = 8
API_INPUT_KEY_SPACE = 9
API_INPUT_KEY_LSHIFT = 10
API_INPUT_KEY_RSHIFT = 11
API_INPUT_KEY_LALT = 12
API_INPUT_KEY_RALT = 13
API_INPUT_KEY_LCTRL = 14
API_INPUT_KEY_RCTRL = 15
API_INPUT_KEY_TAB = 16
API_INPUT_KEY_F1 = 17
API_INPUT_KEY_F2 = 18
API_INPUT_KEY_F3 = 19
API_INPUT_KEY_F4 = 20
API_INPUT_KEY_F5 = 21
API_INPUT_KEY_F6 = 22
API_INPUT_KEY_F7 = 23
API_INPUT_KEY_F8 = 24
API_INPUT_KEY_F9 = 25
API_INPUT_KEY_F10 = 26
API_INPUT_KEY_F11 = 27
API_INPUT_KEY_F12 = 28
API_INPUT_KEY_1 = 29
API_INPUT_KEY_2 = 30
API_INPUT_KEY_3 = 31
API_INPUT_KEY_4 = 32
API_INPUT_KEY_5 = 33
API_INPUT_KEY_6 = 34
API_INPUT_KEY_7 = 35
API_INPUT_KEY_8 = 36
API_INPUT_KEY_9 = 37
API_INPUT_KEY_0 = 38
API_INPUT_KEY_A = 39
API_INPUT_KEY_B = 40
API_INPUT_KEY_C = 41
API_INPUT_KEY_D = 42
API_INPUT_KEY_E = 43
API_INPUT_KEY_F = 44
API_INPUT_KEY_G = 45
API_INPUT_KEY_H = 46
API_INPUT_KEY_I = 47
API_INPUT_KEY_J = 48
API_INPUT_KEY_K = 49
API_INPUT_KEY_L = 50
API_INPUT_KEY_M = 51
API_INPUT_KEY_N = 52
API_INPUT_KEY_O = 53
API_INPUT_KEY_P = 54
API_INPUT_KEY_Q = 55
API_INPUT_KEY_R = 56
API_INPUT_KEY_S = 57
API_INPUT_KEY_T = 58
API_INPUT_KEY_U = 59
API_INPUT_KEY_V = 60
API_INPUT_KEY_W = 61
API_INPUT_KEY_X = 62
API_INPUT_KEY_Y = 63
API_INPUT_KEY_Z = 64

API_VECTOR_IPL_LINEAR = 0
API_VECTOR_IPL_SPLINE = 1

API_MESH_TRIANGLE_STRIP = 0
API_MESH_TRIANGLE_FAN = 1
API_MESH_TRIANGLES = 2

API_MATRIX_AXIS_X = 0
API_MATRIX_AXIS_Y = 1
API_MATRIX_AXIS_Z = 2

API_PHYSICS_NO_DEBUG = 0
API_PHYSICS_DRAW_WIREFRAME = math.pow(2, 0)
API_PHYSICS_DRAW_AABB = math.pow(2, 1)
API_PHYSICS_DRAW_FEATURES_TEXT = math.pow(2, 2)
API_PHYSICS_DRAW_CONTACT_POINTS = math.pow(2, 3)
API_PHYSICS_NO_DEACTIVATION = math.pow(2, 4)
API_PHYSICS_NO_HELP_TEXT = math.pow(2, 5)
API_PHYSICS_DRAW_TEXT = math.pow(2, 6)
API_PHYSICS_PROFILE_TIMINGS = math.pow(2, 7)
API_PHYSICS_ENABLE_SAT_COMPARISON = math.pow(2, 8)
API_PHYSICS_DISABLE_BULLET_LCP = math.pow(2, 9)
API_PHYSICS_ENABLE_CCD = math.pow(2, 10)
API_PHYSICS_DRAW_CONSTRAINTS = math.pow(2, 11)
API_PHYSICS_DRAW_CONSTRAINT_LIMITS = math.pow(2, 12)
API_PHYSICS_FAST_WIREFRAME = math.pow(2, 13)
API_PHYSICS_DRAW_NORMALS = math.pow(2, 14)

API_TEXT_FONT_8_BY_13 = 0
API_TEXT_FONT_9_BY_15 = 1
API_TEXT_FONT_TIMES_ROMAN_10 = 2
API_TEXT_FONT_TIMES_ROMAN_24 = 3
API_TEXT_FONT_HELVETICA_10 = 4
API_TEXT_FONT_HELVETICA_12 = 5
API_TEXT_FONT_HELVETICA_18 = 6
