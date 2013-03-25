local M = {}

local cfg = require 'config'
local util = require 'core.util'
local meshes = require 'game.meshes'
local shader = require 'game.shader.shader'
local rendershuni = require 'core.render.shuni'
local rendermesh = require 'core.render.mesh'
local renderibuf = require 'core.render.ibuf'
local rendervbuf = require 'core.render.vbuf'
local rendertex = require 'core.render.tex'
local matrix = require 'core.matrix'

local TEX_MIP = 0
local TEX_SIZE = 32

local ibuf, vbuf, tex

function M.alloc(x, y, r)
    local self = {}
    local mesh, mfinal, utex

    function self.free()
        mfinal.free()
        mesh.free()
        utex.free()
    end

    do
        mfinal = util.matrix_pos_scl_stop(x,y,-0.5,  r,r,1)
        mesh = rendermesh.alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf,
                                shader.texture(), mfinal)
        utex = rendershuni.alloc_tex(shader.texture(), mesh, tex, 'texunit', 'texlayer')
    end
    return self
end

function M.init()
    do
        vbuf = rendervbuf.alloc(4)
        ibuf = renderibuf.alloc(6, vbuf)
        tex = rendertex.alloc(TEX_SIZE)

        util.wait_prepared(true, vbuf, ibuf, tex)
        vbuf.set(0, -1,-1,0,  1,1,1,1,  0,0,
                     1,-1,0,  1,1,1,1,  1,0,
                     1, 1,0,  1,1,1,1,  1,1,
                    -1, 1,0,  1,1,1,1,  0,1)
        ibuf.set(0, 0,1,2,  0,2,3)
        for y = 0, tex.mip(TEX_MIP).size()-1 do
            for x = 0, tex.mip(TEX_MIP).size()-1 do
                local r = ((x + y) % 16) / 16
                local g = ((x + y) % 32) / 32
                local b = ((x + y) % 64) / 64
                local a = 1
                tex.mip(TEX_MIP).set(x, y, r, g, b, a)
                coroutine.yield(false)
            end
        end

        ibuf.finalize()
        vbuf.finalize()
        tex.finalize()
        util.wait_finalized(true, vbuf, ibuf, tex)
    end
end

function M.done()
    vbuf.free()
    ibuf.free()
    tex.free()
end

return M

