local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local bufs

function M.init()
    bufs = pool.alloc('Buffers', cfg.BUF_SIZE, cfg.BUF_COUNT, cfg.BUF_POOL,
                      api_buf_alloc, api_buf_free)
end

function M.done()
    bufs.free()
    bufs = nil
end

function M.alloc(size)
    return bufs.alloc(size)
end

return M
