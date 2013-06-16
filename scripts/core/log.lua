local M = {}

function log(level, ...)
    local d = debug.getinfo(3)
    api_log_out(level, d.short_src, d.currentline, string.format(...))
end

function M.err(...)
    log(API_LOG_ERROR, ...)
end

function M.info(...)
    log(API_LOG_INFO, ...)
end

return M
