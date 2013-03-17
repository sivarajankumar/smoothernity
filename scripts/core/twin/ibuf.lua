local M = {}

local cfg = require 'config'
local twinpool = require 'core.twin.pool'

local ibufs

function M.init()
    ibufs = twinpool.alloc('Index buffers', cfg.IBUF_TWIN_SIZE, cfg.IBUF_COPY_SIZE,
                           cfg.IBUF_POOL, api_ibuf_set, api_ibuf_map, api_ibuf_unmap,
                           api_ibuf_copy, api_ibuf_waiting)
end

function M.done()
    ibufs.free()
    ibufs = nil
end

function M.alloc(size)
    return ibufs.alloc(size)
end

return M
