local M = {}

local cfg = require 'config'
local shuni = require 'core.shuni'

function M.alloc_vector(shprog, mesh, name, vec)
    local self = {}
    local shunis = {}
    for i = 0, cfg.TWINS - 1 do
        shunis[i] = shuni.alloc_vector(shprog, mesh.twin(i), name, vec)
    end
    function self.free()
        for i = 0, cfg.TWINS - 1 do
            shunis[i].free()
        end
    end
    return self
end

function M.alloc_int(shprog, mesh, name, int)
    local self = {}
    local shunis = {}
    for i = 0, cfg.TWINS - 1 do
        shunis[i] = shuni.alloc_int(shprog, mesh.twin(i), name, int)
    end
    function self.free()
        for i = 0, cfg.TWINS - 1 do
            shunis[i].free()
        end
    end
    return self
end

return M
