local M = {}

local util = require 'util'
local pwld = require 'physwld'
local cfg = require 'config'

CORD_MIN = 20
CORD_MAX = 20
FROM_OFFSET_Y = 5
FROM_RUBBER_Y = 0.01
FROM_RUBBER_XZ = 0.05
SPHERE_SCALE = 2
TO_OFFSET_Y = 1
TO_RUBBER_Y = 0.05
TO_RUBBER_XZ = 0.05

function M.alloc(uid, mstarttgt, startx, starty, startz)
    local self = {}

    self.matrix = api_matrix_alloc()
    local vtgt_center = api_vector_alloc()
    local vtgt_center_xz = api_vector_alloc()
    local vcam_to = api_vector_alloc()
    local vcam_to_smooth = api_vector_alloc()
    local vcam_to_rubber = api_vector_alloc()
    local vcam_to_y = api_vector_alloc()
    local vcam_to_ofs = api_vector_alloc()
    local vcam_from = api_vector_alloc()
    local vcam_from_smooth = api_vector_alloc()
    local vcam_from_rubber = api_vector_alloc()
    local vcam_from_xz = api_vector_alloc()
    local vcam_from_y = api_vector_alloc()
    local vcam_from_ofs = api_vector_alloc()
    local vcam_ofs_weights = api_vector_alloc()
    local vcast_from = api_vector_alloc()
    local vcast_sky_ofs = api_vector_alloc()
    local vcast_sky = api_vector_alloc()
    local mcast_sky = api_matrix_alloc()
    local mcast_ground = api_matrix_alloc()
    local vzero = api_vector_alloc()
    local vone = api_vector_alloc()
    local vup = api_vector_alloc()
    local sphere

    function self.free()
        api_matrix_free(self.matrix)
        api_vector_free(vtgt_center)
        api_vector_free(vtgt_center_xz)
        api_vector_free(vcam_to)
        api_vector_free(vcam_to_smooth)
        api_vector_free(vcam_to_rubber)
        api_vector_free(vcam_to_y)
        api_vector_free(vcam_to_ofs)
        api_vector_free(vcam_from)
        api_vector_free(vcam_from_smooth)
        api_vector_free(vcam_from_rubber)
        api_vector_free(vcam_from_xz)
        api_vector_free(vcam_from_y)
        api_vector_free(vcam_from_ofs)
        api_vector_free(vcam_ofs_weights)
        api_vector_free(vcast_from)
        api_vector_free(vcast_sky_ofs)
        api_vector_free(vcast_sky)
        api_matrix_free(mcast_sky)
        api_matrix_free(mcast_ground)
        api_vector_free(vzero)
        api_vector_free(vone)
        api_vector_free(vup)
        api_physics_cs_free(sphere)
    end

    function self.move(vofs)
        util.vector_move(vcam_from_smooth, vofs)
        util.vector_move(vcam_to_smooth, vofs)
        util.vector_move_xz(vcam_from_xz, vofs)
        api_vector_cord(vcam_from_xz, vtgt_center_xz, CORD_MIN, CORD_MAX)
        api_vector_rubber(vcam_from_smooth, vcast_from, vcam_from_rubber)
        api_vector_rubber(vcam_to_smooth, vcam_to, vcam_to_rubber)
    end

    function self.save()
        local x, y, z, w = api_vector_get(vcam_from_xz)
        util.async_write(util.uid_save(string.format('%s.lua', uid)),
            string.format('return %f, %f, %f', x, y, z))
    end

    -- collision sphere
    do
        local sx, sy = util.camera_dims()
        local sr = math.sqrt(sx*sx + sy*sy)
        local r = math.sqrt(sr*sr + cfg.CAMERA_DIST*cfg.CAMERA_DIST)
        sphere = api_physics_cs_alloc_sphere(r * SPHERE_SCALE)
    end

    api_vector_const(vzero, 0, 0, 0, 0)
    api_vector_const(vone, 1, 1, 1, 1)
    api_vector_const(vup, 0, 1, 0, 0)
    api_vector_const(vcast_sky_ofs, 0, cfg.LAND_HEIGHT, 0, 0)
    api_vector_const(vcam_from_ofs, 0, FROM_OFFSET_Y, 0, 0)
    api_vector_const(vcam_to_ofs, 0, TO_OFFSET_Y, 0, 0)
    api_vector_const(vcam_ofs_weights, 1, 1, 0, 0)
    api_vector_const(vcam_from_rubber, FROM_RUBBER_XZ,
                                       FROM_RUBBER_Y,
                                       FROM_RUBBER_XZ, 0)
    api_vector_const(vcam_to_rubber, TO_RUBBER_XZ,
                                     TO_RUBBER_Y,
                                     TO_RUBBER_XZ, 0)

    local x, y, z
    local chunk = util.async_read(util.uid_save(string.format('%s.lua', uid)))
    if chunk == '' then
        x, y, z = startx, starty, startz
    else
        x, y, z = loadstring(chunk)()
    end

    api_vector_mpos(vtgt_center, mstarttgt)
    api_vector_pick(vtgt_center_xz, vtgt_center, vzero, vtgt_center, vzero)

    api_vector_const(vcam_from_xz, x, 0, z, 0)
    api_vector_cord(vcam_from_xz, vtgt_center_xz, CORD_MIN, CORD_MAX)
    api_vector_wsum(vcam_from_y, vcam_ofs_weights, vtgt_center, vcam_from_ofs, vzero, vzero)
    api_vector_pick(vcam_from, vcam_from_xz, vcam_from_y, vcam_from_xz, vzero)

    api_vector_wsum(vcast_sky, vcam_ofs_weights, vcam_from, vcast_sky_ofs, vzero, vzero)
    api_matrix_pos_scl_rot(mcast_sky, vcast_sky, vone, vzero, API_MATRIX_AXIS_X, 0)
    api_matrix_pos_scl_rot(mcast_ground, vcam_from, vone, vzero, API_MATRIX_AXIS_X, 0)
    api_vector_cast(vcast_from, pwld.wld, sphere, mcast_sky, mcast_ground)
    api_vector_update(vcast_from, 0, API_VECTOR_FORCED_UPDATE)

    util.vector_copy(vcam_from_smooth, vcast_from)
    api_vector_rubber(vcam_from_smooth, vcast_from, vcam_from_rubber)

    api_vector_wsum(vcam_to_y, vcam_ofs_weights, vtgt_center, vcam_to_ofs, vzero, vzero)
    api_vector_pick(vcam_to, vtgt_center_xz, vcam_to_y, vtgt_center_xz, vzero)
    api_vector_update(vcam_to, 0, API_VECTOR_FORCED_UPDATE)
    util.vector_copy(vcam_to_smooth, vcam_to)
    api_vector_rubber(vcam_to_smooth, vcam_to, vcam_to_rubber)

    api_matrix_from_to_up(self.matrix, vcam_from_smooth, vcam_to_smooth, vup)

    return self
end

return M
