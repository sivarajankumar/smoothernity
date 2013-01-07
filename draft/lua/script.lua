function thread1(self)
    local counter = 0
    while true
    do
        io.write("First thread yields ", counter, "\n");
        myyield(self)
        counter = counter + 1
    end
end

function thread2(self)
    local counter = 100
    while true
    do
        io.write("Second thread yields ", counter, "\n");
        mycount(self, 3)
        counter = counter + 1
    end
end
