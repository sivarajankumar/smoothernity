quit = false

API_MESH_TRIANGLE_STRIP = 0
API_MESH_TRIANGLE_FAN = 1
API_MESH_TRIANGLES = 2

API_SPACE_AXIS_X = 0
API_SPACE_AXIS_Y = 1
API_SPACE_AXIS_Z = 2

API_TEXT_FONT_8_BY_13 = 0
API_TEXT_FONT_9_BY_15 = 1
API_TEXT_FONT_TIMES_ROMAN_10 = 2
API_TEXT_FONT_TIMES_ROMAN_24 = 3
API_TEXT_FONT_HELVETICA_10 = 4
API_TEXT_FONT_HELVETICA_12 = 5
API_TEXT_FONT_HELVETICA_18 = 6

function configure()
    return {["mpool_sizes"] = function() return 64, 4096, 8192 end,
            ["mpool_counts"] = function() return 1000, 100, 10 end,
            ["logic_time"] = 10000,
            ["gc_step"] = 10,
            ["min_delay"] = 1000,
            ["display_width"] = 1920,
            ["display_height"] = 1080,
            ["fps"] = 60,
            ["tween_pool"] = 100,
            ["space_pool"] = 100,
            ["space_nesting"] = 10,
            ["mesh_pool"] = 100,
            ["vbuf_size"] = 1024,
            ["vbuf_count"] = 100,
            ["ibuf_size"] = 1024,
            ["ibuf_count"] = 100,
            ["text_size"] = 100,
            ["text_count"] = 100}
end

function control(self)
    while not quit
    do
        if api_input_key_escape() == 1 then
            quit = true
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

    local w = api_tween_alloc()
    api_tween_play_sine(w, 0.5, 0.5, 1.0)
    api_display_tween_clear_color(w, -1, w)

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

    local w1 = api_tween_alloc()
    api_tween_play_saw(w1, 0, math.pi * 2, 10)

    local w2 = api_tween_alloc()
    api_tween_play_saw(w2, 0, math.pi * 2, 4)

    local w3 = api_tween_alloc()
    api_tween_play_sine(w3, 0, 1, 1)

    local w4 = api_tween_alloc()
    api_tween_play_saw(w4, 0, math.pi * 2, 10)

    local s1 = api_space_alloc()
    api_space_offset(s1, 0, 0, -5)
    api_space_rotation_tween(s1, API_SPACE_AXIS_Y, w1)

    local s2 = api_space_alloc()
    api_space_offset(s2, 0, 0, 2)
    api_space_offset_tween(s2, -1, w3, -1)
    api_space_scale(s2, 0.5, 0.5, 0.5)
    api_space_rotation_tween(s2, API_SPACE_AXIS_Y, w2)
    api_space_attach(s2, s1)

    local s3 = api_space_alloc()
    api_space_rotation_tween(s3, API_SPACE_AXIS_X, w4)
    api_space_attach(s3, s2)

    local m1 = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, s1, 0, 36)
    local m2 = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, s3, 0, 36)

    local t1 = api_text_alloc("Hello world!", API_TEXT_FONT_8_BY_13, 0, 13)
    local t2 = api_text_alloc("Life is good!", API_TEXT_FONT_8_BY_13, 0, 30)

    while not quit
    do
        api_sleep(self)
    end
end
