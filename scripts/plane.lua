local M = {}

local lod = require 'lod'
local cfg = require 'config'
local util = require 'util'

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
        local clip = lod.lods[lodi].clip_far
        local fov = util.camera_fov(cfg.CAMERA_DIST)
        return clip / math.cos(0.5*fov)
    end

    local function add_land(mach, z, x)
        if lands[z] == nil then
            lands[z] = {}
        end
        if lands[z][x] == nil then
            local wx, wy, wz = grid_to_world(x, 0, z)
            lands[z][x] = landalloc(mach, noise, move, lodi, wx, wy, wz)
        end
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

        local r = vis_range() + BUFFER + REST
        local xmin, ymin, zmin = world_to_grid(genx - r, 0, genz - r)
        local xmax, ymax, zmax = world_to_grid(genx + r, 0, genz + r)

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
