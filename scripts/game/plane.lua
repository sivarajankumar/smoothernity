local M = {}

local lod = require 'game.lod'
local cfg = require 'config'
local util = require 'core.util'
local quit = require 'game.quit'

local BUFFER = 20
local REST = 200

-- TODO:
-- Store single continuous texture for the whole plane.
-- Every land chunk should use the same big texture.
-- When it's time to move generation window, use glCopyImageSubData to move texture image.
-- Also adjustment to the existing chunks' texture coordinates should be made using shaders.
-- This way, arbitrary texture can be used for the terrain without visible seams
-- between land chunks even in case of mip-mapping.

function M.alloc(uid, noise, move, lodi, landalloc, centx, centy, centz)
    local self = {}

    local lands = {}
    local size = lod.lods[lodi].size
    local genx, genz = 0, 0

    function self.free()
        for z, xs in pairs(lands) do
            for x, lnd in pairs(xs) do
                lnd.free()
            end
        end
    end

    local function world_to_grid(x, y, z)
        return math.floor(x / size), y, math.floor(z / size)
    end

    local function grid_to_world(x, y, z)
        return centx + x * size, centy, centz + z * size
    end

    local function vis_range()
        local sx, sy = util.camera_dims()
        local cd = lod.lods[lodi].clip_far
        local cx = sx * cd / cfg.CAMERA_DIST
        local cy = sy * cd / cfg.CAMERA_DIST
        local c = math.sqrt(cx*cx + cy*cy)
        return math.sqrt(c*c + cd*cd)
    end

    local function get_land(z, x)
        if lands[z] ~= nil then
            return lands[z][x]
        end
    end

    local function add_land(wrk, z, x)
        if lands[z] == nil then
            lands[z] = {}
        end
        if lands[z][x] == nil and not quit.requested() then
            local wx, wy, wz = grid_to_world(x, 0, z)
            wrk.plan(
                function()
                    lands[z][x] = landalloc(string.format('%s_land_%i_%i', uid, z, x),
                                            noise, move, lodi, wx, wy, wz, x, 0, z, get_land)
                    lands[z][x].notify()
                end)
        end
    end

    local function gen_bounds(z, x)
        local r = vis_range() + BUFFER + REST
        local xmin, ymin, zmin = world_to_grid(x - r, 0, z - r)
        local xmax, ymax, zmax = world_to_grid(x + r, 0, z + r)
        return zmin, xmin, zmax, xmax
    end

    local function gen_align(z, x, wz, wx)
        while x < wx - BUFFER do
            x = x + 0.5 * BUFFER
        end
        while x > wx + BUFFER do
            x = x - 0.5 * BUFFER
        end
        while z < wz - BUFFER do
            z = z + 0.5 * BUFFER
        end
        while z > wz + BUFFER do
            z = z - 0.5 * BUFFER
        end
        return z, x
    end

    function self.generate(wrk, wx, wy, wz)

        genz, genx = gen_align(genz, genx, wz, wx)
        local zmin, xmin, zmax, xmax = gen_bounds(genz, genx)

        -- clear
        do
            for z, xs in pairs(lands) do
                local empty = true
                for x, lnd in pairs(xs) do
                    if x < xmin or x > xmax or z < zmin or z > zmax then
                        xs[x] = nil
                        lnd.notify()
                        lnd.delete()
                        lnd.free()
                    else
                        empty = false
                    end
                end
                if empty == true then
                    lands[z] = nil
                end
            end
        end

        -- generate
        do
            local gx, gy, gz = world_to_grid(genx, 0, genz)
            for z = zmin, zmax do
                for x = xmin, xmax do
                    add_land(wrk, z, x)
                end
            end
        end
    end

    function self.gen_progress(wx, wy, wz)
        local zmin, xmin, zmax, xmax = gen_bounds(gen_align(genz, genx, wz, wx))
        local count = 0
        for z = zmin, zmax do
            for x = xmin, xmax do
                if lands[z] ~= nil and lands[z][x] ~= nil then
                    count = count + 1
                end
            end
        end
        local total = (zmax - zmin + 1) * (xmax - xmin + 1)
        return count / total
    end

    function self.edge_dist(wx, wy, wz)
        local r = vis_range() + REST
        local xmin, ymin, zmin = world_to_grid(wx - r, 0, wz - r)
        local xmax, ymax, zmax = world_to_grid(wx + r, 0, wz + r)
        local min_dist = r
        for z = zmin, zmax do
            for x = xmin, xmax do
                if lands[z] == nil or lands[z][x] == nil then
                    local cxmin, cymin, czmin = grid_to_world(x, 0, z)
                    local cxmax, cymax, czmax = grid_to_world(x+1, 0, z+1)
                    if wx >= cxmin and wx <= cxmax and wz >= czmin and wz <= czmax then
                        return 0
                    elseif wx >= cxmin and wx <= cxmax then
                        local zdist = math.min(math.abs(wz - czmin), math.abs(wz - czmax))
                        min_dist = math.min(min_dist, zdist)
                    elseif wz >= czmin and wz <= czmax then
                        local xdist = math.min(math.abs(wx - cxmin), math.abs(wx - cxmax))
                        min_dist = math.min(min_dist, xdist)
                    else
                        local xdist = math.min(math.abs(wx - cxmin), math.abs(wx - cxmax))
                        local zdist = math.min(math.abs(wz - czmin), math.abs(wz - czmax))
                        min_dist = math.max(min_dist, math.max(xdist, zdist))
                    end
                end
            end
        end
        return util.lerp(min_dist, vis_range(), vis_range() + REST, 0, 1)
    end

    function self.move()
        for z, xs in pairs(lands) do
            for x, lnd in pairs(xs) do
                lnd.move()
            end
        end
    end

    function self.showhide(wx, wy, wz)
        local r = vis_range()
        local xmin, ymin, zmin = world_to_grid(wx - r, 0, wz - r)
        local xmax, ymax, zmax = world_to_grid(wx + r, 0, wz + r)
        for z, xs in pairs(lands) do
            for x, lnd in pairs(xs) do
                if z < zmin or z > zmax or x < xmin or x > xmax then
                    lnd.hide()
                else
                    lnd.show()
                end
            end
        end
    end

    return self
end

return M
