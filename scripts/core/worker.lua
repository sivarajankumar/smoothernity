local M = {}
local util = require 'core.util'

function M.alloc()
    local self = {}
    local cs = {}
    local next_id = 0
    function self.plan(func)
        cs[next_id] = coroutine.create(func)
        next_id = next_id + 1
    end
    function self.run()
        while not util.empty(cs) do
            local skip_frame = false
            for k, v in pairs(cs) do
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
        empty = true
    end
    return self
end

return M
