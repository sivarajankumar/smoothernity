local M = {}

function M.init()
    M.wld = api_physics_wld_alloc()
end

function M.done()
    api_physics_wld_free(M.wld)
end

return M
