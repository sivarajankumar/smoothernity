local M = {}

local plane = require 'plane'
local land = require 'land' 
local noise = require 'noise'
local pwld = require 'physwld'
local cfg = require 'config'
local meshes = require 'meshes'

local SCENE = 50
local RES_NEAR = 20
local RES_FAR = 20

local function move_alloc()
    local self = {}
    self.x, self.y, self.z = 0, 0, 0
    return self
end

function M.alloc(centx, centy, centz)
    local self = {}

    local nse = noise.alloc()
    local move = move_alloc()
    local vplayer = api_vector_alloc()
    local text

    local planes =
        {plane.alloc(nse, move, meshes.GROUP_NEAR, land.phys_alloc,
                     cfg.RANGE_NEAR, cfg.RANGE_NEAR, RES_NEAR, centx, centy, centz),
         plane.alloc(nse, move, meshes.GROUP_FAR, land.vis_alloc,
                     cfg.RANGE_FAR, cfg.RANGE_FAR, RES_FAR, centx, centy, centz)}

    function self.free()
        if text ~= nil then
            api_text_free(text)
        end
        api_vector_free(vplayer)
        for k, v in pairs(planes) do
            v.free()
        end
    end

    local function scene_to_world(x, y, z)
        return x - centx - move.x, y - centy - move.y, z - centz - move.z
    end

    function self.attach(mplayer)
        api_vector_mpos(vplayer, mplayer)
    end

    function self.generate(mach)
        api_vector_update(vplayer)
        local wx, wy, wz = scene_to_world(api_vector_get(vplayer))
        for k, v in pairs(planes) do
            v.generate(mach, wx, wy, wz)
        end
    end

    function self.move(car, camc)
        api_vector_update(vplayer)
        local x, y, z = api_vector_get(vplayer)
        local wx, wy, wz = scene_to_world(x, y, z)

        if text ~= nil then
            api_text_free(text)
        end
        text = api_text_alloc(string.format('(%i, %i, %i) (%i, %i, %i)',
                                            x, y, z, wx, wy, wz),
                              API_TEXT_FONT_8_BY_13, 20, 40)

        local dx, dz = 0, 0
        while x + dx < -SCENE do
            dx = dx + SCENE
        end
        while x + dx > SCENE do
            dx = dx - SCENE
        end
        while z + dz < -SCENE do
            dz = dz + SCENE
        end
        while z + dz > SCENE do
            dz = dz - SCENE
        end
        if dx ~= 0 or dz ~= 0 then
            local dv = api_vector_alloc()
            api_vector_const(dv, dx, 0, dz, 0)
            api_physics_wld_move(pwld.wld, dv)
            car.move(dv)
            camc.move(dv)
            api_vector_free(dv)

            move.x = move.x + dx
            move.z = move.z + dz

            for k, v in pairs(planes) do
                v.move()
            end
        end
    end

    function self.showhide()
        api_vector_update(vplayer)
        local wx, wy, wz = scene_to_world(api_vector_get(vplayer))
        for k, v in pairs(planes) do
            v.showhide(wx, wy, wz)
        end
    end

    return self
end

return M
