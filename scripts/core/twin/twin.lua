local M = {}

local cfg = require 'config'

local counter = 0

function M.active()
    return counter
end

function M.inactive()
    return (counter + 1) % cfg.TWINS
end

function M.swap()
    counter = M.inactive()
end

return M
