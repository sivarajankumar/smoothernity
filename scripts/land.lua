local M = {}

local util = require 'util'
local pwld = require 'physwld'
local cfg = require 'config'

function M.world_height(noise, lod, z, x)
    local n = 0
    if lod <= 0 then
        n = noise.get(z * 0.001, x * 0.001)
    elseif lod <= 1 then
        n = n + 0.995*noise.get(z * 0.001, x * 0.001)
        n = n + 0.005*noise.get(z * 0.01, x * 0.01)
    else
        n = n + 0.995*noise.get(z * 0.001, x * 0.001)
        n = n + 0.004*noise.get(z * 0.01, x * 0.01)
        n = n + 0.001*noise.get(z * 0.05, x * 0.05)
    end
    return n
end

local function common_alloc(mach, noise, move, group, lod, size, res, basx, basy, basz)
    local self = {}

    self.mmesh = api_matrix_alloc()
    self.hmap = {}
    local vb = api_vbuf_alloc()
    local ib = api_ibuf_alloc()
    local mesh

    function self.free()
        api_vbuf_free(vb)
        api_ibuf_free(ib)
        api_matrix_free(self.mmesh)
        if mesh ~= nil then
            api_mesh_free(mesh)
        end
    end

    function self.hide()
        if mesh ~= nil then
            api_mesh_free(mesh)
            mesh = nil
        end
    end

    function self.show()
        if mesh == nil then
            mesh = api_mesh_alloc(group, API_MESH_TRIANGLES, vb, ib, -1,
                                  self.mmesh, 0, 6 * (res - 1) * (res - 1))
        end
    end

    local function to_world(z, x)
        return basz + (z * size / (res-1)),
               basx + (x * size / (res-1))
    end

    local function color_noise(z, x, ofsz, ofsx)
        local wz, wx = to_world(z, x)
        wz = wz + ofsz
        wx = wx + ofsx
        local n = 0
        if lod <= 0 then
            n = noise.get(wz * 0.005, wx * 0.005)
        elseif lod <= 1 then
            n = n + 0.7*noise.get(wz * 0.005, wx * 0.005)
            n = n + 0.3*noise.get(wz * 0.04, wx * 0.04)
        else
            n = n + 0.7*noise.get(wz * 0.005, wx * 0.005)
            n = n + 0.2*noise.get(wz * 0.04, wx * 0.04)
            n = n + 0.1*noise.get(wz * 0.4, wx * 0.4)
        end
        return n
    end

    local function height_noise(z, x)
        local wz, wx = to_world(z, x)
        return M.world_height(noise, lod, wz, wx)
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
        for z = 0, res - 1 do
            self.hmap[z] = {}
            for x = 0, res - 1 do
                self.hmap[z][x] = util.lerp(height_noise(z, x), 0, 1,
                                            -0.5*cfg.LAND_HEIGHT, 0.5*cfg.LAND_HEIGHT)
                api_machine_yield(mach)
            end
        end
    end

    -- vertex buffer
    do
        for z = 0, res - 1 do
            for x = 0, res - 1 do
                local r, g, b, a = color(z, x)
                api_vbuf_set(vb, x + z * res,
                             x - 0.5 * (res - 1),
                             self.hmap[z][x],
                             z - 0.5 * (res - 1),
                             r, g, b, a,
                             0, 0)
                api_machine_yield(mach)
            end
        end
        api_vbuf_bake(vb)
    end

    -- index buffer
    do
        for z = 0, res - 2 do
            for x = 0, res - 2 do
                local i00 = x + z * res
                local i01 = x + (z + 1) * res
                local i10 = (x + 1) + z * res
                local i11 = (x + 1) + (z + 1) * res
                local i = (x + z * (res - 1)) * 6
                api_ibuf_set(ib, i,  i00,i01,i10,  i10,i01,i11)
                api_machine_yield(mach)
            end
        end
        api_ibuf_bake(ib)
    end

    return self
end

function M.phys_alloc(mach, noise, move, group, lod, size, res, basx, basy, basz)
    local self = {}

    local common = common_alloc(mach, noise, move, group, lod, size, res, basx, basy, basz)
    local scale = size / (res - 1)
    local buf = api_buf_alloc()
    local mvis = util.matrix_scl_stop(scale, 1, scale)
    local mrb = api_matrix_alloc()
    local cs, rb

    function self.free()
        api_matrix_free(mvis)
        api_matrix_free(mrb)
        api_physics_rb_free(rb)
        api_physics_cs_free(cs)
        api_buf_free(buf)
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

    -- physics
    do
        local vsize = api_vector_alloc()
        api_vector_const(vsize, scale, 1, scale, 0)
        for z = 0, res - 1 do
            for x = 0, res - 1 do
                api_buf_set(buf, x + z * res, common.hmap[z][x])
                api_machine_yield(mach)
            end
        end
        local mpos = util.matrix_pos_stop(basx + move.x + 0.5*size,
                                          basy + move.y,
                                          basz + move.z + 0.5*size)
        cs = api_physics_cs_alloc_hmap(buf, 0, res, res,
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

    return self
end

function M.vis_alloc(mach, noise, move, group, lod, size, res, basx, basy, basz)
    local self = {}
    local common = common_alloc(mach, noise, move, group, lod, size, res, basx, basy, basz)

    function self.free()
        common.free()
    end

    function self.hide()
        common.hide()
    end

    function self.show()
        common.show()
    end

    function self.move()
        local scale = size / (res - 1)
        local m = util.matrix_pos_scl_stop(basx + move.x + 0.5*size,
                                           basy + move.y,
                                           basz + move.z + 0.5*size,
                                           scale, 1, scale)
        api_matrix_copy(common.mmesh, m)
        api_matrix_free(m)
    end

    self.move()
    return self
end

return M
