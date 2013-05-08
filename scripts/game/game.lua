local M = {}
local core = require 'core.core'

function M.run()
    io.write('Game run init\n')
    core.init()
    core.done()
    io.write('Game run done\n')
end

return M
