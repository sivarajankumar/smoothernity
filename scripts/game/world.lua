local M = {}

local plane = require 'game.plane'
local land = require 'game.land' 
local noise = require 'game.noise'
local pwld = require 'game.physwld'
local cfg = require 'config'
local util = require 'core.util'
local lod = require 'game.lod'
local vector = require 'core.vector'

local SCENE = 50

local function move_alloc(uid)
    local self = {}

    function self.save()
        util.async_write(util.uid_save(string.format('%s.lua', uid)),
            string.format('return %i, %i, %i', self.x, self.y, self.z))
    end

    local chunk = util.async_read(util.uid_save(string.format('%s.lua', uid)))
    if chunk == '' then
        self.x, self.y, self.z = 0, 0, 0
    else
        self.x, self.y, self.z = loadstring(chunk)()
    end

    return self
end

function M.alloc(uid, centx, centy, centz)
    local self = {}

    local planes = {}
    local nse = noise.alloc(string.format('%s_noise', uid))
    local move = move_alloc(string.format('%s_move', uid))
    local vplayer = vector.alloc()
    local generating = false

    function self.free()
        vplayer.free()
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
        vplayer.mpos(mplayer)
    end

    function self.generate()
        generating = true
        vplayer.update(0, API_VECTOR_FORCED_UPDATE)
        local wx, wy, wz = self.scene_to_world(vplayer.get())
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
        vplayer.update(0, API_VECTOR_FORCED_UPDATE)
        local x, y, z = vplayer.get()
        local wx, wy, wz = self.scene_to_world(x, y, z)

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
            local dv = vector.alloc()
            dv.const(dx, dy, dz, 0)
            pwld.wld.move(dv)
            car.move(dv)
            camc.move(dv)
            dv.free()

            move.x = move.x + dx
            move.y = move.y + dy
            move.z = move.z + dz

            for k, v in pairs(planes) do
                v.move()
            end
        end
    end

    function self.showhide()
        vplayer.update(0, API_VECTOR_FORCED_UPDATE)
        local wx, wy, wz = self.scene_to_world(vplayer.get())
        for k, v in pairs(planes) do
            v.showhide(wx, wy, wz)
        end
    end

    function self.gen_progress()
        vplayer.update(0, API_VECTOR_FORCED_UPDATE)
        local wx, wy, wz = self.scene_to_world(vplayer.get())
        local sum = 0
        for k, v in pairs(planes) do
            sum = sum + v.gen_progress(wx, wy, wz)
            coroutine.yield(false)
        end
        return sum / lod.count
    end

    function self.edge_dist()
        vplayer.update(0, API_VECTOR_FORCED_UPDATE)
        local wx, wy, wz = self.scene_to_world(vplayer.get())
        local min_dist = 1
        for k, v in pairs(planes) do
            min_dist = math.min(min_dist, v.edge_dist(wx, wy, wz))
            coroutine.yield(false)
        end
        return min_dist
    end

    function self.save()
        move.save()
    end

    for lodi = 0, lod.count - 1 do
        local landalloc
        if lodi == lod.count - 1 then
            landalloc = land.phys_alloc
        else
            landalloc = land.vis_alloc
        end
        planes[lodi] = plane.alloc(string.format('%s_plane_%i', uid, lodi),
                                   nse, move, lodi, landalloc, centx, centy, centz)
    end

    return self
end

return M
