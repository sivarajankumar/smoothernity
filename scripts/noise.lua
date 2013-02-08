local M = {}

local util = require 'util'

local LENGTH = 256
local WIDTH = 256

function M.alloc(uid)
    local self = {}
    local data = {}

    local function pick(z, x)
        return data[math.floor(z) % LENGTH][math.floor(x) % WIDTH]
    end

    local function get_lerp(z, x)
        local d00 = pick(z, x)
        local d01 = pick(z, x + 1)
        local d10 = pick(z + 1, x)
        local d11 = pick(z + 1, x + 1)
        local d0x = util.lerp(x - math.floor(x), 0, 1, d00, d01)
        local d1x = util.lerp(x - math.floor(x), 0, 1, d10, d11)
        local dzx = util.lerp(z - math.floor(z), 0, 1, d0x, d1x)
        return math.min(1, math.max(0, dzx))
    end

    local function get_spline(z, x)
        local d00 = pick(z - 1, x - 1)
        local d01 = pick(z - 1, x)
        local d02 = pick(z - 1, x + 1)
        local d03 = pick(z - 1, x + 2)
        local d10 = pick(z, x - 1)
        local d11 = pick(z, x)
        local d12 = pick(z, x + 1)
        local d13 = pick(z, x + 2)
        local d20 = pick(z + 1, x - 1)
        local d21 = pick(z + 1, x)
        local d22 = pick(z + 1, x + 1)
        local d23 = pick(z + 1, x + 2)
        local d30 = pick(z + 2, x - 1)
        local d31 = pick(z + 2, x)
        local d32 = pick(z + 2, x + 1)
        local d33 = pick(z + 2, x + 2)
        local d0x = util.spline(x - math.floor(x), 0, 1, d00, d01, d02, d03)
        local d1x = util.spline(x - math.floor(x), 0, 1, d10, d11, d12, d13)
        local d2x = util.spline(x - math.floor(x), 0, 1, d20, d21, d22, d23)
        local d3x = util.spline(x - math.floor(x), 0, 1, d30, d31, d32, d33)
        local dzx = util.spline(z - math.floor(z), 0, 1, d0x, d1x, d2x, d3x)
        return math.min(1, math.max(0, dzx))
    end

    function self.get(z, x)
        return get_spline(z, x)
    end

    for z = 0, LENGTH - 1 do
        local chunk = util.async_read(util.uid_save(string.format('%s_%i', uid, z)))
        if chunk ~= '' then
            data[z] = loadstring(chunk)()
        else
            data[z] = {}
            for x = 0, WIDTH - 1 do
                data[z][x] = math.random()
            end
            do
                local line = 'return {'
                local first_x = true
                for x, v in pairs(data[z]) do
                    if not first_x then
                        line = line .. ', '
                    end
                    first_x = false
                    line = line .. string.format('[%i] = %f', x, v)
                    coroutine.yield(false)
                end
                line = line .. '}'
                util.async_write(util.uid_save(string.format('%s_%i', uid, z)), line)
            end
        end
    end

    return self
end

return M
