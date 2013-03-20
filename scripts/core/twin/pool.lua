local M = {}

local cfg = require 'config'
local corepool = require 'core.corepool.corepool'
local twin = require 'core.twin.twin'
local util = require 'core.util'

local MAX_MAP = 20
local MAX_UNMAP = 20
local MAX_COPY = 20

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

function M.alloc(title, twin_size, copy_size, pool_dims, res_api)
    local pool = {}
    local pools = {}
    for i = 0, cfg.TWINS - 1 do
        pools[i] = corepool.alloc(string.format('%s (twin %i)', title, i),
                                  twin_size, i, 1, pool_dims)
    end
    local copy_pool = corepool.alloc(string.format('%s copy', title),
                                     copy_size, cfg.TWINS, cfg.COPIES,
                                     {[copy_size] = cfg.COPIES})

    local preparing = {}
    local mapping = {}
    local prepared = {}
    local finalizing = {}
    local unmapping = {}
    local copying = {}
    local paused = {}
    local unpaused = {}
    local cloning = {}
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
                if count < MAX_COPY then
                    count = count + 1
                    unmapping[k] = nil
                    copying[k] = v
                    v.state = 'copying'
                    res_api.copy(v.copy.res, v.twin(twin.inactive()),
                                 v.copy.start, v.start, v.size)
                else
                    break
                end
            end
        end
        for k, v in pairs(copying) do
            if not res_api.waiting(v.copy.res) then
                copying[k] = nil
                paused[k] = v
                v.state = 'paused'
            end
        end
        for k, v in pairs(unpaused) do
            if count < MAX_COPY then
                count = count + 1
                unpaused[k] = nil
                cloning[k] = v
                v.state = 'cloning'
                res_api.copy(v.copy.res, v.twin(twin.inactive()),
                             v.copy.start, v.start, v.size)
            else
                break
            end
        end
        for k, v in pairs(cloning) do
            if not res_api.waiting(v.copy.res) then
                cloning[k] = nil
                finalized[k] = v
                v.state = 'finalized'
                v.copy.free()
                v.copy = nil
            end
        end
    end

    function pool.switch()
        assert(pool.ready_to_switch())
        for k, v in pairs(paused) do
            paused[k] = nil
            unpaused[k] = v
            v.state = 'unpaused'
        end
    end

    function pool.ready_to_switch()
        return util.empty(copying) and util.empty(cloning) and not util.empty(paused)
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

        return chunk
    end

    return pool
end

return M
