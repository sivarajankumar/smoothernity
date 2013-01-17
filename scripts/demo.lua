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
