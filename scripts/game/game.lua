local M = {}
local core = require 'core.core'

function M.run()
    io.write('Game run init')
    core.init()
    core.done()
    io.write('Game run done')
end

return M
