local M = {}

local util = require 'util'
local meshes = require 'meshes'
local shader = require 'shader.shader'

local ibuf, vbuf, vcolfr, vcolbk

local BACK_COLOR = function() return 0, 0, 0, 1 end
local FRONT_COLOR = function() return 0, 1, 0, 1 end

function M.alloc(xmin, ymin, xmax, ymax)
    local self = {}
    local mesh_back, mesh_front, mback, vfront_pos, vfront_scl
    local mfront = api_matrix_alloc()
    local mfront_local = api_matrix_alloc()
    local vzero = util.vector_const(0, 0, 0, 0)
    local ucolfr, ucolbk

    function self.free()
        api_mesh_free(mesh_back)
        api_mesh_free(mesh_front)
        api_matrix_free(mback)
        api_matrix_free(mfront)
        api_matrix_free(mfront_local)
        api_vector_free(vfront_pos)
        api_vector_free(vfront_scl)
        api_vector_free(vzero)
        api_shuni_free(ucolfr)
        api_shuni_free(ucolbk)
    end

    function self.set(value)
        api_vector_const(vfront_scl, value, 1, 1, 0)
    end

    do
        local centx, centy = 0.5*(xmin+xmax), 0.5*(ymin+ymax)
        local sclx, scly = 0.5*(xmax-xmin), 0.5*(ymax-ymin)
        mback = util.matrix_pos_scl_stop(xmin, centy, -0.5, sclx, scly, 1)
        vfront_pos = util.vector_const(0, 0, 0.1, 0)
        vfront_scl = util.vector_const(0, 1, 1, 0)
        api_matrix_pos_scl_rot(mfront_local, vfront_pos, vfront_scl, vzero, API_MATRIX_AXIS_X, 0)
        api_matrix_mul(mfront, mback, mfront_local)
    end

    do
        mesh_back = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf, -1,
                                   shader.default(), mback, 0, 6)
        mesh_front = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf, -1,
                                    shader.default(), mfront, 0, 6)
        ucolfr = api_shuni_alloc_vector(shader.default(), mesh_front, 'color', vcolfr)
        ucolbk = api_shuni_alloc_vector(shader.default(), mesh_back, 'color', vcolbk)
    end

    return self
end

function M.init()
    do
        vbuf = api_vbuf_alloc()
        api_vbuf_set(vbuf, 0, 0,-1, 0,   1, 1, 1, 1,   0, 0,
                              0, 1, 0,   1, 1, 1, 1,   0, 0,
                              2,-1, 0,   1, 1, 1, 1,   0, 0,
                              2, 1, 0,   1, 1, 1, 1,   0, 0)
        api_vbuf_bake(vbuf)
    end
    do
        ibuf = api_ibuf_alloc()
        api_ibuf_set(ibuf, 0,  1,0,2,  1,2,3)
        api_ibuf_bake(ibuf)
    end
    do
        vcolfr = util.vector_const(FRONT_COLOR())
        vcolbk = util.vector_const(BACK_COLOR())
    end
end

function M.done()
    api_vbuf_free(vbuf)
    api_ibuf_free(ibuf)
    api_vector_free(vcolfr)
    api_vector_free(vcolbk)
end

return M
