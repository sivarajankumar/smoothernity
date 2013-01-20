local M = {}

local util = require 'util'

local LAND_DEVIATION = 0.1
local LAND_HEIGHT = 5
local LAND_SIZE_X = 50
local LAND_SIZE_Z = 50
local LAND_WIDTH = 10
local LAND_LENGTH = 10

local function land_alloc(x, y, z, left, right, front, back)
    local self = {}

    local vb = api_vbuf_alloc()
    local ib = api_ibuf_alloc()
    local width = LAND_WIDTH
    local length = LAND_LENGTH
    local scalex = LAND_SIZE_X / (width - 1)
    local scalez = LAND_SIZE_Z / (length - 1)
    local buf = api_buf_alloc()
    local mvis = util.matrix_scl_stop(scalex,1,scalez)
    local mmul = api_matrix_alloc()
    local mrb = api_matrix_alloc()
    local hmin, hmax = math.huge, -math.huge
    local cs, rb, hmap, hcenter, mesh, mstart
    local col_r, col_g, col_b
    self.land_x, self.land_y, self.land_z = 0, 0, 0

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

    local function deviation()
        return (math.random() - 0.5) * LAND_DEVIATION
    end

    local function color()
        local shade = math.random()
        return col_r * shade, col_g * shade, col_b * shade, 1
    end

    local function refine(z, x, height)
        if hmap[z][x] == nil then
            hmap[z][x] = height
        end
    end

    local function subdivide(z1, x1, z2, x2)
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
        hz1xmid = hz1xmid + deviation()
        hz2xmid = hz2xmid + deviation()
        hzmidx1 = hzmidx1 + deviation()
        hzmidx2 = hzmidx2 + deviation()
        hzmidxmid = hzmidxmid + deviation()
        if x2 - x1 > 1 then
            if z2 - z1 > 1 then
                refine(z1, xmid, hz1xmid)
                refine(z2, xmid, hz2xmid)
                refine(zmid, x1, hzmidx1)
                refine(zmid, x2, hzmidx2)
                refine(zmid, xmid, hzmidxmid)
                subdivide(z1, x1, zmid, xmid)
                subdivide(z1, xmid, zmid, x2)
                subdivide(zmid, x1, z2, xmid)
                subdivide(zmid, xmid, z2, x2)
            else
                refine(z1, xmid, hz1xmid)
                refine(z2, xmid, hz2xmid)
                subdivide(z1, x1, z2, xmid)
                subdivide(z1, xmid, z2, x2)
            end
        else
            if z2 - z1 > 1 then
                refine(zmid, x1, hzmidx1)
                refine(zmid, x2, hzmidx2)
                subdivide(z1, x1, zmid, x2)
                subdivide(zmid, x1, z2, x2)
            end
        end
    end

    function self.height_world(z, x)
        return hmap[z][x] + self.land_y
    end

    -- height map
    do
        -- clear
        hmap = {}
        for z = 1, length do
            hmap[z] = {}
        end

        -- join
        if left then
            for z = 1, length do
                hmap[z][1] = left.height_world(z, width)
            end
        end
        if right then
            for z = 1, length do
                hmap[z][width] = right.height_world(z, 1)
            end
        end
        if front then
            for x = 1, width do
                hmap[1][x] = front.height_world(length, x)
            end
        end
        if back then
            for x = 1, width do
                hmap[length][x] = back.height_world(1, x)
            end
        end

        -- corners
        do
            local corn_count = 0
            local corn_sum = 0
            local function corn_offset()
                if corn_count > 0 then
                    return corn_sum / corn_count
                else
                    return 0
                end
            end
            local function count_corner(z, x)
                if hmap[z][x] ~= nil then
                    corn_count = corn_count + 1
                    corn_sum = corn_sum + hmap[z][x]
                end
            end
            local function put_corner(z, x)
                if hmap[z][x] == nil then
                    hmap[z][x] = corn_offset() + math.random() * LAND_HEIGHT
                end
            end
            count_corner(1, 1)
            count_corner(1, width)
            count_corner(length, 1)
            count_corner(length, width)

            put_corner(1, 1)
            put_corner(1, width)
            put_corner(length, 1)
            put_corner(length, width)
        end

        -- fill
        subdivide(1, 1, length, width)

        -- shift
        for z = 1, length do
            for x = 1, width do
                hmin = math.min(hmin, hmap[z][x])
                hmax = math.max(hmax, hmap[z][x])
            end
        end
        hcenter = 0.5 * (hmax + hmin)
        for z = 1, length do
            for x = 1, width do
                hmap[z][x] = hmap[z][x] - hcenter
            end
        end
        hmin = hmin - hcenter
        hmax = hmax - hcenter
    end

    -- position
    do
        if left == nil and right == nil and front == nil and back == nil then
            self.land_x, self.land_y, self.land_z = x, y + hcenter, z
        elseif left ~= nil then
            self.land_x, self.land_y, self.land_z = left.land_x + LAND_SIZE_X, hcenter, left.land_z
        elseif right ~= nil then
            self.land_x, self.land_y, self.land_z = right.land_x - LAND_SIZE_X, hcenter, right.land_z
        elseif front ~= nil then
            self.land_x, self.land_y, self.land_z = front.land_x, hcenter, front.land_z + LAND_SIZE_Z
        elseif back ~= nil then
            self.land_x, self.land_y, self.land_z = back.land_x, hcenter, back.land_z - LAND_SIZE_Z
        end
        mstart = util.matrix_pos_stop(self.land_x, self.land_y, self.land_z)
    end

    -- color
    do
        col_r, col_g, col_b = math.random(), math.random(), math.random()
        local col_len = math.max(0.01, math.sqrt(col_r*col_r + col_g*col_g + col_b*col_b))
        col_r = col_r / col_len
        col_g = col_g / col_len
        col_b = col_b / col_len
    end

    -- vertex buffer
    do
        for x = 0, width - 1 do
            for z = 0, length - 1 do
                local r, g, b, a = color()
                api_vbuf_set(vb, x + z * width,
                             x - 0.5 * (width - 1),
                             hmap[z + 1][x + 1],
                             z - 0.5 * (length - 1),
                             r, g, b, a,
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
        api_vector_const(size, scalex, 1, scalez, 0)
        for x = 0, width - 1 do
            for z = 0, length - 1 do
                api_buf_set(buf, x + z * width, hmap[z + 1][x + 1])
            end
        end
        cs = api_physics_cs_alloc_hmap(buf, 0, width, length, hmin, hmax, size)
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

function M.alloc_root(x, y, z)
    return land_alloc(x, y, z)
end    

function M.alloc_join(left, right, front, back)
    return land_alloc(0, 0, 0, left, right, front, back)
end

return M
