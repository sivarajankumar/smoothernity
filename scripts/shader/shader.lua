local M = {}

local shdef

function M.init()
    shdef = api_shprog_alloc()
    api_shprog_link(shdef)
end

function M.done()
    api_shprog_free(shdef)
end

function M.default()
    return shdef
end

return M
