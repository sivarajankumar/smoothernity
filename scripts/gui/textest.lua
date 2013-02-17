local M = {}

local cfg = require 'config'
local util = require 'util'
local meshes = require 'meshes'
local shader = require 'shader.shader'
local poolbuf = require 'pool.buf'
local poolibuf = require 'pool.ibuf'
local poolvbuf = require 'pool.vbuf'
local poolpbuf = require 'pool.pbuf'

local TEX_UNIT = 0
local TEX_LAYER = 0
local TEX_MIP = 0

local ibuf, vbuf, vtexlayer

function M.alloc(x, y, r)
    local self = {}
    local mesh, mfinal, utexunit, utexlayer

    function self.free()
        api_matrix_free(mfinal)
        api_mesh_free(mesh)
        api_shuni_free(utexunit)
        api_shuni_free(utexlayer)
    end

    do
        mfinal = util.matrix_pos_scl_stop(x,y,-0.5,  r,r,1)
        mesh = api_mesh_alloc(meshes.GROUP_GUI, API_MESH_TRIANGLES, vbuf.res, ibuf.res,
                              shader.texture(), mfinal, ibuf.start, ibuf.size)
        utexunit = api_shuni_alloc_int(shader.texture(), mesh, 'texunit', TEX_UNIT)
        utexlayer = api_shuni_alloc_vector(shader.texture(), mesh, 'texlayer', vtexlayer)
    end
    return self
end

function M.init()
    do
        vbuf = poolvbuf.alloc(4)
        vbuf.map()
        api_vbuf_set(vbuf.res, vbuf.start, -1,-1,0,  1,1,1,1,  0,0,
                                            1,-1,0,  1,1,1,1,  1,0,
                                            1, 1,0,  1,1,1,1,  1,1,
                                           -1, 1,0,  1,1,1,1,  0,1)
        vbuf.unmap()
    end
    do
        ibuf = poolibuf.alloc(6)
        local o = vbuf.start
        ibuf.map()
        api_ibuf_set(ibuf.res, ibuf.start, o+0,o+1,o+2,  o+0,o+2,o+3)
        ibuf.unmap()
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

