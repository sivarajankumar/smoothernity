local M = {}

local cfg = require 'config'
local renderpool = require 'core.render.pool'
local pool = require 'core.pool.pool'

local vbufs

function M.init()
    local vbuf_api = {}
    vbuf_api.map = api_vbuf_map
    vbuf_api.unmap = api_vbuf_unmap
    vbuf_api.copy = api_vbuf_copy
    vbuf_api.waiting = api_vbuf_waiting
    vbufs = renderpool.alloc('Vertex buffers', cfg.VBUF_TWIN_SIZE, cfg.VBUF_COPY_SIZE,
                             cfg.VBUF_POOL, vbuf_api)
end

function M.done()
    vbufs.free()
end

function M.restore(state)
    local self = pool.restore_chunk(state)
    function self.set(i, ...)
        api_vbuf_set(self.res, self.start + i, ...)
    end
    return self
end

function M.alloc(size)
    local self = vbufs.alloc(size)
    function self.set(i, ...)
        assert(self.state == 'prepared')
        api_vbuf_set(self.copy.res, self.copy.start + i, ...)
    end
    function self.store()
        assert(self.state == 'prepared')
        return self.copy.store()
    end
    return self
end

function M.update()
    vbufs.update()
end

function M.update_copy(twin)
    vbufs.update_copy(twin)
end

function M.sync_copy_ready()
    return vbufs.sync_copy_ready()
end

function M.sync_copy()
    vbufs.sync_copy()
end

return M
