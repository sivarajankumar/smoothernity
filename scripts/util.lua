local M = {}

local pwld = require 'physwld'
local cfg = require 'config'

function M.camera_dims()
    local mindim = math.min(cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT)
    return cfg.SCREEN_WIDTH / mindim, cfg.SCREEN_HEIGHT / mindim
end

function M.vector_const(x, y, z, w)
    local v = api_vector_alloc()
    api_vector_const(v, x, y, z, w)
    return v
end

function M.vector_dist(v1, v2)
    local x1, y1, z1, w1 = api_vector_get(v1)
    local x2, y2, z2, w2 = api_vector_get(v2)
    local x, y, z = x1 - x2, y1 - y2, z1 - z2
    return math.sqrt(x*x + y*y + z*z)
end

function M.vector_copy(v, src)
    local x, y, z, w = api_vector_get(src)
    api_vector_const(v, x, y, z, w)
end

function M.vector_move(v, vofs)
    local x, y, z, w = api_vector_get(v)
    local dx, dy, dz, dw = api_vector_get(vofs)
    api_vector_const(v, x + dx, y + dy, z + dz, w + dw)
end

function M.vector_move_xz(v, vofs)
    local x, y, z, w = api_vector_get(v)
    local dx, dy, dz, dw = api_vector_get(vofs)
    api_vector_const(v, x + dx, y, z + dz, w)
end

function M.spline(t, t1, t2, v0, v1, v2, v3)
    t = (t - t1) / (t2 - t1)
    assert (t >= 0 and t <= 1)
    local tt = t * t
    local ttt = tt * t
    local v = 2 * v1
    v = v + t * (-v0 + v2)
    v = v + tt * (2*v0 - 5*v1 + 4*v2 - v3)
    v = v + ttt * (-v0 + 3*v1 - 3*v2 + v3)
    v = v * 0.5
    return v
end

function M.lerp(t, t0, t1, v0, v1)
    t = math.min(t1, math.max(t0, t))
    return v0 + ((v1 - v0) * (t - t0) / (t1 - t0))
end

function M.set_gravity(x, y, z)
    local grav = api_vector_alloc()
    api_vector_const(grav, x, y, z, 0)
    api_physics_wld_gravity(pwld.wld, grav)
    api_vector_free(grav)
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
    api_matrix_update(m)
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
    return M.matrix_pos_scl_rot_stop(0, 0, 0, sx, sy, sz, API_MATRIX_AXIS_X, 0)
end

function M.matrix_move_global(m, x, y, z)
    local dm = M.matrix_pos_stop(x, y, z)
    api_matrix_mul_stop(m, dm, m)
    api_matrix_free(dm)
end

function M.matrix_move_local(m, x, y, z)
    local dm = M.matrix_pos_stop(x, y, z)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

function M.matrix_rotate_local(m, axis, angle)
    local dm = M.matrix_rot_stop(axis, angle)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

return M
