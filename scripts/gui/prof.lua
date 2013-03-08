local M = {}

local bar = require 'gui.bar'
local util = require 'core.util'

local BORDER = 0.05
local COLOR_BACK = {0, 0, 0, 1}
local COLOR_REF = {1, 1, 1, 1}
local MAX_FRAMES = 300

function M.alloc(xmin, ymin, xmax, ymax, refvalue, ...)
    local self = {}
    local barmin, barmax, barcur, barref, barback
    local maxsum = -math.huge
    local maxsumprev = -math.huge
    local minsum = math.huge
    local minsumprev = math.huge
    local maxvals
    local maxvalsprev
    local minvals
    local minvalsprev
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
            maxsumprev = maxsum
            minsumprev = minsum
            maxvalsprev = maxvals
            minvalsprev = minvals
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
        if sum > maxsumprev then
            maxsumprev = sum
            maxvalsprev = {...}
        end
        if sum < minsumprev then
            minsumprev = sum
            minvalsprev = {...}
        end
        local limit = math.max(refvalue, maxsumprev)
        barref.set(refvalue, limit - refvalue)
        barmax.set(augment(limit, unpack(maxvalsprev)))
        barmin.set(augment(limit, unpack(minvalsprev)))
        barcur.set(augment(limit, ...))
    end

    do
        local b = BORDER * math.min(xmax - xmin, ymax - ymin)
        local h = (ymax-ymin - b*6) / 3
        local cols = {...}
        table.insert(cols, COLOR_BACK)
        barback = bar.alloc(xmin, ymin, xmax, ymax, COLOR_BACK)
        barref = bar.alloc(xmin+b, ymin+b, xmax-b, ymax-b, COLOR_REF, COLOR_BACK)
        barmax = bar.alloc(xmin+b, ymin + b*2 + h*0, xmax-b, ymin + b*2 + h*1, unpack(cols))
        barcur = bar.alloc(xmin+b, ymin + b*3 + h*1, xmax-b, ymin + b*3 + h*2, unpack(cols))
        barmin = bar.alloc(xmin+b, ymin + b*4 + h*2, xmax-b, ymin + b*4 + h*3, unpack(cols))
        barback.set(1)
    end

    return self
end

return M
