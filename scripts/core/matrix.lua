local M = {}

local cfg = require 'config'

local matrices = {}
local left, left_min
local allocs = 0
local frees = 0

local function make_matrix(mi)
    local self = {}
    function self.alloc()
        allocs = allocs + 1
        left = left - 1
        left_min = math.min(left, left_min)
    end
    function self.free()
        frees = frees + 1
        left = left + 1
        matrices[mi] = self
    end
    function self.id()
        return mi
    end
    function self.copy(src)
        api_matrix_copy(mi, src.id())
    end
    function self.stop()
        api_matrix_stop(mi)
    end
    function self.update(dt, tag)
        api_matrix_update(mi, dt, tag)
    end
    function self.mul(m0, m1)
        api_matrix_mul(mi, m0.id(), m1.id())
    end
    function self.mul_stop(m0, m1)
        api_matrix_mul_stop(mi, m0.id(), m1.id())
    end
    function self.inv(m0)
        api_matrix_inv(mi, m0.id())
    end
    function self.frustum(v0, v1, zneari, zfari)
        api_matrix_frustum(mi, v0.id(), v1.id(), zneari, zfari)
    end
    function self.ortho(v0, v1, zneari, zfari)
        api_matrix_ortho(mi, v0.id(), v1.id(), zneari, zfari)
    end
    function self.pos_scl_rot(pos, scl, rot, rotaxis, rotanglei)
        api_matrix_pos_scl_rot(mi, pos.id(), scl.id(), rot.id(), rotaxis, rotanglei)
    end
    function self.from_to_up(from, to, up)
        api_matrix_from_to_up(mi, from.id(), to.id(), up.id())
    end
    function self.rigid_body(rb)
        api_matrix_rigid_body(mi, rb.id())
    end
    function self.vehicle_chassis(veh)
        api_matrix_vehicle_chassis(mi, veh.id())
    end
    function self.vehicle_wheel(wheel)
        api_matrix_vehicle_wheel(mi, wheel.veh_id(), wheel.id())
    end
    return self
end

function M.init()
    for mi = 0, cfg.MATRIX_COUNT - 1 do
        matrices[mi] = make_matrix(mi)
    end
    left = cfg.MATRIX_COUNT
    left_min = cfg.MATRIX_COUNT
end

function M.done()
    io.write(string.format('Matrices usage: %i/%i, allocs/frees: %i/%i\n',
                           cfg.MATRIX_COUNT - left_min, cfg.MATRIX_COUNT,
                           allocs, frees))
end

function M.alloc()
    if left == 0 then
        error('out of matrices')
    end
    for mi, m in pairs(matrices) do
        matrices[mi] = nil
        m.alloc()
        return m
    end
end

return M

