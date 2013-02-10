local M = {}

local util = require 'util'

local shcolor, shdefault

function M.init()
    shcolor = api_shprog_alloc()
    api_shprog_attach(shcolor, API_SHPROG_FRAGMENT,
        'uniform vec4 color;\n' ..
        'void main()\n' ..
        '{\n' ..
        '   gl_FragColor = color * gl_Color;\n' ..
        '}\n'
    )
    api_shprog_link(shcolor)
    shdefault = api_shprog_alloc()
    api_shprog_link(shdefault)
end

function M.done()
    api_shprog_free(shcolor)
    api_shprog_free(shdefault)
end

function M.default()
    return shdefault
end

function M.color()
    return shcolor
end

return M
