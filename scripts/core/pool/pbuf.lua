local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'

local pbufs

local pbuf_api = {}
pbuf_api.set = api_pbuf_set
pbuf_api.map = api_pbuf_map
pbuf_api.unmap = api_pbuf_unmap

function M.init()
    pbufs = pool.alloc('Pixel buffers', cfg.PBUF_SIZE, 0, cfg.PBUF_COUNT, cfg.PBUF_POOL, pbuf_api)
end

function M.done()
    pbufs.free()
    pbufs = nil
end

function M.alloc(size)
    return pbufs.alloc(size)
end

function M.restore(state)
    return pool.restore_chunk(state, pbuf_api)
end

return M

