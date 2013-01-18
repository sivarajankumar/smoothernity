local M = {}

local util = require 'util'

local LAND_DEVIATION = 0.1
local LAND_SIZE_X = 100
local LAND_SIZE_Y = 5
local LAND_SIZE_Z = 100
local LAND_WIDTH = 20
local LAND_HEIGHT = 20

function M.alloc(x, y, z)
    local self = {}

    local vb = api_vbuf_alloc()
    local ib = api_ibuf_alloc()
    local cs
    local rb
    local width = LAND_WIDTH
    local length = LAND_HEIGHT
    local scalex = LAND_SIZE_X / (width - 1)
    local scaley = LAND_SIZE_Y
    local scalez = LAND_SIZE_Z / (length - 1)
    local hmap
    local buf = api_buf_alloc()
    local mstart = util.matrix_pos_stop(x, y, z)
    local mvis = util.matrix_pos_scl_stop(0,0,0, scalex,scaley,scalez)
    local mmul = api_matrix_alloc()
    local mrb = api_matrix_alloc()
    local mesh

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

    local function subdivide(x1, z1, x2, z2)
        local zmid = math.floor(0.5 * (z1 + z2))
        local xmid = math.floor(0.5 * (x1 + x2))
        local hz1x1 = hmap[z1][x1]
        local hz1x2 = hmap[z1][x2]
        local hz2x1 = hmap[z2][x1]
        local hz2x2 = hmap[z2][x2]
        local hz1xmid = 0.5 * (hz1x1 + hz1x2)
        local hz2xmid = 0.5 * (hz2x1 + hz2x2)
        local hzmidx1 = 0.5 * (hz1x1 + hz2x1)
        local hzmidx2 = 0.5 * (hz1x2 + hz2x2)
        local hzmidxmid = 0.25 * (hz1xmid + hz2xmid + hzmidx1 + hzmidx2)
        hz1xmid = hz1xmid + (math.random() - 0.5) * LAND_DEVIATION
        hz2xmid = hz2xmid + (math.random() - 0.5) * LAND_DEVIATION
        hzmidx1 = hzmidx1 + (math.random() - 0.5) * LAND_DEVIATION
        hzmidx2 = hzmidx2 + (math.random() - 0.5) * LAND_DEVIATION
        hzmidxmid = hzmidxmid + (math.random() - 0.5) * LAND_DEVIATION
        if x2 - x1 > 1 then
            if z2 - z1 > 1 then
                hmap[z1][xmid] = hz1xmid
                hmap[z2][xmid] = hz2xmid
                hmap[zmid][x1] = hzmidx1
                hmap[zmid][x2] = hzmidx2
                hmap[zmid][xmid] = hzmidxmid
                subdivide(x1, z1, xmid, zmid)
                subdivide(xmid, z1, x2, zmid)
                subdivide(x1, zmid, xmid, z2)
                subdivide(xmid, zmid, x2, z2)
            else
                hmap[z1][xmid] = hz1xmid
                hmap[z2][xmid] = hz2xmid
                subdivide(x1, z1, xmid, z2)
                subdivide(xmid, z1, x2, z2)
            end
        else
            if z2 - z1 > 1 then
                hmap[zmid][x1] = hzmidx1
                hmap[zmid][x2] = hzmidx2
                subdivide(x1, z1, x2, zmid)
                subdivide(x1, zmid, x2, z2)
            end
        end
    end

    -- height map
    do
        -- clear
        hmap = {}
        for z = 1, length do
            hmap[z] = {}
            for x = 1, width do
                hmap[z][x] = 0
            end
        end

        -- fill
        hmap[1][1] = math.random()
        hmap[1][width] = math.random()
        hmap[length][1] = math.random()
        hmap[length][width] = math.random()
        subdivide(1, 1, width, length)

        -- normalize
        local hmin = math.huge
        local hmax = -math.huge
        for z = 1, length do
            for x = 1, width do
                hmin = math.min(hmin, hmap[z][x])
                hmax = math.max(hmax, hmap[z][x])
            end
        end
        for z = 1, length do
            for x = 1, width do
                hmap[z][x] = (hmap[z][x] - hmin) / (hmax - hmin)
            end
        end
    end

    -- vertex buffer
    do
        for x = 0, width - 1 do
            for z = 0, length - 1 do
                api_vbuf_set(vb, x + z * width,
                             x - 0.5 * (width - 1),
                             hmap[z + 1][x + 1] - 0.5,
                             z - 0.5 * (length - 1),
                             math.random(), math.random(), math.random(), 1,
                             0, 0)
            end
        end
        api_vbuf_bake(vb)
    end

    -- index buffer
    do
        for x = 0, width - 2 do
            for z = 0, length - 2 do
                local i00 = x + z * width
                local i01 = x + (z + 1) * width
                local i10 = (x + 1) + z * width
                local i11 = (x + 1) + (z + 1) * width
                local i = (x + z * (width - 1)) * 6
                api_ibuf_set(ib, i,  i00,i01,i10,  i10,i01,i11)
            end
        end
        api_ibuf_bake(ib)
    end

    -- physics
    do
        local size = api_vector_alloc()
        api_vector_const(size, scalex, scaley, scalez, 0)
        for x = 0, width - 1 do
            for z = 0, length - 1 do
                api_buf_set(buf, x + z * width, hmap[z + 1][x + 1])
            end
        end
        cs = api_physics_cs_alloc_hmap(buf, 0, width, length, 0, 1, size)
        rb = api_physics_rb_alloc(cs, mstart, 1, 1)
        api_vector_free(size)
    end

    -- visual
    do
        api_matrix_rigid_body(mrb, rb)
        api_matrix_mul(mmul, mrb, mvis)
        mesh = api_mesh_alloc(API_MESH_TRIANGLES, vb, ib, -1, mmul, 0,
                              6 * (width - 1) * (length - 1))
    end

    return self
end

return M