local M = {}

function M.alloc()
    local self = {}
    local cs = {}
    function self.plan(func)
        table.insert(cs, coroutine.create(func))
    end
    function self.run()
        local keep_going = true
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
                coroutine.yield(false)
            end
            coroutine.yield(skip_frame)
        end
    end
    return self
end

return M
