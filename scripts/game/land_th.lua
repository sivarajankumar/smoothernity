local M = {}

local cfg = require 'config'
local noise = require 'game.noise'
local lod = require 'game.lod'
local util = require 'core.util'
local poolbuf = require 'core.pool.buf'

function M.thread_run(thi)
    local uid, noise_state, hmap_state, lodi, basx, basy, basz =
        loadstring(api_thread_respond(thi, ''))()

    local funcs = {}
    local size = lod.lods[lodi].size
    local res = lod.lods[lodi].res
    local nse = noise.restore(noise_state)
    local hmap = poolbuf.restore(hmap_state)

    local function to_world(z, x)
        return basz + (z * size / (res-1)),
               basx + (x * size / (res-1))
    end

    local function color_noise(z, x, ofsz, ofsx)
        local wz, wx = to_world(z, x)
        wz = wz + ofsz
        wx = wx + ofsx
        return lod.lods[lodi].colorfunc(nse, wz, wx)
    end

    local function height_noise(z, x)
        local wz, wx = to_world(z, x)
        return lod.lods[lodi].heightfunc(nse, wz, wx)
    end

    local function color(z, x)
        local r = color_noise(z, x, 0, 0)
        local g = color_noise(z, x, 300, 400)
        local b = color_noise(z, x, 1000, -500)
        local len = math.sqrt(r*r + g*g + b*b)
        if len > 0.1 then
            r = r / len
            g = g / len
            b = b / len
        else
            r, g, b = 0.1, 0.1, 0.1
        end
        return util.clamp(r, 0, 1),
               util.clamp(g, 0, 1),
               util.clamp(b, 0, 1),
               1
    end

    local function keep_going()
        funcs[api_thread_respond(thi, '')]()
    end

    function funcs.make_hmap()
        local fname = util.uid_cache(string.format('%s_hmap.lua', uid))
        local data = util.sync_read(fname)
        if data == '' then
            local f = io.open(fname, 'w')
            f:write('return {')
            local cnt = 0
            for z = 0, res - 1 do
                for x = 0, res - 1 do
                    if cnt >= cfg.SAVE_NUMS_PER_ROW then
                        cnt = 0
                    end
                    if z > 0 or x > 0 then
                        f:write(', ')
                    end
                    if cnt == 0 then
                        f:write('\n    ')
                    end
                    cnt = cnt + 1
                    local v = util.lerp(height_noise(z, x), 0, 1, -0.5, 0.5) * cfg.LAND_HEIGHT
                    hmap.set(x + z * res, v)
                    f:write(string.format('%f', v))
                end
            end
            f:write('\n}\n')
            f:close()
        else
            for i, v in pairs(loadstring(data)()) do
                hmap.set(i - 1, v)
            end
        end
        keep_going()
    end

    function funcs.finish()
    end

    keep_going()
end

return M
