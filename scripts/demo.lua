demo = {}

function demo.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, axis, angle)
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

function demo.matrix_pos_stop(x, y, z)
    return demo.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, API_MATRIX_AXIS_X, 0)
end

function demo.matrix_pos_scl_stop(px, py, pz, sx, sy, sz)
    return demo.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, API_MATRIX_AXIS_X, 0)
end

function demo.matrix_pos_rot_stop(x, y, z, axis, angle)
    return demo.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, axis, angle)
end

function demo.matrix_rot_stop(axis, angle)
    return demo.matrix_pos_scl_rot_stop(0, 0, 0, 1, 1, 1, axis, angle)
end

function demo.matrix_scl_stop(sx, sy, sz)
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

function demo.matrix_move(m, x, y, z)
    local dm = demo.matrix_pos_stop(x, y, z)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

function demo.matrix_rotate(m, axis, angle)
    local dm = demo.matrix_rot_stop(axis, angle)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end
