local M = {}

local cfg = require 'config'
local util = require 'util'
local pwld = require 'physwld'
local meshes = require 'meshes'

local PROJ_FOV = 60 * math.pi / 360

local function make_frustum(znear, zfar)
    local mproj = api_matrix_alloc()
    local vbounds = api_vector_alloc()
    local vz = api_vector_alloc()

    local ymax = znear * math.tan(PROJ_FOV)
    local xmax = ymax * cfg.SCREEN_WIDTH / cfg.SCREEN_HEIGHT

    api_vector_const(vbounds, -xmax, xmax, -ymax, ymax)
    api_vector_const(vz, znear, zfar, 0, 0)

    api_matrix_frustum(mproj, vbounds, vz, 0, 1)
    api_matrix_update(mproj)
    api_matrix_stop(mproj)
    api_vector_free(vbounds)
    api_vector_free(vz)
    return mproj
end

local function make_ortho()
    local mproj = api_matrix_alloc()
    local vbounds = api_vector_alloc()
    local vz = api_vector_alloc()

    api_vector_const(vbounds, 0, cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT, 0)
    api_vector_const(vz, -1, 1, 0, 0)

    api_matrix_ortho(mproj, vbounds, vz, 0, 1)
    api_matrix_update(mproj)
    api_matrix_stop(mproj)
    api_vector_free(vbounds)
    api_vector_free(vz)
    return mproj
end

local function visual_alloc()
    local self = {}

    local mproj2d = make_ortho()
    local mproj3dnear = make_frustum(1, 0.5 * cfg.RANGE_NEAR)
    local mproj3dfar = make_frustum(0.5 * cfg.RANGE_NEAR, 0.5 * cfg.RANGE_FAR)
    local mview2d = util.matrix_pos_stop(0, 0, 0)
    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    self.vclrcol = util.vector_const(0, 0, 0, 0)
    local vclrdep = util.vector_const(1, 0, 0 ,0)
    local vtscale = util.vector_const(1, 0, 0, 0)

    local rroot = api_rop_alloc_root()
    local rclrdep = api_rop_alloc_clear_depth(rroot, vclrdep, 0)
    local rclrcol = api_rop_alloc_clear_color(rclrdep, self.vclrcol)
    local rtscale = api_rop_alloc_tscale(rclrcol, vtscale, 0)

    local rclrfar = api_rop_alloc_clear(rtscale, API_ROP_CLEAR_COLOR + API_ROP_CLEAR_DEPTH)
    local rproj3dfar = api_rop_alloc_proj(rclrfar, mproj3dfar)
    local rmview3dfar = api_rop_alloc_mview(rproj3dfar, self.mview3d)
    local rmeshfar = api_rop_alloc_draw_meshes(rmview3dfar, meshes.GROUP_FAR)

    local rclrnear = api_rop_alloc_clear(rmeshfar, API_ROP_CLEAR_DEPTH)
    local rproj3dnear = api_rop_alloc_proj(rclrnear, mproj3dnear)
    local rmview3dnear = api_rop_alloc_mview(rproj3dnear, self.mview3d)
    local rmeshnear = api_rop_alloc_draw_meshes(rmview3dnear, meshes.GROUP_NEAR)

    local rproj2d = api_rop_alloc_proj(rmeshnear, mproj2d)
    local rmview2d = api_rop_alloc_mview(rproj2d, mview2d)
    local rtext = api_rop_alloc_dbg_text(rmview2d)

    function self.free()
        api_matrix_free(mproj2d)
        api_matrix_free(mproj3dnear)
        api_matrix_free(mproj3dfar)
        api_matrix_free(mview2d)
        api_matrix_free(self.mview3d)
        api_vector_free(self.vclrcol)
        api_vector_free(vclrdep)
        api_vector_free(vtscale)

        api_rop_free(rroot)
        api_rop_free(rclrdep)
        api_rop_free(rclrcol)
        api_rop_free(rtscale)

        api_rop_free(rclrfar)
        api_rop_free(rproj3dfar)
        api_rop_free(rmview3dfar)
        api_rop_free(rmeshfar)

        api_rop_free(rclrnear)
        api_rop_free(rproj3dnear)
        api_rop_free(rmview3dnear)
        api_rop_free(rmeshnear)

        api_rop_free(rproj2d)
        api_rop_free(rmview2d)
        api_rop_free(rtext)
    end

    function self.engage()
        api_render_engage(rroot)
    end

    return self
end

local function eagle_alloc()
    local self = {}

    local mproj2d = make_ortho()
    local mproj3d = make_frustum(1, 1024)
    local mview2d = util.matrix_pos_stop(0, 0, 0)
    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    local vclrcol = util.vector_const(0, 0, 0, 0)
    local vclrdep = util.vector_const(1, 0, 0 ,0)
    local vtscale = util.vector_const(1, 0, 0, 0)
    local rroot = api_rop_alloc_root()
    local rclrcol = api_rop_alloc_clear_color(rroot, vclrcol)
    local rclrdep = api_rop_alloc_clear_depth(rclrcol, vclrdep, 0)
    local rclr = api_rop_alloc_clear(rclrdep, API_ROP_CLEAR_COLOR + API_ROP_CLEAR_DEPTH)
    local rtscale = api_rop_alloc_tscale(rclr, vtscale, 0)
    local rproj3d = api_rop_alloc_proj(rtscale, mproj3d)
    local rmview3d = api_rop_alloc_mview(rproj3d, self.mview3d)
    local rmesh = api_rop_alloc_draw_meshes(rmview3d, meshes.GROUP_NEAR)
    local rproj2d = api_rop_alloc_proj(rmesh, mproj2d)
    local rmview2d = api_rop_alloc_mview(rproj2d, mview2d)
    local rtext = api_rop_alloc_dbg_text(rmview2d)

    function self.free()
        api_matrix_free(mproj2d)
        api_matrix_free(mproj3d)
        api_matrix_free(mview2d)
        api_matrix_free(self.mview3d)
        api_vector_free(vclrcol)
        api_vector_free(vclrdep)
        api_vector_free(vtscale)
        api_rop_free(rroot)
        api_rop_free(rclrcol)
        api_rop_free(rclrdep)
        api_rop_free(rclr)
        api_rop_free(rtscale)
        api_rop_free(rproj3d)
        api_rop_free(rmview3d)
        api_rop_free(rmesh)
        api_rop_free(rproj2d)
        api_rop_free(rmview2d)
        api_rop_free(rtext)
    end

    function self.engage()
        api_render_engage(rroot)
    end

    return self
end

local function debug_alloc()
    local self = {}

    local mproj2d = make_ortho()
    local mproj3d = make_frustum(1, 1024)
    local mview2d = util.matrix_pos_stop(0, 0, 0)
    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    local vclrcol = util.vector_const(0, 0, 0, 0)
    local vclrdep = util.vector_const(1, 0, 0 ,0)
    local rroot = api_rop_alloc_root()
    local rclrcol = api_rop_alloc_clear_color(rroot, vclrcol)
    local rclrdep = api_rop_alloc_clear_depth(rclrcol, vclrdep, 0)
    local rclr = api_rop_alloc_clear(rclrdep, API_ROP_CLEAR_COLOR + API_ROP_CLEAR_DEPTH)
    local rproj3d = api_rop_alloc_proj(rclr, mproj3d)
    local rmview3d = api_rop_alloc_mview(rproj3d, self.mview3d)
    local rphys = api_rop_alloc_dbg_physics(rmview3d, pwld.wld)
    local rproj2d = api_rop_alloc_proj(rphys, mproj2d)
    local rmview2d = api_rop_alloc_mview(rproj2d, mview2d)
    local rtext = api_rop_alloc_dbg_text(rmview2d)

    function self.free()
        api_matrix_free(mproj2d)
        api_matrix_free(mproj3d)
        api_matrix_free(mview2d)
        api_matrix_free(self.mview3d)
        api_vector_free(vclrcol)
        api_vector_free(vclrdep)
        api_rop_free(rroot)
        api_rop_free(rclrcol)
        api_rop_free(rclrdep)
        api_rop_free(rclr)
        api_rop_free(rproj3d)
        api_rop_free(rmview3d)
        api_rop_free(rphys)
        api_rop_free(rproj2d)
        api_rop_free(rmview2d)
        api_rop_free(rtext)
    end

    function self.engage()
        api_render_engage(rroot)
    end

    return self
end

function M.camera(m)
    api_matrix_inv(M.visual.mview3d, m)
    api_matrix_inv(M.debug.mview3d, m)
    api_matrix_inv(M.eagle.mview3d, m)
end

function M.init()
    M.visual = visual_alloc()
    M.debug = debug_alloc()
    M.eagle = eagle_alloc()
end

function M.done()
    M.visual.free()
    M.debug.free()
    M.eagle.free()
end

return M
