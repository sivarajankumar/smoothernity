local M = {}

local cfg = require 'config'
local log = require 'core.log'

local vectors = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_vector(vi)
    local self = {}
    function self.alloc()
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        vectors[vi] = self
    end
    function self.id()
        return vi
    end
    function self.get()
        return api_vector_get(vi)
    end
    function self.update(dt, tag)
        api_vector_update(vi, dt, tag)
    end
    function self.const(x, y, z, w)
        api_vector_const(vi, x, y, z, w)
    end
    function self.rubber(v0, v1)
        api_vector_rubber(vi, v0.id(), v1.id())
    end
    function self.cord(v0, min, max)
        api_vector_cord(vi, v0.id(), min, max)
    end
    function self.mpos(m0)
        api_vector_mpos(vi, m0.id())
    end
    function self.wsum(v0, v1, v2, v3, w)
        api_vector_wsum(vi, v0.id(), v1.id(), v2.id(), v3.id(), w.id())
    end
    function self.pick(v0, v1, v2, v3)
        api_vector_pick(vi, v0.id(), v1.id(), v2.id(), v3.id())
    end
    function self.seq(buf, len, loop, ipl)
        api_vector_seq(vi, buf.start, len, loop, ipl)
    end
    function self.cast(wld, cs, m0, m1)
        api_vector_cast(vi, wld.id(), cs.id(), m0.id(), m1.id())
    end
    return self
end

function M.init()
    for vi = 0, cfg.VECTOR_COUNT - 1 do
        vectors[vi] = make_vector(vi)
    end
    left = cfg.VECTOR_COUNT
    left_min = cfg.VECTOR_COUNT
end

function M.done()
    log.info('Vectors usage: %i/%i, allocs/frees: %i/%i',
             cfg.VECTOR_COUNT - left_min, cfg.VECTOR_COUNT, allocs, frees)
    if allocs ~= frees then
        error('Allocs/frees mismatch')
    end
end

function M.alloc()
    if left == 0 then
        error('out of vectors')
    end
    for vi, v in pairs(vectors) do
        vectors[vi] = nil
        v.alloc()
        return v
    end
end

return M


