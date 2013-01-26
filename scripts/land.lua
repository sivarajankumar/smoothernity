local M = {}

local util = require 'util'
local pwld = require 'physwld'
local meshes = require 'meshes'

local HEIGHT = 10
local resx = 20
local resz = 20

function M.alloc(noise, mach, basx, basy, basz, movx, movy, movz,
                 sizex, sizez, resx, resz)
    local self = {}

    local vb = api_vbuf_alloc()
    local ib = api_ibuf_alloc()
    local scalex = sizex / (resx - 1)
    local scalez = sizez / (resz - 1)
    local buf = api_buf_alloc()
    local mvis = util.matrix_scl_stop(scalex,1,scalez)
    local mmul = api_matrix_alloc()
    local mrb = api_matrix_alloc()
    local mstart = util.matrix_pos_stop(basx + movx, basy + movy, basz + movz)
    local cs, rb, hmap, mesh

    function self.free()
        api_vbuf_free(vb)
        api_ibuf_free(ib)
        api_matrix_free(mstart)
        api_matrix_free(mvis)
        api_matrix_free(mrb)
        api_matrix_free(mmul)
        api_physics_rb_free(rb)
        api_physics_cs_free(cs)
        api_buf_free(buf)
        api_mesh_free(mesh)
    end

    local function to_world(z, x)
        return basz + z * scalez, basx + x * scalex
    end

    local function color_noise(z, x)
        local wz, wx = to_world(z, x)
        local n = 0
        n = n + 0.9*noise.get(wz * 0.04, wx * 0.04)
        n = n + 0.1*noise.get(wz * 0.4, wx * 0.4)
        return n
    end

    local function height_noise(z, x)
        local wz, wx = to_world(z, x)
        local n = 0
        n = n + 0.9*noise.get(wz * 0.02, wx * 0.02)
        n = n + 0.1*noise.get(wz * 0.08, wx * 0.08)
        return n
    end

    local function color(z, x)
        local r = color_noise(z, x)
        local g = color_noise(z + 30, x + 40)
        local b = color_noise(z + 100, x - 50)
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
        hmap = {}
        for z = 0, resz - 1 do
            hmap[z] = {}
            for x = 0, resx - 1 do
                hmap[z][x] = util.lerp(height_noise(z, x), 0, 1, -0.5*HEIGHT, 0.5*HEIGHT)
                api_machine_yield(mach)
            end
        end
    end

    -- vertex buffer
    do
        for z = 0, resz - 1 do
            for x = 0, resx - 1 do
                local r, g, b, a = color(z, x)
                api_vbuf_set(vb, x + z * resx,
                             x - 0.5 * (resx - 1),
                             hmap[z][x],
                             z - 0.5 * (resz - 1),
                             r, g, b, a,
                             0, 0)
                api_machine_yield(mach)
            end
        end
        api_vbuf_bake(vb)
    end

    -- index buffer
    do
        for z = 0, resz - 2 do
            for x = 0, resx - 2 do
                local i00 = x + z * resx
                local i01 = x + (z + 1) * resx
                local i10 = (x + 1) + z * resx
                local i11 = (x + 1) + (z + 1) * resx
                local i = (x + z * (resx - 1)) * 6
                api_ibuf_set(ib, i,  i00,i01,i10,  i10,i01,i11)
                api_machine_yield(mach)
            end
        end
        api_ibuf_bake(ib)
    end

    -- physics
    do
        local size = api_vector_alloc()
        api_vector_const(size, scalex, 1, scalez, 0)
        for z = 0, resz - 1 do
            for x = 0, resx - 1 do
                api_buf_set(buf, x + z * resx, hmap[z][x])
                api_machine_yield(mach)
            end
        end
        cs = api_physics_cs_alloc_hmap(buf, 0, resx, resz, -0.5 * HEIGHT, 0.5 * HEIGHT, size)
        rb = api_physics_rb_alloc(pwld.wld, cs, mstart, 0, 1, 1)
        api_vector_free(size)
    end

    -- visual
    do
        api_matrix_rigid_body(mrb, rb)
        api_matrix_mul(mmul, mrb, mvis)
        mesh = api_mesh_alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib, -1, mmul, 0,
                              6 * (resx - 1) * (resz - 1))
    end

    return self
end

return M
