local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local cfg = require 'config'
local lod = require 'game.lod'
local meshes = require 'game.meshes'
local shader = require 'game.shader.shader'
local poolbuf = require 'core.pool.buf'
local rendermesh = require 'core.render.mesh'
local renderibuf = require 'core.render.ibuf'
local rendervbuf = require 'core.render.vbuf'
local rigidbody = require 'core.rigidbody'
local colshape = require 'core.colshape'
local matrix = require 'core.matrix'
local vector = require 'core.vector'
local thread = require 'core.thread'

local function common_alloc(uid, noise, lodi, basx, basy, basz)
    local self = {}

    self.size = lod.lods[lodi].size
    self.res = lod.lods[lodi].res
    self.mmesh = matrix.alloc()
    self.hmap = poolbuf.alloc(self.res * self.res)
    local vb = rendervbuf.alloc(self.res * self.res)
    local ib = renderibuf.alloc(6 * (self.res - 1) * (self.res - 1), vb)
    local mesh

    function self.free()
        mesh.free()
        vb.free()
        ib.free()
        self.mmesh.free()
    end

    function self.hide()
        mesh.group(meshes.GROUP_HIDDEN)
    end

    function self.show()
        mesh.group(meshes.GROUP_LODS[lodi])
    end

    function self.delete()
        util.async_write(util.uid_cache(string.format('%s_hmap.lua', uid, z)), '')
        util.async_write(util.uid_cache(string.format('%s_colmap.lua', uid, z)), '')
    end

    util.wait_prepared(true, vb, ib)

    while thread.left() == 0 do
        coroutine.yield(true)
    end
    local th = thread.alloc('game.land_th')
    util.wait_thread_responding(th, false)
    th.request(string.format('return "%s", %s, %s, %s, %s, %i, %f, %f, %f',
                             uid, noise.store(), self.hmap.store(),
                             vb.store(), ib.store(), lodi, basx, basy, basz))
    util.wait_thread_idle(th, true)
    th.free()

    vb.finalize()
    ib.finalize()
    util.wait_finalized(true, vb, ib)

    mesh = rendermesh.alloc(meshes.GROUP_HIDDEN, API_MESH_TRIANGLES, vb, ib,
                            shader.default(), self.mmesh)

    return self
end

function M.phys_alloc(uid, noise, move, lodi, basx, basy, basz)
    local self = {}

    local common = common_alloc(uid, noise, lodi, basx, basy, basz)
    local scale = common.size / (common.res - 1)
    local mvis = util.matrix_scl_stop(scale, 1, scale)
    local mrb = matrix.alloc()
    local cs, rb

    self.hide = common.hide
    self.show = common.show
    self.delete = common.delete

    function self.free()
        mvis.free()
        mrb.free()
        rb.free()
        cs.free()
        common.hmap.free()
        common.free()
    end

    function self.move()
    end

    -- physics
    do
        local mpos = util.matrix_pos_stop(basx + move.x + 0.5*common.size,
                                          basy + move.y,
                                          basz + move.z + 0.5*common.size)
        local vsize = vector.alloc()
        vsize.const(scale, 1, scale, 0)
        cs = colshape.alloc_hmap(common.hmap, common.res, common.res,
                                 -0.5 * cfg.LAND_HEIGHT, 0.5 * cfg.LAND_HEIGHT, vsize)
        rb = rigidbody.alloc(pwld.wld, cs, mpos, 0, 1, 1)
        vsize.free()
        mpos.free()
    end

    -- visual
    do
        mrb.rigid_body(rb)
        common.mmesh.mul(mrb, mvis)
    end

    return self
end

function M.vis_alloc(uid, noise, move, lodi, basx, basy, basz)
    local self = common_alloc(uid, noise, lodi, basx, basy, basz)

    function self.move()
        local scale = self.size / (self.res - 1)
        local m = util.matrix_pos_scl_stop(basx + move.x + 0.5*self.size,
                                           basy + move.y,
                                           basz + move.z + 0.5*self.size,
                                           scale, 1, scale)
        self.mmesh.copy(m)
        m.free()
    end

    self.hmap.free()
    self.move()
    return self
end

return M
