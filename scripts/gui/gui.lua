local M = {}

local bar = require 'gui.bar'
local util = require 'util'

local genbar

function M.init()
    bar.init()

    -- generation progress bar
    do
        local sx, sy = util.camera_dims()
        local posx, posy = -sx + 0.1, -sy + 0.1
        local sizex, sizey = 0.5, 0.1
        genbar = bar.alloc(posx, posy, posx + sizex, posy + sizey, 0)
    end
end

function M.done()
    genbar.free()
    bar.done()
end

return M
