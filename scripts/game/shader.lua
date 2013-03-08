local M = {}

local shprog = require 'shprog'

local shcolor, shdefault, shtex

function M.init()
    shcolor = shprog.alloc()
    shcolor.attach_frag(
        'uniform vec4 color;\n' ..
        'void main()\n' ..
        '{\n' ..
        '   gl_FragColor = color * gl_Color;\n' ..
        '}\n'
    )
    shcolor.link()

    shtex = shprog.alloc()
    shtex.attach_frag(
        'uniform sampler2DArray texunit;\n' ..
        'uniform vec4 texlayer;\n' ..
        'void main()\n' ..
        '{\n' ..
        '   gl_FragColor = vec4(1,1,1,1);\n' ..
        '}\n'
    )
    shtex.link()

    shdefault = shprog.alloc()
    shdefault.attach_frag(
        'void main()\n' ..
        '{\n' ..
        '   gl_FragColor = gl_Color;\n' ..
        '}\n'
    )
    shdefault.link(shdefault)
end

function M.done()
    shcolor.free()
    shtex.free()
    shdefault.free()
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
