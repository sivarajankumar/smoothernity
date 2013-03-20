local M = {}

local cfg = require 'config'
local corepool = require 'core.corepool.corepool'
local twin = require 'core.twin.twin'
local util = require 'core.util'

function M.sizes(twin_size, copy_size)
    local t = {}
    for i = 1, cfg.TWINS do
        table.insert(t, twin_size)
    end
    for i = 1, cfg.COPIES do
        table.insert(t, copy_size)
    end
    return unpack(t)
end

function M.alloc(title, twin_size, copy_size, pool_dims)
    local pool = {}
    local pools = {}
    for i = 0, cfg.TWINS - 1 do
        pools[i] = corepool.alloc(string.format('%s (twin %i)', title, i),
                                  twin_size, i, 1, pool_dims)
    end
    local copy_pool = corepool.alloc(string.format('%s copy', title),
                                     copy_size, cfg.TWINS, cfg.COPIES,
                                     {[copy_size] = cfg.COPIES})

    function pool.free()
        for i = 0, cfg.TWINS - 1 do
            pools[i].free()
        end
        copy_pool.free()
    end

    function pool.left(size)
        return pools[0].left(size)
    end

    function pool.copies_left(size)
        return copy_pool.left(size)
    end

    function pool.alloc(size)
        local chunks = {}
        for i = 0, cfg.TWINS - 1 do
            chunks[i] = pools[i].alloc(size)
        end

        local state = 'preparing'
        local chunk = {}
        chunk.size = chunks[0].size
        chunk.start = chunks[0].start
        chunk.copy = nil

        function chunk.free()
            assert(state == 'finalized')
            for i = 0, cfg.TWINS - 1 do
                chunks[i].free()
            end
        end

        function chunk.twin(i)
            return chunks[i].res
        end

        function chunk.state()
            return state
        end

        function chunk.finalize()
            assert(state == 'prepared')
            state = 'finalizing'
        end

        return chunk
    end

    return pool
end

return M
