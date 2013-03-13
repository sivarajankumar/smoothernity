local M = {}

local util = require 'core.util'
local meshes = require 'game.meshes'
local shader = require 'game.shader'
local twinibuf = require 'core.twin.ibuf'
local twinvbuf = require 'core.twin.vbuf'
local twinmesh = require 'core.twin.mesh'
local twinshuni = require 'core.twin.shuni'
local matrix = require 'core.matrix'

local ibuf, vbuf

local BACK_Z = -0.5
local FRONT_Z = 0.1

function M.alloc(xmin, ymin, xmax, ymax, ...)
    local self = {}
    local mroot
    local vzero = util.vector_const(0, 0, 0, 0)
    local stripes = {}

    function self.free()
        mroot.free()
        vzero.free()
        for i, s in ipairs(stripes) do
            s.vpos.free()
            s.vscl.free()
            s.vcol.free()
            s.mlocal.free()
            s.mfinal.free()
            s.mesh.free()
            s.ucol.free()
        end
    end

    function self.set(...)
        local sum = util.sum(...)
        local x = 0
        for i, v in ipairs({...}) do
            local stripe = stripes[i]
            local nv = 0
            if sum > 0 then
                nv = v / sum
            end
            stripe.vpos.const(x, 0, FRONT_Z, 0)
            stripe.vscl.const(nv, 1, 1, 0)
            x = x + nv
        end
    end

    do
        local centx, centy = 0.5*(xmin+xmax), 0.5*(ymin+ymax)
        local sclx, scly = xmax-xmin, ymax-ymin
        mroot = util.matrix_pos_scl_stop(xmin, centy, BACK_Z, sclx, scly, 1)
        for i, col in ipairs({...}) do
            local stripe = {}
            stripe.vpos = util.vector_const(0, 0, FRONT_Z, 0)
            stripe.vscl = util.vector_const(0, 1, 1, 0)
            stripe.vcol = util.vector_const(unpack(col))
            stripe.mlocal = matrix.alloc()
            stripe.mfinal = matrix.alloc()
            stripe.mlocal.pos_scl_rot(stripe.vpos, stripe.vscl, vzero, API_MATRIX_AXIS_X, 0)
            stripe.mfinal.mul(mroot, stripe.mlocal)
            stripe.mesh = twinmesh.alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf,
                                         shader.color(), stripe.mfinal)
            stripe.ucol = twinshuni.alloc_vector(shader.color(), stripe.mesh, 'color', stripe.vcol)
            table.insert(stripes, stripe)
        end
    end

    return self
end

function M.init()
    do
        vbuf = twinvbuf.alloc(4)
        vbuf.prepare()
        vbuf.set(0, 0,-0.5, 0,   1, 1, 1, 1,   0, 0,
                    0, 0.5, 0,   1, 1, 1, 1,   0, 0,
                    1,-0.5, 0,   1, 1, 1, 1,   0, 0,
                    1, 0.5, 0,   1, 1, 1, 1,   0, 0)
        vbuf.finalize()
    end
    do
        ibuf = twinibuf.alloc(6)
        local o = vbuf.start
        ibuf.prepare()
        ibuf.set(0,  o+1,o+0,o+2,  o+1,o+2,o+3)
        ibuf.finalize()
    end
end

function M.done()
    vbuf.free()
    ibuf.free()
end

return M
