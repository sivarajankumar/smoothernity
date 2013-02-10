local M = {}

local util = require 'util'
local meshes = require 'meshes'
local shader = require 'shader.shader'
local poolibuf = require 'pool.ibuf'
local poolvbuf = require 'pool.vbuf'

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
        mesh_back = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf.res, ibuf.res, -1,
                                   shader.default(), mback, ibuf.start, 6)
        mesh_front = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf.res, ibuf.res, -1,
                                    shader.default(), mfront, ibuf.start, 6)
        ucolfr = api_shuni_alloc_vector(shader.default(), mesh_front, 'color', vcolfr)
        ucolbk = api_shuni_alloc_vector(shader.default(), mesh_back, 'color', vcolbk)
    end

    return self
end

function M.init()
    do
        vbuf = poolvbuf.alloc(4)
        api_vbuf_map(vbuf.res, vbuf.start, vbuf.size)
        api_vbuf_set(vbuf.res, vbuf.size, 0,-1, 0,   1, 1, 1, 1,   0, 0,
                                          0, 1, 0,   1, 1, 1, 1,   0, 0,
                                          2,-1, 0,   1, 1, 1, 1,   0, 0,
                                          2, 1, 0,   1, 1, 1, 1,   0, 0)
        api_vbuf_unmap(vbuf.res)
    end
    do
        ibuf = poolibuf.alloc(6)
        local o = vbuf.start
        api_ibuf_map(ibuf.res, ibuf.start, ibuf.size)
        api_ibuf_set(ibuf.res, ibuf.start,  o+1,o+0,o+2,  o+1,o+2,o+3)
        api_ibuf_unmap(ibuf.res)
    end
    do
        vcolfr = util.vector_const(FRONT_COLOR())
        vcolbk = util.vector_const(BACK_COLOR())
    end
end

function M.done()
    vbuf.free()
    ibuf.free()
    api_vector_free(vcolfr)
    api_vector_free(vcolbk)
end

return M
