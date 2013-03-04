local M = {}

local cfg = require 'config'
local twinpool = require 'twin.pool'

local vbufs

function M.init()
    vbufs = twinpool.alloc('Vertex buffers', cfg.VBUF_SIZE, cfg.VBUF_COUNT,
                           cfg.VBUF_POOL, api_vbuf_alloc, api_vbuf_free,
                           api_vbuf_set, api_vbuf_map, api_vbuf_unmap,
                           api_vbuf_waiting)
end

function M.done()
    vbufs.free()
    vbufs = nil
end

function M.alloc(size)
    return vbufs.alloc(size)
end

return M
