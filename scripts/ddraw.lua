local M = {}

local render = require 'render'
local pwld = require 'physwld'

local debug = 0
local pressed = 0

function M.update()
    if pressed == 0 then
        if api_input_key(API_INPUT_KEY_F1) == 1 then
            pressed = 1
            if debug == 0 then
                debug = 1
                render.debug.engage()
                api_physics_wld_ddraw_mode(pwld.wld, API_PHYSICS_DRAW_WIREFRAME + API_PHYSICS_DRAW_AABB)
            else
                debug = 0
                render.visual.engage()
            end
        end
    elseif pressed == 1 then
        if api_input_key(API_INPUT_KEY_F1) == 0 then
            pressed = 0
        end
    end
end

return M
