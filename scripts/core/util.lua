local M = {}

local cfg = require 'config'
local thread = require 'core.thread'
local matrix = require 'core.matrix'
local vector = require 'core.vector'
local prog = require 'core.prog'
local log = require 'core.log'

local MAX_WAIT_TIME = 10

function M.log2(v)
    local res = 0
    while true do
        v = math.floor(v / 2)
        if v > 0 then
            res = res + 1
        else
            break
        end
    end
    return res
end

function M.keys(src)
    local t = {}
    for k, _ in pairs(src) do
        table.insert(t, k)
    end
    return t
end

function M.values(src)
    local t = {}
    for _, v in pairs(src) do
        table.insert(t, v)
    end
    return t
end

function M.sorted(t)
    table.sort(t)
    return t
end

function M.reduce_and(func, args)
    for k, v in pairs(args) do
        if not func(v) then
            return false
        end
    end
    return true
end

function M.reduce_or(func, args)
    for k, v in pairs(args) do
        if func(v) then
            return true
        end
    end
    return false
end

function M.map(func, args)
    local res = {}
    for k, v in pairs(args) do
        res[k] = func(v)
    end
    return res
end

function M.empty(t)
    return M.reduce_and(function(...) return false end, t)
end

function M.prog_from_files(prefix)
    return prog.alloc(M.sync_read(prefix .. '.vert'),
                      M.sync_read(prefix .. '.frag'))
end

function M.sync_read(uid)
    local f = io.open(uid, 'r')
    if f then
        local s = f:read('*a')
        f:close()
        return s
    else
        return ''
    end
end

function M.sync_write(uid, data)
    if data == '' then
        os.remove(uid)
    else
        local f = io.open(uid, 'w')
        if f then
            f:write(data)
            f:close()
        else
            log.err('Cannot write "%s"', uid)
        end
    end
end

function M.wait_thread_idle(th, skip_frame)
    local t = api_timer()
    while not th.idle() do
        if api_timer() - t > MAX_WAIT_TIME then
            error('wait_thread_idle: too long\n')
        end
        coroutine.yield(skip_frame)
    end
end

function M.wait_thread_responding(th, skip_frame)
    local t = api_timer()
    while not th.responding() do
        if api_timer() - t > MAX_WAIT_TIME then
            error('wait_thread_responding: too long\n')
        end
        coroutine.yield(skip_frame)
    end
end

function M.sum(...)
    local s = 0
    for _, v in ipairs({...}) do
        s = s + v
    end
    return s
end

function M.async_read(uid)
    local th = thread.alloc('core.util_th')
    M.wait_thread_responding(th, false)
    th.request('async_read')
    M.wait_thread_responding(th, false)
    th.request(uid)
    M.wait_thread_responding(th, false)
    local res = th.request('')
    M.wait_thread_idle(th, false)
    th.free()
    return res
end

function M.async_write(uid, data)
    local th = thread.alloc('core.util_th')
    M.wait_thread_responding(th, false)
    th.request('async_write')
    M.wait_thread_responding(th, false)
    th.request(uid)
    M.wait_thread_responding(th, false)
    th.request(data)
    M.wait_thread_idle(th, false)
    th.free()
end

function M.uid_cache(uid)
    return string.format('%s/%s', os.getenv('SMOOTHERNITY_CACHE_DIR'), uid)
end

function M.uid_save(uid)
    return string.format('%s/%s', os.getenv('SMOOTHERNITY_SAVE_DIR'), uid)
end

function M.camera_dims()
    local mindim = math.min(cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT)
    return cfg.SCREEN_WIDTH / mindim, cfg.SCREEN_HEIGHT / mindim
end

function M.vector_const(x, y, z, w)
    local v = vector.alloc()
    v.const(x, y, z, w)
    return v
end

function M.vector_dist(v1, v2)
    local x1, y1, z1, w1 = v1.get()
    local x2, y2, z2, w2 = v2.get()
    local x, y, z = x1 - x2, y1 - y2, z1 - z2
    return math.sqrt(x*x + y*y + z*z)
end

function M.vector_copy(v, src)
    v.const(src.get())
end

function M.vector_move(v, vofs)
    local x, y, z, w = v.get()
    local dx, dy, dz, dw = vofs.get()
    v.const(x + dx, y + dy, z + dz, w + dw)
end

function M.vector_move_xz(v, vofs)
    local x, y, z, w = v.get()
    local dx, dy, dz, dw = vofs.get()
    v.const(x + dx, y, z + dz, w)
end

function M.spline(t, t1, t2, v0, v1, v2, v3)
    t = (t - t1) / (t2 - t1)
    assert (t >= 0 and t <= 1)
    local tt = t * t
    local ttt = tt * t
    local v = 2 * v1
    v = v + t * (-v0 + v2)
    v = v + tt * (2*v0 - 5*v1 + 4*v2 - v3)
    v = v + ttt * (-v0 + 3*v1 - 3*v2 + v3)
    v = v * 0.5
    return v
end

function M.clamp(x, min, max)
    return math.min(max, math.max(min, x))
end

function M.lerp(t, t0, t1, v0, v1)
    t = M.clamp(t, t0, t1)
    return v0 + ((v1 - v0) * (t - t0) / (t1 - t0))
end

function M.matrix_from_to_up_stop(fx, fy, fz, tx, ty, tz, ux, uy, uz)
    local m = matrix.alloc()
    local from = vector.alloc()
    local to = vector.alloc()
    local up = vector.alloc()
    from.const(fx, fy, fz, 0)
    to.const(tx, ty, tz, 0)
    up.const(ux, uy, uz, 0)
    m.from_to_up(from, to, up)
    m.update(0, API_MATRIX_FORCED_UPDATE)
    m.stop()
    from.free()
    to.free()
    up.free()
    return m
end

function M.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, axis, angle)
    local m = matrix.alloc()
    local pos = vector.alloc()
    local scl = vector.alloc()
    local rot = vector.alloc()
    pos.const(px, py, pz, 0)
    scl.const(sx, sy, sz, 0)
    rot.const(angle, 0, 0, 0)
    m.pos_scl_rot(pos, scl, rot, axis, 0)
    m.update(0, API_MATRIX_FORCED_UPDATE)
    m.stop()
    pos.free()
    scl.free()
    rot.free()
    return m
end

function M.matrix_pos_stop(x, y, z)
    return M.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, API_MATRIX_AXIS_X, 0)
end

function M.matrix_pos_scl_stop(px, py, pz, sx, sy, sz)
    return M.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, API_MATRIX_AXIS_X, 0)
end

function M.matrix_pos_rot_stop(x, y, z, axis, angle)
    return M.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, axis, angle)
end

function M.matrix_rot_stop(axis, angle)
    return M.matrix_pos_scl_rot_stop(0, 0, 0, 1, 1, 1, axis, angle)
end

function M.matrix_scl_stop(sx, sy, sz)
    return M.matrix_pos_scl_rot_stop(0, 0, 0, sx, sy, sz, API_MATRIX_AXIS_X, 0)
end

function M.matrix_move_global(m, x, y, z)
    local dm = M.matrix_pos_stop(x, y, z)
    m.mul_stop(dm, m)
    dm.free()
end

function M.matrix_move_local(m, x, y, z)
    local dm = M.matrix_pos_stop(x, y, z)
    m.mul_stop(m, dm)
    dm.free()
end

function M.matrix_rotate_local(m, axis, angle)
    local dm = M.matrix_rot_stop(axis, angle)
    m.mul_stop(m, dm)
    dm.free()
end

return M
