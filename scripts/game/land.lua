local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local cfg = require 'config'
local lod = require 'game.lod'
local meshes = require 'game.meshes'
local quit = require 'quit'
local shader = require 'game.shader'
local poolbuf = require 'core.pool.buf'
local twinibuf = require 'core.twin.ibuf'
local twinvbuf = require 'core.twin.vbuf'
local twinmesh = require 'core.twin.mesh'

local function common_alloc(uid, noise, move, lodi, basx, basy, basz)
    local self = {}

    self.size = lod.lods[lodi].size
    self.res = lod.lods[lodi].res
    self.mmesh = api_matrix_alloc()
    self.hmap = {}
    local vb = twinvbuf.alloc(self.res * self.res)
    local ib = twinibuf.alloc(6 * (self.res - 1) * (self.res - 1))
    local mesh

    function self.free()
        mesh.free()
        vb.free()
        ib.free()
        api_matrix_free(self.mmesh)
    end

    function self.hide()
        mesh.group(meshes.GROUP_HIDDEN)
    end

    function self.show()
        mesh.group(meshes.GROUP_LODS[lodi])
    end

    function self.delete()
        for z = 0, self.res - 1 do
            util.async_write(util.uid_cache(string.format('%s_hmap_%i.lua', uid, z)), '')
            util.async_write(util.uid_cache(string.format('%s_colmap_%i.lua', uid, z)), '')
        end
    end

    local function to_world(z, x)
        return basz + (z * self.size / (self.res-1)),
               basx + (x * self.size / (self.res-1))
    end

    local function color_noise(z, x, ofsz, ofsx)
        local wz, wx = to_world(z, x)
        wz = wz + ofsz
        wx = wx + ofsx
        if quit.requested() then
            return 0
        else
            return lod.lods[lodi].colorfunc(noise, wz, wx)
        end
    end

    local function height_noise(z, x)
        local wz, wx = to_world(z, x)
        if quit.requested() then
            return 0
        else
            return lod.lods[lodi].heightfunc(noise, wz, wx)
        end
    end

    local function color(z, x)
        local r = color_noise(z, x, 0, 0)
        local g = color_noise(z, x, 300, 400)
        local b = color_noise(z, x, 1000, -500)
        local len = math.sqrt(r*r + g*g + b*b)
        if len > 0.1 then
            r = r / len
            g = g / len
            b = b / len
        else
            r, g, b = 0.1, 0.1, 0.1
        end
        return r, g, b, 1
    end

    -- height map
    do
        for z = 0, self.res - 1 do
            local chunk = util.async_read(util.uid_cache(string.format('%s_hmap_%i.lua', uid, z)))
            if chunk ~= '' then
                self.hmap[z] = loadstring(chunk)()
            else
                self.hmap[z] = {}
                for x = 0, self.res - 1 do
                    self.hmap[z][x] = util.lerp(height_noise(z, x), 0, 1, -0.5, 0.5) * cfg.LAND_HEIGHT
                    coroutine.yield(false)
                end
                if not quit.requested() then
                    chunk = 'return {\n'
                    local first_x = true
                    for x, v in pairs(self.hmap[z]) do
                        if not first_x then
                            chunk = chunk .. ',\n'
                        end
                        first_x = false
                        chunk = chunk .. string.format('    [%i] = %f', x, v)
                        coroutine.yield(false)
                    end
                    chunk = chunk .. '\n}'
                    util.async_write(util.uid_cache(string.format('%s_hmap_%i.lua', uid, z)), chunk)
                end
            end
        end
    end

    -- vertex buffer
    do
        vb.prepare()
        for z = 0, self.res - 1 do
            local colmap
            local chunk = util.async_read(util.uid_cache(string.format('%s_colmap_%i.lua', uid, z)))
            if chunk ~= '' then
                colmap = loadstring(chunk)()
            else
                colmap = {}
                for x = 0, self.res - 1 do
                    local r, g, b, a = color(z, x)
                    colmap[x] = {r = r, g = g, b = b, a = a}
                    coroutine.yield(false)
                end
                if not quit.requested() then
                    chunk = 'return {\n'
                    local first_x = true
                    for x, v in pairs(colmap) do
                        if not first_x then
                            chunk = chunk .. ',\n'
                        end
                        first_x = false
                        chunk = chunk .. string.format('    [%i] = {r = %f, g = %f, b = %f, a = %f}',
                                                       x, v.r, v.g, v.b, v.a)
                        coroutine.yield(false)
                    end
                    chunk = chunk .. '\n}'
                    util.async_write(util.uid_cache(string.format('%s_colmap_%i.lua', uid, z)), chunk)
                end
            end
            for x = 0, self.res - 1 do
                local col = colmap[x]
                vb.set(x + z * self.res,
                       x - 0.5 * (self.res - 1),
                       self.hmap[z][x],
                       z - 0.5 * (self.res - 1),
                       col.r, col.g, col.b, col.a,
                       0, 0)
                coroutine.yield(false)
            end
        end
        vb.finalize()
    end

    -- index buffer
    do
        ib.prepare()
        local o = vb.start
        for z = 0, self.res - 2 do
            for x = 0, self.res - 2 do
                local i00 = o + x + z * self.res
                local i01 = o + x + (z + 1) * self.res
                local i10 = o + (x + 1) + z * self.res
                local i11 = o + (x + 1) + (z + 1) * self.res
                local i = (x + z * (self.res - 1)) * 6
                ib.set(i,  i00,i01,i10,  i10,i01,i11)
                coroutine.yield(false)
            end
        end
        ib.finalize()
    end

    mesh = twinmesh.alloc(meshes.GROUP_HIDDEN, API_MESH_TRIANGLES, vb, ib,
                          shader.default(), self.mmesh)

    return self
end

function M.phys_alloc(uid, noise, move, lodi, basx, basy, basz)
    local self = {}

    local common = common_alloc(uid, noise, move, lodi, basx, basy, basz)
    local scale = common.size / (common.res - 1)
    local buf = poolbuf.alloc(common.res * common.res)
    local mvis = util.matrix_scl_stop(scale, 1, scale)
    local mrb = api_matrix_alloc()
    local cs, rb

    function self.free()
        api_matrix_free(mvis)
        api_matrix_free(mrb)
        api_physics_rb_free(rb)
        api_physics_cs_free(cs)
        buf.free()
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
        local vsize = api_vector_alloc()
        api_vector_const(vsize, scale, 1, scale, 0)
        for z = 0, common.res - 1 do
            for x = 0, common.res - 1 do
                api_buf_set(buf.start + x + z * common.res, common.hmap[z][x])
                coroutine.yield(false)
            end
        end
        local mpos = util.matrix_pos_stop(basx + move.x + 0.5*common.size,
                                          basy + move.y,
                                          basz + move.z + 0.5*common.size)
        cs = api_physics_cs_alloc_hmap(buf.start, common.res, common.res,
                                       -0.5 * cfg.LAND_HEIGHT, 0.5 * cfg.LAND_HEIGHT, vsize)
        rb = api_physics_rb_alloc(pwld.wld, cs, mpos, 0, 1, 1)
        api_vector_free(vsize)
        api_matrix_free(mpos)
    end

    -- visual
    do
        api_matrix_rigid_body(mrb, rb)
        api_matrix_mul(common.mmesh, mrb, mvis)
    end

    common.hmap = nil

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
        api_matrix_copy(common.mmesh, m)
        api_matrix_free(m)
    end

    common.hmap = nil

    self.move()
    return self
end

return M