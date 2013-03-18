local M = {}

local cfg = require 'config'

local counter = 0
local locks = 0

function M.active()
    return counter
end

function M.inactive()
    return (counter + 1) % cfg.TWINS
end

function M.swap()
    counter = M.inactive()
end

function M.lock()
    while locks ~= 0 do
        coroutine.yield(true)
    end
    locks = locks + 1
end

function M.unlock()
    locks = locks - 1
end

return M
