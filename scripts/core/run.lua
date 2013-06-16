local M = {}

local log = require 'core.log'

function M.run(mod, func)
    local errmsg
    xpcall(require(mod)[func],
        function(msg)
            log.err('"%s.%s" execution failed%s',
                    mod, func, debug.traceback('', 2))
            errmsg = msg
        end)
    if errmsg ~= nil then
        error(errmsg)
    end
end

return M
