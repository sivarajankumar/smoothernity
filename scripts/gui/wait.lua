local M = {}

local util = require 'util'
local meshes = require 'meshes'
local shader = require 'shader.shader'
local poolbuf = require 'pool.buf'
local poolibuf = require 'pool.ibuf'
local poolvbuf = require 'pool.vbuf'

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
        api_mesh_free(mesh)
    end

    function self.show()
        api_mesh_group(mesh, meshes.GROUP_GUI)
    end

    function self.hide()
        api_mesh_group(mesh, meshes.GROUP_HIDDEN)
    end

    vpos = util.vector_const(x, y, -0.5, 0)
    vscl = util.vector_const(r, r, 1, 0)
    api_matrix_pos_scl_rot(mfinal, vpos, vscl, vrot, API_MATRIX_AXIS_Z, 0)
    mesh = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf.res, ibuf.res, -1,
                          shader.default(), mfinal, ibuf.start, ibuf.size)
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
        vbuf = poolvbuf.alloc(3)
        api_vbuf_map(vbuf.res, vbuf.start, vbuf.size)
        api_vbuf_set(vbuf.res, vbuf.start, x1,y1, 0,   r, g, b, a,   0, 0,
                                           x2,y2, 0,   r, g, b, a,   0, 0,
                                           x3,y3, 0,   r, g, b, a,   0, 0)
        api_vbuf_unmap(vbuf.res)
    end
    do
        ibuf = poolibuf.alloc(3)
        local o = vbuf.start
        api_ibuf_map(ibuf.res, ibuf.start, ibuf.size)
        api_ibuf_set(ibuf.res, ibuf.start, o+0,o+1,o+2)
        api_ibuf_unmap(ibuf.res)
    end
    do
        vrot = api_vector_alloc()
        brot = poolbuf.alloc(10)
        api_buf_set(brot.res, brot.start,   0,0,0,0,PERIOD,   math.pi*2,0,0,0,0)
        api_vector_seq(vrot, brot.res, brot.start, 2, 1, API_VECTOR_IPL_LINEAR)
    end
end

function M.done()
    vbuf.free()
    ibuf.free()
    brot.free()
    api_vector_free(vrot)
end

return M
