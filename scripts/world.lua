local M = {}

local plane = require 'plane'
local land = require 'land' 
local noise = require 'noise'
local pwld = require 'physwld'
local cfg = require 'config'
local util = require 'util'
local lod = require 'lod'

local SCENE = 50

local function move_alloc()
    local self = {}
    self.x, self.y, self.z = 0, 0, 0
    return self
end

function M.alloc(centx, centy, centz)
    local self = {}

    local planes = {}
    local nse = noise.alloc('noise')
    local move = move_alloc()
    local vplayer = api_vector_alloc()
    local generating = false
    local text

    function self.free()
        if text ~= nil then
            api_text_free(text)
        end
        api_vector_free(vplayer)
        for k, v in pairs(planes) do
            v.free()
        end
    end

    function self.scene_to_world(x, y, z)
        return x - centx - move.x, y - centy - move.y, z - centz - move.z
    end

    function self.world_to_scene(x, y, z)
        return x + centx + move.x, y + centy + move.y, z + centz + move.z
    end

    function self.attach(mplayer)
        api_vector_mpos(vplayer, mplayer)
    end

    function self.generate()
        generating = true
        api_vector_update(vplayer)
        local wx, wy, wz = self.scene_to_world(api_vector_get(vplayer))
        for lodi = lod.count - 1, 0, -1 do
            planes[lodi].generate(wx, wy, wz)
        end
        generating = false
    end

    function self.height(z, x)
        local y = lod.lods[lod.count - 1].heightfunc(nse, z, x)
        y = util.lerp(y, 0, 1, -0.5, 0.5) * cfg.LAND_HEIGHT
        return y
    end

    function self.move(car, camc)
        api_vector_update(vplayer)
        local x, y, z = api_vector_get(vplayer)
        local wx, wy, wz = self.scene_to_world(x, y, z)

        do
            if text ~= nil then
                api_text_free(text)
            end
            local str = ''
            if generating then
                str = str .. 'G ' 
            else
                str = str .. '  ' 
            end
            str = str .. string.format('(% 3i, % 3i, % 3i) (%i, %i, %i)',
                                       x, y, z, wx, wy, wz)
            text = api_text_alloc(str, API_TEXT_FONT_8_BY_13, 20, 40)
        end

        local dx, dy, dz = 0, 0, 0
        while x + dx < -SCENE do
            dx = dx + SCENE
        end
        while x + dx > SCENE do
            dx = dx - SCENE
        end
        while y + dy < -SCENE do
            dy = dy + SCENE
        end
        while y + dy > SCENE do
            dy = dy - SCENE
        end
        while z + dz < -SCENE do
            dz = dz + SCENE
        end
        while z + dz > SCENE do
            dz = dz - SCENE
        end
        if dx ~= 0 or dy ~= 0 or dz ~= 0 then
            local dv = api_vector_alloc()
            api_vector_const(dv, dx, dy, dz, 0)
            api_physics_wld_move(pwld.wld, dv)
            car.move(dv)
            camc.move(dv)
            api_vector_free(dv)

            move.x = move.x + dx
            move.y = move.y + dy
            move.z = move.z + dz

            for k, v in pairs(planes) do
                v.move()
            end
        end
    end

    function self.showhide()
        api_vector_update(vplayer)
        local wx, wy, wz = self.scene_to_world(api_vector_get(vplayer))
        for k, v in pairs(planes) do
            v.showhide(wx, wy, wz)
        end
    end

    function self.gen_progress()
        api_vector_update(vplayer)
        local wx, wy, wz = self.scene_to_world(api_vector_get(vplayer))
        local sum = 0
        for k, v in pairs(planes) do
            sum = sum + v.gen_progress(wx, wy, wz)
        end
        return sum / lod.count
    end

    function self.edge_dist()
        api_vector_update(vplayer)
        local wx, wy, wz = self.scene_to_world(api_vector_get(vplayer))
        local min_dist = 1
        for k, v in pairs(planes) do
            min_dist = math.min(min_dist, v.edge_dist(wx, wy, wz))
        end
        return min_dist
    end

    for lodi = 0, lod.count - 1 do
        local landalloc
        if lodi == lod.count - 1 then
            landalloc = land.phys_alloc
        else
            landalloc = land.vis_alloc
        end
        planes[lodi] = plane.alloc(nse, move, lodi, landalloc, centx, centy, centz)
    end

    return self
end

return M
