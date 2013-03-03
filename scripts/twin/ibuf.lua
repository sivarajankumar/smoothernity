local M = {}

local cfg = require 'config'
local twinpool = require 'twin.pool'

local ibufs

function M.init()
    ibufs = twinpool.alloc('Index buffers', cfg.IBUF_SIZE, cfg.IBUF_COUNT,
                           cfg.IBUF_POOL, api_ibuf_alloc, api_ibuf_free,
                           api_ibuf_set, api_ibuf_map, api_ibuf_unmap)
end

function M.done()
    ibufs.free()
    ibufs = nil
end

function M.alloc(size)
    return ibufs.alloc(size)
end

return M
