local M = {}
local cfg = require 'config'
local core = require 'core.core'
local quit = require 'game.quit'
local blinker = require 'game.blinker'

GC_STEP = 10
FRAME_TIME = 1 / 60

function M.run()
    io.write('Game run init\n')
    core.init()

    local tag = 0
    local blink = blinker.alloc()
    collectgarbage('stop')
    while not quit.requested()
    do
        tag = tag + 1
        collectgarbage('step', GC_STEP)
        api_input_update()
        quit.control()
        blink.update(FRAME_TIME, tag)
        api_render_clear_color(blink.color_id())
        api_render_clear(API_RENDER_CLEAR_COLOR)
        api_render_swap()
    end
    collectgarbage('restart')
    blink.free()
    core.done()
    io.write('Game run done\n')
end

return M
