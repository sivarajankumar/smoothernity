local M = {}

local util = require 'core.util'
local color = require 'game.color'
local query = require 'core.query'

local fids = {}
local last_fid = 0

M.cpu = {}
M.gpu = {}

local function cpu_timers()
    return {M.cpu.core, M.cpu.control, M.cpu.slowpok, M.cpu.work,
            M.cpu.rupdate, M.cpu.rclear, M.cpu.rdraw, M.cpu.rupload, M.cpu.rswap}
end

local function gpu_timers()
    return {M.gpu.logic, M.gpu.rclear, M.gpu.rdraw, M.gpu.rupload, M.gpu.rswap}
end

local function cpu_timer_alloc(color)
    local self = {}
    self.time = 0
    self.color = color
    function self.start()
        self.time = api_timer()
    end
    function self.finish()
        self.time = api_timer() - self.time
    end
    return self
end

local function gpu_timer_alloc(color)
    local self = {}
    local queries = {}
    self.color = color
    function self.free()
        for k, v in pairs(queries) do
            util.query_free(v)
        end
    end
    function self.start()
        assert(queries[last_fid] == nil)
        queries[last_fid] = query.alloc()
        queries[last_fid].begin_time()
    end
    function self.finish()
        queries[last_fid].end_time()
    end
    function self.ready(fid)
        return queries[fid] ~= nil and queries[fid].idle()
    end
    function self.pop(fid)
        local res = queries[fid].result()
        queries[fid].free()
        queries[fid] = nil
        return res
    end
    return self
end

function M.cpu_colors()
    return unpack(util.map(function(v) return v.color end, cpu_timers()))
end

function M.gpu_colors()
    return unpack(util.map(function(v) return v.color end, gpu_timers()))
end

function M.thread_color()
    return M.cpu.work.color
end

function M.init()
    M.cpu.core = cpu_timer_alloc(color.RED)
    M.cpu.control = cpu_timer_alloc(color.YELLOW)
    M.cpu.slowpok = cpu_timer_alloc(color.PURPLE)
    M.cpu.work = cpu_timer_alloc(color.BLUE_L)
    M.cpu.rupdate = cpu_timer_alloc(color.ORANGE_D)
    M.cpu.rclear = cpu_timer_alloc(color.PURPLE_D)
    M.cpu.rdraw = cpu_timer_alloc(color.GREEN)
    M.cpu.rupload = cpu_timer_alloc(color.YELLOW)
    M.cpu.rswap = cpu_timer_alloc(color.ORANGE)

    M.gpu.logic = gpu_timer_alloc(M.cpu.work.color)
    M.gpu.rclear = gpu_timer_alloc(M.cpu.rclear.color)
    M.gpu.rdraw = gpu_timer_alloc(M.cpu.rdraw.color)
    M.gpu.rupload = gpu_timer_alloc(M.cpu.rupload.color)
    M.gpu.rswap = gpu_timer_alloc(M.cpu.rswap.color)
end

function M.done()
    for k, v in pairs(M.gpu) do
        v.free()
    end
end

function M.update(gui)
    last_fid = last_fid + 1
    fids[last_fid] = true
    for fid, _ in pairs(fids) do
        if util.reduce_and(function(q) return q.ready(fid) end, gpu_timers()) then
            times = util.map(function(q) return q.pop(fid) end, gpu_timers())
            gui.gpu_times(times)
            gui.frame_time(util.sum(unpack(times)))
            fids[fid] = nil
        end
    end
    gui.cpu_times(util.map(function(v) return v.time end, cpu_timers()))
    gui.thread_times(api_thread_timings())
end

return M
