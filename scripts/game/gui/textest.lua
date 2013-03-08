local M = {}

local cfg = require 'config'
local util = require 'core.util'
local meshes = require 'meshes'
local shader = require 'game.shader'
local poolpbuf = require 'core.pool.pbuf'
local twinibuf = require 'core.twin.ibuf'
local twinvbuf = require 'core.twin.vbuf'
local twinmesh = require 'core.twin.mesh'
local twinshuni = require 'core.twin.shuni'

local TEX_UNIT = 0
local TEX_LAYER = 0
local TEX_MIP = 0

local ibuf, vbuf, vtexlayer

function M.alloc(x, y, r)
    local self = {}
    local mesh, mfinal, utexunit, utexlayer

    function self.free()
        api_matrix_free(mfinal)
        mesh.free()
        utexunit.free()
        utexlayer.free()
    end

    do
        mfinal = util.matrix_pos_scl_stop(x,y,-0.5,  r,r,1)
        mesh = twinmesh.alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf, ibuf,
                              shader.texture(), mfinal)
        utexunit = twinshuni.alloc_int(shader.texture(), mesh, 'texunit', TEX_UNIT)
        utexlayer = twinshuni.alloc_vector(shader.texture(), mesh, 'texlayer', vtexlayer)
    end
    return self
end

function M.init()
    do
        vbuf = twinvbuf.alloc(4)
        vbuf.prepare()
        vbuf.set(0, -1,-1,0,  1,1,1,1,  0,0,
                     1,-1,0,  1,1,1,1,  1,0,
                     1, 1,0,  1,1,1,1,  1,1,
                    -1, 1,0,  1,1,1,1,  0,1)
        vbuf.finalize()
    end
    do
        ibuf = twinibuf.alloc(6)
        local o = vbuf.start
        ibuf.prepare()
        ibuf.set(0, o+0,o+1,o+2,  o+0,o+2,o+3)
        ibuf.finalize()
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
    api_vector_free(vtexlayer)
end

return M

