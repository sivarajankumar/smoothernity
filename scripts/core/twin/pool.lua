local M = {}

local cfg = require 'config'
local pool = require 'core.pool.pool'
local twin = require 'core.twin.twin'

function M.alloc(title, res_size, res_count, pool_dims,
                 res_set, res_map, res_unmap, res_waiting)
    local self = {}
    local pools = {}
    local res_start = 0
    for i = 0, cfg.TWINS - 1 do
        local name = string.format('%s (twin %i)', title, i)
        local count = res_count / cfg.TWINS
        pools[i] = pool.alloc(name, res_size, res_start, count,
                              pool_dims, res_map, res_unmap, res_waiting)
        res_start = res_start + count
    end

    function self.free()
        for i = 0, cfg.TWINS - 1 do
            pools[i].free()
        end
    end

    function self.left(size)
        return pools[0].left(size)
    end

    function self.alloc(size)
        local chunks = {}
        for i = 0, cfg.TWINS - 1 do
            chunks[i] = pools[i].alloc(size)
        end

        local data = {}
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

        function chunk.set(i, ...)
            res_set(inactive().res, inactive().start + i, ...)
            data[i] = {...}
        end

        function chunk.prepare()
            inactive().map()
        end

        function chunk.finalize()
            inactive().unmap()
            twin.swap()
            inactive().map()
            for i, v in pairs(data) do
                res_set(inactive().res, inactive().start + i, unpack(v))
                coroutine.yield(false)
            end
            inactive().unmap()
            data = {}
        end

        return chunk
    end

    return self
end

return M
