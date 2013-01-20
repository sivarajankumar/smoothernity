local M = {}

local util = require 'util'

local LENGTH = 256
local WIDTH = 256

function M.alloc()
    local self = {}
    local data = {}

    local function pick(z, x)
        return data[math.floor(z % LENGTH)][math.floor(x % WIDTH)]
    end

    function self.get(z, x, steps, progress)
        local sx, sz, sv = 1, 1, 1
        local svsum = 0
        local value = 0
        for s = 1, steps do
            local d00 = pick(z, x)
            local d01 = pick(z, x + 1)
            local d10 = pick(z + 1, x)
            local d11 = pick(z + 1, x + 1)
            local d0x = util.lerp(x % sx, 0, sx, d00, d01)
            local d1x = util.lerp(x % sx, 0, sx, d10, d11)
            local dzx = util.lerp(z % sz, 0, sz, d0x, d1x)
            value = value + dzx * sv
            sx = sx * WIDTH
            sz = sz * LENGTH
            sv = sv * progress
            svsum = svsum + sv
        end
        return value / svsum
    end

    for z = 0, LENGTH - 1 do
        data[z] = {}
        for x = 0, WIDTH - 1 do
            data[z][x] = math.random()
        end
    end

    return self
end

return M
