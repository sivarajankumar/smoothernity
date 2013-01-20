local M = {}

local util = require 'util'

M.SIZE_X = 50
M.SIZE_Z = 50

local HEIGHT = 2
local WIDTH = 10
local LENGTH = 10
local NOISE_SCALE = 0.1
local NOISE_STEPS = 5
local NOISE_PROGRESS = 5

function M.alloc(world, wz, wx)
    local self = {}

    local vb = api_vbuf_alloc()
    local ib = api_ibuf_alloc()
    local scalex = M.SIZE_X / (WIDTH - 1)
    local scalez = M.SIZE_Z / (LENGTH - 1)
    local buf = api_buf_alloc()
    local mvis = util.matrix_scl_stop(scalex,1,scalez)
    local mmul = api_matrix_alloc()
    local mrb = api_matrix_alloc()
    local mstart = util.matrix_pos_stop(world.centx + wx * M.SIZE_X,
                                        world.centy,
                                        world.centz + wz * M.SIZE_Z)
    local cs, rb, hmap, mesh
    local col_r, col_g, col_b

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

    local function color(z, x)
        local n = world.noise.get(((wz * LENGTH) + z),
                                  ((wx * WIDTH) + x),
                                  1, 1)
        return col_r * n, col_g * n, col_b * n, 1
    end

    -- height map
    do
        hmap = {}
        for z = 0, LENGTH - 1 do
            hmap[z] = {}
            for x = 0, WIDTH - 1 do
                local n = world.noise.get(((wz * (LENGTH - 1)) + z) * 0.5,
                                          ((wx * (WIDTH - 1)) + x) * 0.5,
                                          2, 2)
                hmap[z][x] = HEIGHT * (n - 0.5)
            end
        end
    end

    -- color
    do
        col_r = world.noise.get(wz, wx, 1, 1)
        col_g = world.noise.get(wz + 50, wx + 50, 1, 1)
        col_b = world.noise.get(wz - 30, wx - 30, 1, 1)
        local col_len = math.max(0.01, math.sqrt(col_r*col_r + col_g*col_g + col_b*col_b))
        col_r = col_r / col_len
        col_g = col_g / col_len
        col_b = col_b / col_len
    end

    -- vertex buffer
    do
        for z = 0, LENGTH - 1 do
            for x = 0, WIDTH - 1 do
                local r, g, b, a = color(z, x)
                api_vbuf_set(vb, x + z * WIDTH,
                             x - 0.5 * (WIDTH - 1),
                             hmap[z][x],
                             z - 0.5 * (LENGTH - 1),
                             r, g, b, a,
                             0, 0)
            end
        end
        api_vbuf_bake(vb)
    end

    -- index buffer
    do
        for z = 0, LENGTH - 2 do
            for x = 0, WIDTH - 2 do
                local i00 = x + z * WIDTH
                local i01 = x + (z + 1) * WIDTH
                local i10 = (x + 1) + z * WIDTH
                local i11 = (x + 1) + (z + 1) * WIDTH
                local i = (x + z * (WIDTH - 1)) * 6
                api_ibuf_set(ib, i,  i00,i01,i10,  i10,i01,i11)
            end
        end
        api_ibuf_bake(ib)
    end

    -- physics
    do
        local size = api_vector_alloc()
        api_vector_const(size, scalex, 1, scalez, 0)
        for z = 0, LENGTH - 1 do
            for x = 0, WIDTH - 1 do
                api_buf_set(buf, x + z * WIDTH, hmap[z][x])
            end
        end
        cs = api_physics_cs_alloc_hmap(buf, 0, WIDTH, LENGTH, -0.5 * HEIGHT, 0.5 * HEIGHT, size)
        rb = api_physics_rb_alloc(cs, mstart, 1, 1)
        api_vector_free(size)
    end

    -- visual
    do
        api_matrix_rigid_body(mrb, rb)
        api_matrix_mul(mmul, mrb, mvis)
        mesh = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, mmul, 0,
                              6 * (WIDTH - 1) * (LENGTH - 1))
    end

    return self
end

return M
