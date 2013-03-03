local M = {}

local util = require 'util'
local meshes = require 'meshes'
local shader = require 'shader.shader'
local twinibuf = require 'twin.ibuf'
local twinvbuf = require 'twin.vbuf'
local twinmesh = require 'twin.mesh'
local twinshuni = require 'twin.shuni'

local ibuf, vbuf

local BACK_Z = -0.5
local FRONT_Z = 0.1

function M.alloc(xmin, ymin, xmax, ymax, ...)
    local self = {}
    local mroot
    local vzero = util.vector_const(0, 0, 0, 0)
    local stripes = {}

    function self.free()
        api_matrix_free(mroot)
        api_vector_free(vzero)
        for i, s in ipairs(stripes) do
            api_vector_free(s.vpos)
            api_vector_free(s.vscl)
            api_vector_free(s.vcol)
            api_matrix_free(s.mlocal)
            api_matrix_free(s.mfinal)
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
            api_vector_const(stripe.vpos, x, 0, FRONT_Z, 0)
            api_vector_const(stripe.vscl, nv, 1, 1, 0)
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
            stripe.mlocal = api_matrix_alloc()
            stripe.mfinal = api_matrix_alloc()
            api_matrix_pos_scl_rot(stripe.mlocal, stripe.vpos, stripe.vscl, vzero, API_MATRIX_AXIS_X, 0)
            api_matrix_mul(stripe.mfinal, mroot, stripe.mlocal)
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
