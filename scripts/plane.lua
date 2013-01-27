local M = {}

local lod = require 'lod'
local cfg = require 'config'
local util = require 'util'
local quit = require 'quit'

local BUFFER = 20
local REST = 50

function M.alloc(noise, move, lodi, landalloc, centx, centy, centz)
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

    local function add_land(mach, z, x)
        if lands[z] == nil then
            lands[z] = {}
        end
        if lands[z][x] == nil and not quit.requested() then
            local wx, wy, wz = grid_to_world(x, 0, z)
            lands[z][x] = landalloc(mach, noise, move, lodi, wx, wy, wz)
        end
    end

    local function gen_bounds()
        local r = vis_range() + BUFFER + REST
        local xmin, ymin, zmin = world_to_grid(genx - r, 0, genz - r)
        local xmax, ymax, zmax = world_to_grid(genx + r, 0, genz + r)
        return zmin, xmin, zmax, xmax
    end

    function self.generate(mach, wx, wy, wz)

        -- align
        while genx < wx - BUFFER do
            genx = genx + BUFFER
        end
        while genx > wx + BUFFER do
            genx = genx - BUFFER
        end
        while genz < wz - BUFFER do
            genz = genz + BUFFER
        end
        while genz > wz + BUFFER do
            genz = genz - BUFFER
        end

        local zmin, xmin, zmax, xmax = gen_bounds()

        -- clear
        do
            for z, xs in pairs(lands) do
                local empty = true
                for x, lnd in pairs(xs) do
                    if x < xmin or x > xmax or z < zmin or z > zmax then
                        lnd.free()
                        xs[x] = nil
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
            add_land(mach, gz, gx)
            for z = zmin, zmax do
                for x = xmin, xmax do
                    add_land(mach, z, x)
                end
            end
        end
    end

    function self.gen_progress()
        local zmin, xmin, zmax, xmax = gen_bounds()
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
