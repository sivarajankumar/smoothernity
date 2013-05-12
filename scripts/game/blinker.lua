local M = {}

local poolbuf = require 'core.pool.buf'
local vector = require 'core.vector'

function M.alloc()
    local self = {}
    local buf = poolbuf.alloc(10)
    local color = vector.alloc()
    function self.free()
        buf.free()
        color.free()
    end
    self.update = color.update
    self.color_id = color.id
    buf.set(0,   0,0.5,0,1,1,   0,0,0.5,1,1)
    color.seq(buf, 2, 1, API_VECTOR_IPL_SPLINE)
    return self
end

return M

