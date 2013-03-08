local M = {}

function M.init()
    M.wld = api_physics_wld_alloc()
end

function M.done()
    api_physics_wld_free(M.wld)
end

function M.set_gravity(x, y, z)
    local grav = api_vector_alloc()
    api_vector_const(grav, x, y, z, 0)
    api_physics_wld_gravity(M.wld, grav)
    api_vector_free(grav)
end

return M
