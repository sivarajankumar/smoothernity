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

local current = nil
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
    api_matrix_update(mproj, 0, API_MATRIX_FORCED_UPDATE)
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
    api_matrix_update(mproj, 0, API_MATRIX_FORCED_UPDATE)
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
    api_matrix_update(mproj, 0, API_MATRIX_FORCED_UPDATE)
    api_matrix_stop(mproj)
    api_vector_free(vbounds)
    api_vector_free(vz)
    return mproj
end

local function visual_alloc()
    local self = {}

    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    self.vclrcol = util.vector_const(0, 0, 0, 0)
    self.tscale = 1

    function self.free()
        api_matrix_free(self.mview3d)
        api_vector_free(self.vclrcol)
    end

    function self.draw(draw_tag)
        local vclrdep = util.vector_const(1, 0, 0 ,0)
        local vfogdist = util.vector_const(FOG_NEAR, FOG_FAR, 0, 0)
        local mproj2d = make_ortho()
        local mview2d = util.matrix_pos_stop(0, 0, 0)

        api_render_fog_off()
        api_render_clear_depth(vclrdep, 0)
        api_render_clear_color(self.vclrcol)
        api_render_fog_lin(self.vclrcol, vfogdist, 0, 1)
        api_render_mview(self.mview3d)
        for lodi = 0, lod.count - 1 do
            local mproj3d = make_frustum(lod.lods[lodi].clip_near, lod.lods[lodi].clip_far, cfg.CAMERA_DIST)
            if lodi == 0 then
                api_render_clear(API_RENDER_CLEAR_COLOR + API_RENDER_CLEAR_DEPTH)
            else
                api_render_clear(API_RENDER_CLEAR_DEPTH)
            end
            api_render_proj(mproj3d)
            api_mesh_draw(meshes.lod_group(lodi), draw_tag)
            api_matrix_free(mproj3d)
        end
        api_render_fog_off()
        api_render_clear(API_RENDER_CLEAR_DEPTH)
        api_render_proj(mproj2d)
        api_render_mview(mview2d)
        api_mesh_draw(meshes.GROUP_GUI, draw_tag)
        api_render_swap()

        api_vector_free(vfogdist)
        api_vector_free(vclrdep)
        api_matrix_free(mproj2d)
        api_matrix_free(mview2d)
    end

    function self.update(dt, update_tag)
        api_vector_update(self.vclrcol, dt, update_tag)
        api_matrix_update(self.mview3d, dt, update_tag)
        for lodi = 0, lod.count - 1 do
            api_mesh_update(meshes.lod_group(lodi), dt * self.tscale, update_tag)
        end
        api_mesh_update(meshes.GROUP_GUI, dt, update_tag)
    end

    return self
end

local function eagle_alloc()
    local self = {}

    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    self.tscale = 1

    function self.free()
        api_matrix_free(self.mview3d)
    end

    function self.draw(draw_tag)
        local vclrcol = util.vector_const(0, 0, 0, 0)
        local vclrdep = util.vector_const(1, 0, 0 ,0)
        local mproj2d = make_screen()
        local mproj3d = make_frustum(cfg.CAMERA_DIST, EAGLE_ZFAR, cfg.CAMERA_DIST)
        local mview2d = util.matrix_pos_stop(0, 0, 0)

        api_render_fog_off()
        api_render_clear_depth(vclrdep, 0)
        api_render_clear_color(vclrcol)
        api_render_proj(mproj3d)
        api_render_mview(self.mview3d)
        for lodi = 0, lod.count - 1 do
            if lodi == 0 then
                api_render_clear(API_RENDER_CLEAR_COLOR + API_RENDER_CLEAR_DEPTH)
            else
                api_render_clear(API_RENDER_CLEAR_DEPTH)
            end
            api_mesh_draw(meshes.lod_group(lodi), draw_tag)
        end
        api_render_proj(mproj2d)
        api_render_mview(mview2d)
        api_text_draw()
        api_render_swap()

        api_vector_free(vclrcol)
        api_vector_free(vclrdep)
        api_matrix_free(mproj2d)
        api_matrix_free(mview2d)
        api_matrix_free(mproj3d)
    end

    function self.update(dt, update_tag)
        api_matrix_update(self.mview3d, dt, update_tag)
        for lodi = 0, lod.count - 1 do
            api_mesh_update(meshes.lod_group(lodi), dt * self.tscale, update_tag)
        end
    end

    return self
end

local function debug_alloc()
    local self = {}

    self.mview3d = util.matrix_pos_stop(0, 0, 0)

    function self.free()
        api_matrix_free(self.mview3d)
    end

    function self.draw(draw_tag)
        local vclrcol = util.vector_const(0, 0, 0, 0)
        local vclrdep = util.vector_const(1, 0, 0 ,0)
        local mproj2d = make_screen()
        local mproj3d = make_frustum(cfg.CAMERA_DIST, DEBUG_ZFAR, cfg.CAMERA_DIST)
        local mview2d = util.matrix_pos_stop(0, 0, 0)

        api_render_fog_off()
        api_render_clear_depth(vclrdep, 0)
        api_render_clear_color(vclrcol)
        api_render_clear(API_RENDER_CLEAR_COLOR + API_RENDER_CLEAR_DEPTH)
        api_render_proj(mproj3d)
        api_render_mview(self.mview3d)
        api_physics_wld_ddraw(pwld.wld)

        api_render_proj(mproj2d)
        api_render_mview(mview2d)
        api_text_draw()
        api_render_swap()

        api_vector_free(vclrcol)
        api_vector_free(vclrdep)
        api_matrix_free(mproj2d)
        api_matrix_free(mview2d)
        api_matrix_free(mproj3d)
    end

    function self.update(dt, update_tag)
        api_matrix_update(self.mview3d, dt, update_tag)
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
    M.visual.tscale = t
    M.eagle.tscale = t
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

function M.engage(what)
    current = what
end

function M.update()
    frame_tag = frame_tag + 1
    if current ~= nil then
        current.update(cfg.FRAME_TIME, frame_tag)
    end
end

function M.draw()
    if current ~= nil then
        current.draw(frame_tag)
    end
end

return M
