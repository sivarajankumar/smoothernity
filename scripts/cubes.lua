local M = {}

local util = require 'util'
local pwld = require 'physwld'
local meshes = require 'meshes'
local shader = require 'shader.shader'
local poolbuf = require 'pool.buf'
local poolvbuf = require 'pool.vbuf'
local poolibuf = require 'pool.ibuf'

function M.alloc(x, y, z)
    local self = {}

    local vb = poolvbuf.alloc(8)
    local ib = poolibuf.alloc(36)
    local mbig = util.matrix_pos_stop(x, y, z)
    local mrb = api_matrix_alloc()
    local mloc = api_matrix_alloc()
    local msmall = api_matrix_alloc()
    local brot = poolbuf.alloc(10)
    local bpos = poolbuf.alloc(20)
    local vrot = api_vector_alloc()
    local vpos = api_vector_alloc()
    local vscl = api_vector_alloc()
    local mesh_big
    local mesh_small
    local cs
    local rb

    function self.free()
        vb.free()
        ib.free()
        api_matrix_free(mrb)
        api_matrix_free(mbig)
        api_matrix_free(mloc)
        api_matrix_free(msmall)
        api_vector_free(vrot)
        api_vector_free(vpos)
        api_vector_free(vscl)
        brot.free()
        bpos.free()
        api_mesh_free(mesh_big)
        api_mesh_free(mesh_small)
        api_physics_rb_free(rb)
        api_physics_cs_free(cs)
    end

    -- vertex buffer
    do
        api_vbuf_map(vb.res, vb.start, vb.size)
        api_vbuf_set(vb.res, vb.start,  -1,-1, 1,   1, 0, 0, 1,   0, 0,
                                         1,-1, 1,   0, 1, 0, 1,   0, 0,
                                         1, 1, 1,   0, 0, 1, 1,   0, 0,
                                        -1, 1, 1,   1, 1, 1, 1,   0, 0,
                                        -1,-1,-1,   0, 1, 1, 1,   0, 0,
                                         1,-1,-1,   0, 0, 0, 1,   0, 0,
                                         1, 1,-1,   1, 1, 0, 1,   0, 0,
                                        -1, 1,-1,   1, 0, 1, 1,   0, 0)
        api_vbuf_unmap(vb.res)
    end

    -- index buffer
    do
        api_ibuf_map(ib.res, ib.start, ib.size)
        local o = vb.start
        api_ibuf_set(ib.res, ib.start,  o+0,o+1,o+2,  o+0,o+2,o+3,
                                        o+1,o+5,o+6,  o+1,o+6,o+2,
                                        o+5,o+4,o+7,  o+5,o+7,o+6,
                                        o+4,o+0,o+3,  o+4,o+3,o+7,
                                        o+3,o+2,o+6,  o+3,o+6,o+7,
                                        o+1,o+0,o+4,  o+1,o+4,o+5)
        api_ibuf_unmap(ib.res)
    end

    -- matrices
    do
        api_buf_set(brot.res, brot.start,   0,0,0,0,3,   math.pi*2,0,0,0,0)
        api_buf_set(bpos.res, bpos.start,   2,1, 2,0,1,   2,-1,-2,0,1,
                                           -2,1,-2,0,1,  -2,-1, 2,0,1)
        api_vector_seq(vrot, brot.res, brot.start, 2, 1, API_VECTOR_IPL_LINEAR)
        api_vector_seq(vpos, bpos.res, bpos.start, 4, 1, API_VECTOR_IPL_SPLINE)
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
        mesh_big = api_mesh_alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb.res, ib.res,
                                  -1, shader.default(), mrb, ib.start, 36)
        mesh_small = api_mesh_alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb.res, ib.res,
                                    -1, shader.default(), msmall, ib.start, 36)
    end

    return self
end

return M
