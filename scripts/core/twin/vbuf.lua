local M = {}

local cfg = require 'config'
local twinpool = require 'core.twin.pool'

local vbufs

local vbuf_api = {}
vbuf_api.set = api_vbuf_set
vbuf_api.map = api_vbuf_map
vbuf_api.unmap = api_vbuf_unmap
vbuf_api.copy = api_vbuf_copy

function M.init()
    vbufs = twinpool.alloc('Vertex buffers', cfg.VBUF_TWIN_SIZE, cfg.VBUF_COPY_SIZE, cfg.VBUF_POOL, vbuf_api)
end

function M.done()
    vbufs.free()
    vbufs = nil
end

function M.alloc(size)
    return vbufs.alloc(size)
end

function M.restore(state)
    return twinpool.restore_chunk(state, vbuf_api)
end

return M
