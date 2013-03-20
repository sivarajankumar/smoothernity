local M = {}

local util = require 'core.util'
local meshes = require 'game.meshes'
local shader = require 'game.shader'
local poolbuf = require 'core.pool.buf'
local render = require 'core.render.render'
local rendermesh = require 'core.render.mesh'
local matrix = require 'core.matrix'
local vector = require 'core.vector'

local ibuf, vbuf, vrot, brot

local COLOR = function() return 0, 1, 0, 1 end
local PERIOD = 1

function M.alloc(x, y, r)
    local self = {}
    local mesh, vpos, vscl
    local mfinal = matrix.alloc()

    function self.free()
        mfinal.free()
        vpos.free()
        vscl.free()
        mesh.free()
    end

    function self.show()
        mesh.group(meshes.GROUP_GUI)
    end

    function self.hide()
        mesh.group(meshes.GROUP_HIDDEN)
    end

    vpos = util.vector_const(x, y, -0.5, 0)
    vscl = util.vector_const(r, r, 1, 0)
    mfinal.pos_scl_rot(vpos, vscl, vrot, API_MATRIX_AXIS_Z, 0)
    mesh = rendermesh.alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf,
                            shader.default(), mfinal)
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

        vbuf = render.vbuf_alloc(3)
        ibuf = render.ibuf_alloc(3, vbuf)

        util.wait_state(true, 'prepared', vbuf, ibuf)
        vbuf.set(0, x1,y1, 0,   r, g, b, a,   0, 0,
                    x2,y2, 0,   r, g, b, a,   0, 0,
                    x3,y3, 0,   r, g, b, a,   0, 0)
        ibuf.set(0, 0,1,2)

        vbuf.finalize()
        ibuf.finalize()
        util.wait_state(true, 'finalized', vbuf, ibuf)
    end
    do
        vrot = vector.alloc()
        brot = poolbuf.alloc(10)
        api_buf_set(brot.start,   0,0,0,0,PERIOD,   math.pi*2,0,0,0,0)
        vrot.seq(brot, 2, 1, API_VECTOR_IPL_LINEAR)
    end
end

function M.done()
    vbuf.free()
    ibuf.free()
    brot.free()
    vrot.free()
end

return M
