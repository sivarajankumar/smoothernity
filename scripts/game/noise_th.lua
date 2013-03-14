local M = {}

local cfg = require 'config'
local util = require 'core.util'

local NUMS_PER_ROW = 10

function M.thread_run(thi)
    local uid = util.uid_save(string.format('%s.lua', api_thread_respond(thi, '')))
    local start = api_thread_respond(thi, '')
    local data = util.sync_read(uid)
    if data == '' then
        local f = io.open(uid, 'w')
        f:write('return {')
        local cnt = 0
        for i = 1, cfg.NOISE_SIZE * cfg.NOISE_SIZE do
            if cnt >= NUMS_PER_ROW then
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
            api_buf_set(start + i - 1, v)
            f:write(string.format('%f', v))
        end
        f:write('\n}\n')
        f:close()
    else
        for i, v in pairs(loadstring(data)()) do
            api_buf_set(start + i - 1, v)
        end
    end
end

return M
