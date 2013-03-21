local M = {}

local cfg = require 'config'
local renderpool = require 'core.render.pool'
local pool = require 'core.pool.pool'
local coresync = require 'core.sync'

local SWITCH_THRESH = 10

local vbufs, ibufs, sync
local twin = 0
local switch_count = 0
local switch_state = 'copying'

function M.twin_active()
    return twin
end

function M.twin_inactive()
    return (twin + 1) % cfg.TWINS
end

function M.init()
    local vbuf_api = {}
    vbuf_api.map = api_vbuf_map
    vbuf_api.unmap = api_vbuf_unmap
    vbuf_api.copy = api_vbuf_copy
    vbuf_api.waiting = api_vbuf_waiting

    local ibuf_api = {}
    ibuf_api.map = api_ibuf_map
    ibuf_api.unmap = api_ibuf_unmap
    ibuf_api.copy = api_ibuf_copy
    ibuf_api.waiting = api_ibuf_waiting

    vbufs = renderpool.alloc('Vertex buffers', cfg.VBUF_TWIN_SIZE, cfg.VBUF_COPY_SIZE,
                             cfg.VBUF_POOL, vbuf_api)
    ibufs = renderpool.alloc('Index buffers', cfg.IBUF_TWIN_SIZE, cfg.IBUF_COPY_SIZE,
                             cfg.IBUF_POOL, ibuf_api)
end

function M.done()
    if sync then
        sync.free()
    end
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

local function update_bufs()
    vbufs.update()
    ibufs.update()
    if switch_state == 'copying' then
        vbufs.update_copy(M.twin_inactive())
        ibufs.update_copy(M.twin_inactive())
        if vbufs.sync_copy_ready() and ibufs.sync_copy_ready() then
            switch_count = switch_count + 1
            if switch_count >= SWITCH_THRESH then
                switch_count = 0
                switch_state = 'synching'
                sync = coresync.alloc()
            end
        else
            switch_count = 0
        end
    elseif switch_state == 'synching' then
        if sync.ready() or switch_count >= SWITCH_THRESH then
            switch_count = 0
            vbufs.sync_copy()
            ibufs.sync_copy()
            twin = M.twin_inactive()
            sync.free()
            sync = nil
            switch_state = 'copying'
        else
            switch_count = switch_count + 1
        end
    end
end

function M.finish_frame(prof)
    prof.cpu.rupload.start()
    prof.gpu.rupload.start()
    update_bufs()
    prof.gpu.rupload.finish()
    prof.cpu.rupload.finish()

    prof.cpu.rswap.start()
    prof.gpu.rswap.start()
    api_render_swap()
    prof.gpu.rswap.finish()
    prof.cpu.rswap.finish()
end

return M
