local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local meshes = require 'game.meshes'
local shader = require 'game.shader'
local poolbuf = require 'core.pool.buf'
local render = require 'core.render.render'
local mesh = require 'core.render.mesh'
local rigidbody = require 'core.rigidbody'
local colshape = require 'core.colshape'
local matrix = require 'core.matrix'
local vector = require 'core.vector'

function M.alloc(x, y, z)
    local self = {}

    local vb = render.vbuf_alloc(8)
    local ib = render.ibuf_alloc(36, vb)
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

    -- resources
    do
        util.wait_state(true, 'prepared', vb, ib)
        vb.set(0,  -1,-1, 1,   1, 0, 0, 1,   0, 0,
                    1,-1, 1,   0, 1, 0, 1,   0, 0,
                    1, 1, 1,   0, 0, 1, 1,   0, 0,
                   -1, 1, 1,   1, 1, 1, 1,   0, 0,
                   -1,-1,-1,   0, 1, 1, 1,   0, 0,
                    1,-1,-1,   0, 0, 0, 1,   0, 0,
                    1, 1,-1,   1, 1, 0, 1,   0, 0,
                   -1, 1,-1,   1, 0, 1, 1,   0, 0)
        ib.set(0,  0,1,2,  0,2,3,
                   1,5,6,  1,6,2,
                   5,4,7,  5,7,6,
                   4,0,3,  4,3,7,
                   3,2,6,  3,6,7,
                   1,0,4,  1,4,5)

        vb.finalize()
        ib.finalize()
        util.wait_state(true, 'finalized', vb, ib)
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
        mesh_big = mesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                              shader.default(), mrb)
        mesh_small = mesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                                shader.default(), msmall)
    end

    return self
end

return M
