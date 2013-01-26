local M = {}

local render = require 'render'
local pwld = require 'physwld'

local MODE_VISUAL = 0
local MODE_EAGLE = 1
local MODE_DEBUG = 2

local mode = MODE_VISUAL
local pressed = 0

function M.update()
    if pressed == 0 then
        if api_input_key(API_INPUT_KEY_F1) == 1 then
            pressed = 1
            if mode == MODE_VISUAL then
                mode = MODE_EAGLE
                render.eagle.engage()
            elseif mode == MODE_EAGLE then
                mode = MODE_DEBUG
                render.debug.engage()
                api_physics_wld_ddraw_mode(pwld.wld, API_PHYSICS_DRAW_WIREFRAME + API_PHYSICS_DRAW_AABB)
            elseif mode == MODE_DEBUG then
                mode = MODE_VISUAL
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
