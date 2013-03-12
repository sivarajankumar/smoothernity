local M = {}

local util = require 'core.util'
local pwld = require 'game.physwld'
local meshes = require 'game.meshes'
local cfg = require 'config'
local gui = require 'game.gui.gui'
local key = require 'core.key'
local shader = require 'game.shader'
local twinibuf = require 'core.twin.ibuf'
local twinvbuf = require 'core.twin.vbuf'
local twinmesh = require 'core.twin.mesh'
local colshape = require 'core.colshape'
local vehicle = require 'core.vehicle'

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
local SPEED_MIN = 30 * 1000 / 3600
local SPEED_MAX = 50 * 1000 / 3600
local SAVE_OFS_Y = 5

function M.alloc(uid, startx, starty, startz)
    local self = {}

    self.mchassis = api_matrix_alloc()
    local vb = twinvbuf.alloc(8)
    local ib = twinibuf.alloc(36)
    local cs_inert, cs_shape_box, cs_shape, veh
    local wheels, wheel_fr, wheel_fl, wheel_br, wheel_bl
    local mchassis_local = util.matrix_pos_scl_stop(0, CH_OFFSET_Y, 0,
                                      0.5*CH_SIZE_X, 0.5*CH_SIZE_Y, 0.5*CH_SIZE_Z)
    local mchassis_phys = api_matrix_alloc()
    local mwheel_local = util.matrix_scl_stop(WHEEL_RADIUS, WHEEL_RADIUS, WHEEL_RADIUS)
    local mwheel_physic = {}
    local mwheel = {}
    local mrecov_next = api_matrix_alloc()
    local mrecov = api_matrix_alloc()
    local mesh_chassis
    local mesh_wheel = {}
    local accel, brake, steer = 0, 0, 0
    local recov_frames = 0
    local recov_pressed = 0
    local freedom = 1
    local freedom_speed = 1
    local freedom_move = 1
    local vpos = api_vector_alloc()
    local cruise = false
    local cruise_key = key.alloc(function() return API_INPUT_KEY_C end,
                                 function() cruise = not cruise end,
                                 function() end)

    function self.free()
        for i, w in pairs(wheels) do
            api_matrix_free(mwheel_physic[i])
            api_matrix_free(mwheel[i])
            mesh_wheel[i].free()
        end
        mesh_chassis.free()
        api_matrix_free(mwheel_local)
        api_matrix_free(mchassis_local)
        api_matrix_free(mchassis_phys)
        api_matrix_free(self.mchassis)
        api_matrix_free(mrecov_next)
        api_matrix_free(mrecov)
        api_vector_free(vpos)
        vb.free()
        ib.free()
        veh.free()
        cs_shape_box.free()
        cs_shape.free()
        cs_inert.free()
    end

    function self.move(vofs)
        local x, y, z, w = api_vector_get(vofs)
        util.matrix_move_global(mrecov, x, y, z)
        util.matrix_move_global(mrecov_next, x, y, z)
        util.vector_move(vpos, vofs)
    end

    function self.restrain(value)
        freedom_move = value
    end

    function self.save(wld)
        local vfrom = api_vector_alloc()
        local vto = api_vector_alloc()
        local mfwd = util.matrix_pos_stop(0, 0, -1)
        local mto = api_matrix_alloc()
        api_matrix_mul(mto, self.mchassis, mfwd)
        api_vector_mpos(vfrom, self.mchassis)
        api_vector_update(vfrom, 0, API_VECTOR_FORCED_UPDATE)
        api_vector_mpos(vto, mto)
        api_vector_update(vto, 0, API_VECTOR_FORCED_UPDATE)
        local fx, fy, fz = api_vector_get(vfrom)
        local tx, ty, tz = api_vector_get(vto)
        local wx, wy, wz = wld.scene_to_world(fx, fy, fz)
        wy = wld.height(wz, wx) + SAVE_OFS_Y
        local sx, sy, sz = wld.world_to_scene(wx, wy, wz)
        util.async_write(util.uid_save(string.format('%s.lua', uid)),
            string.format('return %f, %f, %f, %f, %f, %f', fx,sy,fz, tx,sy,tz))
        api_vector_free(vfrom)
        api_vector_free(vto)
        api_matrix_free(mfwd)
        api_matrix_free(mto)
    end

    function self.update()
        -- restrict speed
        do
            local vprev = api_vector_alloc()
            util.vector_copy(vprev, vpos)
            api_vector_mpos(vpos, self.mchassis)
            api_vector_update(vpos, 0, API_VECTOR_FORCED_UPDATE)
            local speed = util.vector_dist(vprev, vpos) / cfg.FRAME_TIME
            freedom_speed = util.lerp(speed, SPEED_MIN, SPEED_MAX, 1, 0)
            api_vector_free(vprev)
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
                api_matrix_copy(mrecov, mrecov_next)
                api_matrix_copy(mrecov_next, mchassis_phys)
                api_matrix_update(mrecov_next, 0, API_MATRIX_FORCED_UPDATE)
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
        local dir = api_vector_alloc()
        local axl = api_vector_alloc()
        local pos = api_vector_alloc()
        api_vector_const(pos, posx, posy, posz, 0)
        api_vector_const(axl, -1, 0, 0, 0)
        api_vector_const(dir, 0, -1, 0, 0)
        local wheel = veh.add_wheel(pos, dir, axl, SUS_REST,
                                    ROLL_INF, WHEEL_RADIUS, front)
        api_vector_free(pos)
        api_vector_free(dir)
        api_vector_free(axl)
        return wheel
    end

    -- vertex buffer
    do
        vb.prepare()
        vb.set(0,  -1,-1, 1,   1, 0, 0, 1,   0, 0,
                    1,-1, 1,   0, 1, 0, 1,   0, 0,
                    1, 1, 1,   0, 0, 1, 1,   0, 0,
                   -1, 1, 1,   1, 1, 1, 1,   0, 0,
                   -1,-1,-1,   0, 1, 1, 1,   0, 0,
                    1,-1,-1,   0, 0, 0, 1,   0, 0,
                    1, 1,-1,   1, 1, 0, 1,   0, 0,
                   -1, 1,-1,   1, 0, 1, 1,   0, 0)
        vb.finalize()
    end

    -- index buffer
    do
        local o = vb.start
        ib.prepare()
        ib.set(0,   o+0,o+1,o+2,  o+0,o+2,o+3,
                    o+1,o+5,o+6,  o+1,o+6,o+2,
                    o+5,o+4,o+7,  o+5,o+7,o+6,
                    o+4,o+0,o+3,  o+4,o+3,o+7,
                    o+3,o+2,o+6,  o+3,o+6,o+7,
                    o+1,o+0,o+4,  o+1,o+4,o+5)
        ib.finalize()
    end

    -- collision shape
    do
        local size = api_vector_alloc()
        local ofs = util.matrix_pos_stop(0, CH_OFFSET_Y, 0)
        api_vector_const(size, 0.5*CH_SIZE_X, 0.5*CH_SIZE_Y, 0.5*CH_SIZE_Z, 0)
        cs_inert = colshape.alloc_box(size)
        cs_shape_box = colshape.alloc_box(size)
        cs_shape = colshape.alloc_comp()
        cs_shape.comp_add(ofs, cs_shape_box)
        api_vector_free(size)
        api_matrix_free(ofs)
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
        api_matrix_free(m)
        wheel_fr = add_wheel( WHEEL_POS_X, WHEEL_POS_Y, WHEEL_POS_Z, 1)
        wheel_fl = add_wheel(-WHEEL_POS_X, WHEEL_POS_Y, WHEEL_POS_Z, 1)
        wheel_br = add_wheel( WHEEL_POS_X, WHEEL_POS_Y,-WHEEL_POS_Z, 0)
        wheel_bl = add_wheel(-WHEEL_POS_X, WHEEL_POS_Y,-WHEEL_POS_Z, 0)
        wheels = {wheel_fr, wheel_fl, wheel_bl, wheel_br}
    end

    -- matrices
    do
        api_matrix_vehicle_chassis(mchassis_phys, veh.id())
        api_matrix_mul(self.mchassis, mchassis_phys, mchassis_local)
        for i, w in pairs(wheels) do
            mwheel_physic[i] = api_matrix_alloc()
            mwheel[i] = api_matrix_alloc()
            api_matrix_vehicle_wheel(mwheel_physic[i], veh.id(), w.id())
            api_matrix_mul(mwheel[i], mwheel_physic[i], mwheel_local)
        end
        api_matrix_copy(mrecov, mchassis_phys)
        api_matrix_update(mrecov, 0, API_MATRIX_FORCED_UPDATE)
        api_matrix_stop(mrecov)
        api_vector_mpos(vpos, self.mchassis)
        api_vector_update(vpos, 0, API_VECTOR_FORCED_UPDATE)
    end

    -- visual
    do
        mesh_chassis = twinmesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                                      shader.default(), self.mchassis)
        for i, w in pairs(wheels) do
            mesh_wheel[i] = twinmesh.alloc(meshes.GROUP_NEAR, API_MESH_TRIANGLES, vb, ib,
                                           shader.default(), mwheel[i])
        end
    end

    return self
end

return M