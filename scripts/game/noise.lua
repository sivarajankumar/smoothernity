local M = {}

local cfg = require 'config'
local util = require 'core.util'
local thread = require 'core.thread'
local poolbuf = require 'core.pool.buf'

local function alloc_common(buf_start)
    local self = {}
    function self.get(z, x)
        return api_buf_get(buf_start, API_BUF_IPL_SPLINE,
                          cfg.NOISE_SIZE, cfg.NOISE_SIZE, z, x)
    end
    return self
end

function M.restore(state)
    return alloc_common(state)
end

function M.alloc(uid)
    local buf = poolbuf.alloc(cfg.NOISE_SIZE * cfg.NOISE_SIZE)
    local self = alloc_common(buf.start)
    function self.free()
        buf.free()
    end
    function self.store()
        return string.format("%i", buf.start)
    end
    local th = thread.alloc('game.noise_th')
    util.wait_thread_responding(th, false)
    th.request(string.format('return "%s", %s', uid, buf.store()))
    util.wait_thread_idle(th, true)
    th.free()
    return self
end

return M
