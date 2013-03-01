local M = {}

local quit = require 'quit'
local cfg = require 'config'
local util = require 'util'

local LOGIC_TIME = 0.013
local GC_STEP = 10
local CLIP_FAR = 1000
local GRID_RES = 100
local SCALE = {0.1, 2, 0.1, 0}
local POSITION = {0, -5, -30, 0}
local CLEAR_COLOR = {0, 1, 0, 0}
local ROT_PERIOD = 15
local MESH_HIDDEN = cfg.TWINS
local SIN_Y_D_SCALE = math.pi * 2
local SIN_Y_T_SCALE = 3 / (math.pi * 2)
local SIN_R_XZ_SCALE = math.pi * 2
local SIN_R_T_SCALE = 4 / (math.pi * 2)
local SIN_G_XZ_SCALE = math.pi * 3
local SIN_G_T_SCALE = 5 / (math.pi * 2)
local SIN_B_XZ_SCALE = math.pi * 5
local SIN_B_T_SCALE = 6 / (math.pi * 2)
local COL_MIN = 0.5

local shader, transform, rotbuf, vpos, vscl, vrot
local mesh_group = {}
local vbufs = {}
local ibufs = {}
local meshes = {}
local draw_tag = 0
local update_tag = 0
local twin = 0

local function twin_active()
    return twin
end

local function twin_inactive()
    return (twin + 1) % cfg.TWINS
end

local function twin_swap()
    twin = twin_inactive()
end

local function run_co(co, start_time, max_time)
    while coroutine.status(co) ~= 'dead' do
        api_main_gc_step(GC_STEP)
        local res, arg = coroutine.resume(co)
        if res and arg then
            break
        elseif not res then
            io.write('Coroutine\n', debug.traceback(co), '\n')
            error(arg)
        end
        if api_timer() - start_time > max_time then
            break
        end
    end
end

local function make_frustum(znear, zfar, dist)
    local mproj = api_matrix_alloc()
    local vbounds = api_vector_alloc()
    local vz = api_vector_alloc()
    local sx, sy = util.camera_dims()
    local ymax = sy * znear / dist
    local xmax = sx * znear / dist

    api_vector_const(vbounds, -xmax, xmax, -ymax, ymax)
    api_vector_const(vz, znear, zfar, 0, 0)

    api_matrix_frustum(mproj, vbounds, vz, 0, 1)
    api_matrix_update(mproj, 0, API_MATRIX_FORCED_UPDATE)
    api_matrix_stop(mproj)
    api_vector_free(vbounds)
    api_vector_free(vz)
    return mproj
end

local function render_draw()
    local vclrdep = util.vector_const(1, 0, 0, 0)
    local vclrcol = util.vector_const(unpack(CLEAR_COLOR))
    local mview3d = util.matrix_pos_stop(0, 0, 0)
    local mproj3d = make_frustum(cfg.CAMERA_DIST, CLIP_FAR, cfg.CAMERA_DIST)

    draw_tag = draw_tag + 1

    api_render_fog_off()
    api_render_clear_depth(vclrdep, 0)
    api_render_clear_color(vclrcol)
    api_render_clear(API_RENDER_CLEAR_COLOR + API_RENDER_CLEAR_DEPTH)
    api_render_mview(mview3d)
    api_render_proj(mproj3d)
    api_mesh_draw(mesh_group[twin_active()], draw_tag)
    api_render_swap()

    api_vector_free(vclrcol)
    api_vector_free(vclrdep)
    api_matrix_free(mview3d)
    api_matrix_free(mproj3d)
end

local function render_update()
    update_tag = update_tag + 1
    api_mesh_update(mesh_group[twin_active()], cfg.FRAME_TIME, update_tag)
end

local function init()
    do
        transform = api_matrix_alloc()
        rotbuf = api_buf_alloc()
        vrot = api_vector_alloc()
        vscl = util.vector_const(unpack(SCALE))
        vpos = util.vector_const(unpack(POSITION))
        api_buf_set(rotbuf, 0,   0,0,0,0,ROT_PERIOD,   math.pi*2,0,0,0,0)
        api_vector_seq(vrot, rotbuf, 0, 2, 1, API_VECTOR_IPL_LINEAR)
        api_matrix_pos_scl_rot(transform, vpos, vscl, vrot, API_MATRIX_AXIS_Y, 0)
    end
    do
        shader = api_shprog_alloc()
        api_shprog_attach(shader, API_SHPROG_FRAGMENT,
            'void main()\n' ..
            '{\n' ..
            '   gl_FragColor = gl_Color;\n' ..
            '}\n'
        )
        api_shprog_link(shader)
    end
    for i = 0, cfg.TWINS - 1 do
        mesh_group[i] = i
        vbufs[i] = api_vbuf_alloc()
        ibufs[i] = api_ibuf_alloc()
        meshes[i] = api_mesh_alloc(MESH_HIDDEN, API_MESH_TRIANGLES, vbufs[i], ibufs[i],
                                   shader, transform, 0, 6 * (GRID_RES - 1) * (GRID_RES - 1))
        do
            api_ibuf_map(ibufs[i], 0, 6 * (GRID_RES - 1) * (GRID_RES - 1))
            for z = 0, GRID_RES - 2 do
                for x = 0, GRID_RES - 2 do
                    local o00 = x + z * GRID_RES
                    local o01 = x + (z + 1) * GRID_RES
                    local o10 = (x + 1) + z * GRID_RES
                    local o11 = (x + 1) + (z + 1) * GRID_RES
                    local o = (x + z * (GRID_RES - 1)) * 6
                    api_ibuf_set(ibufs[i], o,  o00,o01,o10,  o10,o01,o11)
                end
            end
            api_ibuf_unmap(ibufs[i])
        end
    end
end

local function done()
    for i = 0, cfg.TWINS - 1 do
        api_vbuf_free(vbufs[i])
        api_ibuf_free(ibufs[i])
        api_mesh_free(meshes[i])
    end
    do
        api_matrix_free(transform)
        api_vector_free(vpos)
        api_vector_free(vscl)
        api_vector_free(vrot)
        api_buf_free(rotbuf)
        api_shprog_free(shader)
    end
end

local function fill_vbuf(vbuf, vmap)
    api_vbuf_map(vbuf, 0, GRID_RES * GRID_RES)
    for z = 0, GRID_RES - 1 do
        for x = 0, GRID_RES - 1 do
            local y, r, g, b = unpack(vmap[z][x])
            api_vbuf_set(vbuf, x + z * GRID_RES,
                         x - 0.5 * (GRID_RES - 1),
                         y,
                         z - 0.5 * (GRID_RES - 1),
                         r, g, b, 0, 0, 0)
            coroutine.yield(false)
        end
    end
    api_vbuf_unmap(vbuf)
end

local function generate(t)
    local vmap = {}
    for z = 0, GRID_RES - 1 do
        vmap[z] = {}
        for x = 0, GRID_RES - 1 do
            local dz, dx = z - (GRID_RES-1)/2, x - (GRID_RES-1)/2
            local d = math.sqrt(dz*dz + dx*dx)
            local y = math.sin((d/GRID_RES)*SIN_Y_D_SCALE + t*SIN_Y_T_SCALE)
            local r = util.lerp(math.sin(((x+z)/GRID_RES)*SIN_R_XZ_SCALE + t*SIN_R_T_SCALE), -1, 1, COL_MIN, 1)
            local g = util.lerp(math.sin(((x+z)/GRID_RES)*SIN_G_XZ_SCALE + t*SIN_G_T_SCALE), -1, 1, COL_MIN, 1)
            local b = util.lerp(math.sin(((x+z)/GRID_RES)*SIN_B_XZ_SCALE + t*SIN_B_T_SCALE), -1, 1, COL_MIN, 1)
            vmap[z][x] = {y, r, g, b}
            coroutine.yield(false)
        end
    end
    fill_vbuf(vbufs[twin_inactive()], vmap)
    api_mesh_group(meshes[twin_inactive()], mesh_group[twin_inactive()])
    twin_swap()
    util.sync_wait()
end

function M.run()

    local control = coroutine.create(
        function()
            while not quit.requested()
            do
                quit.control()
                coroutine.yield(true)
            end
        end)

    local work = coroutine.create(
        function()
            while not quit.requested()
            do
                generate(update_tag * cfg.FRAME_TIME)
                coroutine.yield(true)
            end
        end)

    init()

    while coroutine.status(control) ~= 'dead'
       or coroutine.status(work) ~= 'dead'
    do
        local logic_time = api_timer()
        api_input_update()
        api_main_gc_step(GC_STEP)
        run_co(control, logic_time, 0)
        run_co(work, logic_time, LOGIC_TIME)
        render_update()
        render_draw()
    end

    done()
end

return M
