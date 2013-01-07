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
    while not quit
    do
        local time = api_time(self)
        while api_time(self) - time < 300000
        do
            api_sleep(self);
        end
    end
end
