local M = {}

local land = require('land')

function M.alloc(x, y, z)
    local self = {}
    local lands = {}

    function self.free()
        for z, xs in pairs(lands) do
            for x, lnd in pairs(xs) do
                lnd.free()
            end
        end
    end

    local function get_land(z, x)
        if lands[z] ~= nil then
            return lands[z][x]
        end
    end

    local function set_land(z, x, lnd)
        if lands[z] == nil then
            lands[z] = {}
        end
        lands[z][x] = lnd
    end

    local function add_land(z, x)
        local left = get_land(z, x - 1)
        local right = get_land(z, x + 1)
        local front = get_land(z - 1, x)
        local back = get_land(z + 1, x)
        if left ~= nil or right ~= nil or front ~= nil or back ~= nil then
            set_land(z, x, land.alloc_join(left, right, front, back))
        end
    end

    set_land(0, 0, land.alloc_root(x, y, z))

    add_land( 1, 0)
    add_land(-1, 0)
    add_land( 0, 1)
    add_land( 0, -1)

    add_land(-1, -1)
    add_land(-1, 1)
    add_land( 1, -1)
    add_land( 1, 1)

    return self
end

return M
