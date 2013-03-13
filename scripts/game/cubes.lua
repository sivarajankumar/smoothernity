local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local meshes = require 'game.meshes'
local shader = require 'game.shader'
local poolbuf = require 'core.pool.buf'
local twinvbuf = require 'core.twin.vbuf'
local twinibuf = require 'core.twin.ibuf'
local twinmesh = require 'core.twin.mesh'
local rigidbody = require 'core.rigidbody'
local colshape = require 'core.colshape'
local matrix = require 'core.matrix'
local vector = require 'core.vector'

function M.alloc(x, y, z)
    local self = {}

    local vb = twinvbuf.alloc(8)
    local ib = twinibuf.alloc(36)
    local mbig = util.matrix_pos_stop(x, y, z)
    local mrb = matrix.alloc()
    local mloc = matrix.alloc()
    local msmall = matrix.alloc()
    local brot = poolbuf.alloc(10)
    local bpos = poolbuf.alloc(20)
    local vrot = vector.alloc()
    local vpos = vector.alloc()
    local vscl = vector.alloc()
    local mesh_big
    local mesh_small
    local cs
    local rb

    function self.free()
        vb.free()
        ib.free()
        mrb.free()
        mbig.free()
        mloc.free()
        msmall.free()
        vrot.free()
        vpos.free()
        vscl.free()
        brot.free()
        bpos.free()
        mesh_big.free()
        mesh_small.free()
        rb.free()
        cs.free()
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
        vrot.seq(brot, 2, 1, API_VECTOR_IPL_LINEAR)
        vpos.seq(bpos, 4, 1, API_VECTOR_IPL_SPLINE)
        vscl.const(0.5, 0.5, 0.5, 0)
        mloc.pos_scl_rot(vpos, vscl, vrot, API_MATRIX_AXIS_Y, 0)
        msmall.mul(mrb, mloc)
    end

    -- physics
    do
        local size = vector.alloc()
        size.const(1, 1, 1, 0)
        cs = colshape.alloc_box(size)
        rb = rigidbody.alloc(pwld.wld, cs, mbig, 1000, 1, 1)
        mrb.rigid_body(rb)
        size.free()
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
