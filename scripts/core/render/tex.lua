local M = {}

local cfg = require 'config'
local pbuf = require 'core.render.pbuf'
local tex = require 'core.tex'
local util = require 'core.util'

local MAX_MAP = 20
local MAX_UNMAP = 20
local MAX_COPY = 20

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

function M.update()
    local count = 0
    for k, v in pairs(preparing) do
        if count < MAX_MAP then
            count = count + 1
            preparing[k] = nil
            mapping[k] = v
            v.state = 'mapping'
            v.copy = pbuf.alloc(v.size()*v.size())
            api_pbuf_map(v.copy.id(), 0, v.size()*v.size())
        else
            break
        end
    end
    for k, v in pairs(mapping) do
        if not api_pbuf_waiting(v.copy.id()) then
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
            api_pbuf_unmap(v.copy.id())
        else
            break
        end
    end
    for k, v in pairs(unmapping) do
        if not api_pbuf_waiting(v.copy.id()) then
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

function M.update_copy(twin)
    local count = 0
    for k, v in pairs(synched) do
        if count < MAX_COPY and v.twins_done < cfg.TWINS then
            count = count + 1
            synched[k] = nil
            copying[k] = v
            v.state = 'copying'
            api_tex_set(v.twin(twin).unit(), v.copy.id(), 0, v.twin(twin).layer(),
                        v.level(), 0, 0, v.size(), v.size())
        else
            break
        end
    end
    for k, v in pairs(copying) do
        if not api_pbuf_waiting(v.copy.id()) then
            copying[k] = nil
            synching[k] = v
            v.state = 'synching'
        end
    end
end

function M.sync_copy_ready()
    return util.empty(copying)
end

function M.need_sync()
    return not util.empty(synching)
end

function M.sync_copy()
    assert(M.sync_copy_ready())
    for k, v in pairs(synching) do
        assert(v.twins_done < cfg.TWINS)
        synching[k] = nil
        synched[k] = v
        v.state = 'synched'
        v.twins_done = v.twins_done + 1
    end
end

function M.restore(state)
    local self = {}
    local mips = {}
    local max_mip = 0

    function self.mips()
        return max_mip
    end

    function self.mip(i)
        return mips[i]
    end

    local function make_mip(level, copy)
        local mip = {}
        function mip.set(...)
            copy.set(...)
        end
        function mip.size()
            return copy.side()
        end
        function mip.level()
            return level
        end
        return mip
    end

    local copies = util.map(function(x) return pbuf.restore(x) end, state)
    for k, v in pairs(copies) do
        max_mip = math.max(max_mip, k)
        mips[k] = make_mip(k, v)
    end
    return self
end

function M.alloc(size)
    local self = {}

    local twins = {}
    local mips = {}

    function self.free()
        for _, v in pairs(mips) do
            v.free()
        end
        for i = 0, cfg.TWINS - 1 do
            twins[i].free()
        end
    end

    function self.mips()
        return util.log2(size)
    end

    function self.twin(i)
        return twins[i]
    end

    function self.mip(i)
        return mips[i]
    end

    function self.prepared()
        return util.reduce_and(function(x) return x.state == 'prepared' end, mips)
    end

    function self.finalized()
        return util.reduce_and(function(x) return x.state == 'finalized' end, mips)
    end

    function self.store()
        assert(self.prepared())
        local states = util.map(function(x) return x.copy.store() end, mips)
        return string.format('{%s}', table.concat(states, ', ', 0, self.mips()))
    end

    function self.finalize()
        for _, v in pairs(mips) do
            v.finalize()
        end
    end

    local function make_mip(level)
        local mip = {}

        mip.twins_done = 0
        mip.copy = nil
        mip.twin = self.twin
    
        local id = next_id
        next_id = next_id + 1

        mip.state = 'preparing'
        preparing[id] = mip

        function mip.free()
            assert(mip.state == 'finalized')
            mip.state = 'vacant'
            finalized[id] = nil
        end

        function mip.finalize()
            assert(mip.state == 'prepared')
            mip.state = 'finalizing'
            prepared[id] = nil
            finalizing[id] = mip
        end

        function mip.set(...)
            assert(mip.state == 'prepared')
            mip.copy.set(...)
        end

        function mip.size()
            return twins[0].size() / math.pow(2, level)
        end

        function mip.level()
            return level
        end

        return mip
    end

    for i = 0, cfg.TWINS - 1 do
        twins[i] = tex.alloc(size)
    end

    for i = 0, self.mips() do
        mips[i] = make_mip(i)
    end

    return self
end

return M
