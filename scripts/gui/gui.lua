local M = {}

local bar = require 'gui.bar'
local wait = require 'gui.wait'
local util = require 'util'
local cfg = require 'config'
local prof = require 'gui.prof'

local genbar, edgebar, frbar, fpsbar, wt, gpuprof, cpuprof
local whole_frames = 0
local accum = 0

local MAX_FRAMES = 600
local THRESH = 1

function M.gen_progress(value)
    genbar.set(value, 1 - value)
end

function M.edge_dist(value)
    edgebar.set(value, 1 - value)
end

function M.player_freedom(value)
    frbar.set(value, 1 - value)
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
    local x = util.lerp(whole_frames, 0, MAX_FRAMES, 0, 1)
    fpsbar.set(x, 1 - x)
end

function M.gpu_times(logic, draw, swap)
    gpuprof.set(logic, draw, swap)
end

function M.cpu_times(core, control, work, rupdate, rdraw, rswap)
    cpuprof.set(core, control, work, rupdate, rdraw, rswap)
end

function M.init()
    bar.init()
    wait.init()

    local sx, sy = util.camera_dims()
    local sizex, sizey = 0.5, 0.05
    local posx, posy = -sx + 0.1, -sy + 0.1

    genbar = bar.alloc(posx, posy, posx + sizex, posy + sizey,
                       {0,1,0,1}, {0,0,0,1})

    posy = posy + sizey + 0.05
    edgebar = bar.alloc(posx, posy, posx + sizex, posy + sizey,
                       {0,1,0,1}, {0,0,0,1})

    posy = posy + sizey + 0.05
    frbar = bar.alloc(posx, posy, posx + sizex, posy + sizey,
                      {0,1,0,1}, {0,0,0,1})

    posy = posy + sizey + 0.05
    fpsbar = bar.alloc(posx, posy, posx + sizex, posy + sizey,
                       {0,1,0,1}, {0,0,0,1})

    wt = wait.alloc(-sx + 0.3, sy - 0.3, 0.25)
    wt.hide()

    sizex, sizey = 0.5, 0.15
    posx, posy = sx - sizex - 0.1, -sy + 0.1

    gpuprof = prof.alloc(posx, posy, posx + sizex, posy + sizey, cfg.FRAME_TIME,
                         {0,0.5,1,1}, {0,1,0,1}, {1,0.5,0,1})

    posy = posy + sizey + 0.05
    cpuprof = prof.alloc(posx, posy, posx + sizex, posy + sizey, cfg.FRAME_TIME,
                         {1,0,1,1}, {1,1,0,1}, {0,0.5,1,1},
                         {1,0.5,0.5,1}, {0,1,0,1}, {1,0.5,0,1})
end

function M.done()
    gpuprof.free()
    cpuprof.free()
    genbar.free()
    edgebar.free()
    frbar.free()
    fpsbar.free()
    wt.free()
    bar.done()
    wait.done()
end

return M
