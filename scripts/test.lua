quit = false

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

function configure()
    return {["mpool_sizes"] = function() return   100, 1000, 10000, 100000, 1000000, 10000000 end,
            ["mpool_counts"] = function() return 1000,  100,   100,     10,       1,        1 end,
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
            ["buf_size"] = 10000,
            ["buf_count"] = 10}
end

function control(self)
    local debug = 0
    while not quit
    do
        if api_input_key(API_INPUT_KEY_ESCAPE) == 1 then
            quit = true
        end
        if api_input_key(API_INPUT_KEY_F1) == 1 then
            if debug == 0 then
                debug = 1
                api_physics_set_ddraw(API_PHYSICS_DRAW_WIREFRAME)
                api_display_draw_scene(0)
            else
                debug = 0
                api_physics_set_ddraw(API_PHYSICS_NO_DEBUG)
                api_display_draw_scene(1)
            end
            while api_input_key(API_INPUT_KEY_F1) == 1 do
                api_yield(self)
            end
        end
        api_yield(self)
    end
end

function work(self)

    function wait(us)
        local time = api_time(self)
        while api_time(self) - time < us
        do
            api_sleep(self)
        end
    end

    local v0 = api_vector_alloc()
    local v1 = api_vector_alloc()
    api_vector_const(v0, 0, 0.05, 0, 1)
    api_vector_const(v1, 0, 0, 0.05, 1)

    local v = api_vector_alloc()
    local buf = api_buf_alloc()
    api_buf_set(buf, 0, 0,0.05,   0,1,1,
                        0,   0,0.05,1,1)
    api_vector_seq(v, buf, 0, 2, 1, API_VECTOR_IPL_SPLINE)
    api_display_clear_color(v)

    local vb = api_vbuf_alloc()
    api_vbuf_write(vb, 0,   -1,-1, 1,   1, 0, 0, 1,   0, 0)
    api_vbuf_write(vb, 1,    1,-1, 1,   0, 1, 0, 1,   0, 0)
    api_vbuf_write(vb, 2,    1, 1, 1,   0, 0, 1, 1,   0, 0)
    api_vbuf_write(vb, 3,   -1, 1, 1,   1, 1, 1, 1,   0, 0)
    api_vbuf_write(vb, 4,   -1,-1,-1,   0, 1, 1, 1,   0, 0)
    api_vbuf_write(vb, 5,    1,-1,-1,   0, 0, 0, 1,   0, 0)
    api_vbuf_write(vb, 6,    1, 1,-1,   1, 1, 0, 1,   0, 0)
    api_vbuf_write(vb, 7,   -1, 1,-1,   1, 0, 1, 1,   0, 0)
    api_vbuf_bake(vb)

    local ib = api_ibuf_alloc()
    api_ibuf_write(ib, 0, 0) api_ibuf_write(ib, 1, 1) api_ibuf_write(ib, 2, 2)
    api_ibuf_write(ib, 3, 0) api_ibuf_write(ib, 4, 2) api_ibuf_write(ib, 5, 3)
    api_ibuf_write(ib, 6, 1) api_ibuf_write(ib, 7, 5) api_ibuf_write(ib, 8, 6)
    api_ibuf_write(ib, 9, 1) api_ibuf_write(ib,10, 6) api_ibuf_write(ib,11, 2)
    api_ibuf_write(ib,12, 5) api_ibuf_write(ib,13, 4) api_ibuf_write(ib,14, 7)
    api_ibuf_write(ib,15, 5) api_ibuf_write(ib,16, 7) api_ibuf_write(ib,17, 6)
    api_ibuf_write(ib,18, 4) api_ibuf_write(ib,19, 0) api_ibuf_write(ib,20, 3)
    api_ibuf_write(ib,21, 4) api_ibuf_write(ib,22, 3) api_ibuf_write(ib,23, 7)
    api_ibuf_write(ib,24, 3) api_ibuf_write(ib,25, 2) api_ibuf_write(ib,26, 6)
    api_ibuf_write(ib,27, 3) api_ibuf_write(ib,28, 6) api_ibuf_write(ib,29, 7)
    api_ibuf_write(ib,30, 1) api_ibuf_write(ib,31, 0) api_ibuf_write(ib,32, 4)
    api_ibuf_write(ib,33, 1) api_ibuf_write(ib,34, 4) api_ibuf_write(ib,35, 5)
    api_ibuf_bake(ib)

    local rot1 = api_vector_alloc()
    api_vector_const(rot1, 0, 0, 0, 0)

    local rot2 = api_vector_alloc()
    local buf = api_buf_alloc()
    api_buf_set(buf, 0, 0,0,0,0,4, math.pi*2,0,0,0,0)
    api_vector_seq(rot2, buf, 0, 2, 1, API_VECTOR_IPL_LINEAR)

    local pos1 = api_vector_alloc()
    local buf = api_buf_alloc()
    api_buf_set(buf, 0, 2,1,0,0,1, 2,-1,0,0,1)
    api_vector_seq(pos1, buf, 0, 2, 1, API_VECTOR_IPL_SPLINE)

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
    local rb = api_physics_rb_alloc(cs, m1)
    api_matrix_rigid_body(m1, rb)

    --
    -- ground
    --

    local mposrot = api_matrix_alloc()
    local pos = api_vector_alloc()
    local rot = api_vector_alloc()
    local scl = api_vector_alloc()
    api_vector_const(pos, 0, -15, -3, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_vector_const(scl, 1, 1, 1, 0)
    api_matrix_pos_scl_rot(mposrot, pos, scl, rot, API_MATRIX_AXIS_Y, 0)

    local mscale = api_matrix_alloc()
    local pos = api_vector_alloc()
    local rot = api_vector_alloc()
    local scl = api_vector_alloc()
    api_vector_const(pos, 0, 0, 0, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_vector_const(scl, 20, 2, 20, 0)
    api_matrix_pos_scl_rot(mscale, pos, scl, rot, API_MATRIX_AXIS_Y, 0)

    local mmul = api_matrix_alloc()
    api_matrix_mul(mmul, mposrot, mscale)

    api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, mmul, 0, 36)

    local scale = api_vector_alloc()
    api_vector_const(scale, 8, 4, 8, 0)
    local buf = api_buf_alloc()
    api_buf_set(buf, 0,  1, 1, 1, 1, 1, 1,
                         1, 0, 0, 0, 0, 1,
                         1, 0, 1, 1, 0, 1, 
                         1, 0, 1, 1, 0, 1,
                         1, 0, 0, 0, 0, 1,
                         1, 1, 1, 1, 1, 1)
    local cs = api_physics_cs_alloc_hmap(buf, 0, 6, 6, 0, 1, scale)
    local rb = api_physics_rb_alloc(cs, mposrot)

    local mrb = api_matrix_alloc()
    api_matrix_rigid_body(mrb, rb)
    api_matrix_mul(mmul, mrb, mscale)

    --
    -- camera
    --

    local cam = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, 0, -10, 20, 0)
    api_vector_const(scl, 1, 1, 1, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_matrix_pos_scl_rot(cam, pos, scl, rot, API_MATRIX_AXIS_X, 0)
    api_vector_const(pos, 0, 0, 0, 0)
    api_matrix_stop(cam)

    local delta = 0.05

    local move_left = api_matrix_alloc()
    local pos_left = api_vector_alloc()
    api_vector_const(pos_left, -delta, 0, 0, 0)
    api_matrix_pos_scl_rot(move_left, pos_left, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(move_left)
    api_vector_free(pos_left)

    local move_right = api_matrix_alloc()
    local pos_right = api_vector_alloc()
    api_vector_const(pos_right, delta, 0, 0, 0)
    api_matrix_pos_scl_rot(move_right, pos_right, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(move_right)
    api_vector_free(pos_right)

    local move_up = api_matrix_alloc()
    local pos_up = api_vector_alloc()
    api_vector_const(pos_up, 0, delta, 0, 0)
    api_matrix_pos_scl_rot(move_up, pos_up, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(move_up)
    api_vector_free(pos_up)

    local move_down = api_matrix_alloc()
    local pos_down = api_vector_alloc()
    api_vector_const(pos_down, 0, -delta, 0, 0)
    api_matrix_pos_scl_rot(move_down, pos_down, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(move_down)
    api_vector_free(pos_down)

    local move_fwd = api_matrix_alloc()
    local pos_fwd = api_vector_alloc()
    api_vector_const(pos_fwd, 0, 0, -delta, 0)
    api_matrix_pos_scl_rot(move_fwd, pos_fwd, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(move_fwd)
    api_vector_free(pos_fwd)

    local move_back = api_matrix_alloc()
    local pos_back = api_vector_alloc()
    api_vector_const(pos_back, 0, 0, delta, 0)
    api_matrix_pos_scl_rot(move_back, pos_back, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(move_back)
    api_vector_free(pos_back)

    local rot_deltas = api_vector_alloc()
    api_vector_const(rot_deltas, 0.01, -0.01, 0, 0)

    local look_left = api_matrix_alloc()
    local look_right = api_matrix_alloc()
    local look_up = api_matrix_alloc()
    local look_down = api_matrix_alloc()
    local roll_left = api_matrix_alloc()
    local roll_right = api_matrix_alloc()
    api_matrix_pos_scl_rot(look_left, pos, scl, rot_deltas, API_MATRIX_AXIS_Y, 0)
    api_matrix_pos_scl_rot(look_right, pos, scl, rot_deltas, API_MATRIX_AXIS_Y, 1)
    api_matrix_pos_scl_rot(look_up, pos, scl, rot_deltas, API_MATRIX_AXIS_X, 0)
    api_matrix_pos_scl_rot(look_down, pos, scl, rot_deltas, API_MATRIX_AXIS_X, 1)
    api_matrix_pos_scl_rot(roll_left, pos, scl, rot_deltas, API_MATRIX_AXIS_Z, 0)
    api_matrix_pos_scl_rot(roll_right, pos, scl, rot_deltas, API_MATRIX_AXIS_Z, 1)
    api_matrix_stop(look_left)
    api_matrix_stop(look_right)
    api_matrix_stop(look_up)
    api_matrix_stop(look_down)
    api_matrix_stop(roll_left)
    api_matrix_stop(roll_right)

    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    api_vector_free(rot_deltas)

    local invcam = api_matrix_alloc()
    api_matrix_inv(invcam, cam)
    api_display_camera(invcam)

    while not quit
    do
        if api_input_key(API_INPUT_KEY_E) == 1 then
            api_matrix_mul_stop(cam, cam, move_fwd)
        end
        if api_input_key(API_INPUT_KEY_D) == 1 then
            api_matrix_mul_stop(cam, cam, move_back)
        end
        if api_input_key(API_INPUT_KEY_S) == 1 then
            api_matrix_mul_stop(cam, cam, move_left)
        end
        if api_input_key(API_INPUT_KEY_F) == 1 then
            api_matrix_mul_stop(cam, cam, move_right)
        end
        if api_input_key(API_INPUT_KEY_A) == 1 then
            api_matrix_mul_stop(cam, cam, move_up)
        end
        if api_input_key(API_INPUT_KEY_Z) == 1 then
            api_matrix_mul_stop(cam, cam, move_down)
        end
        if api_input_key(API_INPUT_KEY_LEFT) == 1 then
            api_matrix_mul_stop(cam, cam, look_left)
        end
        if api_input_key(API_INPUT_KEY_RIGHT) == 1 then
            api_matrix_mul_stop(cam, cam, look_right)
        end
        if api_input_key(API_INPUT_KEY_UP) == 1 then
            api_matrix_mul_stop(cam, cam, look_up)
        end
        if api_input_key(API_INPUT_KEY_DOWN) == 1 then
            api_matrix_mul_stop(cam, cam, look_down)
        end
        if api_input_key(API_INPUT_KEY_PAGEUP) == 1 then
            api_matrix_mul_stop(cam, cam, roll_left)
        end
        if api_input_key(API_INPUT_KEY_PAGEDOWN) == 1 then
            api_matrix_mul_stop(cam, cam, roll_right)
        end
        api_sleep(self)
    end
end
