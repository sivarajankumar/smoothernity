local M = {}
local corewld = require 'core.world'

function M.init()
    M.wld = corewld.alloc()
end

function M.done()
    M.wld.free()
end

return M
