local M = {}

M.lods = {}
M.count = 0

local function add_lod(clip_near, clip_far, size, res, texres, heightfunc, colorfunc)
    local lod = {}
    lod.clip_near = clip_near
    lod.clip_far = clip_far
    lod.size = size
    lod.res = res
    lod.texres = texres
    lod.heightfunc = heightfunc
    lod.colorfunc = colorfunc
    M.lods[M.count] = lod
    M.count = M.count + 1
end

--
-- height
--

local function height0(n, z, x)
    return 0.900*n.get(z * 0.001, x * 0.001)
end

local function height1(n, z, x)
    return height0(n, z, x) + 0.099*n.get(z * 0.01, x * 0.01)
end

local function height2(n, z, x)
    return height1(n, z, x) + 0.001*n.get(z * 0.05, x * 0.05)
end

--
-- color
--

local function color0(n, z, x)
    return n.get(z * 0.002, x * 0.002)
end

local function color1(n, z, x)
    return 0.9*color0(n, z, x) + 0.1*n.get(z * 0.020, x * 0.020)
end

local function color2(n, z, x)
    return 0.9*color1(n, z, x) + 0.1*n.get(z * 0.100, x * 0.100)
end

local function color3(n, z, x)
    return 0.9*color2(n, z, x) + 0.1*n.get(z * 1.000, x * 1.000)
end

local function color4(n, z, x)
    return 0.9*color3(n, z, x) + 0.1*n.get(z * 4.000, x * 4.000)
end

--
-- lods
--

add_lod(6000, 12800, 6400, 40, 32, height0, color0)
add_lod(3000,  6400, 3200, 40, 32, height0, color1)
add_lod( 700,  3200, 1600, 40, 64, height1, color2)
add_lod( 150,   800,  800, 40, 128, height2, color3)
add_lod(   1,   200,  400, 80, 256, height2, color4)

return M
