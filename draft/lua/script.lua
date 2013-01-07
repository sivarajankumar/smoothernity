function thread1()
    counter = 0
    while true
    do
        io.write("First thread yields ", counter, "\n");
        coroutine.yield()
        counter = counter + 1
    end
end

function thread2()
    counter = 100
    while true
    do
        io.write("Second thread yields ", counter, "\n");
        coroutine.yield()
        counter = counter + 1
    end
end
