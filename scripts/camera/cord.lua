local M = {}

CORD_MIN = 20
CORD_MAX = 20
FROM_OFFSET_Y = 5
FROM_RUBBER_Y = 0.01
FROM_RUBBER_XZ = 0.1
TO_OFFSET_Y = 1
TO_RUBBER_Y = 0.1
TO_RUBBER_XZ = 0.1

function M.alloc(x, y, z, mtarget)
    local self = {}

    self.invmatrix = api_matrix_alloc()
    local mcam = api_matrix_alloc()
    local vcar_center = api_vector_alloc()
    local vcar_center_xz = api_vector_alloc()
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
    local vzero = api_vector_alloc()
    local vup = api_vector_alloc()

    function self.free()
        api_matrix_free(mcam)
        api_matrix_free(self.invmatrix)
        api_vector_free(vcar_center)
        api_vector_free(vcar_center_xz)
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
        api_vector_free(vzero)
        api_vector_free(vup)
    end

    api_vector_const(vzero, 0, 0, 0, 0)
    api_vector_const(vup, 0, 1, 0, 0)
    api_vector_const(vcam_from_ofs, 0, FROM_OFFSET_Y, 0, 0)
    api_vector_const(vcam_to_ofs, 0, TO_OFFSET_Y, 0, 0)
    api_vector_const(vcam_ofs_weights, 1, 1, 0, 0)
    api_vector_const(vcam_from_rubber, FROM_RUBBER_XZ,
                                       FROM_RUBBER_Y,
                                       FROM_RUBBER_XZ, 0)
    api_vector_const(vcam_to_rubber, TO_RUBBER_XZ,
                                     TO_RUBBER_Y,
                                     TO_RUBBER_XZ, 0)

    api_vector_mpos(vcar_center, mtarget)
    api_vector_pick(vcar_center_xz, vcar_center, vzero, vcar_center, vzero)

    api_vector_const(vcam_from_xz, x, 0, z, 0)
    api_vector_cord(vcam_from_xz, vcar_center_xz, CORD_MIN, CORD_MAX)
    api_vector_wsum(vcam_from_y, vcam_ofs_weights, vcar_center, vcam_from_ofs, vzero, vzero)
    api_vector_pick(vcam_from, vcam_from_xz, vcam_from_y, vcam_from_xz, vzero)
    api_vector_rubber(vcam_from_smooth, vcam_from, vcam_from_rubber)

    api_vector_wsum(vcam_to_y, vcam_ofs_weights, vcar_center, vcam_to_ofs, vzero, vzero)
    api_vector_pick(vcam_to, vcar_center_xz, vcam_to_y, vcar_center_xz, vzero)
    api_vector_rubber(vcam_to_smooth, vcam_to, vcam_to_rubber)

    api_matrix_from_to_up(mcam, vcam_from_smooth, vcam_to_smooth, vup)

    api_matrix_inv(self.invmatrix, mcam)

    return self
end

return M