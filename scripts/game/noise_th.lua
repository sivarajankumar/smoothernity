local M = {}

local cfg = require 'config'
local util = require 'core.util'
local poolbuf = require 'core.pool.buf'

function M.thread_run(thi)
    local uid, buf_state = loadstring(api_thread_respond(thi, ''))()
    local fname = util.uid_save(string.format('%s.lua', uid))
    local buf = poolbuf.restore(buf_state)
    local data = util.sync_read(fname)
    if data == '' then
        local f = io.open(fname, 'w')
        f:write('return {')
        local cnt = 0
        for i = 1, cfg.NOISE_SIZE * cfg.NOISE_SIZE do
            if cnt >= cfg.SAVE_NUMS_PER_ROW then
                cnt = 0
            end
            if i > 1 then
                f:write(', ')
            end
            if cnt == 0 then
                f:write('\n    ')
            end
            cnt = cnt + 1
            local v = math.random()
            buf.set(i - 1, v)
            f:write(string.format('%f', v))
        end
        f:write('\n}\n')
        f:close()
    else
        for i, v in pairs(loadstring(data)()) do
            buf.set(i - 1, v)
        end
    end
end

return M
