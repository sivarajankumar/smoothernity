function thread1(self)
    for i = 1, 5
    do
        api_yield(self)
    end
end

function thread2(self)
    for i = 1, 30
    do
        local time = api_time(self)
        while api_time(self) - time < 300000
        do
            api_sleep(self);
        end
    end
end
