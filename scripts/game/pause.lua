local M = {}

local pwld = require 'physwld'
local render = require 'render'
local key = require 'core.key'

local pause = false
local keyobj = key.alloc(function() return API_INPUT_KEY_P end,
                         function()
                            if pause then
                                pause = false
                                api_physics_wld_tscale(pwld.wld, 1)
                                render.timescale(1)
                            else
                                pause = true
                                api_physics_wld_tscale(pwld.wld, 0)
                                render.timescale(0)
                            end
                         end, function() end)

function M.control()
    keyobj.update()
end

return M
