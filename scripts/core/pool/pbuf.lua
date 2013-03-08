local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'

local pbufs

function M.init()
    pbufs = pool.alloc('Pixel buffers', cfg.PBUF_SIZE, 0, cfg.PBUF_COUNT, cfg.PBUF_POOL,
                       api_pbuf_map, api_pbuf_unmap, api_pbuf_waiting)
end

function M.done()
    pbufs.free()
    pbufs = nil
end

function M.alloc(size)
    return pbufs.alloc(size)
end

return M

