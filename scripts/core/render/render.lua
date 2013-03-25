local M = {}

local cfg = require 'config'
local coresync = require 'core.sync'
local ibuf = require 'core.render.ibuf'
local vbuf = require 'core.render.vbuf'
local tex = require 'core.render.tex'
local util = require 'core.util'

local UPLOAD_THRESH = 10

local sync
local twin = 0
local upload_count = 0
local upload_state = 'copying'

local function twin_active()
    return twin
end

local function twin_inactive()
    return (twin + 1) % cfg.TWINS
end

local function upload()
    vbuf.update()
    ibuf.update()
    tex.update()
    if upload_state == 'copying' then
        vbuf.update_copy(twin_inactive())
        ibuf.update_copy(twin_inactive())
        tex.update_copy(twin_inactive())
        if util.reduce_and(function(x) return x.sync_copy_ready() end, {vbuf, ibuf, tex})
        and util.reduce_or(function(x) return x.need_sync() end, {vbuf, ibuf, tex})
        then
            upload_count = upload_count + 1
            if upload_count >= UPLOAD_THRESH then
                upload_count = 0
                upload_state = 'synching'
                sync = coresync.alloc()
            end
        else
            upload_count = 0
        end
    elseif upload_state == 'synching' then
        if sync.ready() or upload_count >= UPLOAD_THRESH then
            upload_count = 0
            vbuf.sync_copy()
            ibuf.sync_copy()
            tex.sync_copy()
            twin = twin_inactive()
            sync.free()
            sync = nil
            upload_state = 'copying'
        else
            upload_count = upload_count + 1
        end
    end
end

function M.init()
end

function M.done()
    if sync then
        sync.free()
    end
end

function M.mesh_draw(group, draw_tag)
    api_mesh_draw(group.twin(twin_active()), draw_tag)
end

function M.mesh_update(group, dt, update_tag)
    api_mesh_update(group.twin(twin_active()), dt, update_tag)
end

function M.finish_frame(prof)
    prof.cpu.rupload.start()
    prof.gpu.rupload.start()
    upload()
    prof.gpu.rupload.finish()
    prof.cpu.rupload.finish()

    prof.cpu.rswap.start()
    prof.gpu.rswap.start()
    api_render_swap()
    prof.gpu.rswap.finish()
    prof.cpu.rswap.finish()
end

return M
