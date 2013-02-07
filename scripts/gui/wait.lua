local M = {}

local util = require 'util'
local meshes = require 'meshes'

local ibuf, vbuf, vrot, brot

local COLOR = function() return 0, 1, 0, 1 end
local PERIOD = 1

function M.alloc(x, y, r)
    local self = {}
    local mesh, vpos, vscl
    local mfinal = api_matrix_alloc()

    function self.free()
        api_matrix_free(mfinal)
        api_vector_free(vpos)
        api_vector_free(vscl)
        if mesh ~= nil then
            api_mesh_free(mesh)
        end
    end

    function self.show()
        if mesh == nil then
            mesh = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf, -1,
                                  mfinal, 0, 3)
        end
    end

    function self.hide()
        if mesh ~= nil then
            api_mesh_free(mesh)
            mesh = nil
        end
    end

    do
        vpos = util.vector_const(x, y, -0.5, 0)
        vscl = util.vector_const(r, r, 1, 0)
        api_matrix_pos_scl_rot(mfinal, vpos, vscl, vrot, API_MATRIX_AXIS_Z, 0)
    end

    return self
end

function M.init()
    do
        local function cossin(deg) return math.cos(deg * math.pi / 180),
                                          math.sin(deg * math.pi / 180) end
        local x1, y1 = cossin(90)
        local x2, y2 = cossin(90 + 120)
        local x3, y3 = cossin(90 + 120 + 120)
        local r, g, b, a = COLOR()
        vbuf = api_vbuf_alloc()
        api_vbuf_set(vbuf, 0, x1,y1, 0,   r, g, b, a,   0, 0,
                              x2,y2, 0,   r, g, b, a,   0, 0,
                              x3,y3, 0,   r, g, b, a,   0, 0)
        api_vbuf_bake(vbuf)
    end
    do
        ibuf = api_ibuf_alloc()
        api_ibuf_set(ibuf, 0, 0,1,2)
        api_ibuf_bake(ibuf)
    end
    do
        vrot = api_vector_alloc()
        brot = api_buf_alloc()
        api_buf_set(brot, 0,   0,0,0,0,PERIOD,   math.pi*2,0,0,0,0)
        api_vector_seq(vrot, brot, 0, 2, 1, API_VECTOR_IPL_LINEAR)
    end
end

function M.done()
    api_vbuf_free(vbuf)
    api_ibuf_free(ibuf)
    api_buf_free(brot)
    api_vector_free(vrot)
end

return M
