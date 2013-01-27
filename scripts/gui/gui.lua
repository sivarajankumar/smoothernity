local M = {}

local bar = require 'gui.bar'
local util = require 'util'

local genbar, exbar

function M.gen_progress(value)
    genbar.set(value)
end

function M.existence(value)
end

function M.init()
    bar.init()

    -- generation progress bar
    do
        local sx, sy = util.camera_dims()
        local sizex, sizey = 0.5, 0.05
        local posx, posy = -sx + 0.1, -sy + 0.1
        genbar = bar.alloc(posx, posy, posx + sizex, posy + sizey)
    end

    -- existence bar
    do
        local sx, sy = util.camera_dims()
        local sizex, sizey = 0.5, 0.05
        local posx, posy = -sx + 0.1, -sy + 0.1 + sizey + 0.05
        exbar = bar.alloc(posx, posy, posx + sizex, posy + sizey)
    end
end

function M.done()
    genbar.free()
    exbar.free()
    bar.done()
end

return M
