local M = {}

local util = require 'util'

local shcolor, shdefault, shtex

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

    shtex = api_shprog_alloc()
    api_shprog_attach(shtex, API_SHPROG_FRAGMENT,
        'uniform sampler2DArray texunit;\n' ..
        'uniform vec4 texlayer;\n' ..
        'void main()\n' ..
        '{\n' ..
        '   gl_FragColor = vec4(1,1,1,1);\n' ..
        '}\n'
    )
    api_shprog_link(shtex)

    shdefault = api_shprog_alloc()
    api_shprog_attach(shdefault, API_SHPROG_FRAGMENT,
        'void main()\n' ..
        '{\n' ..
        '   gl_FragColor = gl_Color;\n' ..
        '}\n'
    )
    api_shprog_link(shdefault)
end

function M.done()
    api_shprog_free(shcolor)
    api_shprog_free(shtex)
    api_shprog_free(shdefault)
end

function M.default()
    return shdefault
end

function M.color()
    return shcolor
end

function M.texture()
    return shtex
end

return M
