local M = {}

local cfg = require 'config'

local progs = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_prog(si)
    local self = {}
    function self.alloc()
        api_prog_alloc(si)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        progs[si] = self
        api_prog_free(si)
    end
    function self.attach_frag(data)
        api_prog_attach(si, API_PROG_FRAGMENT, data)
    end
    function self.attach_vert(data)
        api_prog_attach(si, API_PROG_VERTEX, data)
    end
    function self.link()
        api_prog_link(si)
    end
    function self.id()
        return si
    end
    return self
end

function M.init()
    for si = 0, cfg.PROG_COUNT - 1 do
        progs[si] = make_prog(si)
    end
    left = cfg.PROG_COUNT
    left_min = cfg.PROG_COUNT
end

function M.done()
    io.write(string.format('Shader programs usage: %i/%i, allocs/frees: %i/%i\n',
                           cfg.PROG_COUNT - left_min, cfg.PROG_COUNT,
                           allocs, frees))
end

function M.alloc()
    if left == 0 then
        error('out of progs')
    end
    for si, s in pairs(progs) do
        progs[si] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        s.alloc()
        return s
    end
end

return M

