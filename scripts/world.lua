local M = {}

local land = require 'land' 
local noise = require 'noise'

local CELL_SIZE_X = 50
local CELL_SIZE_Z = 50

function M.alloc(x, y, z)
    local self = {}
    local lands = {}

    self.noise = noise.alloc()
    self.centx, self.centy, self.centz = x, y, z
    self.movex, self.movey, self.movez = 0, 0, 0
    self.cell_size_x = CELL_SIZE_X
    self.cell_size_z = CELL_SIZE_Z
    local vplayer = api_vector_alloc()
    local frames = 0
    local text
    local bound_front, bound_back, bound_left, bound_right
    local generating = false
    local move_dz, move_dx = 0, 0

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
        return math.floor(((x - self.centx - self.movex) / self.cell_size_x) + 0.5),
               y - self.centy - self.movey,
               math.floor(((z - self.centz - self.movez) / self.cell_size_z) + 0.5)
    end

    function self.attach(mplayer)
        api_vector_mpos(vplayer, mplayer)
        if bound_back == nil or bound_front == nil or bound_left == nil or bound_right == nil then
            local x, y, z, w = api_vector_get(vplayer)
            x, y, z = to_grid(x, y, z)
            bound_back = z + 1
            bound_front = z
            bound_left = x
            bound_right = x + 1
        end
    end

    local function get_land(z, x)
        if lands[z] ~= nil then
            return lands[z][x]
        end
    end

    local function add_land(mach, z, x)
        if lands[z] == nil then
            lands[z] = {}
        end
        if lands[z][x] == nil then
            lands[z][x] = land.alloc(self, mach, z, x)
        end
    end

    function self.generate(mach)
        local gx, gy, gz

        if move_dz ~= 0 or move_dx ~= 0 then
            return
        end
        generating = true

        -- align
        do
            local px, py, pz, pw = api_vector_get(vplayer)
            if text ~= nil then
                api_text_free(text)
            end
            gx, gy, gz = to_grid(px, py, pz)
            text = api_text_alloc(string.format('(%i, %i, %i) (%i, %i, %i)',
                                                px, py, pz, gx, gy, gz),
                                  API_TEXT_FONT_8_BY_13, 20, 40)
            while gx < bound_left do
                move_dx = move_dx + 1
                bound_left = bound_left - 1
                bound_right = bound_right - 1
            end
            while gx > bound_right do
                move_dx = move_dx - 1
                bound_left = bound_left + 1
                bound_right = bound_right + 1
            end
            while gz < bound_front do
                move_dz = move_dz + 1
                bound_back = bound_back - 1
                bound_front = bound_front - 1
            end
            while gz > bound_back do
                move_dz = move_dz - 1
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

        generating = false
    end

    function self.move(car)
        if (move_dz ~= 0 or move_dx ~= 0) and not generating then
            io.write(string.format('moving world by %i, %i, %i\n', move_dx, 0, move_dz))
            move_dz, move_dx = 0, 0

            do
                local px, py, pz, pw = api_vector_get(vplayer)
                local gx, gy, gz = to_grid(px, py, pz)
                io.write(string.format('car before move: (%i, %i, %i), (%i, %i, %i)\n',
                         px, py, pz, gx, gy, gz))
            end

            do
                local v = api_vector_alloc()
                api_vector_const(v, move_dx * self.cell_size_x, 0, move_dz * self.cell_size_z, 0)
                api_physics_move(v)
                api_vector_free(v)
            end

            self.movez = self.movez + (move_dz * self.cell_size_z)
            self.movex = self.movex + (move_dx * self.cell_size_x)

            do
                local px, py, pz, pw = api_vector_get(vplayer)
                local gx, gy, gz = to_grid(px, py, pz)
                io.write(string.format('car after move: (%i, %i, %i), (%i, %i, %i)\n',
                         px, py, pz, gx, gy, gz))
            end

            move_dz, move_dx = 0, 0
        end
    end

    return self
end

return M
