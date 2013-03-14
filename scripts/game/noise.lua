local M = {}

local cfg = require 'config'
local util = require 'core.util'
local thread = require 'core.thread'
local poolbuf = require 'core.pool.buf'

function M.alloc(uid)
    local self = {}
    local buf = poolbuf.alloc(cfg.NOISE_SIZE * cfg.NOISE_SIZE)
    function self.free()
        buf.free()
    end
    function self.get(z, x)
        local v = api_buf_get(buf.start, API_BUF_IPL_SPLINE,
                              cfg.NOISE_SIZE, cfg.NOISE_SIZE, z, x)
        return util.clamp(v, 0, 1)
    end
    local th = thread.alloc('game.noise_th')
    util.wait_thread_responding(th)
    th.request(uid)
    util.wait_thread_responding(th)
    th.request(buf.start)
    util.wait_thread_idle(th)
    th.free()
    return self
end

return M
