function thread1(self)
    for i = 1, 5
    do
        api_yield(self)
    end
end

function thread2(self)
    for i = 1, 30
    do
        api_sleep(self, 300000);
    end
end
