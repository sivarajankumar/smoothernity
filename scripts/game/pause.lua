local M = {}

local pwld = require 'game.physwld'
local render = require 'game.render'
local key = require 'core.key'

local pause = false
local keyobj = key.alloc(function() return API_INPUT_KEY_P end,
                         function()
                            if pause then
                                pause = false
                                pwld.wld.tscale(1)
                                render.timescale(1)
                            else
                                pause = true
                                pwld.wld.tscale(0)
                                render.timescale(0)
                            end
                         end, function() end)

function M.control()
    keyobj.update()
end

return M
