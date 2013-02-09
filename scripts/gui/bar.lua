local M = {}

local util = require 'util'
local meshes = require 'meshes'
local shader = require 'shader.shader'

local ibuf, vbuf

local BACK_COLOR = function() return 0, 0, 0, 1 end
local BACK_VBUF_OFS = 0
local BACK_IBUF_OFS = 0

local FRONT_COLOR = function() return 0, 1, 0, 1 end
local FRONT_VBUF_OFS = 4
local FRONT_IBUF_OFS = 6

function M.alloc(xmin, ymin, xmax, ymax)
    local self = {}
    local mesh_back, mesh_front, mback, vfront_pos, vfront_scl
    local mfront = api_matrix_alloc()
    local mfront_local = api_matrix_alloc()
    local vzero = util.vector_const(0, 0, 0, 0)

    function self.free()
        api_mesh_free(mesh_back)
        api_mesh_free(mesh_front)
        api_matrix_free(mback)
        api_matrix_free(mfront)
        api_matrix_free(mfront_local)
        api_vector_free(vfront_pos)
        api_vector_free(vfront_scl)
        api_vector_free(vzero)
    end

    function self.set(value)
        api_vector_const(vfront_scl, value, 1, 1, 0)
    end

    -- matrices
    do
        local centx, centy = 0.5*(xmin+xmax), 0.5*(ymin+ymax)
        local sclx, scly = 0.5*(xmax-xmin), 0.5*(ymax-ymin)
        mback = util.matrix_pos_scl_stop(centx, centy, -0.5, sclx, scly, 1)
        vfront_pos = util.vector_const(-1, 0, 0.1, 0)
        vfront_scl = util.vector_const(0, 1, 1, 0)
        api_matrix_pos_scl_rot(mfront_local, vfront_pos, vfront_scl, vzero, API_MATRIX_AXIS_X, 0)
        api_matrix_mul(mfront, mback, mfront_local)
    end

    -- visual
    do
        mesh_back = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf, -1,
                                   shader.default(), mback, BACK_IBUF_OFS, 6)
        mesh_front = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf, -1,
                                    shader.default(), mfront, FRONT_IBUF_OFS, 6)
    end

    return self
end

function M.init()
    -- vertex buffer
    do
        vbuf = api_vbuf_alloc()
        local i = BACK_VBUF_OFS
        local r, g, b, a = BACK_COLOR()
        api_vbuf_set(vbuf, i, -1,-1, 0,   r, g, b, a,   0, 0,
                              -1, 1, 0,   r, g, b, a,   0, 0,
                               1,-1, 0,   r, g, b, a,   0, 0,
                               1, 1, 0,   r, g, b, a,   0, 0)
        local i = FRONT_VBUF_OFS
        local r, g, b, a = FRONT_COLOR()
        api_vbuf_set(vbuf, i, 0,-1, 0,   r, g, b, a,   0, 0,
                              0, 1, 0,   r, g, b, a,   0, 0,
                              2,-1, 0,   r, g, b, a,   0, 0,
                              2, 1, 0,   r, g, b, a,   0, 0)
        api_vbuf_bake(vbuf)
    end
    -- index buffer
    do
        ibuf = api_ibuf_alloc()
        local vofs, iofs = BACK_VBUF_OFS, BACK_IBUF_OFS
        api_ibuf_set(ibuf, iofs,  vofs+1,vofs+0,vofs+2,
                                  vofs+1,vofs+2,vofs+3)
        local vofs, iofs = FRONT_VBUF_OFS, FRONT_IBUF_OFS
        api_ibuf_set(ibuf, iofs,  vofs+1,vofs+0,vofs+2,
                                  vofs+1,vofs+2,vofs+3)
        api_ibuf_bake(ibuf)
    end
end

function M.done()
    api_vbuf_free(vbuf)
    api_ibuf_free(ibuf)
end

return M
