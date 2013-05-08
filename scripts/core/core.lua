local M = {}

local modules = {
    require 'core.colshape',
    require 'core.matrix',
    require 'core.pool.buf',
    require 'core.rigidbody',
    require 'core.thread',
    require 'core.vector',
    require 'core.vehicle',
    require 'core.world'
}

function M.init()
    for _, m in pairs(modules) do
        m.init()
    end
end

function M.done()
    for _, m in pairs(modules) do
        m.done()
    end
end

return M
