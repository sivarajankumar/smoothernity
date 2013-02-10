local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local vbufs

function M.init()
    vbufs = pool.alloc('Vertex buffers', cfg.VBUF_SIZE, cfg.VBUF_COUNT, cfg.VBUF_POOL,
                       api_vbuf_alloc, api_vbuf_free)
end

function M.done()
    vbufs.free()
    vbufs = nil
end

function M.alloc(size)
    return vbufs.alloc(size)
end

return M
