local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local ibufs

function M.init()
    ibufs = pool.alloc('Index buffers', cfg.IBUF_SIZE, cfg.IBUF_COUNT, cfg.IBUF_POOL,
                       api_ibuf_alloc, api_ibuf_free)
end

function M.done()
    ibufs.free()
    ibufs = nil
end

function M.alloc(size)
    return ibufs.alloc(size)
end

return M

