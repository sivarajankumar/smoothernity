local M = {}

local render = require 'game.render'
local poolbuf = require 'core.pool.buf'

function M.alloc()
    local self = {}
    local buf = poolbuf.alloc(10)
    function self.free()
        buf.free()
    end
    api_buf_set(buf.start,   0,0.5,0,1,1,   0,0,0.5,1,1)
    render.visual.vclrcol.seq(buf, 2, 1, API_VECTOR_IPL_SPLINE)
    return self
end

return M
