local M = {}

function M.alloc()
    local self = {}
    local cs = {}
    local empty = true
    function self.plan(func)
        empty = false
        table.insert(cs, coroutine.create(func))
    end
    function self.empty()
        return empty
    end
    function self.run(max_steps)
        local keep_going = true
        local step = 0
        while keep_going do
            local skip_frame = false
            keep_going = false
            for k, v in pairs(cs) do
                keep_going = true
                local res, arg = coroutine.resume(v)
                if res then
                    if arg then
                        skip_frame = true
                    end
                    if coroutine.status(v) == 'dead' then
                        cs[k] = nil
                    end
                else
                    io.write('Worker coroutine\n', debug.traceback(v), '\n')
                    error(arg)
                end
                step = step + 1
                if max_steps ~= nil and step > max_steps then
                    step = 0
                    coroutine.yield(true)
                else
                    coroutine.yield(false)
                end
            end
            coroutine.yield(skip_frame)
        end
        empty = true
    end
    return self
end

return M
