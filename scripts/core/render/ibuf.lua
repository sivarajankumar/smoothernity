local M = {}

local cfg = require 'config'
local renderpool = require 'core.render.pool'
local pool = require 'core.pool.pool'

local ibufs

function M.init()
    local ibuf_api = {}
    ibuf_api.map = api_ibuf_map
    ibuf_api.unmap = api_ibuf_unmap
    ibuf_api.copy = api_ibuf_copy
    ibuf_api.waiting = api_ibuf_waiting
    ibufs = renderpool.alloc('Index buffers', cfg.IBUF_TWIN_SIZE, cfg.IBUF_COPY_SIZE,
                             cfg.IBUF_POOL, ibuf_api)
end

function M.done()
    ibufs.free()
end

function M.restore(state)
    local chunk_state, vbuf_start = unpack(state)
    local self = pool.restore_chunk(chunk_state)
    function self.set(i, ...)
        local args = {}
        for k, v in pairs({...}) do
            table.insert(args, v + vbuf_start)
        end
        api_ibuf_set(self.res, self.start + i, unpack(args))
    end
    return self
end

function M.alloc(size, vbuf)
    local self = ibufs.alloc(size)
    function self.set(i, ...)
        assert(self.state == 'prepared')
        local args = {}
        for k, v in pairs({...}) do
            table.insert(args, v + vbuf.start)
        end
        api_ibuf_set(self.copy.res, self.copy.start + i, unpack(args))
    end
    function self.store()
        assert(self.state == 'prepared')
        return string.format('{%s, %i}', self.copy.store(), vbuf.start)
    end
    return self
end

function M.update()
    ibufs.update()
end

function M.update_copy(twin)
    ibufs.update_copy(twin)
end

function M.sync_copy_ready()
    return ibufs.sync_copy_ready()
end

function M.sync_copy()
    ibufs.sync_copy()
end

return M
