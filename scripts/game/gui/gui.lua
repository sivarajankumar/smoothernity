local M = {}

local bar = require 'game.gui.bar'
local wait = require 'game.gui.wait'
local util = require 'core.util'
local cfg = require 'config'
local guiprof = require 'game.gui.prof'
local color = require 'game.color'
local textest = require 'game.gui.textest'
local prof = require 'game.prof'

local MAX_FRAMES = 600
local THRESH = 1.1

local genbar, edgebar, frbar, fpsbar, wt, gpuprof, cpuprof, threadprof, ttest
local whole_frames = 0
local move_frames = 0
local inited = false

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
    if not inited then
        return
    end
    if value > cfg.FRAME_TIME * THRESH then
        whole_frames = 0
    else
        whole_frames = whole_frames + 1
    end
    local x = util.lerp(whole_frames, 0, MAX_FRAMES, 0, 1)
    fpsbar.set(x, 1 - x)
end

function M.gpu_times(args)
    if inited then
        gpuprof.set(unpack(args))
    end
end

function M.cpu_times(args)
    if inited then
        cpuprof.set(unpack(args))
    end
end

function M.thread_times(...)
    if inited then
        threadprof.set(util.sum(...) / cfg.CPU_CORES)
    end
end

function M.init()
    bar.init()
    wait.init()
    --textest.init()

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

    gpuprof = guiprof.alloc(posx, posy, posx + sizex, posy + sizey, cfg.FRAME_TIME,
                            prof.gpu_colors())

    posy = posy + sizey + 0.05
    cpuprof = guiprof.alloc(posx, posy, posx + sizex, posy + sizey, cfg.FRAME_TIME,
                            prof.cpu_colors())

    posy = posy + sizey + 0.05
    threadprof = guiprof.alloc(posx, posy, posx + sizex, posy + sizey, cfg.FRAME_TIME,
                               prof.thread_color())

    --ttest = textest.alloc(0, 0, 1)

    inited = true
end

function M.done()
    inited = false
    gpuprof.free()
    cpuprof.free()
    threadprof.free()
    genbar.free()
    edgebar.free()
    frbar.free()
    fpsbar.free()
    wt.free()
    --ttest.free()
    bar.done()
    wait.done()
    --textest.done()
end

return M
