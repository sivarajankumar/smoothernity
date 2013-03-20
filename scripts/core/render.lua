local M = {}

local cfg = require 'config'
local mesh = require 'core.twin.mesh'
local twinpool = require 'core.twin.pool'
local pool = require 'core.pool.pool'

local SWITCH_THRESH = 10

local vbufs, ibufs

function M.init()
    local vbuf_api = {}
    vbuf_api.map = api_vbuf_map
    vbuf_api.unmap = api_vbuf_unmap
    vbuf_api.copy = api_vbuf_copy

    local ibuf_api = {}
    ibuf_api.map = api_ibuf_map
    ibuf_api.unmap = api_ibuf_unmap
    ibuf_api.copy = api_ibuf_copy

    vbufs = twinpool.alloc('Vertex buffers', cfg.VBUF_TWIN_SIZE, cfg.VBUF_COPY_SIZE, cfg.VBUF_POOL, vbuf_api)
    ibufs = twinpool.alloc('Index buffers', cfg.IBUF_TWIN_SIZE, cfg.IBUF_COPY_SIZE, cfg.IBUF_POOL, ibuf_api)
end

function M.done()
    vbufs.free()
    ibufs.free()
end

function M.vbuf_restore(state)
    local self = pool.restore_chunk(state)
    function self.set(i, ...)
        api_vbuf_set(self.res, self.start + i, ...)
    end
    return self
end

function M.ibuf_restore(state)
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

function M.vbuf_alloc(size)
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

function M.ibuf_alloc(size, vbuf)
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

function M.group_alloc()
    return mesh.group()
end

function M.mesh_alloc(group, kind, vbuf, ibuf, shader, matrix)
    return mesh.alloc(group, kind, vbuf, ibuf, shader, matrix)
end

function M.mesh_draw(group, draw_tag)
    api_mesh_draw(group.twin(twin.active()), draw_tag)
end

function M.mesh_update(group, dt, update_tag)
    api_mesh_update(group.twin(twin.active()), dt, update_tag)
end

local function update_bufs()
    vbufs.update()
    ibufs.update()
    if vbufs.ready_to_switch() and ibufs.ready_to_switch() then
        switch_count = switch_count + 1
        if switch_count >= SWITCH_THRESH then
            vbufs.switch()
            ibufs.switch()
            twin.switch()
        end
    else
        switch_count = 0
    end
end

function M.finish_frame()
    update_bufs()
    api_render_swap()
end

return M
