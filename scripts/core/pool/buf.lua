local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'

local bufs
local buf_api = {}

function buf_api.set(res, i, ...)
    api_buf_set(i, ...)
end

function M.init()
    bufs = pool.alloc('Buffers', cfg.BUF_SIZE, 0, 1, cfg.BUF_POOL, buf_api)
end

function M.done()
    bufs.free()
    bufs = nil
end

function M.alloc(size)
    return bufs.alloc(size)
end

function M.restore(state)
    return pool.restore_chunk(state, buf_api)
end

return M
