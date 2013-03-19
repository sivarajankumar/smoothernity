local M = {}

local function buf_alloc(size)
    local self = {}

    local state = 'preparing'

    function self.free()
        assert(state == 'finalized')
        state = 'vacant'
    end

    function self.state()
        return oneof('vacant', 'preparing', 'prepared', 'finalizing', 'finalized')
    end

    function self.set(i, ...)
        assert(state == 'prepared')
    end

    function self.finalize()
        assert(state == 'prepared')
        state = 'finalizing'
    end

    return self
end

function M.init()
end

function M.done()
end

function M.vbuf_alloc(size)
end

function M.ibuf_alloc(size)
end

function M.group_alloc()
end

function M.mesh_alloc(ib, vb, ...)
    assert(ib.state() == 'finalized')
    assert(vb.state() == 'finalized')
end

function M.draw_meshes(group)
end

function M.finish_frame()
    update_bufs()
    api_render_swap()
end

return M
