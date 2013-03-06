local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local bufs

function M.init()
    bufs = pool.alloc('Buffers', cfg.BUF_SIZE, 1, cfg.BUF_POOL,
                      function() end, function(i) end)
end

function M.done()
    bufs.free()
    bufs = nil
end

function M.alloc(size)
    return bufs.alloc(size)
end

return M
