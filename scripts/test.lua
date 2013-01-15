quit = false

CAMERA_MOVE_SLOW = 0.05
CAMERA_MOVE_FAST = 0.25
CAMERA_ROTATE_SLOW = 0.01
CAMERA_ROTATE_FAST = 0.02

function configure()
    return {["mpool_sizes"] = function() return  1000, 10000, 100000, 1000000, 10000000 end,
            ["mpool_counts"] = function() return 1000,   100,     10,       1,        1 end,
            ["logic_time"] = 10000,
            ["gc_step"] = 10,
            ["min_delay"] = 1000,
            ["display_width"] = 1920,
            ["display_height"] = 1080,
            ["fps"] = 60,
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

function control(state)
    local ds = demo["ddraw_switcher_create"]()
    while not quit
    do
        if api_input_key(API_INPUT_KEY_ESCAPE) == 1 then
            quit = true
        end
        ds["update"](ds)
        api_yield(state)
    end
end

function work(state)

    local v = api_vector_alloc()
    local buf = api_buf_alloc()
    api_buf_set(buf, 0,   0,0.05,0,1,1,   0,0,0.05,1,1)
    api_vector_seq(v, buf, 0, 2, 1, API_VECTOR_IPL_SPLINE)
    api_display_clear_color(v)

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

    local ib = api_ibuf_alloc()
    api_ibuf_set(ib, 0, 0, 1, 2,
                        0, 2, 3,
                        1, 5, 6,
                        1, 6, 2,
                        5, 4, 7,
                        5, 7, 6,
                        4, 0, 3,
                        4, 3, 7,
                        3, 2, 6,
                        3, 6, 7,
                        1, 0, 4,
                        1, 4, 5)
    api_ibuf_bake(ib)

    local rot1 = api_vector_alloc()
    api_vector_const(rot1, 0, 0, 0, 0)

    local rot2 = api_vector_alloc()
    local buf = api_buf_alloc()
    api_buf_set(buf, 0,   0,0,0,0,3,   math.pi*2,0,0,0,0)
    api_vector_seq(rot2, buf, 0, 2, 1, API_VECTOR_IPL_LINEAR)

    local pos1 = api_vector_alloc()
    local buf = api_buf_alloc()
    api_buf_set(buf, 0,   2,1, 2,0,1,   2,-1,-2,0,1,
                         -2,1,-2,0,1,  -2,-1, 2,0,1)
    api_vector_seq(pos1, buf, 0, 4, 1, API_VECTOR_IPL_SPLINE)

    local m1 = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    api_vector_const(pos, 0, 0, -5, 0)
    api_vector_const(scl, 1, 1, 1, 0)
    api_matrix_pos_scl_rot(m1, pos, scl, rot1, API_MATRIX_AXIS_Y, 0)

    local m2 = api_matrix_alloc()
    local scl = api_vector_alloc()
    api_vector_const(scl, 0.5, 0.5, 0.5, 0)
    api_matrix_pos_scl_rot(m2, pos1, scl, rot2, API_MATRIX_AXIS_Y, 0)

    local m3 = api_matrix_alloc()
    api_matrix_mul(m3, m1, m2)

    local e1 = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, m1, 0, 36)
    local e2 = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, m3, 0, 36)

    local t1 = api_text_alloc("Hello world!", API_TEXT_FONT_8_BY_13, 0, 13)
    local t2 = api_text_alloc("Life is good!", API_TEXT_FONT_8_BY_13, 0, 30)

    --
    -- drop
    --

    local grav = api_vector_alloc()
    api_vector_const(grav, 0, -10, 0, 0)
    api_physics_set_gravity(grav)

    local size = api_vector_alloc()
    api_vector_const(size, 1, 1, 1, 0)
    local cs = api_physics_cs_alloc_box(10, size)
    local rb = api_physics_rb_alloc(cs, m1, 1, 1)
    api_matrix_rigid_body(m1, rb)

    --
    -- ground
    --

    local vb = api_vbuf_alloc()
    api_vbuf_set(vb, 0, -2, 1,-2,   0, 0, 1, 1,   0, 0,
                        -1, 1,-2,   0, 1, 0, 1,   0, 0,
                         0, 1,-2,   0, 1, 1, 1,   0, 0,
                         1, 1,-2,   1, 0, 0, 1,   0, 0,
                         2, 1,-2,   1, 0, 1, 1,   0, 0)

    api_vbuf_set(vb, 5, -2, 1,-1,   1, 1, 0, 1,   0, 0,
                        -1, 0,-1,   1, 1, 1, 1,   0, 0,
                         0, 0,-1,   0, 0, 1, 1,   0, 0,
                         1, 0,-1,   0, 1, 0, 1,   0, 0,
                         2, 1,-1,   0, 1, 1, 1,   0, 0)

    api_vbuf_set(vb, 10,-2, 1, 0,   1, 0, 0, 1,   0, 0,
                        -1, 0, 0,   1, 0, 1, 1,   0, 0,
                         0, 1, 0,   1, 1, 0, 1,   0, 0,
                         1, 0, 0,   1, 1, 1, 1,   0, 0,
                         2, 1, 0,   0, 0, 1, 1,   0, 0)

    api_vbuf_set(vb, 15,-2, 1, 1,   0, 1, 0, 1,   0, 0,
                        -1, 0, 1,   0, 1, 1, 1,   0, 0,
                         0, 0, 1,   1, 0, 0, 1,   0, 0,
                         1, 0, 1,   1, 0, 1, 1,   0, 0,
                         2, 1, 1,   1, 1, 0, 1,   0, 0)

    api_vbuf_set(vb, 20,-2, 1, 2,   1, 1, 1, 1,   0, 0,
                        -1, 1, 2,   0, 0, 1, 1,   0, 0,
                         0, 1, 2,   0, 1, 0, 1,   0, 0,
                         1, 1, 2,   0, 1, 1, 1,   0, 0,
                         2, 1, 2,   1, 0, 0, 1,   0, 0)
    api_vbuf_bake(vb)

    local ib = api_ibuf_alloc()
    api_ibuf_set(ib, 0*6*4,   0, 5, 1, 1, 5, 6,   1, 6, 2, 2, 6, 7,   2, 7, 3, 3, 7, 8,   3, 8, 4, 4, 8, 9)
    api_ibuf_set(ib, 1*6*4,   5,10, 6, 6,10,11,   6,11, 7, 7,11,12,   7,12, 8, 8,12,13,   8,13, 9, 9,13,14)
    api_ibuf_set(ib, 2*6*4,  10,15,11,11,15,16,  11,16,12,12,16,17,  12,17,13,13,17,18,  13,18,14,14,18,19)
    api_ibuf_set(ib, 3*6*4,  15,20,16,16,20,21,  16,21,17,17,21,22,  17,22,18,18,22,23,  18,23,19,19,23,24)
    api_ibuf_bake(ib)

    local mstart = api_matrix_alloc()
    local pos = api_vector_alloc()
    local rot = api_vector_alloc()
    local scl = api_vector_alloc()
    api_vector_const(pos, 0, -15, -3, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_vector_const(scl, 1, 1, 1, 0)
    api_matrix_pos_scl_rot(mstart, pos, scl, rot, API_MATRIX_AXIS_Y, 0)

    local mvis = api_matrix_alloc()
    local pos = api_vector_alloc()
    local rot = api_vector_alloc()
    local scl = api_vector_alloc()
    api_vector_const(pos, 0, -1, 0, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_vector_const(scl, 10, 2, 10, 0)
    api_matrix_pos_scl_rot(mvis, pos, scl, rot, API_MATRIX_AXIS_Y, 0)

    local scale = api_vector_alloc()
    api_vector_const(scale, 10, 2, 10, 0)
    local buf = api_buf_alloc()
    api_buf_set(buf, 0,  1, 1, 1, 1, 1,
                         1, 0, 0, 0, 1,
                         1, 0, 1, 0, 1, 
                         1, 0, 0, 0, 1,
                         1, 1, 1, 1, 1)
    local cs = api_physics_cs_alloc_hmap(buf, 0, 5, 5, 0, 1, scale)
    local rb = api_physics_rb_alloc(cs, mstart, 1, 1)

    local mmul = api_matrix_alloc()
    local mrb = api_matrix_alloc()
    api_matrix_rigid_body(mrb, rb)
    api_matrix_mul(mmul, mrb, mvis)

    api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, mmul, 0, 4*6*4)

    --
    -- camera
    --

    local freecam = demo["free_camera_create"](0, -10, 20)
    local invcam = api_matrix_alloc()
    api_matrix_inv(invcam, freecam["matrix"])
    api_display_camera(invcam)

    while not quit
    do
        freecam["update"](freecam)
        api_sleep(state)
    end

    freecam["destruct"](freecam)
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

demo = {}
demo["ddraw_switcher_create"] = function ()
    return {
        ["debug"] = 0,
        ["pressed"] = 0,
        ["update"] = function(self)
            if self["pressed"] == 0 then
                if api_input_key(API_INPUT_KEY_F1) == 1 then
                    self["pressed"] = 1
                    if self["debug"] == 0 then
                        self["debug"] = 1
                        api_physics_set_ddraw(API_PHYSICS_DRAW_WIREFRAME)
                        api_display_draw_scene(0)
                    else
                        self["debug"] = 0
                        api_physics_set_ddraw(API_PHYSICS_NO_DEBUG)
                        api_display_draw_scene(1)
                    end
                end
            elseif self["pressed"] == 1 then
                if api_input_key(API_INPUT_KEY_F1) == 0 then
                    self["pressed"] = 0
                end
            end
        end
    }
end

demo["matrix_pos_stop"] = function(x, y, z)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, x, y, z, 0)
    api_vector_const(scl, 1, 1, 1, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

demo["matrix_rot_stop"] = function(axis, angle)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, 0, 0, 0, 0)
    api_vector_const(scl, 1, 1, 1, 0)
    api_vector_const(rot, angle, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, axis, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

demo["matrix_move"] = function(m, x, y, z)
    local dm = demo["matrix_pos_stop"](x, y, z)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

demo["matrix_rotate"] = function(m, axis, angle)
    local dm = demo["matrix_rot_stop"](axis, angle)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

demo["free_camera_create"] = function(x, y, z)
    local new_cam = {
        ["matrix"] = nil,
        ["construct"] = function(self)
            self["matrix"] = demo["matrix_pos_stop"](x, y, z)
        end,
        ["destruct"] = function(self)
            api_matrix_free(self["matrix"])
            self["matrix"] = nil
        end,
        ["update"] = function(self)
            local ofs = CAMERA_MOVE_SLOW
            local ang = CAMERA_ROTATE_SLOW
            if api_input_key(API_INPUT_KEY_LSHIFT) == 1 then
                ofs = CAMERA_MOVE_FAST
                ang = CAMERA_ROTATE_FAST
            end
        
            if api_input_key(API_INPUT_KEY_E) == 1 then
                demo["matrix_move"](self["matrix"], 0, 0, -ofs)
            end
            if api_input_key(API_INPUT_KEY_D) == 1 then
                demo["matrix_move"](self["matrix"], 0, 0, ofs)
            end
            if api_input_key(API_INPUT_KEY_S) == 1 then
                demo["matrix_move"](self["matrix"], -ofs, 0, 0)
            end
            if api_input_key(API_INPUT_KEY_F) == 1 then
                demo["matrix_move"](self["matrix"], ofs, 0, 0)
            end
            if api_input_key(API_INPUT_KEY_A) == 1 then
                demo["matrix_move"](self["matrix"], 0, ofs, 0)
            end
            if api_input_key(API_INPUT_KEY_Z) == 1 then
                demo["matrix_move"](self["matrix"], 0, -ofs, 0)
            end
            if api_input_key(API_INPUT_KEY_LEFT) == 1 then
                demo["matrix_rotate"](self["matrix"], API_MATRIX_AXIS_Y, ang)
            end
            if api_input_key(API_INPUT_KEY_RIGHT) == 1 then
                demo["matrix_rotate"](self["matrix"], API_MATRIX_AXIS_Y, -ang)
            end
            if api_input_key(API_INPUT_KEY_UP) == 1 then
                demo["matrix_rotate"](self["matrix"], API_MATRIX_AXIS_X, ang)
            end
            if api_input_key(API_INPUT_KEY_DOWN) == 1 then
                demo["matrix_rotate"](self["matrix"], API_MATRIX_AXIS_X, -ang)
            end
            if api_input_key(API_INPUT_KEY_PAGEUP) == 1 then
                demo["matrix_rotate"](self["matrix"], API_MATRIX_AXIS_Z, ang)
            end
            if api_input_key(API_INPUT_KEY_PAGEDOWN) == 1 then
                demo["matrix_rotate"](self["matrix"], API_MATRIX_AXIS_Z, -ang)
            end
        end
    }
    new_cam["construct"](new_cam)
    return new_cam
end

demo["wait"] = function(state, us)
    local time = api_time(state)
    while api_time(state) - time < us
    do
        api_sleep(state)
    end
end
