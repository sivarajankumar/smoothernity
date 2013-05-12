local M = {}

local util = require 'core.util'

function M.thread_run(thi)
    local fns = {}

    function fns.async_read()
        local uid = api_thread_respond(thi, '')
        api_thread_respond(thi, util.sync_read(uid))
    end

    function fns.async_write()
        local uid = api_thread_respond(thi, '')
        local data = api_thread_respond(thi, '')
        util.sync_write(uid, data)
    end

    fns[api_thread_respond(thi, '')]()
end

return M
