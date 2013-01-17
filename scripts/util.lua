local M = {}

function M.set_gravity(x, y, z)
    local grav = api_vector_alloc()
    api_vector_const(grav, x, y, z, 0)
    api_physics_set_gravity(grav)
    api_vector_free(grav)
end

function M.wait(mach, us)
    local time = api_machine_time(mach)
    while api_machine_time(mach) - time < us
    do
        api_machine_sleep(mach)
    end
end

return M
