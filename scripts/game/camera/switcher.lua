local M = {}

local render = require 'game.render'

function M.alloc(camc, camd)
    local self = {}
    local camera = camc
    local pressed = 0

    function self.update()
        if pressed == 0 then
            if api_input_key(API_INPUT_KEY_F3) == 1 then
                pressed = 1
                if camera == camc then
                    camd.moveto(camc.matrix)
                    camera = camd
                else
                    camera = camc
                end
                render.camera(camera.matrix)
            end
        elseif pressed == 1 then
            if api_input_key(API_INPUT_KEY_F3) == 0 then
                pressed = 0
            end
        end
    end

    render.camera(camera.matrix)
    return self
end

return M
