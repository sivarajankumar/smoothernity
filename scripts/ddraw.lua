local M = {}

local debug = 0
local pressed = 0

function M.update()
    if pressed == 0 then
        if api_input_key(API_INPUT_KEY_F1) == 1 then
            pressed = 1
            if debug == 0 then
                debug = 1
                api_physics_set_ddraw(API_PHYSICS_DRAW_WIREFRAME)
                api_display_draw_scene(0)
            else
                debug = 0
                api_physics_set_ddraw(API_PHYSICS_NO_DEBUG)
                api_display_draw_scene(1)
            end
        end
    elseif pressed == 1 then
        if api_input_key(API_INPUT_KEY_F1) == 0 then
            pressed = 0
        end
    end
end

return M
