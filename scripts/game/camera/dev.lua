local M = {}

local util = require 'core.util'

function M.alloc(x, y, z)
    local self = {}

    self.matrix = util.matrix_pos_stop(x, y, z)

    function self.free()
        self.matrix.free()
    end

    function self.moveto(where)
        self.matrix.copy(where)
        self.matrix.stop()
    end

    function self.update()
        local ofs = 2
        local ang = 0.02
        if api_input_key(API_INPUT_KEY_LSHIFT) == 1 then
            ofs = 20
            ang = 0.02
        end
    
        if api_input_key(API_INPUT_KEY_E) == 1 then
            util.matrix_move_local(self.matrix, 0, 0, -ofs)
        end
        if api_input_key(API_INPUT_KEY_D) == 1 then
            util.matrix_move_local(self.matrix, 0, 0, ofs)
        end
        if api_input_key(API_INPUT_KEY_S) == 1 then
            util.matrix_move_local(self.matrix, -ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_F) == 1 then
            util.matrix_move_local(self.matrix, ofs, 0, 0)
        end
        if api_input_key(API_INPUT_KEY_A) == 1 then
            util.matrix_move_local(self.matrix, 0, ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_Z) == 1 then
            util.matrix_move_local(self.matrix, 0, -ofs, 0)
        end
        if api_input_key(API_INPUT_KEY_LEFT) == 1 then
            util.matrix_rotate_local(self.matrix, API_MATRIX_AXIS_Y, ang)
        end
        if api_input_key(API_INPUT_KEY_RIGHT) == 1 then
            util.matrix_rotate_local(self.matrix, API_MATRIX_AXIS_Y, -ang)
        end
        if api_input_key(API_INPUT_KEY_UP) == 1 then
            util.matrix_rotate_local(self.matrix, API_MATRIX_AXIS_X, ang)
        end
        if api_input_key(API_INPUT_KEY_DOWN) == 1 then
            util.matrix_rotate_local(self.matrix, API_MATRIX_AXIS_X, -ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEUP) == 1 then
            util.matrix_rotate_local(self.matrix, API_MATRIX_AXIS_Z, ang)
        end
        if api_input_key(API_INPUT_KEY_PAGEDOWN) == 1 then
            util.matrix_rotate_local(self.matrix, API_MATRIX_AXIS_Z, -ang)
        end
    end

    return self
end

return M
