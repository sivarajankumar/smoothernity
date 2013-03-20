local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local meshes = require 'game.meshes'
local cfg = require 'config'
local gui = require 'game.gui.gui'
local key = require 'core.key'
local shader = require 'game.shader'
local render = require 'core.render.render'
local mesh = require 'core.render.mesh'
local colshape = require 'core.colshape'
local vehicle = require 'core.vehicle'
local matrix = require 'core.matrix'
local vector = require 'core.vector'

local CH_OFFSET_Y = 1.0
local CH_SIZE_X = 2
local CH_SIZE_Y = 1
local CH_SIZE_Z = 4
local CH_MASS = 800
local CH_FRICT = 1
local CH_ROLL_FRICT = 1
local SUS_STIF = 20
local SUS_COMP = 4.4
local SUS_DAMP = 2.3
local SUS_TRAV = 500
local SUS_FORCE = 100000
local SUS_REST = 0.6
local SLIP_FRICT = 2
local ROLL_INF = 0.1
local WHEEL_RADIUS = 0.5
local WHEEL_POS_X = 1
local WHEEL_POS_Y = 1
local WHEEL_POS_Z = 2
local ACCEL_MAX = 5000
local ACCEL_PUSH = 100
local ACCEL_POP = 100
local BRAKE_MAX = 1000
local BRAKE_PUSH = 100
local BRAKE_POP = 100
local BRAKE_RESTRAIN = 200
local STEER_MAX = 0.6
local STEER_PUSH = 0.05
local STEER_POP = 0.05
local RECOVERY_FRAMES = 10
local RECOVERY_OFS_Y = 1
local FREEDOM_RUBBER = 1
local SPEED_MIN = 100 * 1000 / 3600
local SPEED_MAX = 150 * 1000 / 3600
local SAVE_OFS_Y = 5

function M.alloc(uid, startx, starty, startz)
    local self = {}

    self.mchassis = matrix.alloc()
    local vb = render.vbuf_alloc(8)
    local ib = render.ibuf_alloc(36, vb)
    local cs_inert, cs_shape_box, cs_shape, veh
    local wheels, wheel_fr, wheel_fl, wheel_br, wheel_bl
    local mchassis_local = util.matrix_pos_scl_stop(0, CH_OFFSET_Y, 0,
                                      0.5*CH_SIZE_X, 0.5*CH_SIZE_Y, 0.5*CH_SIZE_Z)
    local mchassis_phys = matrix.alloc()
    local mwheel_local = util.matrix_scl_stop(WHEEL_RADIUS, WHEEL_RADIUS, WHEEL_RADIUS)
    local mwheel_physic = {}
    local mwheel = {}
    local mrecov_next = matrix.alloc()
    local mrecov = matrix.alloc()
    local mesh_chassis
    local mesh_wheel = {}
    local accel, brake, steer = 0, 0, 0
    local recov_frames = 0
    local recov_pressed = 0
    local freedom = 1
    local freedom_speed = 1
    local freedom_move = 1
    local vpos = vector.alloc()
    local cruise = false
    local cruise_key = key.alloc(function() return API_INPUT_KEY_C end,
                                 function() cruise = not cruise end,
                                 function() end)

    function self.free()
        for i, w in pairs(wheels) do
            mwheel_physic[i].free()
            mwheel[i].free()
            mesh_wheel[i].free()
        end
        mesh_chassis.free()
        mwheel_local.free()
        mchassis_local.free()
        mchassis_phys.free()
        self.mchassis.free()
        mrecov_next.free()
        mrecov.free()
        vpos.free()
        vb.free()
        ib.free()
        veh.free()
        cs_shape_box.free()
        cs_shape.free()
        cs_inert.free()
    end

    function self.move(vofs)
        local x, y, z, w = vofs.get()
        util.matrix_move_global(mrecov, x, y, z)
        util.matrix_move_global(mrecov_next, x, y, z)
        util.vector_move(vpos, vofs)
    end

    function self.restrain(value)
        freedom_move = value
    end

    function self.save(wld)
        local vfrom = vector.alloc()
        local vto = vector.alloc()
        local mfwd = util.matrix_pos_stop(0, 0, -1)
        local mto = matrix.alloc()
        mto.mul(self.mchassis, mfwd)
        vfrom.mpos(self.mchassis)
        vfrom.update(0, API_VECTOR_FORCED_UPDATE)
        vto.mpos(mto)
        vto.update(0, API_VECTOR_FORCED_UPDATE)
        local fx, fy, fz = vfrom.get()
        local tx, ty, tz = vto.get()
        local wx, wy, wz = wld.scene_to_world(fx, fy, fz)
        wy = wld.height(wz, wx) + SAVE_OFS_Y
        local sx, sy, sz = wld.world_to_scene(wx, wy, wz)
        util.async_write(util.uid_save(string.format('%s.lua', uid)),
            string.format('return %f, %f, %f, %f, %f, %f', fx,sy,fz, tx,sy,tz))
        vfrom.free()
        vto.free()
        mfwd.free()
        mto.free()
    end

    function self.update()
        -- restrict speed
        do
            local vprev = vector.alloc()
            util.vector_copy(vprev, vpos)
            vpos.mpos(self.mchassis)
            vpos.update(0, API_VECTOR_FORCED_UPDATE)
            local speed = util.vector_dist(vprev, vpos) / cfg.FRAME_TIME
            freedom_speed = util.lerp(speed, SPEED_MIN, SPEED_MAX, 1, 0)
            vprev.free()
        end

        -- update freedom
        do
            local frdest = math.min(freedom_move, freedom_speed)
            freedom = freedom + (frdest - freedom) * FREEDOM_RUBBER
            gui.player_freedom(freedom)
        end

        -- controls
        do
            if api_input_key(API_INPUT_KEY_I) == 1 
            and api_input_key(API_INPUT_KEY_K) == 0 then
                accel = accel + ACCEL_PUSH
                if accel > ACCEL_MAX then
                    accel = ACCEL_MAX
                end
            elseif api_input_key(API_INPUT_KEY_I) == 0 
            and api_input_key(API_INPUT_KEY_K) == 1 then
                accel = accel - ACCEL_PUSH
                if accel < -ACCEL_MAX then
                    accel = -ACCEL_MAX
                end
            else
                if accel < -ACCEL_POP then
                    accel = accel + ACCEL_POP
                elseif accel > ACCEL_POP then
                    accel = accel - ACCEL_POP
                else
                    accel = 0
                end
            end
            if api_input_key(API_INPUT_KEY_J) == 1 
            and api_input_key(API_INPUT_KEY_L) == 0 then
                steer = steer - STEER_PUSH
                if steer < -STEER_MAX then
                    steer = -STEER_MAX
                end
            elseif api_input_key(API_INPUT_KEY_J) == 0 
            and api_input_key(API_INPUT_KEY_L) == 1 then
                steer = steer + STEER_PUSH
                if steer > STEER_MAX then
                    steer = STEER_MAX
                end
            else
                if steer < -STEER_POP then
                    steer = steer + STEER_POP
                elseif steer > STEER_POP then
                    steer = steer - STEER_POP
                else
                    steer = 0
                end
            end
            if api_input_key(API_INPUT_KEY_SPACE) == 1 then
                brake = brake + BRAKE_PUSH
                if brake > BRAKE_MAX then
                    brake = BRAKE_MAX
                end
            else
                brake = brake - BRAKE_POP
                if brake < 0 then
                    brake = 0
                end
            end

            -- cruise control
            cruise_key.update()
            if cruise then
                accel = ACCEL_MAX
            end

            -- engage
            do
                local acc = util.lerp(freedom, 0, 1, 0, accel)
                local brk = util.lerp(freedom, 0, 1, BRAKE_RESTRAIN, 0)
                wheel_fl.set(acc, brk, -steer)
                wheel_fr.set(acc, brk, -steer)
                wheel_bl.set(0, brake + brk, 0)
                wheel_br.set(0, brake + brk, 0)
            end
        end

        -- recovery
        do
            local count = 0
            count = count + wheel_fl.contact()
            count = count + wheel_fr.contact()
            count = count + wheel_bl.contact()
            count = count + wheel_br.contact()
            if count == 4 then
                recov_frames = recov_frames + 1
            else
                recov_frames = 0
            end
            if recov_frames >= RECOVERY_FRAMES then
                recov_frames = 0
                mrecov.copy(mrecov_next)
                mrecov_next.copy(mchassis_phys)
                mrecov_next.update(0, API_MATRIX_FORCED_UPDATE)
                util.matrix_move_global(mrecov_next, 0, RECOVERY_OFS_Y, 0)
            end
            if recov_pressed == 0 then
                if api_input_key(API_INPUT_KEY_R) == 1 then
                    recov_pressed = 1
                    veh.transform(mrecov)
                end
            elseif recov_pressed == 1 then
                if api_input_key(API_INPUT_KEY_R) == 0 then
                    recov_pressed = 0
                end
            end
        end
    end

    local function add_wheel(posx, posy, posz, front)
        local pos = util.vector_const(posx, posy, posz, 0)
        local dir = util.vector_const(0, -1, 0, 0)
        local axl = util.vector_const(-1, 0, 0, 0)
        local wheel = veh.add_wheel(pos, dir, axl, SUS_REST,
                                    ROLL_INF, WHEEL_RADIUS, front)
        pos.free()
        dir.free()
        axl.free()
        return wheel
    end

    -- buffers
    do
        util.wait_state(true, 'prepared', vb, ib)
        vb.set(0,  -1,-1, 1,   1, 0, 0, 1,   0, 0,
                    1,-1, 1,   0, 1, 0, 1,   0, 0,
                    1, 1, 1,   0, 0, 1, 1,   0, 0,
                   -1, 1, 1,   1, 1, 1, 1,   0, 0,
                   -1,-1,-1,   0, 1, 1, 1,   0, 0,
                    1,-1,-1,   0, 0, 0, 1,   0, 0,
                    1, 1,-1,   1, 1, 0, 1,   0, 0,
                   -1, 1,-1,   1, 0, 1, 1,   0, 0)
        ib.set(0,   0,1,2,  0,2,3,
                    1,5,6,  1,6,2,
                    5,4,7,  5,7,6,
                    4,0,3,  4,3,7,
                    3,2,6,  3,6,7,
                    1,0,4,  1,4,5)

        vb.finalize()
        ib.finalize()
        util.wait_state(true, 'finalized', vb, ib)
    end

    -- collision shape
    do
        local size = util.vector_const(0.5*CH_SIZE_X, 0.5*CH_SIZE_Y, 0.5*CH_SIZE_Z, 0)
        local ofs = util.matrix_pos_stop(0, CH_OFFSET_Y, 0)
        cs_inert = colshape.alloc_box(size)
        cs_shape_box = colshape.alloc_box(size)
        cs_shape = colshape.alloc_comp()
        cs_shape.comp_add(ofs, cs_shape_box)
        size.free()
        ofs.free()
    end

    -- vehicle
    do
        local fx, fy, fz, tx, ty, tz
        local chunk = util.async_read(util.uid_save(string.format('%s.lua', uid)))
        if chunk == '' then
            fx, fy, fz = startx, starty, startz
            tx, ty, tz = startx, starty, startz - 1
        else
            fx, fy, fz, tx, ty, tz = loadstring(chunk)()
        end
        local m = util.matrix_from_to_up_stop(fx, fy, fz, tx, ty, tz, 0, 1, 0)
        veh = vehicle.alloc(pwld.wld, cs_shape, cs_inert, m, CH_MASS, CH_FRICT,
                            CH_ROLL_FRICT, SUS_STIF, SUS_COMP, SUS_DAMP,
                            SUS_TRAV, SUS_FORCE, SLIP_FRICT)
        m.free()
        wheel_fr = add_wheel( WHEEL_POS_X, WHEEL_POS_Y, WHEEL_POS_Z, 1)
        wheel_fl = add_wheel(-WHEEL_POS_X, WHEEL_POS_Y, WHEEL_POS_Z, 1)
        wheel_br = add_wheel( WHEEL_POS_X, WHEEL_POS_Y,-WHEEL_POS_Z, 0)
        wheel_bl = add_wheel(-WHEEL_POS_X, WHEEL_POS_Y,-WHEEL_POS_Z, 0)
        wheels = {wheel_fr, wheel_fl, wheel_bl, wheel_br}
    end

    -- matrices
    do
        mchassis_phys.vehicle_chassis(veh)
        self.mchassis.mul(mchassis_phys, mchassis_local)
        for i, w in pairs(wheels) do
            mwheel_physic[i] = matrix.alloc()
            mwheel_physic[i].vehicle_wheel(w)
            mwheel[i] = matrix.alloc()
            mwheel[i].mul(mwheel_physic[i], mwheel_local)
        end
        mrecov.copy(mchassis_phys)
        mrecov.update(0, API_MATRIX_FORCED_UPDATE)
        mrecov.stop()
        vpos.mpos(self.mchassis)
        vpos.update(0, API_VECTOR_FORCED_UPDATE)
    end

    -- visual
    do
        mesh_chassis = mesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                                  shader.default(), self.mchassis)
        for i, w in pairs(wheels) do
            mesh_wheel[i] = mesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                                       shader.default(), mwheel[i])
        end
    end

    return self
end

return M
