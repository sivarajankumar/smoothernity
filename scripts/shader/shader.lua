local M = {}

local util = require 'util'

local vcolor, shprog, shuni

function M.init()
    shprog = api_shprog_alloc()
    api_shprog_attach(shprog, API_SHPROG_FRAGMENT,
        'uniform vec4 color;\n' ..
        'void main()\n' ..
        '{\n' ..
        '   gl_FragColor = color * gl_Color;\n' ..
        '}\n'
    )
    api_shprog_link(shprog)
    vcolor = util.vector_const(1, 1, 1, 1)
    shuni = api_shuni_alloc_vector(shprog, API_SHUNI_ALL_MESHES, 'color', vcolor)
end

function M.done()
    api_shprog_free(shprog)
    api_vector_free(vcolor)
    api_shuni_free(shuni)
end

function M.default()
    return shprog
end

return M
