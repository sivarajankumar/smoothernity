local M = {}

local cfg = require 'config'

local syncs = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_sync(si)
    local self = {}
    function self.alloc()
        api_sync_alloc(si)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        api_sync_free(si)
    end
    function self.ready()
        return api_sync_ready(si)
    end
    return self
end

function M.init()
    for si = 0, cfg.SYNC_COUNT - 1 do
        syncs[si] = make_sync(si)
    end
    left = cfg.SYNC_COUNT
    left_min = cfg.SYNC_COUNT
end

function M.done()
    io.write(string.format('Syncs usage: %i/%i, allocs/frees: %i/%i\n',
                           cfg.SYNC_COUNT - left_min, cfg.SYNC_COUNT,
                           allocs, frees))
end

function M.alloc()
    if left == 0 then
        error('out of syncs')
    end
    for si, s in pairs(syncs) do
        syncs[si] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        s.alloc()
        return s
    end
end

return M
