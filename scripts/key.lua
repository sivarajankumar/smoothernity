local M = {}

function M.alloc(keyfunc, pushfunc, popfunc)
    local self = {}
    local pressed = false

    function self.update()
        if pressed and api_input_key(keyfunc()) == 0 then
            pressed = false
            popfunc()
        elseif not pressed and api_input_key(keyfunc()) == 1 then
            pressed = true
            pushfunc()
        end
    end

    return self
end

return M
