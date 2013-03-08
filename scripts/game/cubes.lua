local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local meshes = require 'game.meshes'
local shader = require 'game.shader'
local poolbuf = require 'core.pool.buf'
local twinvbuf = require 'core.twin.vbuf'
local twinibuf = require 'core.twin.ibuf'
local twinmesh = require 'core.twin.mesh'

function M.alloc(x, y, z)
    local self = {}

    local vb = twinvbuf.alloc(8)
    local ib = twinibuf.alloc(36)
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
        mesh_big.free()
        mesh_small.free()
        api_physics_rb_free(rb)
        api_physics_cs_free(cs)
    end

    -- vertex buffer
    do
        vb.prepare()
        vb.set(0,  -1,-1, 1,   1, 0, 0, 1,   0, 0,
                    1,-1, 1,   0, 1, 0, 1,   0, 0,
                    1, 1, 1,   0, 0, 1, 1,   0, 0,
                   -1, 1, 1,   1, 1, 1, 1,   0, 0,
                   -1,-1,-1,   0, 1, 1, 1,   0, 0,
                    1,-1,-1,   0, 0, 0, 1,   0, 0,
                    1, 1,-1,   1, 1, 0, 1,   0, 0,
                   -1, 1,-1,   1, 0, 1, 1,   0, 0)
        vb.finalize()
    end

    -- index buffer
    do
        ib.prepare()
        local o = vb.start
        ib.set(0,  o+0,o+1,o+2,  o+0,o+2,o+3,
                   o+1,o+5,o+6,  o+1,o+6,o+2,
                   o+5,o+4,o+7,  o+5,o+7,o+6,
                   o+4,o+0,o+3,  o+4,o+3,o+7,
                   o+3,o+2,o+6,  o+3,o+6,o+7,
                   o+1,o+0,o+4,  o+1,o+4,o+5)
        ib.finalize()
    end

    -- matrices
    do
        api_buf_set(brot.start,   0,0,0,0,3,   math.pi*2,0,0,0,0)
        api_buf_set(bpos.start,   2,1, 2,0,1,   2,-1,-2,0,1,
                                 -2,1,-2,0,1,  -2,-1, 2,0,1)
        api_vector_seq(vrot, brot.start, 2, 1, API_VECTOR_IPL_LINEAR)
        api_vector_seq(vpos, bpos.start, 4, 1, API_VECTOR_IPL_SPLINE)
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
        mesh_big = twinmesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                                  shader.default(), mrb)
        mesh_small = twinmesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                                    shader.default(), msmall)
    end

    return self
end

return M
