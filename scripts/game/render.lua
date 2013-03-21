local M = {}

local cfg = require 'config'
local util = require 'core.util'
local pwld = require 'game.physwld'
local meshes = require 'game.meshes'
local lod = require 'game.lod'
local matrix = require 'core.matrix'
local vector = require 'core.vector'
local mesh = require 'core.render.mesh'
local render = require 'core.render.render'
local prof = require 'game.prof'

local DEBUG_ZFAR = 200
local EAGLE_ZFAR = 20000
local ORTHO_ZNEAR = 0
local ORTHO_ZFAR = 1
local FOG_NEAR = 10000
local FOG_FAR = 12800

local current
local frame_tag = 1000

local function make_frustum(znear, zfar, dist)
    local mproj = matrix.alloc()
    local vbounds = vector.alloc()
    local vz = vector.alloc()
    local sx, sy = util.camera_dims()
    local ymax = sy * znear / dist
    local xmax = sx * znear / dist

    vbounds.const(-xmax, xmax, -ymax, ymax)
    vz.const(znear, zfar, 0, 0)

    mproj.frustum(vbounds, vz, 0, 1)
    mproj.update(0, API_MATRIX_FORCED_UPDATE)
    mproj.stop()
    vbounds.free()
    vz.free()
    return mproj
end

local function make_ortho()
    local mproj = matrix.alloc()
    local vbounds = vector.alloc()
    local vz = vector.alloc()
    local sx, sy = util.camera_dims()

    vbounds.const(-sx, sx, -sy, sy)
    vz.const(ORTHO_ZNEAR, ORTHO_ZFAR, 0, 0)

    mproj.ortho(vbounds, vz, 0, 1)
    mproj.update(0, API_MATRIX_FORCED_UPDATE)
    mproj.stop()
    vbounds.free()
    vz.free()
    return mproj
end

local function visual_alloc()
    local self = {}

    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    self.vclrcol = util.vector_const(0, 0, 0, 0)
    self.tscale = 1

    function self.free()
        self.mview3d.free()
        self.vclrcol.free()
    end

    function self.draw(draw_tag)
        local vclrdep = util.vector_const(1, 0, 0 ,0)
        local mproj2d = make_ortho()
        local mview2d = util.matrix_pos_stop(0, 0, 0)

        prof.cpu.rclear.start()
        prof.gpu.rclear.start()
        api_render_clear_depth(vclrdep.id(), 0)
        api_render_clear_color(self.vclrcol.id())
        api_render_clear(API_RENDER_CLEAR_COLOR + API_RENDER_CLEAR_DEPTH)
        prof.gpu.rclear.finish()
        prof.cpu.rclear.finish()

        prof.cpu.rdraw.start()
        prof.gpu.rdraw.start()
        api_render_mview(self.mview3d.id())
        for lodi = 0, lod.count - 1 do
            local mproj3d = make_frustum(lod.lods[lodi].clip_near, lod.lods[lodi].clip_far, cfg.CAMERA_DIST)
            if lodi > 0 then
                api_render_clear(API_RENDER_CLEAR_DEPTH)
            end
            api_render_proj(mproj3d.id())
            mesh.draw(meshes.GROUP_LODS[lodi], draw_tag)
            mproj3d.free()
        end
        api_render_clear(API_RENDER_CLEAR_DEPTH)
        api_render_proj(mproj2d.id())
        api_render_mview(mview2d.id())
        mesh.draw(meshes.GROUP_GUI, draw_tag)
        prof.gpu.rdraw.finish()
        prof.cpu.rdraw.finish()

        render.finish_frame(prof)

        vclrdep.free()
        mproj2d.free()
        mview2d.free()
    end

    function self.update(dt, update_tag)
        self.vclrcol.update(dt, update_tag)
        self.mview3d.update(dt, update_tag)
        for lodi = 0, lod.count - 1 do
            mesh.update(meshes.GROUP_LODS[lodi], dt * self.tscale, update_tag)
        end
        mesh.update(meshes.GROUP_GUI, dt, update_tag)
    end

    return self
end

local function eagle_alloc()
    local self = {}

    self.mview3d = util.matrix_pos_stop(0, 0, 0)
    self.tscale = 1

    function self.free()
        self.mview3d.free()
    end

    function self.draw(draw_tag)
        local vclrcol = util.vector_const(0, 0, 0, 0)
        local vclrdep = util.vector_const(1, 0, 0 ,0)
        local mproj3d = make_frustum(cfg.CAMERA_DIST, EAGLE_ZFAR, cfg.CAMERA_DIST)

        api_render_clear_depth(vclrdep.id(), 0)
        api_render_clear_color(vclrcol.id())
        api_render_proj(mproj3d.id())
        api_render_mview(self.mview3d.id())
        for lodi = 0, lod.count - 1 do
            if lodi == 0 then
                api_render_clear(API_RENDER_CLEAR_COLOR + API_RENDER_CLEAR_DEPTH)
            else
                api_render_clear(API_RENDER_CLEAR_DEPTH)
            end
            mesh.draw(meshes.GROUP_LODS[lodi], draw_tag)
        end
        render.finish_frame()

        vclrcol.free()
        vclrdep.free()
        mproj3d.free()
    end

    function self.update(dt, update_tag)
        self.mview3d.update(dt, update_tag)
        for lodi = 0, lod.count - 1 do
            mesh.update(meshes.GROUP_LODS[lodi], dt * self.tscale, update_tag)
        end
    end

    return self
end

local function debug_alloc()
    local self = {}

    self.mview3d = util.matrix_pos_stop(0, 0, 0)

    function self.free()
        self.mview3d.free()
    end

    function self.draw(draw_tag)
        local vclrcol = util.vector_const(0, 0, 0, 0)
        local vclrdep = util.vector_const(1, 0, 0 ,0)
        local mproj3d = make_frustum(cfg.CAMERA_DIST, DEBUG_ZFAR, cfg.CAMERA_DIST)

        api_render_clear_depth(vclrdep.id(), 0)
        api_render_clear_color(vclrcol.id())
        api_render_clear(API_RENDER_CLEAR_COLOR + API_RENDER_CLEAR_DEPTH)
        api_render_proj(mproj3d.id())
        api_render_mview(self.mview3d.id())
        pwld.wld.ddraw()
        render.finish_frame()

        vclrcol.free()
        vclrdep.free()
        mproj3d.free()
    end

    function self.update(dt, update_tag)
        self.mview3d.update(dt, update_tag)
    end

    return self
end

function M.camera_stop()
    M.visual.mview3d.stop()
    M.debug.mview3d.stop()
    M.eagle.mview3d.stop()
end

function M.camera(m)
    M.visual.mview3d.inv(m)
    M.debug.mview3d.inv(m)
    M.eagle.mview3d.inv(m)
end

function M.timescale(t)
    M.visual.tscale = t
    M.eagle.tscale = t
end

function M.init()
    render.init()
    M.visual = visual_alloc()
    M.debug = debug_alloc()
    M.eagle = eagle_alloc()
end

function M.done()
    M.visual.free()
    M.debug.free()
    M.eagle.free()
    render.done()
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
