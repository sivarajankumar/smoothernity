local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'

local bufs

function M.init()
    bufs = pool.alloc('Buffers', cfg.BUF_SIZE, 0, 1, cfg.BUF_POOL,
        function (res, i, ...) api_buf_set(i, ...) end,
        nil, nil, nil, nil)
end

function M.done()
    bufs.free()
    bufs = nil
end

function M.alloc(size)
    return bufs.alloc(size)
end

return M
