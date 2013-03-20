local M = {}

local lod = require 'game.lod'
local mesh = require 'core.render.mesh'

function M.init()
    M.GROUP_HIDDEN = mesh.group()
    M.GROUP_GUI = mesh.group()
    M.GROUP_LODS = {}
    for i = 0, lod.count - 1 do
        M.GROUP_LODS[i] = mesh.group()
    end
    M.GROUP_NEAR = M.GROUP_LODS[lod.count - 1]
end

return M
