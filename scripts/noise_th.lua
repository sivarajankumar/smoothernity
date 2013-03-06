local M = {}

local cfg = require 'config'
local util = require 'util'

function M.thread_run(thi)
    local uid = api_thread_respond(thi, '')
    local fname = util.uid_save(string.format('%s.lua', uid))

    local data = util.fread(fname)
    if not data then
        local f = io.open(fname, 'w')
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
        data = util.fread(fname)
    end
    api_thread_respond(thi, data)
end

return M
