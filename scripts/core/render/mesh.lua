local M = {}

local cfg = require 'config'
local mesh = require 'core.mesh'
local render = require 'core.render.render'
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
    assert(vbuf.state == 'finalized')
    assert(ibuf.state == 'finalized')
    for i = 0, cfg.TWINS - 1 do
        meshes[i] = mesh.alloc(group.twin(i), kind, vbuf.twin(i),
                               ibuf.twin(i), shader, matrix,
                               ibuf.start, ibuf.size)
    end
    function self.group(group)
        for i = 0, cfg.TWINS - 1 do
            meshes[i].group(group.twin(i))
        end
    end
    function self.twin(i)
        return meshes[i]
    end
    function self.free()
        for i = 0, cfg.TWINS - 1 do
            meshes[i].free()
        end
    end
    return self
end

function M.draw(group, draw_tag)
    api_mesh_draw(group.twin(render.twin_active()), draw_tag)
end

function M.update(group, dt, update_tag)
    api_mesh_update(group.twin(render.twin_active()), dt, update_tag)
end

return M