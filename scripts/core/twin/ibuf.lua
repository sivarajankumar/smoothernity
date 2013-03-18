local M = {}

local cfg = require 'config'
local twinpool = require 'core.twin.pool'

local ibufs

local ibuf_api = {}
ibuf_api.set = api_ibuf_set
ibuf_api.map = api_ibuf_map
ibuf_api.unmap = api_ibuf_unmap
ibuf_api.copy = api_ibuf_copy
ibuf_api.waiting = api_ibuf_waiting

function M.init()
    ibufs = twinpool.alloc('Index buffers', cfg.IBUF_TWIN_SIZE, cfg.IBUF_COPY_SIZE, cfg.IBUF_POOL, ibuf_api)
end

function M.done()
    ibufs.free()
    ibufs = nil
end

function M.alloc(size)
    return ibufs.alloc(size)
end

function M.restore(state)
    return twinpool.restore_chunk(state, ibuf_api)
end

return M
