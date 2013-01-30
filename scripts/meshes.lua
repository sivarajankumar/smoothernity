local M = {}

local lod = require 'lod'

M.GROUP_GUI = 0
M.GROUP_NEAR = 1
M.GROUP_LODS = M.GROUP_NEAR

function M.lod_group(lodi)
    return M.GROUP_LODS + lod.count - 1 - lodi
end

return M
