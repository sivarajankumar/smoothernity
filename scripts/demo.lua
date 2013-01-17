demo = {}

function demo.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, axis, angle)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, px, py, pz, 0)
    api_vector_const(scl, sx, sy, sz, 0)
    api_vector_const(rot, angle, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, axis, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

function demo.matrix_pos_stop(x, y, z)
    return demo.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, API_MATRIX_AXIS_X, 0)
end

function demo.matrix_pos_scl_stop(px, py, pz, sx, sy, sz)
    return demo.matrix_pos_scl_rot_stop(px, py, pz, sx, sy, sz, API_MATRIX_AXIS_X, 0)
end

function demo.matrix_pos_rot_stop(x, y, z, axis, angle)
    return demo.matrix_pos_scl_rot_stop(x, y, z, 1, 1, 1, axis, angle)
end

function demo.matrix_rot_stop(axis, angle)
    return demo.matrix_pos_scl_rot_stop(0, 0, 0, 1, 1, 1, axis, angle)
end

function demo.matrix_scl_stop(sx, sy, sz)
    local m = api_matrix_alloc()
    local pos = api_vector_alloc()
    local scl = api_vector_alloc()
    local rot = api_vector_alloc()
    api_vector_const(pos, 0, 0, 0, 0)
    api_vector_const(scl, sx, sy, sz, 0)
    api_vector_const(rot, 0, 0, 0, 0)
    api_matrix_pos_scl_rot(m, pos, scl, rot, API_MATRIX_AXIS_X, 0)
    api_matrix_stop(m)
    api_vector_free(pos)
    api_vector_free(scl)
    api_vector_free(rot)
    return m
end

function demo.matrix_move(m, x, y, z)
    local dm = demo.matrix_pos_stop(x, y, z)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

function demo.matrix_rotate(m, axis, angle)
    local dm = demo.matrix_rot_stop(axis, angle)
    api_matrix_mul_stop(m, m, dm)
    api_matrix_free(dm)
end

CAR_CAMERA_CORD_MIN = 20
CAR_CAMERA_CORD_MAX = 20
CAR_CAMERA_FROM_OFFSET_Y = 5
CAR_CAMERA_FROM_RUBBER_Y = 0.01
CAR_CAMERA_FROM_RUBBER_XZ = 0.1
CAR_CAMERA_TO_OFFSET_Y = 1
CAR_CAMERA_TO_RUBBER_Y = 0.1
CAR_CAMERA_TO_RUBBER_XZ = 0.1

function demo.cord_camera_create(x, y, z, mtarget)
    local obj = {}
    function obj.construct(self, x, y, z, mtarget)
        local mcam = api_matrix_alloc()
        local mcaminv = api_matrix_alloc()
        local vcar_center = api_vector_alloc()
        local vcar_center_xz = api_vector_alloc()
        local vcam_to = api_vector_alloc()
        local vcam_to_smooth = api_vector_alloc()
        local vcam_to_rubber = api_vector_alloc()
        local vcam_to_y = api_vector_alloc()
        local vcam_to_ofs = api_vector_alloc()
        local vcam_from = api_vector_alloc()
        local vcam_from_smooth = api_vector_alloc()
        local vcam_from_rubber = api_vector_alloc()
        local vcam_from_xz = api_vector_alloc()
        local vcam_from_y = api_vector_alloc()
        local vcam_from_ofs = api_vector_alloc()
        local vcam_ofs_weights = api_vector_alloc()
        local vzero = api_vector_alloc()
        local vup = api_vector_alloc()

        api_vector_const(vzero, 0, 0, 0, 0)
        api_vector_const(vup, 0, 1, 0, 0)
        api_vector_const(vcam_from_ofs, 0, CAR_CAMERA_FROM_OFFSET_Y, 0, 0)
        api_vector_const(vcam_to_ofs, 0, CAR_CAMERA_TO_OFFSET_Y, 0, 0)
        api_vector_const(vcam_ofs_weights, 1, 1, 0, 0)
        api_vector_const(vcam_from_rubber, CAR_CAMERA_FROM_RUBBER_XZ,
                                           CAR_CAMERA_FROM_RUBBER_Y,
                                           CAR_CAMERA_FROM_RUBBER_XZ, 0)
        api_vector_const(vcam_to_rubber, CAR_CAMERA_TO_RUBBER_XZ,
                                         CAR_CAMERA_TO_RUBBER_Y,
                                         CAR_CAMERA_TO_RUBBER_XZ, 0)

        api_vector_mpos(vcar_center, mtarget)
        api_vector_pick(vcar_center_xz, vcar_center, vzero, vcar_center, vzero)

        api_vector_const(vcam_from_xz, x, 0, z, 0)
        api_vector_cord(vcam_from_xz, vcar_center_xz, CAR_CAMERA_CORD_MIN, CAR_CAMERA_CORD_MAX)
        api_vector_wsum(vcam_from_y, vcam_ofs_weights, vcar_center, vcam_from_ofs, vzero, vzero)
        api_vector_pick(vcam_from, vcam_from_xz, vcam_from_y, vcam_from_xz, vzero)
        api_vector_rubber(vcam_from_smooth, vcam_from, vcam_from_rubber)

        api_vector_wsum(vcam_to_y, vcam_ofs_weights, vcar_center, vcam_to_ofs, vzero, vzero)
        api_vector_pick(vcam_to, vcar_center_xz, vcam_to_y, vcar_center_xz, vzero)
        api_vector_rubber(vcam_to_smooth, vcam_to, vcam_to_rubber)

        api_matrix_from_to_up(mcam, vcam_from_smooth, vcam_to_smooth, vup)

        api_matrix_inv(mcaminv, mcam)
        api_display_camera(mcaminv)

        self.mcam = mcam
        self.mcaminv = mcaminv
        self.vcar_center = vcar_center
        self.vcar_center_xz = vcar_center_xz
        self.vcam_to = vcam_to
        self.vcam_to_smooth = vcam_to_smooth
        self.vcam_to_rubber = vcam_to_rubber
        self.vcam_to_y = vcam_to_y
        self.vcam_to_ofs = vcam_to_ofs
        self.vcam_from = vcam_from
        self.vcam_from_smooth = vcam_from_smooth
        self.vcam_from_rubber = vcam_from_rubber
        self.vcam_from_xz = vcam_from_xz
        self.vcam_from_y = vcam_from_y
        self.vcam_from_ofs = vcam_from_ofs
        self.vcam_ofs_weights = vcam_ofs_weights
        self.vzero = vzero
        self.vup = vup
    end
    function obj.destruct(self)
        api_matrix_free(self.mcam)
        api_matrix_free(self.mcaminv)
        api_vector_free(self.vcar_center)
        api_vector_free(self.vcar_center_xz)
        api_vector_free(self.vcam_to)
        api_vector_free(self.vcam_to_smooth)
        api_vector_free(self.vcam_to_rubber)
        api_vector_free(self.vcam_to_y)
        api_vector_free(self.vcam_to_ofs)
        api_vector_free(self.vcam_from)
        api_vector_free(self.vcam_from_smooth)
        api_vector_free(self.vcam_from_rubber)
        api_vector_free(self.vcam_from_xz)
        api_vector_free(self.vcam_from_y)
        api_vector_free(self.vcam_from_ofs)
        api_vector_free(self.vcam_ofs_weights)
        api_vector_free(self.vzero)
        api_vector_free(self.vup)
    end
    obj:construct(x, y, z, mtarget)
    return obj
end

function demo.free_camera_create(x, y, z)
    local obj = {}
    obj.matrix = demo.matrix_pos_stop(x, y, z)
    obj.invmatrix = api_matrix_alloc()
    function obj.destruct(self)
        api_matrix_free(self.matrix)
        api_matrix_free(self.invmatrix)
    end
    function obj.update(self)
        local ofs = 0.25
        local ang = 0.02
        if api_input_key(API_INPUT_KEY_LSHIFT) == 1 then
            ofs = 0.05
            ang = 0.01
        end
    
        if api_input_key(API_INPUT_KEY_E) == 1 then
            demo.matrix_move(self.matrix, 0, 0, -ofs)
        end
        if api_input_key(API_INPUT_KEY_D) == 1 then
            demo.matrix_move(self.matrix, 0, 0, ofs)
        end
        if api_input_key(API_INPUT_KEY_S) == 1 then
            demo.matrix_move(self.matrix, -ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_F) == 1 then
            demo.matrix_move(self.matrix, ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_A) == 1 then
            demo.matrix_move(self.matrix, 0, ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_Z) == 1 then
            demo.matrix_move(self.matrix, 0, -ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_LEFT) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Y, ang)
        end
        if api_input_key(API_INPUT_KEY_RIGHT) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Y, -ang)
        end
        if api_input_key(API_INPUT_KEY_UP) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_X, ang)
        end
        if api_input_key(API_INPUT_KEY_DOWN) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_X, -ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEUP) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Z, ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEDOWN) == 1 then
            demo.matrix_rotate(self.matrix, API_MATRIX_AXIS_Z, -ang)
        end
    end

    api_matrix_inv(obj.invmatrix, obj.matrix)
    api_display_camera(obj.invmatrix)

    return obj
end

CAR_CH_SIZE_X = 2
CAR_CH_SIZE_Y = 1
CAR_CH_SIZE_Z = 4
CAR_CH_MASS = 800
CAR_CH_FRICT = 0.5
CAR_CH_ROLL_FRICT = 0
CAR_SUS_STIF = 20
CAR_SUS_COMP = 4.4
CAR_SUS_DAMP = 2.3
CAR_SUS_TRAV = 500
CAR_SUS_FORCE = 6000
CAR_SUS_REST = 0.6
CAR_SLIP_FRICT = 1000
CAR_ROLL_INF = 0.1
CAR_WHEEL_RADIUS = 0.5
CAR_WHEEL_POS_X = 0.9
CAR_WHEEL_POS_Y = 0.2
CAR_WHEEL_POS_Z = 1.6
CAR_ACCEL_MAX = 1000
CAR_ACCEL_PUSH = 100
CAR_ACCEL_POP = 100
CAR_BRAKE_MAX = 100
CAR_BRAKE_PUSH = 10
CAR_BRAKE_POP = 10
CAR_STEER_MAX = 0.6
CAR_STEER_PUSH = 0.05
CAR_STEER_POP = 0.05

function demo.vehicle_create(x, y, z)
    local obj = {}
    function obj.construct_vb(self)
        local vb = api_vbuf_alloc()
        api_vbuf_set(vb, 0, -1,-1, 1,   1, 0, 0, 1,   0, 0,
                             1,-1, 1,   0, 1, 0, 1,   0, 0,
                             1, 1, 1,   0, 0, 1, 1,   0, 0,
                            -1, 1, 1,   1, 1, 1, 1,   0, 0,
                            -1,-1,-1,   0, 1, 1, 1,   0, 0,
                             1,-1,-1,   0, 0, 0, 1,   0, 0,
                             1, 1,-1,   1, 1, 0, 1,   0, 0,
                            -1, 1,-1,   1, 0, 1, 1,   0, 0)
        api_vbuf_bake(vb)
        self.vb = vb
    end
    function obj.construct_ib(self)
        local ib = api_ibuf_alloc()
        api_ibuf_set(ib, 0,  0,1,2,  0,2,3,
                             1,5,6,  1,6,2,
                             5,4,7,  5,7,6,
                             4,0,3,  4,3,7,
                             3,2,6,  3,6,7,
                             1,0,4,  1,4,5)
        api_ibuf_bake(ib)
        self.ib = ib
    end
    function obj.construct_cs(self)
        local size = api_vector_alloc()
        api_vector_const(size, 0.5*CAR_CH_SIZE_X, 0.5*CAR_CH_SIZE_Y, 0.5*CAR_CH_SIZE_Z, 0)
        self.cs = api_physics_cs_alloc_box(CAR_CH_MASS, size)
        api_vector_free(size)
    end
    function obj.construct_veh(self, x, y, z)
        local m = demo.matrix_pos_rot_stop(x, y, z, API_MATRIX_AXIS_Y, math.pi)
        self.veh = api_physics_veh_alloc(self.cs, m, CAR_CH_FRICT, CAR_CH_ROLL_FRICT,
                                         CAR_SUS_STIF, CAR_SUS_COMP, CAR_SUS_DAMP,
                                         CAR_SUS_TRAV, CAR_SUS_FORCE, CAR_SLIP_FRICT)
        api_matrix_free(m)
        self.wheel_fr = self:add_wheel( CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y, CAR_WHEEL_POS_Z, 1)
        self.wheel_fl = self:add_wheel(-CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y, CAR_WHEEL_POS_Z, 1)
        self.wheel_br = self:add_wheel( CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y,-CAR_WHEEL_POS_Z, 0)
        self.wheel_bl = self:add_wheel(-CAR_WHEEL_POS_X, CAR_WHEEL_POS_Y,-CAR_WHEEL_POS_Z, 0)
    end
    function obj.add_wheel(self, posx, posy, posz, front)
        local dir = api_vector_alloc()
        local axl = api_vector_alloc()
        local pos = api_vector_alloc()
        api_vector_const(pos, posx, posy, posz, 0)
        api_vector_const(axl, -1, 0, 0, 0)
        api_vector_const(dir, 0, -1, 0, 0)
        local wheel = api_physics_veh_add_wheel(self.veh, pos, dir, axl, CAR_SUS_REST,
                                                CAR_ROLL_INF, CAR_WHEEL_RADIUS, front)
        api_vector_free(pos)
        api_vector_free(dir)
        api_vector_free(axl)
        return wheel
    end
    function obj.construct_matrices(self)
        self.mchassis_local = demo.matrix_scl_stop(0.5*CAR_CH_SIZE_X, 0.5*CAR_CH_SIZE_Y, 0.5*CAR_CH_SIZE_Z)
        self.mchassis_physic = api_matrix_alloc()
        self.mchassis = api_matrix_alloc()
        api_matrix_vehicle_chassis(self.mchassis_physic, self.veh)
        api_matrix_mul(self.mchassis, self.mchassis_physic, self.mchassis_local)
        self.mwheel_local = demo.matrix_scl_stop(CAR_WHEEL_RADIUS, CAR_WHEEL_RADIUS, CAR_WHEEL_RADIUS)
        self.mwheel_physic = {}
        self.mwheel = {}
        for i = 0, 3 do
            self.mwheel_physic[i] = api_matrix_alloc()
            self.mwheel[i] = api_matrix_alloc()
            api_matrix_vehicle_wheel(self.mwheel_physic[i], self.veh, i)
            api_matrix_mul(self.mwheel[i], self.mwheel_physic[i], self.mwheel_local)
        end
    end
    function obj.construct_visual(self)
        self.mesh_chassis = api_mesh_alloc(API_MESH_TRIANGLES, self.vb, self.ib, -1, self.mchassis, 0, 36)
        self.mesh_wheel = {}
        for i = 0, 3 do
            self.mesh_wheel[i] = api_mesh_alloc(API_MESH_TRIANGLES, self.vb, self.ib, -1, self.mwheel[i], 0, 36)
        end
    end
    function obj.construct(self, x, y, z)
        self:construct_ib()
        self:construct_vb()
        self:construct_cs()
        self:construct_veh(x, y, z)
        self:construct_matrices()
        self:construct_visual()
    end
    function obj.destruct(self)
        for i = 0, 3 do
            api_matrix_free(self.mwheel_physic[i])
            api_matrix_free(self.mwheel[i])
            api_mesh_free(self.mesh_wheel[i])
        end
        api_mesh_free(self.mesh_chassis)
        api_matrix_free(self.mwheel_local)
        api_matrix_free(self.mchassis_local)
        api_matrix_free(self.mchassis_physic)
        api_matrix_free(self.mchassis)
        api_vbuf_free(self.vb)
        api_ibuf_free(self.ib)
        api_physics_veh_free(self.veh)
        api_physics_cs_free(self.cs)
    end
    obj.accel = 0
    obj.brake = 0
    obj.steer = 0
    function obj.update(self)
        if api_input_key(API_INPUT_KEY_I) == 1 
        and api_input_key(API_INPUT_KEY_K) == 0 then
            self.accel = self.accel + CAR_ACCEL_PUSH
            if self.accel > CAR_ACCEL_MAX then
                self.accel = CAR_ACCEL_MAX
            end
        elseif api_input_key(API_INPUT_KEY_I) == 0 
        and api_input_key(API_INPUT_KEY_K) == 1 then
            self.accel = self.accel - CAR_ACCEL_PUSH
            if self.accel < -CAR_ACCEL_MAX then
                self.accel = -CAR_ACCEL_MAX
            end
        else
            if self.accel < -CAR_ACCEL_POP then
                self.accel = self.accel + CAR_ACCEL_POP
            elseif self.accel > CAR_ACCEL_POP then
                self.accel = self.accel - CAR_ACCEL_POP
            else
                self.accel = 0
            end
        end
        if api_input_key(API_INPUT_KEY_J) == 1 
        and api_input_key(API_INPUT_KEY_L) == 0 then
            self.steer = self.steer - CAR_STEER_PUSH
            if self.steer < -CAR_STEER_MAX then
                self.steer = -CAR_STEER_MAX
            end
        elseif api_input_key(API_INPUT_KEY_J) == 0 
        and api_input_key(API_INPUT_KEY_L) == 1 then
            self.steer = self.steer + CAR_STEER_PUSH
            if self.steer > CAR_STEER_MAX then
                self.steer = CAR_STEER_MAX
            end
        else
            if self.steer < -CAR_STEER_POP then
                self.steer = self.steer + CAR_STEER_POP
            elseif self.steer > CAR_STEER_POP then
                self.steer = self.steer - CAR_STEER_POP
            else
                self.steer = 0
            end
        end
        if api_input_key(API_INPUT_KEY_SPACE) == 1 then
            self.brake = self.brake + CAR_BRAKE_PUSH
            if self.brake > CAR_BRAKE_MAX then
                self.brake = CAR_BRAKE_MAX
            end
        else
            self.brake = self.brake - CAR_BRAKE_POP
            if self.brake < 0 then
                self.brake = 0
            end
        end
        api_physics_veh_set_wheel(self.veh, self.wheel_fl, self.accel, self.brake, -self.steer)
        api_physics_veh_set_wheel(self.veh, self.wheel_fr, self.accel, self.brake, -self.steer)
        api_physics_veh_set_wheel(self.veh, self.wheel_bl, self.accel, self.brake, 0)
        api_physics_veh_set_wheel(self.veh, self.wheel_br, self.accel, self.brake, 0)
    end
    obj:construct(x, y, z)
    return obj
end
