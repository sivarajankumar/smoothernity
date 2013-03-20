local M = {}

local cfg = require 'config'
local noise = require 'game.noise'
local lod = require 'game.lod'
local util = require 'core.util'
local poolbuf = require 'core.pool.buf'
local render = require 'core.render.render'

function M.thread_run(thi)
    local uid, noise_state, hmap_state, vb_state, ib_state, lodi, basx, basy, basz =
        loadstring(api_thread_respond(thi, ''))()

    local size = lod.lods[lodi].size
    local res = lod.lods[lodi].res
    local nse = noise.restore(noise_state)
    local hmap = poolbuf.restore(hmap_state)
    local vb = render.vbuf_restore(vb_state)
    local ib = render.ibuf_restore(ib_state)

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
               util.clamp(b, 0, 1)
    end

    -- height map
    do
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
    end

    -- vertex buffer
    do
        local fname = util.uid_cache(string.format('%s_colmap.lua', uid))
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
                    local r, g, b = color(z, x)
                    local h = api_buf_get(hmap.start, API_BUF_IPL_NEAREST, res, res, x, z)
                    vb.set(x+z*res, x-0.5*(res-1), h, z-0.5*(res-1), r, g, b, 1, 0, 0)
                    f:write(string.format('{%.3f, %.3f, %.3f}', r, g, b))
                end
            end
            f:write('\n}\n')
            f:close()
        else
            for i, v in pairs(loadstring(data)()) do
                local r, g, b = unpack(v)
                local x = (i - 1) % res
                local z = ((i - 1) - x) / res
                local h = api_buf_get(hmap.start, API_BUF_IPL_NEAREST, res, res, x, z)
                vb.set(i - 1, x-0.5*(res-1), h, z-0.5*(res-1), r, g, b, 1, 0, 0)
            end
        end
    end

    -- index buffer
    do
        for z = 0, res - 2 do
            for x = 0, res - 2 do
                local i00 = x + z * res
                local i01 = x + (z + 1) * res
                local i10 = (x + 1) + z * res
                local i11 = (x + 1) + (z + 1) * res
                local i = (x + z * (res - 1)) * 6
                ib.set(i,  i00,i01,i10,  i10,i01,i11)
            end
        end
    end
end

return M
