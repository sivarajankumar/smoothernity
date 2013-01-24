local M = {}

local render = require 'render'

function M.alloc()
    local self = {}
    local buf = api_buf_alloc()
    function self.free()
        api_buf_free(buf)
    end
    api_buf_set(buf, 0,   0,0.05,0,1,1,   0,0,0.05,1,1)
    api_vector_seq(render.visual.vclrcol, buf, 0, 2, 1, API_VECTOR_IPL_SPLINE)
    return self
end

return M
