local M = {}

function M.alloc()
    local self = {}
    local v = api_vector_alloc()
    local buf = api_buf_alloc()
    function self.free()
        api_vector_free(v)
        api_buf_free(buf)
    end
    api_buf_set(buf, 0,   0,0.05,0,1,1,   0,0,0.05,1,1)
    api_vector_seq(v, buf, 0, 2, 1, API_VECTOR_IPL_SPLINE)
    api_render_clear_color(v)
    return self
end

return M
