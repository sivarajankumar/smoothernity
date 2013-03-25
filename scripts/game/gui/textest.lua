local M = {}

local cfg = require 'config'
local util = require 'core.util'
local meshes = require 'game.meshes'
local shader = require 'game.shader.shader'
local poolpbuf = require 'core.pool.pbuf'
local rendershuni = require 'core.render.shuni'
local rendermesh = require 'core.render.mesh'
local renderibuf = require 'core.render.ibuf'
local rendervbuf = require 'core.render.vbuf'
local matrix = require 'core.matrix'
local coretex = require 'core.tex'

local TEX_MIP = 0
local TEX_SIZE = 256

local ibuf, vbuf, tex, vtexlayer

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
        utexunit = rendershuni.alloc_int(shader.texture(), mesh, 'texunit', tex.unit())
        utexlayer = rendershuni.alloc_vector(shader.texture(), mesh, 'texlayer', vtexlayer)
    end
    return self
end

function M.init()
    do
        vbuf = rendervbuf.alloc(4)
        ibuf = renderibuf.alloc(6, vbuf)

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
        tex = coretex.alloc(TEX_SIZE)
        vtexlayer = util.vector_const(tex.layer(), 0, 0, 0)
    end
    do
        pbuf = poolpbuf.alloc(tex.size() * tex.size())
        api_pbuf_map(pbuf.res, pbuf.start, pbuf.size)
        while api_pbuf_waiting(pbuf.res) do
            coroutine.yield(true)
        end
        for y = 0, tex.size()-1 do
            for x = 0, tex.size()-1 do
                local r = ((x + y) % 16) / 16
                local g = ((x + y) % 32) / 32
                local b = ((x + y) % 64) / 64
                local a = 1
                api_pbuf_set(pbuf.res, pbuf.start + x + y*tex.size(),
                             r, g, b, a)
                coroutine.yield(false)
            end
        end
        api_pbuf_unmap(pbuf.res)
        while api_pbuf_waiting(pbuf.res) do
            coroutine.yield(true)
        end
        api_tex_set(tex.unit(), pbuf.res, pbuf.start, tex.layer(),
                    TEX_MIP, 0, 0, tex.size(), tex.size())
        pbuf.free()
    end
end

function M.done()
    vbuf.free()
    ibuf.free()
    tex.free()
    vtexlayer.free()
end

return M

