local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local ibufs

function M.init(render)
    local function def_map(res, start, size)
        render.defer(function() api_ibuf_map(res, start, size) end)
    end
    local function def_unmap(res)
        render.defer(function() api_ibuf_unmap(res) end)
    end
    ibufs = pool.alloc('Index buffers', cfg.IBUF_SIZE, cfg.IBUF_COUNT, cfg.IBUF_POOL,
                       api_ibuf_alloc, api_ibuf_free, def_map, def_unmap)
end

function M.done()
    ibufs.free()
    ibufs = nil
end

function M.alloc(size)
    return ibufs.alloc(size)
end

return M

