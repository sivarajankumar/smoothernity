local M = {}

local cfg = require 'config'
local pool = require 'pool.pool'

local pbufs

function M.init(render)
    local function def_map(res, start, size)
        render.defer(function() api_pbuf_map(res, start, size) end)
    end
    local function def_unmap(res)
        render.defer(function() api_pbuf_unmap(res) end)
    end
    pbufs = pool.alloc('Pixel buffers', cfg.PBUF_SIZE, cfg.PBUF_COUNT, cfg.PBUF_POOL,
                       api_pbuf_alloc, api_pbuf_free, def_map, def_unmap)
end

function M.done()
    pbufs.free()
    pbufs = nil
end

function M.alloc(size)
    return pbufs.alloc(size)
end

return M

