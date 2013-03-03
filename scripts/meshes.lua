local M = {}

local lod = require 'lod'
local twinmesh = require 'twin.mesh'

function M.init()
    M.GROUP_HIDDEN = twinmesh.group()
    M.GROUP_GUI = twinmesh.group()
    M.GROUP_LODS = {}
    for i = 0, lod.count - 1 do
        M.GROUP_LODS[i] = twinmesh.group()
    end
    M.GROUP_NEAR = M.GROUP_LODS[lod.count - 1]
end

return M
