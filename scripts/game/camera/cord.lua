local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local colshape = require 'core.colshape'
local cfg = require 'config'
local coremtx = require 'core.matrix'
local vector = require 'core.vector'

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

    self.matrix = coremtx.alloc()
    local vtgt_center = vector.alloc()
    local vtgt_center_xz = vector.alloc()
    local vcam_to = vector.alloc()
    local vcam_to_smooth = vector.alloc()
    local vcam_to_rubber = vector.alloc()
    local vcam_to_y = vector.alloc()
    local vcam_to_ofs = vector.alloc()
    local vcam_from = vector.alloc()
    local vcam_from_smooth = vector.alloc()
    local vcam_from_rubber = vector.alloc()
    local vcam_from_xz = vector.alloc()
    local vcam_from_y = vector.alloc()
    local vcam_from_ofs = vector.alloc()
    local vcam_ofs_weights = vector.alloc()
    local vcast_from = vector.alloc()
    local vcast_sky_ofs = vector.alloc()
    local vcast_sky = vector.alloc()
    local mcast_sky = coremtx.alloc()
    local mcast_ground = coremtx.alloc()
    local vzero = vector.alloc()
    local vone = vector.alloc()
    local vup = vector.alloc()
    local sphere

    function self.free()
        self.matrix.free()
        vtgt_center.free()
        vtgt_center_xz.free()
        vcam_to.free()
        vcam_to_smooth.free()
        vcam_to_rubber.free()
        vcam_to_y.free()
        vcam_to_ofs.free()
        vcam_from.free()
        vcam_from_smooth.free()
        vcam_from_rubber.free()
        vcam_from_xz.free()
        vcam_from_y.free()
        vcam_from_ofs.free()
        vcam_ofs_weights.free()
        vcast_from.free()
        vcast_sky_ofs.free()
        vcast_sky.free()
        mcast_sky.free()
        mcast_ground.free()
        vzero.free()
        vone.free()
        vup.free()
        sphere.free()
    end

    function self.move(vofs)
        util.vector_move(vcam_from_smooth, vofs)
        util.vector_move(vcam_to_smooth, vofs)
        util.vector_move_xz(vcam_from_xz, vofs)
        vcam_from_xz.cord(vtgt_center_xz, CORD_MIN, CORD_MAX)
        vcam_from_smooth.rubber(vcast_from, vcam_from_rubber)
        vcam_to_smooth.rubber(vcam_to, vcam_to_rubber)
    end

    function self.save()
        local x, y, z, w = vcam_from_xz.get()
        util.async_write(util.uid_save(string.format('%s.lua', uid)),
            string.format('return %f, %f, %f', x, y, z))
    end

    -- collision sphere
    do
        local sx, sy = util.camera_dims()
        local sr = math.sqrt(sx*sx + sy*sy)
        local r = math.sqrt(sr*sr + cfg.CAMERA_DIST*cfg.CAMERA_DIST)
        sphere = colshape.alloc_sphere(r * SPHERE_SCALE)
    end

    vzero.const(0, 0, 0, 0)
    vone.const(1, 1, 1, 1)
    vup.const(0, 1, 0, 0)
    vcast_sky_ofs.const(0, cfg.LAND_HEIGHT, 0, 0)
    vcam_from_ofs.const(0, FROM_OFFSET_Y, 0, 0)
    vcam_to_ofs.const(0, TO_OFFSET_Y, 0, 0)
    vcam_ofs_weights.const(1, 1, 0, 0)
    vcam_from_rubber.const(FROM_RUBBER_XZ,
                           FROM_RUBBER_Y,
                           FROM_RUBBER_XZ, 0)
    vcam_to_rubber.const(TO_RUBBER_XZ,
                         TO_RUBBER_Y,
                         TO_RUBBER_XZ, 0)

    local x, y, z
    local chunk = util.async_read(util.uid_save(string.format('%s.lua', uid)))
    if chunk == '' then
        x, y, z = startx, starty, startz
    else
        x, y, z = loadstring(chunk)()
    end

    vtgt_center.mpos(mstarttgt)
    vtgt_center_xz.pick(vtgt_center, vzero, vtgt_center, vzero)

    vcam_from_xz.const(x, 0, z, 0)
    vcam_from_xz.cord(vtgt_center_xz, CORD_MIN, CORD_MAX)
    vcam_from_y.wsum(vcam_ofs_weights, vtgt_center, vcam_from_ofs, vzero, vzero)
    vcam_from.pick(vcam_from_xz, vcam_from_y, vcam_from_xz, vzero)

    vcast_sky.wsum(vcam_ofs_weights, vcam_from, vcast_sky_ofs, vzero, vzero)
    mcast_sky.pos_scl_rot(vcast_sky, vone, vzero, API_MATRIX_AXIS_X, 0)
    mcast_ground.pos_scl_rot(vcam_from, vone, vzero, API_MATRIX_AXIS_X, 0)
    vcast_from.cast(pwld.wld, sphere, mcast_sky, mcast_ground)
    vcast_from.update(0, API_VECTOR_FORCED_UPDATE)

    util.vector_copy(vcam_from_smooth, vcast_from)
    vcam_from_smooth.rubber(vcast_from, vcam_from_rubber)

    vcam_to_y.wsum(vcam_ofs_weights, vtgt_center, vcam_to_ofs, vzero, vzero)
    vcam_to.pick(vtgt_center_xz, vcam_to_y, vtgt_center_xz, vzero)
    vcam_to.update(0, API_VECTOR_FORCED_UPDATE)
    util.vector_copy(vcam_to_smooth, vcam_to)
    vcam_to_smooth.rubber(vcam_to, vcam_to_rubber)

    self.matrix.from_to_up(vcam_from_smooth, vcam_to_smooth, vup)

    return self
end

return M
