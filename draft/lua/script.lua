quit = false

MESH_TRIANGLE_STRIP = 0
MESH_TRIANGLE_FAN = 1
MESH_TRIANGLES = 2

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

    function tutorial()
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

        local s = api_space_alloc()
        api_space_offset(s, 0, 0, -5)

        local m = api_mesh_alloc(MESH_TRIANGLES, vb, ib, -1, s, 0, 36)
    end

    tutorial()

    tween = api_tween_alloc()
    if tween >= 0 then
        api_tween_play_sine(tween, 0.5, 0.5, 1.0)
        api_display_tween_clear_color(tween, -1, tween)
    end
    while not quit
    do
        for i = 0, 255, 1 do
            api_display_set_clear_color(i / 255, i / 255, i / 255)
            api_sleep(self)
            if quit then
                break
            end
        end
        for i = 255, 0, -1 do
            api_display_set_clear_color(i / 255, i / 255, i / 255)
            api_sleep(self)
            if quit then
                break
            end
        end
    end
end
