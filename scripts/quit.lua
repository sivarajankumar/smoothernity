local M = {}

local key = require 'key'

local quit = false
local keyobj = key.alloc(function() return API_INPUT_KEY_ESCAPE end,
                         function() quit = true end,
                         function() end)

function M.control()
    keyobj.update()
end

function M.requested()
    return quit
end

return M
