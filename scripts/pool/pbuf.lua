local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local pbufs

function M.init()
    pbufs = pool.alloc('Pixel buffers', cfg.PBUF_SIZE, cfg.PBUF_COUNT, cfg.PBUF_POOL,
                       api_pbuf_alloc, api_pbuf_free, api_pbuf_map, api_pbuf_unmap)
end

function M.done()
    pbufs.free()
    pbufs = nil
end

function M.alloc(size)
    return pbufs.alloc(size)
end

return M

