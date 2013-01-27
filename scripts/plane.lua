local M = {}

local lod = require 'lod'

function M.alloc(noise, move, lodi, landalloc, centx, centy, centz)
    local self = {}

    local lands = {}
    local size = lod.lods[lodi].size
    local bound_front, bound_back = 0, 1
    local bound_left, bound_right = 0, 1

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

        local gx, gy, gz = world_to_grid(wx, wy, wz)

        -- align
        do
            while gx < bound_left do
                bound_left = bound_left - 1
                bound_right = bound_right - 1
            end
            while gx > bound_right do
                bound_left = bound_left + 1
                bound_right = bound_right + 1
            end
            while gz < bound_front do
                bound_back = bound_back - 1
                bound_front = bound_front - 1
            end
            while gz > bound_back do
                bound_back = bound_back + 1
                bound_front = bound_front + 1
            end
        end

        -- clear
        do
            for z, xs in pairs(lands) do
                if (z < bound_front - 1) or (z > bound_back + 1) then
                    for x, lnd in pairs(xs) do
                        lnd.free()
                    end
                    lands[z] = nil
                else
                    local empty = true
                    for x, lnd in pairs(xs) do
                        if (x < bound_left - 1) or (x > bound_right + 1) then
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
        end

        -- generate
        do
            add_land(mach, gz, gx)
            for z = bound_front, bound_back do
                for x = bound_left, bound_right do
                    add_land(mach, z, x)
                end
            end
            for z = bound_front - 1, bound_back + 1 do
                for x = bound_left - 1, bound_right + 1 do
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
        local vis_range = lod.lods[lodi].vis_range
        for z, xs in pairs(lands) do
            for x, lnd in pairs(xs) do
                local lx, ly, lz = grid_to_world(x, 0, z)
                lx = lx + 0.5 * size
                lz = lz + 0.5 * size
                if math.max(math.abs(wx-lx), math.abs(wz-lz)) <= vis_range then
                    lnd.show()
                else
                    lnd.hide()
                end
            end
        end
    end

    return self
end

return M
