local M = {}

local land = require 'land' 
local noise = require 'noise'
local pwld = require 'physwld'
local cfg = require 'config'

local SIZE_X = cfg.VIS_RANGE
local SIZE_Z = cfg.VIS_RANGE
local RES_X = 40
local RES_Z = 40

function M.alloc(x, y, z)
    local self = {}
    local lands = {}

    local nse = noise.alloc()
    local centx, centy, centz = x, y, z
    local movex, movey, movez = 0, 0, 0
    local sizex, sizez = SIZE_X, SIZE_Z
    local resx, resz = RES_X, RES_Z
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

    local function scene_to_world(x, y, z)
        return x - centx - movex, y - centy - movey, z - centz - movez
    end

    local function world_to_grid(x, y, z)
        return math.floor((x / sizex) + 0.5), y, math.floor((z / sizez) + 0.5)
    end

    local function grid_to_world(x, y, z)
        return centx + x * sizex, centy, centz + z * sizez
    end

    function self.attach(mplayer)
        api_vector_mpos(vplayer, mplayer)
        if bound_back == nil or bound_front == nil or bound_left == nil or bound_right == nil then
            api_vector_update(vplayer)
            local x, y, z = world_to_grid(scene_to_world(api_vector_get(vplayer)))
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
            local wx, wy, wz = grid_to_world(x, 0, z)
            lands[z][x] = land.alloc(nse, mach, wx, wy, wz,
                                     movex, movey, movez,
                                     sizex, sizez, resx, resz)
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
            api_vector_update(vplayer)
            local px, py, pz, pw = api_vector_get(vplayer)
            if text ~= nil then
                api_text_free(text)
            end
            gx, gy, gz = world_to_grid(scene_to_world(px, py, pz))
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

    function self.move(car, camc)
        if (move_dz ~= 0 or move_dx ~= 0) and not generating then
            local v = api_vector_alloc()
            api_vector_const(v, move_dx * sizex, 0, move_dz * sizez, 0)
            api_physics_wld_move(pwld.wld, v)
            car.move(v)
            camc.move(v)
            api_vector_free(v)

            movez = movez + (move_dz * sizez)
            movex = movex + (move_dx * sizex)

            move_dz, move_dx = 0, 0
        end
    end

    function self.showhide()
        api_vector_update(vplayer)
        local px, py, pz = scene_to_world(api_vector_get(vplayer))
        for z, xs in pairs(lands) do
            for x, lnd in pairs(xs) do
                local lx, ly, lz = grid_to_world(x, 0, z)
                if math.max(math.abs(px-lx), math.abs(pz-lz)) <= cfg.VIS_RANGE then
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
