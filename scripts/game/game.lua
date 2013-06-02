local M = {}
local cfg = require 'config'
local core = require 'core.core'
local quit = require 'game.quit'
local util = require 'core.util'
local blinker = require 'game.blinker'

GC_STEP = 10
FRAME_TIME = 1 / 60

function M.run()
    core.init()
    local tag = 0
    local blink = blinker.alloc()
    local prg = util.prog_from_files('./game/shader/basic')
    collectgarbage('stop')
    while not quit.requested()
    do
        tag = tag + 1
        collectgarbage('step', GC_STEP)
        api_input_update()
        quit.control()
        prg.use()
        blink.update(FRAME_TIME, tag)
        api_render_clear_color(blink.color_id())
        api_render_clear(API_RENDER_COLOR_BUFFER_BIT)
        api_render_swap()
    end
    collectgarbage('restart')
    prg.free()
    blink.free()
    core.done()
end

return M
