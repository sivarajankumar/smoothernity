local M = {}

local cfg = require 'config'
local util = require 'util'
local pwld = require 'physwld'
local meshes = require 'meshes'
local lod = require 'lod'

local DEBUG_ZFAR = 200
local EAGLE_ZFAR = 20000
local ORTHO_ZNEAR = 0
local ORTHO_ZFAR = 1
local FOG_NEAR = 10000
local FOG_FAR = 12800

local current_root = nil
local frame_tag = 1000

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
    local sx, sy = util.camera_dims()

    api_vector_const(vbounds, -sx, sx, -sy, sy)
    api_vector_const(vz, ORTHO_ZNEAR, ORTHO_ZFAR, 0, 0)

    api_matrix_ortho(mproj, vbounds, vz, 0, 1)
    api_matrix_update(mproj)
    api_matrix_stop(mproj)
    api_vector_free(vbounds)
    api_vector_free(vz)
    return mproj
end

local function make_screen()
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
    local mview2d = util.matrix_pos_stop(0, 0, 0)
    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    self.vclrcol = util.vector_const(0, 0, 0, 0)
    local vclrdep = util.vector_const(1, 0, 0 ,0)
    local vfogdist = util.vector_const(FOG_NEAR, FOG_FAR, 0, 0)
    self.vtscale = util.vector_const(1, 0, 0, 0)
    local vtscalegui = util.vector_const(1, 1, 1, 1)

    local rroot = api_rop_alloc_root()
    local rclrdep = api_rop_alloc_clear_depth(rroot, vclrdep, 0)
    local rclrcol = api_rop_alloc_clear_color(rclrdep, self.vclrcol)
    local rfoglin = api_rop_alloc_fog_lin(rclrcol, self.vclrcol, vfogdist, 0, 1)
    local rtscale = api_rop_alloc_tscale(rfoglin, self.vtscale, 0)

    local lods = {}
    for lodi = 0, lod.count - 1 do
        local ld = {}
        ld.mproj3d = make_frustum(lod.lods[lodi].clip_near, lod.lods[lodi].clip_far, cfg.CAMERA_DIST)
        if lodi == 0 then
            ld.rclr = api_rop_alloc_clear(rtscale, API_ROP_CLEAR_COLOR + API_ROP_CLEAR_DEPTH)
        else
            ld.rclr = api_rop_alloc_clear(lods[lodi - 1].rmesh, API_ROP_CLEAR_DEPTH)
        end
        ld.rproj3d = api_rop_alloc_proj(ld.rclr, ld.mproj3d)
        ld.rmview3d = api_rop_alloc_mview(ld.rproj3d, self.mview3d)
        ld.rmesh = api_rop_alloc_draw_meshes(ld.rmview3d, meshes.lod_group(lodi))
        lods[lodi] = ld
    end

    local rtscalegui = api_rop_alloc_tscale(lods[lod.count - 1].rmesh, vtscalegui, 0)
    local rfogoff = api_rop_alloc_fog_off(rtscalegui)
    local rclr2d = api_rop_alloc_clear(rfogoff, API_ROP_CLEAR_DEPTH)
    local rproj2d = api_rop_alloc_proj(rclr2d, mproj2d)
    local rmview2d = api_rop_alloc_mview(rproj2d, mview2d)
    local rmeshgui = api_rop_alloc_draw_meshes(rmview2d, meshes.GROUP_GUI)
    local rswap = api_rop_alloc_swap(rmeshgui)

    function self.free()
        api_matrix_free(mproj2d)
        api_matrix_free(mview2d)
        api_matrix_free(self.mview3d)
        api_vector_free(self.vclrcol)
        api_vector_free(vclrdep)
        api_vector_free(vfogdist)
        api_vector_free(self.vtscale)
        api_vector_free(vtscalegui)

        api_rop_free(rroot)
        api_rop_free(rclrdep)
        api_rop_free(rclrcol)
        api_rop_free(rfoglin)
        api_rop_free(rtscale)

        for k, v in pairs(lods) do
            api_matrix_free(v.mproj3d)
            api_rop_free(v.rclr)
            api_rop_free(v.rproj3d)
            api_rop_free(v.rmview3d)
            api_rop_free(v.rmesh)
        end

        api_rop_free(rtscalegui)
        api_rop_free(rfogoff)
        api_rop_free(rclr2d)
        api_rop_free(rproj2d)
        api_rop_free(rmview2d)
        api_rop_free(rmeshgui)
        api_rop_free(rswap)
    end

    function self.engage()
        current_root = rroot
    end

    return self
end

local function eagle_alloc()
    local self = {}

    local mproj2d = make_screen()
    local mproj3d = make_frustum(cfg.CAMERA_DIST, EAGLE_ZFAR, cfg.CAMERA_DIST)
    local mview2d = util.matrix_pos_stop(0, 0, 0)
    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    local vclrcol = util.vector_const(0, 0, 0, 0)
    local vclrdep = util.vector_const(1, 0, 0 ,0)
    self.vtscale = util.vector_const(1, 0, 0, 0)

    local rroot = api_rop_alloc_root()
    local rclrdep = api_rop_alloc_clear_depth(rroot, vclrdep, 0)
    local rclrcol = api_rop_alloc_clear_color(rclrdep, vclrcol)
    local rtscale = api_rop_alloc_tscale(rclrcol, self.vtscale, 0)
    local rproj3d = api_rop_alloc_proj(rtscale, mproj3d)
    local rmview3d = api_rop_alloc_mview(rproj3d, self.mview3d)

    local lods = {}
    for lodi = 0, lod.count - 1 do
        local ld = {}
        if lodi == 0 then
            ld.rclr = api_rop_alloc_clear(rmview3d, API_ROP_CLEAR_COLOR + API_ROP_CLEAR_DEPTH)
        else
            ld.rclr = api_rop_alloc_clear(lods[lodi - 1].rmesh, API_ROP_CLEAR_DEPTH)
        end
        ld.rmesh = api_rop_alloc_draw_meshes(ld.rclr, meshes.lod_group(lodi))
        lods[lodi] = ld
    end

    local rproj2d = api_rop_alloc_proj(lods[lod.count - 1].rmesh, mproj2d)
    local rmview2d = api_rop_alloc_mview(rproj2d, mview2d)
    local rtext = api_rop_alloc_dbg_text(rmview2d)
    local rswap = api_rop_alloc_swap(rtext)

    function self.free()
        api_matrix_free(mproj2d)
        api_matrix_free(mproj3d)
        api_matrix_free(mview2d)
        api_matrix_free(self.mview3d)
        api_vector_free(vclrcol)
        api_vector_free(vclrdep)
        api_vector_free(self.vtscale)

        api_rop_free(rroot)
        api_rop_free(rclrdep)
        api_rop_free(rclrcol)
        api_rop_free(rtscale)
        api_rop_free(rproj3d)
        api_rop_free(rmview3d)

        for k, v in pairs(lods) do
            api_rop_free(v.rclr)
            api_rop_free(v.rmesh)
        end

        api_rop_free(rproj2d)
        api_rop_free(rmview2d)
        api_rop_free(rtext)
        api_rop_free(rswap)
    end

    function self.engage()
        current_root = rroot
    end

    return self
end

local function debug_alloc()
    local self = {}

    local mproj2d = make_screen()
    local mproj3d = make_frustum(cfg.CAMERA_DIST, DEBUG_ZFAR, cfg.CAMERA_DIST)
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
    local rswap = api_rop_alloc_swap(rtext)

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
        api_rop_free(rswap)
    end

    function self.engage()
        current_root = rroot
    end

    return self
end

function M.camera_stop()
    api_matrix_stop(M.visual.mview3d)
    api_matrix_stop(M.debug.mview3d)
    api_matrix_stop(M.eagle.mview3d)
end

function M.camera(m)
    api_matrix_inv(M.visual.mview3d, m)
    api_matrix_inv(M.debug.mview3d, m)
    api_matrix_inv(M.eagle.mview3d, m)
end

function M.timescale(t)
    api_vector_const(M.visual.vtscale, t, 0, 0, 0)
    api_vector_const(M.eagle.vtscale, t, 0, 0, 0)
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

function M.update()
    frame_tag = frame_tag + 1
    if current_root ~= nil then
        api_rop_update(current_root, cfg.FRAME_TIME, frame_tag)
    end
end

function M.draw()
    if current_root ~= nil then
        api_rop_draw(current_root, frame_tag)
    end
end

return M
