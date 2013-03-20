local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'

local bufs

function M.init()
    bufs = pool.alloc('Buffers', cfg.BUF_SIZE, 0, 1, cfg.BUF_POOL)
end

function M.done()
    bufs.free()
end

function M.alloc(size)
    local self = bufs.alloc(size)
    function self.set(i, ...)
        api_buf_set(self.start + i, ...)
    end
    return self
end

function M.restore(state)
    local self = pool.restore_chunk(state)
    function self.set(i, ...)
        api_buf_set(self.start + i, ...)
    end
    return self
end

return M
