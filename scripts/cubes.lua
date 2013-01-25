local M = {}

local util = require 'util'
local pwld = require 'physwld'

function M.alloc(x, y, z)
    local self = {}

    local vb = api_vbuf_alloc()
    local ib = api_ibuf_alloc()
    local mbig = util.matrix_pos_stop(x, y, z)
    local mrb = api_matrix_alloc()
    local mloc = api_matrix_alloc()
    local msmall = api_matrix_alloc()
    local brot = api_buf_alloc()
    local bpos = api_buf_alloc()
    local vrot = api_vector_alloc()
    local vpos = api_vector_alloc()
    local vscl = api_vector_alloc()
    local mesh_big
    local mesh_small
    local cs
    local rb

    function self.free()
        api_vbuf_free(vb)
        api_ibuf_free(ib)
        api_matrix_free(mrb)
        api_matrix_free(mbig)
        api_matrix_free(mloc)
        api_matrix_free(msmall)
        api_vector_free(vrot)
        api_vector_free(vpos)
        api_vector_free(vscl)
        api_buf_free(brot)
        api_buf_free(bpos)
        api_mesh_free(mesh_big)
        api_mesh_free(mesh_small)
        api_physics_rb_free(rb)
        api_physics_cs_free(cs)
    end

    -- vertex buffer
    do
        api_vbuf_set(vb, 0, -1,-1, 1,   1, 0, 0, 1,   0, 0,
                             1,-1, 1,   0, 1, 0, 1,   0, 0,
                             1, 1, 1,   0, 0, 1, 1,   0, 0,
                            -1, 1, 1,   1, 1, 1, 1,   0, 0,
                            -1,-1,-1,   0, 1, 1, 1,   0, 0,
                             1,-1,-1,   0, 0, 0, 1,   0, 0,
                             1, 1,-1,   1, 1, 0, 1,   0, 0,
                            -1, 1,-1,   1, 0, 1, 1,   0, 0)
        api_vbuf_bake(vb)
    end

    -- index buffer
    do
        api_ibuf_set(ib, 0,  0,1,2,  0,2,3,
                             1,5,6,  1,6,2,
                             5,4,7,  5,7,6,
                             4,0,3,  4,3,7,
                             3,2,6,  3,6,7,
                             1,0,4,  1,4,5)
        api_ibuf_bake(ib)
    end

    -- matrices
    do
        api_buf_set(brot, 0,   0,0,0,0,3,   math.pi*2,0,0,0,0)
        api_buf_set(bpos, 0,   2,1, 2,0,1,   2,-1,-2,0,1,
                              -2,1,-2,0,1,  -2,-1, 2,0,1)
        api_vector_seq(vrot, brot, 0, 2, 1, API_VECTOR_IPL_LINEAR)
        api_vector_seq(vpos, bpos, 0, 4, 1, API_VECTOR_IPL_SPLINE)
        api_vector_const(vscl, 0.5, 0.5, 0.5, 0)
        api_matrix_pos_scl_rot(mloc, vpos, vscl, vrot, API_MATRIX_AXIS_Y, 0)
        api_matrix_mul(msmall, mrb, mloc)
    end

    -- physics
    do
        local size = api_vector_alloc()
        api_vector_const(size, 1, 1, 1, 0)
        cs = api_physics_cs_alloc_box(size)
        rb = api_physics_rb_alloc(pwld.wld, cs, mbig, 1000, 1, 1)
        api_matrix_rigid_body(mrb, rb)
        api_vector_free(size)
    end

    -- visual
    do
        mesh_big = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, mrb, 0, 36)
        mesh_small = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, msmall, 0, 36)
    end

    return self
end

return M
