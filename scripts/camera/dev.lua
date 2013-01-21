local M = {}

local util = require 'util'

function M.alloc(x, y, z)
    local self = {}

    local matrix = util.matrix_pos_stop(x, y, z)
    self.invmatrix = api_matrix_alloc()

    function self.free()
        api_matrix_free(matrix)
        api_matrix_free(self.invmatrix)
    end

    function self.moveto(where)
        api_matrix_copy(matrix, where)
        api_matrix_stop(matrix)
    end

    function self.update()
        local ofs = 0.25
        local ang = 0.02
        if api_input_key(API_INPUT_KEY_LSHIFT) == 1 then
            ofs = 2.5
            ang = 0.02
        end
    
        if api_input_key(API_INPUT_KEY_E) == 1 then
            util.matrix_move_local(matrix, 0, 0, -ofs)
        end
        if api_input_key(API_INPUT_KEY_D) == 1 then
            util.matrix_move_local(matrix, 0, 0, ofs)
        end
        if api_input_key(API_INPUT_KEY_S) == 1 then
            util.matrix_move_local(matrix, -ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_F) == 1 then
            util.matrix_move_local(matrix, ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_A) == 1 then
            util.matrix_move_local(matrix, 0, ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_Z) == 1 then
            util.matrix_move_local(matrix, 0, -ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_LEFT) == 1 then
            util.matrix_rotate_local(matrix, API_MATRIX_AXIS_Y, ang)
        end
        if api_input_key(API_INPUT_KEY_RIGHT) == 1 then
            util.matrix_rotate_local(matrix, API_MATRIX_AXIS_Y, -ang)
        end
        if api_input_key(API_INPUT_KEY_UP) == 1 then
            util.matrix_rotate_local(matrix, API_MATRIX_AXIS_X, ang)
        end
        if api_input_key(API_INPUT_KEY_DOWN) == 1 then
            util.matrix_rotate_local(matrix, API_MATRIX_AXIS_X, -ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEUP) == 1 then
            util.matrix_rotate_local(matrix, API_MATRIX_AXIS_Z, ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEDOWN) == 1 then
            util.matrix_rotate_local(matrix, API_MATRIX_AXIS_Z, -ang)
        end
    end

    api_matrix_inv(self.invmatrix, matrix)
    return self
end

return M
