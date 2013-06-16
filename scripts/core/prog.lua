local M = {}

local cfg = require 'config'
local log = require 'core.log'

local progs = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_prog(progi)
    local self = {}
    function self.alloc(vert, frag)
        api_prog_alloc(progi, vert, frag)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        progs[progi] = self
        api_prog_free(progi)
    end
    function self.use()
        api_prog_use(progi)
    end
    function self.id()
        return progi
    end
    return self
end

function M.init()
    for progi = 0, cfg.PROG_COUNT - 1 do
        progs[progi] = make_prog(progi)
    end
    left = cfg.PROG_COUNT
    left_min = cfg.PROG_COUNT
end

function M.done()
    log.info('Shader programs usage: %i/%i, allocs/frees: %i/%i',
             cfg.PROG_COUNT - left_min, cfg.PROG_COUNT, allocs, frees)
    if allocs ~= frees then
        error('Allocs/frees mismatch')
    end
end

function M.alloc(vert, frag)
    if left == 0 then
        error('out of progs')
    end
    for progi, prog in pairs(progs) do
        progs[progi] = nil
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
        prog.alloc(vert, frag)
        return prog
    end
end

return M

