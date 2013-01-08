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
            api_sleep(self);
        end
    end
    while not quit
    do
        for i = 0, 255 do
            api_display_set_clear_color(i / 255, i / 255, i / 255, i / 255)
            api_sleep(self)
            if quit then
                break
            end
        end
    end
end
