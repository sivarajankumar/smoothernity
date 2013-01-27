local M = {}

local pwld = require 'physwld'
local render = require 'render'

local pause = false
local pressed = false

local KEY = function() return API_INPUT_KEY_P end

function M.control()
    if pressed and api_input_key(KEY()) == 0 then
        pressed = false
    elseif not pressed and api_input_key(KEY()) == 1 then
        pressed = true
        if pause then
            pause = false
            api_physics_wld_tscale(pwld.wld, 1)
            render.timescale(1)
        else
            pause = true
            api_physics_wld_tscale(pwld.wld, 0)
            render.timescale(0)
        end
    end
end

return M
