local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local bufpool

function M.init()
    bufpool = pool.alloc('Buffers', cfg.BUF_SIZE, cfg.BUF_COUNT, cfg.BUF_POOL,
                         api_buf_alloc, api_buf_free)
end

function M.done()
    bufpool.free()
    bufpool = nil
end

return M
