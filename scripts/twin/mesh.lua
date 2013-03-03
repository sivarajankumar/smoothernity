local M = {}

local cfg = require 'config'
local next_group = 0

function M.group()
    local self = {}
    local ids = {}
    for i = 0, cfg.TWINS - 1 do
        ids[i] = next_group
        next_group = next_group + 1
    end
    function self.twin(i)
        return ids[i]
    end
    return self
end

function M.alloc(group, kind, vbuf, ibuf, shader, matrix)
    local self = {}
    local meshes = {}
    for i = 0, cfg.TWINS - 1 do
        meshes[i] = api_mesh_alloc(group.twin(i), kind, vbuf.twin(i),
                                   ibuf.twin(i), shader, matrix,
                                   ibuf.start, ibuf.size)
    end
    function self.group(group)
        for i = 0, cfg.TWINS - 1 do
            api_mesh_group(meshes[i], group.twin(i))
        end
    end
    function self.twin(i)
        return meshes[i]
    end
    function self.free()
        for i = 0, cfg.TWINS - 1 do
            api_mesh_free(meshes[i])
        end
    end
    return self
end

return M
