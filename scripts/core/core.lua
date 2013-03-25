local M = {}

local modules = {
    require 'core.colshape',
    require 'core.matrix',
    require 'core.mesh',
    require 'core.pool.buf',
    require 'core.pool.pbuf',
    require 'core.query',
    require 'core.render.render',
    require 'core.render.ibuf',
    require 'core.render.vbuf',
    require 'core.rigidbody',
    require 'core.shprog',
    require 'core.shuni',
    require 'core.sync',
    require 'core.tex',
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
