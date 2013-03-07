local M = {}

local cfg = require 'config'

local queries = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_query(qi)
    local self = {}
    function self.free()
        if not api_query_idle(qi) then
            error('query is not idle')
        end
        frees = frees + 1
        left = left + 1
        queries[qi] = self
    end
    function self.idle()
        return api_query_idle(qi)
    end
    function self.begin_time()
        api_query_begin_time(qi)
    end
    function self.stamp()
        api_query_stamp(qi)
    end
    function self.end_time()
        api_query_end(qi)
    end
    function self.result()
        return api_query_result(qi)
    end
    return self
end

function M.init()
    for qi = 0, cfg.QUERY_COUNT - 1 do
        queries[qi] = make_query(qi)
    end
    left = cfg.QUERY_COUNT
    left_min = cfg.QUERY_COUNT
end

function M.done()
    io.write(string.format('Queries usage: %i/%i, allocs/frees: %i/%i\n',
                           cfg.QUERY_COUNT - left_min, cfg.QUERY_COUNT,
                           allocs, frees))
end

function M.alloc()
    if left == 0 then
        error('out of queries')
    end
    for qi, q in pairs(queries) do
        queries[qi] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        return q
    end
end

return M
