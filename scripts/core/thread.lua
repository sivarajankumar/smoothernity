local M = {}

local cfg = require 'config'
local log = require 'core.log'

local ths = {}
local allocs = 0
local frees = 0
local left, left_min

local function make_thread(index)
    local self = {}
    function self.free()
        if api_thread_state(index) ~= API_THREAD_IDLE then
            error(string.format('thread %i is not idle', index))
        end
        frees = frees + 1
        left = left + 1
        ths[index] = self
    end
    function self.idle()
        local state = api_thread_state(index)
        if state == API_THREAD_ERROR then
            error(string.format('thread %i error', index))
        end
        return state == API_THREAD_IDLE
    end
    function self.responding()
        local state = api_thread_state(index)
        if state == API_THREAD_ERROR then
            error(string.format('thread %i error', index))
        end
        return state == API_THREAD_RESPONDING
    end
    function self.request(s)
        return api_thread_request(index, s)
    end
    return self
end

function M.init()
    for i = 0, cfg.THREAD_COUNT - 1 do
        ths[i] = make_thread(i)
    end
    left = cfg.THREAD_COUNT
    left_min = cfg.THREAD_COUNT
end

function M.done()
    log.info('Threads usage: %i/%i, allocs/frees: %i/%i',
             cfg.THREAD_COUNT - left_min, cfg.THREAD_COUNT, allocs, frees)
    if allocs ~= frees then
        error('Allocs/frees mismatch')
    end
end

function M.left()
    return left
end

function M.alloc(mod, func)
    if left == 0 then
        error('out of threads')
    end
    for i, thread in pairs(ths) do
        ths[i] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        api_thread_run(i, string.format('(require "core.run").run("%s", "%s")',
                                        mod, func))
        return thread
    end
end

return M
