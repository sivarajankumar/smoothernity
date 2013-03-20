local M = {}

local cfg = require 'config'
local util = require 'core.util'
local meshes = require 'game.meshes'
local shader = require 'game.shader'
local poolpbuf = require 'core.pool.pbuf'
local render = require 'core.render.render'
local shuni = require 'core.render.shuni'
local rendermesh = require 'core.render.mesh'
local matrix = require 'core.matrix'

local TEX_UNIT = 0
local TEX_LAYER = 0
local TEX_MIP = 0

local ibuf, vbuf, vtexlayer

function M.alloc(x, y, r)
    local self = {}
    local mesh, mfinal, utexunit, utexlayer

    function self.free()
        mfinal.free()
        mesh.free()
        utexunit.free()
        utexlayer.free()
    end

    do
        mfinal = util.matrix_pos_scl_stop(x,y,-0.5,  r,r,1)
        mesh = rendermesh.alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf,
                                shader.texture(), mfinal)
        utexunit = shuni.alloc_int(shader.texture(), mesh, 'texunit', TEX_UNIT)
        utexlayer = shuni.alloc_vector(shader.texture(), mesh, 'texlayer', vtexlayer)
    end
    return self
end

function M.init()
    do
        vbuf = render.vbuf_alloc(4)
        ibuf = render.ibuf_alloc(6, vbuf)

        vbuf.prepare()
        ibuf.prepare()
        util.wait_state(true, 'prepared', vbuf, ibuf)

        vbuf.set(0, -1,-1,0,  1,1,1,1,  0,0,
                     1,-1,0,  1,1,1,1,  1,0,
                     1, 1,0,  1,1,1,1,  1,1,
                    -1, 1,0,  1,1,1,1,  0,1)
        ibuf.set(0, 0,1,2,  0,2,3)

        ibuf.finalize()
        vbuf.finalize()
        util.wait_state(true, 'finalized', vbuf, ibuf)
    end
    do
        vtexlayer = util.vector_const(TEX_LAYER, 0, 0, 0)
    end
    do
        local sizelog, layers = unpack(cfg.TEX_POOL[TEX_UNIT+1])
        local size = math.pow(2, sizelog)
        pbuf = poolpbuf.alloc(size * size)
        pbuf.map()
        for y = 0, size-1 do
            for x = 0, size-1 do
                local r = ((x + y) % 16) / 16
                local g = ((x + y) % 32) / 32
                local b = ((x + y) % 64) / 64
                local a = 1
                api_pbuf_set(pbuf.res, pbuf.start + x + y*size,
                             r, g, b, a)
                coroutine.yield(false)
            end
        end
        pbuf.unmap()
        api_tex_set(TEX_UNIT, pbuf.res, pbuf.start, TEX_LAYER, TEX_MIP, 0, 0, size, size)
        pbuf.free()
    end
end

function M.done()
    vbuf.free()
    ibuf.free()
    vtexlayer.free()
end

return M

