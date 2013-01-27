local M = {}

local bar = require 'gui.bar'
local util = require 'util'

local genbar, edgebar

function M.gen_progress(value)
    genbar.set(value)
end

function M.edge_dist(value)
    edgebar.set(value)
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

    -- edge distance bar
    do
        local sx, sy = util.camera_dims()
        local sizex, sizey = 0.5, 0.05
        local posx, posy = -sx + 0.1, -sy + 0.1 + sizey + 0.05
        edgebar = bar.alloc(posx, posy, posx + sizex, posy + sizey)
    end
end

function M.done()
    genbar.free()
    edgebar.free()
    bar.done()
end

return M
