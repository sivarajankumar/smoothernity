local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'
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

function M.restore_chunk(state, res_api)
    return pool.restore_chunk(state, res_api)
end

function M.alloc(title, twin_size, copy_size, pool_dims, res_api)
    local self = {}
    local pools = {}
    for i = 0, cfg.TWINS - 1 do
        pools[i] = pool.alloc(string.format('%s (twin %i)', title, i),
                              twin_size, i, 1, pool_dims, res_api)
    end
    local copy_pool = pool.alloc(string.format('%s copy', title),
                                 copy_size, cfg.TWINS, cfg.COPIES,
                                 {[copy_size] = cfg.COPIES}, res_api)

    function self.free()
        for i = 0, cfg.TWINS - 1 do
            pools[i].free()
        end
        copy_pool.free()
    end

    function self.left(size)
        return pools[0].left(size)
    end

    function self.copies_left(size)
        return copy_pool.left(size)
    end

    function self.alloc(size)
        local chunks = {}
        for i = 0, cfg.TWINS - 1 do
            chunks[i] = pools[i].alloc(size)
        end

        local copy
        local chunk = {}
        chunk.size = chunks[0].size
        chunk.start = chunks[0].start

        local function inactive()
            return chunks[twin.inactive()]
        end

        function chunk.free()
            for i = 0, cfg.TWINS - 1 do
                chunks[i].free()
            end
        end

        function chunk.twin(i)
            return chunks[i].res
        end

        function chunk.store()
            return copy.store()
        end

        function chunk.set(i, ...)
            copy.set(i, ...)
        end

        function chunk.prepare()
            copy = copy_pool.alloc(size)
            copy.map()
        end

        function chunk.finalize()
            chunk.finalize1()
            util.sync_wait()
            twin.swap()
            chunk.finalize2()
            util.sync_wait()
        end

        function chunk.finalize1()
            copy.unmap()
            copy.copy(inactive())
        end

        function chunk.finalize2()
            copy.copy(inactive())
            copy.free()
            copy = nil
        end

        return chunk
    end

    return self
end

return M
