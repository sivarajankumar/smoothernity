local M = {}

local cfg = require 'config'
local corepool = require 'core.pool.pool'
local util = require 'core.util'

local MAX_MAP = 20
local MAX_UNMAP = 20
local MAX_COPY = 20

local function twin_size(pool_dims)
    return corepool.size(pool_dims)
end

local function copy_size(pool_dims)
    return math.max(unpack(util.keys(pool_dims)))
end

function M.sizes(pool_dims)
    local t = {}
    for i = 1, cfg.TWINS do
        table.insert(t, twin_size(pool_dims))
    end
    for i = 1, cfg.COPIES do
        table.insert(t, copy_size(pool_dims))
    end
    return unpack(t)
end

function M.alloc(title, pool_dims, res_api)
    local pool = {}
    local pools = {}
    for i = 0, cfg.TWINS - 1 do
        pools[i] = corepool.alloc(string.format('%s (twin %i)', title, i),
                                  twin_size(pool_dims), i, 1, pool_dims)
    end
    local copy_pool = corepool.alloc(string.format('%s (copy)', title),
                                     copy_size(pool_dims), cfg.TWINS, cfg.COPIES,
                                     {[copy_size(pool_dims)] = cfg.COPIES})

    local preparing = {}
    local mapping = {}
    local prepared = {}
    local finalizing = {}
    local unmapping = {}
    local copying = {}
    local synching = {}
    local synched = {}
    local finalized = {}
    local next_id = 0

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

    function pool.update()
        local count = 0
        for k, v in pairs(preparing) do
            if count < MAX_MAP then
                count = count + 1
                preparing[k] = nil
                mapping[k] = v
                v.state = 'mapping'
                v.copy = copy_pool.alloc(v.size)
                res_api.map(v.copy.res, v.copy.start, v.copy.size)
            else
                break
            end
        end
        for k, v in pairs(mapping) do
            if not res_api.waiting(v.copy.res) then
                mapping[k] = nil
                prepared[k] = v
                v.state = 'prepared'
            end
        end
        for k, v in pairs(finalizing) do
            if count < MAX_UNMAP then
                count = count + 1
                finalizing[k] = nil
                unmapping[k] = v
                v.state = 'unmapping'
                res_api.unmap(v.copy.res)
            else
                break
            end
        end
        for k, v in pairs(unmapping) do
            if not res_api.waiting(v.copy.res) then
                unmapping[k] = nil
                synched[k] = v
                v.state = 'synched'
            end
        end
        for k, v in pairs(synched) do
            if v.twins_done == cfg.TWINS then
                synched[k] = nil
                finalized[k] = v
                v.state = 'finalized'
                v.copy.free()
                v.copy = nil
            end
        end
    end

    function pool.update_copy(twin_inactive)
        local count = 0
        for k, v in pairs(synched) do
            if count < MAX_COPY and v.twins_done < cfg.TWINS then
                count = count + 1
                synched[k] = nil
                copying[k] = v
                v.state = 'copying'
                res_api.copy(v.copy.res, v.twin(twin_inactive),
                             v.copy.start, v.start, v.size)
            else
                break
            end
        end
        for k, v in pairs(copying) do
            if not res_api.waiting(v.copy.res) then
                copying[k] = nil
                synching[k] = v
                v.state = 'synching'
            end
        end
    end

    function pool.sync_copy()
        assert(pool.sync_copy_ready())
        for k, v in pairs(synching) do
            assert(v.twins_done < cfg.TWINS)
            synching[k] = nil
            synched[k] = v
            v.state = 'synched'
            v.twins_done = v.twins_done + 1
        end
    end

    function pool.sync_copy_ready()
        return util.empty(copying)
    end

    function pool.need_sync()
        return not util.empty(synching)
    end

    function pool.alloc(size)
        local twins = {}
        for i = 0, cfg.TWINS - 1 do
            twins[i] = pools[i].alloc(size)
        end

        local chunk = {}
        chunk.size = twins[0].size
        chunk.start = twins[0].start
        chunk.copy = nil
        chunk.twins_done = 0

        local id = next_id
        next_id = next_id + 1

        chunk.state = 'preparing'
        preparing[id] = chunk

        function chunk.free()
            assert(chunk.state == 'finalized')
            chunk.state = 'vacant'
            finalized[id] = nil
            for i = 0, cfg.TWINS - 1 do
                twins[i].free()
            end
        end

        function chunk.twin(i)
            return twins[i].res
        end

        function chunk.finalize()
            assert(chunk.state == 'prepared')
            chunk.state = 'finalizing'
            prepared[id] = nil
            finalizing[id] = chunk
        end

        function chunk.prepared()
            return chunk.state == 'prepared'
        end

        function chunk.finalized()
            return chunk.state == 'finalized'
        end

        return chunk
    end

    return pool
end

return M
