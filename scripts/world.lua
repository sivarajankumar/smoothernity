local M = {}

local land = require 'land' 
local noise = require 'noise'

local FRAMES = 10

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

    local function set_land(z, x, lnd)
        if lands[z] == nil then
            lands[z] = {}
        end
        lands[z][x] = lnd
    end

    function self.update()
        if frames >= FRAMES then
            frames = 0
            local x, y, z, w = api_vector_get(vplayer)
            if text ~= nil then
                api_text_free(text)
            end
            text = api_text_alloc(string.format('%.2f, %.2f, %.2f', x, y, z), API_TEXT_FONT_8_BY_13, 20, 20)
            x, y, z = to_grid(x, y, z)
            while x < bound_left do
                bound_left = bound_left - 1
                bound_right = bound_right - 1
            end
            while x > bound_right do
                bound_left = bound_left + 1
                bound_right = bound_right + 1
            end
            while z > bound_back do
                bound_back = bound_back + 1
                bound_front = bound_front + 1
            end
            while z < bound_front do
                bound_back = bound_back - 1
                bound_front = bound_front - 1
            end
            for z = bound_front - 1, bound_back + 1 do
                for x = bound_left - 1, bound_right + 1 do
                    if get_land(z, x) == nil then
                        set_land(z, x, land.alloc(self, z, x))
                    end
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
        else
            frames = frames + 1
        end
    end

    return self
end

return M
