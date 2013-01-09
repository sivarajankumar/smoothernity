quit = false

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
