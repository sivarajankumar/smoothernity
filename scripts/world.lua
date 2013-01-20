local M = {}

local land = require 'land' 
local noise = require 'noise'

function M.alloc(mach, x, y, z)
    local self = {}
    local lands = {}

    self.mach = mach
    self.noise = noise.alloc()
    self.centx, self.centy, self.centz = x, y, z
    local vplayer = api_vector_alloc()
    local frames = 0
    local text
    local bound_front, bound_back, bound_left, bound_right

    function self.free()
        if text ~= nil then
            api_text_free(text)
        end
        api_vector_free(vplayer)
        for z, xs in pairs(lands) do
            for x, lnd in pairs(xs) do
                lnd.free()
            end
        end
    end

    local function to_grid(x, y, z)
        return math.floor(((x - self.centx) / land.SIZE_X) + 0.5),
               y - self.centy,
               math.floor(((z - self.centz) / land.SIZE_Z) + 0.5)
    end

    function self.attach(mplayer)
        api_vector_mpos(vplayer, mplayer)
        local x, y, z, w = api_vector_get(vplayer)
        x, y, z = to_grid(x, y, z)
        bound_back = z + 1
        bound_front = z
        bound_left = x
        bound_right = x + 1
    end

    local function get_land(z, x)
        if lands[z] ~= nil then
            return lands[z][x]
        end
    end

    local function add_land(z, x)
        if lands[z] == nil then
            lands[z] = {}
        end
        if lands[z][x] == nil then
            lands[z][x] = land.alloc(self, z, x)
        end
    end

    function self.update()
        local px, py, pz, pw = api_vector_get(vplayer)
        if text ~= nil then
            api_text_free(text)
        end
        local gx, gy, gz = to_grid(px, py, pz)
        text = api_text_alloc(string.format('(%i, %i, %i) (%i, %i, %i)', px, py, pz, gx, gy, gz), API_TEXT_FONT_8_BY_13, 20, 40)
        while gx < bound_left do
            bound_left = bound_left - 1
            bound_right = bound_right - 1
        end
        while gx > bound_right do
            bound_left = bound_left + 1
            bound_right = bound_right + 1
        end
        while gz > bound_back do
            bound_back = bound_back + 1
            bound_front = bound_front + 1
        end
        while gz < bound_front do
            bound_back = bound_back - 1
            bound_front = bound_front - 1
        end
        add_land(gz, gx)
        for z = bound_front, bound_back do
            for x = bound_left, bound_right do
                add_land(z, x)
            end
        end
        for z = bound_front - 1, bound_back + 1 do
            for x = bound_left - 1, bound_right + 1 do
                add_land(z, x)
            end
        end
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

    return self
end

return M
