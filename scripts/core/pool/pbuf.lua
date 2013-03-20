local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'

local pbufs

function M.init()
    pbufs = pool.alloc('Pixel buffers', cfg.PBUF_SIZE, 0, cfg.PBUF_COUNT, cfg.PBUF_POOL)
end

function M.done()
    pbufs.free()
end

function M.alloc(size)
    return pbufs.alloc(size)
end

function M.restore(state)
    return pool.restore_chunk(state)
end

return M

