local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local vbufs

function M.init(render)
    local function def_map(res, start, size)
        render.defer(function() api_vbuf_map(res, start, size) end)
    end
    local function def_unmap(res)
        render.defer(function() api_vbuf_unmap(res) end)
    end
    vbufs = pool.alloc('Vertex buffers', cfg.VBUF_SIZE, cfg.VBUF_COUNT, cfg.VBUF_POOL,
                       api_vbuf_alloc, api_vbuf_free, def_map, def_unmap)
end

function M.done()
    vbufs.free()
    vbufs = nil
end

function M.alloc(size)
    return vbufs.alloc(size)
end

return M
