local M = {}

M.lods = {}
M.count = 0

local function add_lod(clip_range, vis_range, size, res, heightfunc, colorfunc)
    local lod = {}
    lod.clip_range = clip_range
    lod.vis_range = vis_range
    lod.size = size
    lod.res = res
    lod.heightfunc = heightfunc
    lod.colorfunc = colorfunc
    M.lods[M.count] = lod
    M.count = M.count + 1
end

--
-- height
--

local function height0(n, z, x)
    return 0.975*n.get(z * 0.001, x * 0.001)
end

local function height1(n, z, x)
    return height0(n, z, x) + 0.015 + 0.004*n.get(z * 0.01, x * 0.01)
end

local function height2(n, z, x)
    return height1(n, z, x) + 0.005 + 0.001*n.get(z * 0.05, x * 0.05)
end

--
-- color
--

local function color0(n, z, x)
    return n.get(z * 0.002, x * 0.002)
end

local function color1(n, z, x)
    return 0.8*color0(n, z, x) + 0.2*n.get(z * 0.020, x * 0.020)
end

local function color2(n, z, x)
    return 0.8*color1(n, z, x) + 0.2*n.get(z * 0.500, x * 0.500)
end

--
-- lods
--

add_lod( 5000, 10000, 10000, 20, height0, color0)
add_lod( 1000,  2000,  2000, 20, height1, color1)
add_lod(  100,   200,   200, 20, height2, color2)

return M
