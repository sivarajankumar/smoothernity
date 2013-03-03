local M = {}

local cfg = require 'config'

function M.alloc_vector(shprog, mesh, uni, vec)
    local self = {}
    local shunis = {}
    for i = 0, cfg.TWINS - 1 do
        shunis[i] = api_shuni_alloc_vector(shprog, mesh.twin(i), uni, vec)
    end
    function self.free()
        for i = 0, cfg.TWINS - 1 do
            api_shuni_free(shunis[i])
        end
    end
    return self
end

function M.alloc_int(shprog, mesh, uni, int)
    local self = {}
    local shunis = {}
    for i = 0, cfg.TWINS - 1 do
        shunis[i] = api_shuni_alloc_int(shprog, mesh.twin(i), uni, int)
    end
    function self.free()
        for i = 0, cfg.TWINS - 1 do
            api_shuni_free(shunis[i])
        end
    end
    return self
end

return M
