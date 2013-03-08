local M = {}

local cfg = require 'config'
local util = require 'core.util'

function M.thread_run(thi)
    local uid = util.uid_save(string.format('%s.lua', api_thread_respond(thi, '')))
    local data = util.sync_read(uid)
    if data == '' then
        local f = io.open(uid, 'w')
        f:write('return {\n')
        for z = 0, cfg.NOISE_SIZE - 1 do
            if z > 0 then
                f:write(',\n')
            end
            f:write(string.format('    [%i] = {\n', z))
            for x = 0, cfg.NOISE_SIZE - 1 do
                if x > 0 then
                    f:write(',\n')
                end
                f:write(string.format('        [%i] = %f', x, math.random()))
            end
            f:write('\n    }')
        end
        f:write('\n}\n')
        f:close()
        data = util.sync_read(uid)
    end
    api_thread_respond(thi, data)
end

return M
