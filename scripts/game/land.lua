local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local cfg = require 'config'
local lod = require 'game.lod'
local meshes = require 'game.meshes'
local quit = require 'game.quit'
local shader = require 'game.shader'
local poolbuf = require 'core.pool.buf'
local twinibuf = require 'core.twin.ibuf'
local twinvbuf = require 'core.twin.vbuf'
local twinmesh = require 'core.twin.mesh'
local rigidbody = require 'core.rigidbody'
local colshape = require 'core.colshape'
local matrix = require 'core.matrix'
local vector = require 'core.vector'
local thread = require 'core.thread'

local function common_alloc(uid, noise, move, lodi, basx, basy, basz)
    local self = {}

    self.size = lod.lods[lodi].size
    self.res = lod.lods[lodi].res
    self.mmesh = matrix.alloc()
    self.hmap = poolbuf.alloc(self.res * self.res)
    local vb = twinvbuf.alloc(self.res * self.res)
    local ib = twinibuf.alloc(6 * (self.res - 1) * (self.res - 1))
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

    local th = thread.alloc('game.land_th')
    util.wait_thread_responding(th)

    th.request(string.format('return "%s", %s, %s, %i, %f, %f, %f',
                             uid, noise.store(), self.hmap.store(),
                             lodi, basx, basy, basz))
    util.wait_thread_responding(th)

    th.request('make_hmap')
    util.wait_thread_responding(th)

    vb.prepare()
    th.request('make_vb')
    util.wait_thread_responding(th)
    th.request(string.format('return %s', vb.store()))
    util.wait_thread_responding(th)
    vb.finalize()

    ib.prepare()
    th.request('make_ib')
    util.wait_thread_responding(th)
    th.request(string.format('return %s, %i', ib.store(), vb.start))
    util.wait_thread_responding(th)
    ib.finalize()

    th.request('finish')
    util.wait_thread_idle(th)

    th.free()

    mesh = twinmesh.alloc(meshes.GROUP_HIDDEN, API_MESH_TRIANGLES, vb, ib,
                          shader.default(), self.mmesh)

    return self
end

function M.phys_alloc(uid, noise, move, lodi, basx, basy, basz)
    local self = {}

    local common = common_alloc(uid, noise, move, lodi, basx, basy, basz)
    local scale = common.size / (common.res - 1)
    local mvis = util.matrix_scl_stop(scale, 1, scale)
    local mrb = matrix.alloc()
    local cs, rb

    function self.free()
        mvis.free()
        mrb.free()
        rb.free()
        cs.free()
        common.hmap.free()
        common.free()
    end

    function self.hide()
        common.hide()
    end

    function self.show()
        common.show()
    end

    function self.move()
    end

    function self.delete()
        common.delete()
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
    local self = {}
    local common = common_alloc(uid, noise, move, lodi, basx, basy, basz)

    function self.free()
        common.free()
    end

    function self.hide()
        common.hide()
    end

    function self.show()
        common.show()
    end

    function self.delete()
        common.delete()
    end

    function self.move()
        local scale = common.size / (common.res - 1)
        local m = util.matrix_pos_scl_stop(basx + move.x + 0.5*common.size,
                                           basy + move.y,
                                           basz + move.z + 0.5*common.size,
                                           scale, 1, scale)
        common.mmesh.copy(m)
        m.free()
    end

    common.hmap.free()

    self.move()
    return self
end

return M
