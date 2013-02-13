local M = {}

local bar = require 'gui.bar'
local util = require 'util'

local BORDER = 0.1
local COLOR_BACK = {0, 0, 0, 1}
local COLOR_REF = {0.5, 0.5, 0.5, 1}
local MAX_FRAMES = 600

function M.alloc(xmin, ymin, xmax, ymax, refvalue, ...)
    local self = {}
    local barmin, barmax, barcur, barref, barback
    local maxsum = -math.huge
    local minsum = math.huge
    local maxvals
    local minvals
    local frames = 0

    function self.free()
        barmin.free()
        barcur.free()
        barmax.free()
        barref.free()
        barback.free()
    end

    local function augment(limit, ...)
        local t = {...}
        table.insert(t, limit - util.sum(...))
        return unpack(t)
    end

    function self.set(...)
        frames = frames + 1
        if frames > MAX_FRAMES then
            frames = 0
            maxsum = -math.huge
            minsum = math.huge
        end
        local sum = util.sum(...)
        if sum > maxsum then
            maxsum = sum
            maxvals = {...}
        end
        if sum < minsum then
            minsum = sum
            minvals = {...}
        end
        local limit = math.max(refvalue, maxsum)
        barref.set(refvalue, limit)
        barmax.set(augment(limit, unpack(maxvals)))
        barmin.set(augment(limit, unpack(minvals)))
        barcur.set(augment(limit, ...))
    end

    do
        local b = BORDER * math.min(xmax - xmin, ymax - ymin)
        local h = (ymax-ymin - b*4) / 3
        local cols = {...}
        table.insert(cols, COLOR_BACK)
        barback = bar.alloc(xmin, ymin, xmax, ymax, COLOR_BACK)
        barref = bar.alloc(xmin+b, ymin+0.5*b, xmax-b, ymax-0.5*b, COLOR_REF, COLOR_BACK)
        barmax = bar.alloc(xmin+b, ymin + b*1 + h*0, xmax-b, ymin + b*1 + h*1, unpack(cols))
        barcur = bar.alloc(xmin+b, ymin + b*2 + h*1, xmax-b, ymin + b*2 + h*2, unpack(cols))
        barmin = bar.alloc(xmin+b, ymin + b*3 + h*2, xmax-b, ymin + b*3 + h*3, unpack(cols))
        barback.set(1)
    end

    return self
end

return M
