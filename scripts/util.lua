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

function M.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, axis, angle)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, px, py, pz, 0)
    api_vector_const(scl, sx, sy, sz, 0)
    api_vector_const(rot, angle, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, axis, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

function M.matrix_pos_stop(x, y, z)
    return M.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, API_MATRIX_AXIS_X, 0)
end

function M.matrix_pos_scl_stop(px, py, pz, sx, sy, sz)
    return M.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, API_MATRIX_AXIS_X, 0)
end

function M.matrix_pos_rot_stop(x, y, z, axis, angle)
    return M.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, axis, angle)
end

function M.matrix_rot_stop(axis, angle)
    return M.matrix_pos_scl_rot_stop(0, 0, 0, 1, 1, 1, axis, angle)
end

function M.matrix_scl_stop(sx, sy, sz)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, 0, 0, 0, 0)
    api_vector_const(scl, sx, sy, sz, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

function M.matrix_move(m, x, y, z)
    local dm = M.matrix_pos_stop(x, y, z)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

function M.matrix_rotate(m, axis, angle)
    local dm = M.matrix_rot_stop(axis, angle)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

return M