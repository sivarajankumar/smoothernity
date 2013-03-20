local M = {}

local cfg = require 'config'
local pool = require 'core.twin.pool'
local mesh = require 'core.twin.mesh'
local twinpool = require 'core.twin.pool'
local pool = require 'core.pool.pool'

local vbufs, ibufs

function M.init()
    vbufs = twinpool.alloc('Vertex buffers', cfg.VBUF_TWIN_SIZE, cfg.VBUF_COPY_SIZE, cfg.VBUF_POOL)
    ibufs = twinpool.alloc('Index buffers', cfg.IBUF_TWIN_SIZE, cfg.IBUF_COPY_SIZE, cfg.IBUF_POOL)
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
        assert(state == 'prepared')
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
        assert(state == 'prepared')
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

function M.draw_meshes(group, draw_tag)
    api_mesh_draw(group.twin(twin.active()), draw_tag)
end

local function update_bufs()

        function chunk.prepare()
            copy = copy_pool.alloc(size)
            copy.map()
        end

        function chunk.finalize()
            chunk.finalize1()
            util.sync_wait()
            twin.swap()
            chunk.finalize2()
            util.sync_wait()
        end

        function chunk.finalize1()
            copy.unmap()
            copy.copy(inactive())
        end

        function chunk.finalize2()
            copy.copy(inactive())
            copy.free()
            copy = nil
        end

        function chunk.map()
            res_api.map(chunk.res, chunk.start, chunk.size)
            while res_api.waiting(chunk.res) do
                coroutine.yield(true)
            end
        end
        function chunk.unmap()
            res_api.unmap(chunk.res)
            while res_api.waiting(chunk.res) do
                coroutine.yield(true)
            end
        end
        function chunk.copy(chunk_to)
            res_api.copy(chunk.res, chunk_to.res, chunk.start, chunk_to.start, chunk_to.size)
            while res_api.waiting(chunk.res) do
                coroutine.yield(true)
            end
        end
end

function M.finish_frame()
    update_bufs()
    api_render_swap()
end

return M
