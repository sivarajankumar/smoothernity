local M = {}

local bar = require 'gui.bar'
local wait = require 'gui.wait'
local util = require 'util'
local cfg = require 'config'

local genbar, edgebar, frbar, fpsbar, wt
local whole_frames = 0
local accum = 0

local MAX_FRAMES = 600
local THRESH = 1.5

function M.gen_progress(value)
    genbar.set(value)
end

function M.edge_dist(value)
    edgebar.set(value)
end

function M.player_freedom(value)
    frbar.set(value)
end

function M.wait_show()
    wt.show()
end

function M.wait_hide()
    wt.hide()
end

function M.frame_time(value)
    if value > cfg.FRAME_TIME * THRESH then
        whole_frames = 0
    else
        whole_frames = whole_frames + 1
    end
    fpsbar.set(util.lerp(whole_frames, 0, MAX_FRAMES, 0, 1))
end

function M.init()
    bar.init()
    wait.init()

    local sx, sy = util.camera_dims()
    local sizex, sizey = 0.5, 0.05
    local posx, posy = -sx + 0.1, -sy + 0.1

    genbar = bar.alloc(posx, posy, posx + sizex, posy + sizey)

    posy = posy + sizey + 0.05
    edgebar = bar.alloc(posx, posy, posx + sizex, posy + sizey)

    posy = posy + sizey + 0.05
    frbar = bar.alloc(posx, posy, posx + sizex, posy + sizey)

    posy = posy + sizey + 0.05
    fpsbar = bar.alloc(posx, posy, posx + sizex, posy + sizey)

    wt = wait.alloc(sx - 0.3, -sy + 0.3, 0.25)
    wt.hide()
end

function M.done()
    genbar.free()
    edgebar.free()
    frbar.free()
    fpsbar.free()
    wt.free()
    bar.done()
    wait.done()
end

return M
