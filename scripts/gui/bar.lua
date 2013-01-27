local M = {}

local util = require 'util'
local meshes = require 'meshes'

local ibuf, vbuf

local BACK_COLOR = function() return 0, 0, 0, 1 end
local BACK_VBUF_OFS = 0
local BACK_IBUF_OFS = 0

function M.alloc(xmin, ymin, xmax, ymax, z)
    local self = {}
    local mesh_back, mback

    function self.free()
        api_mesh_free(mesh_back)
        api_matrix_free(mback)
    end

    -- matrices
    do
        local centx, centy = 0.5*(xmin+xmax), 0.5*(ymin+ymax)
        local sclx, scly = 0.5*(xmax-xmin), 0.5*(ymax-ymin)
        mback = util.matrix_pos_scl_stop(centx, centy, z, sclx, scly, 1)
    end

    -- visual
    do
        mesh_back = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf, -1,
                                   mback, BACK_IBUF_OFS, 6)
    end

    return self
end

function M.init()
    -- vertex buffer
    do
        local r, g, b, a = BACK_COLOR()
        local i = BACK_VBUF_OFS
        vbuf = api_vbuf_alloc()
        api_vbuf_set(vbuf, i, -1,-1, 0,   r, g, b, a,   0, 0,
                              -1, 1, 0,   r, g, b, a,   0, 0,
                               1,-1, 0,   r, g, b, a,   0, 0,
                               1, 1, 0,   r, g, b, a,   0, 0)
        api_vbuf_bake(vbuf)
    end
    -- index buffer
    do
        local vofs, iofs = BACK_VBUF_OFS, BACK_IBUF_OFS
        ibuf = api_ibuf_alloc()
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
