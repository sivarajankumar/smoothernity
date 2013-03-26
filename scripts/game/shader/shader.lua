local M = {}

local shprog = require 'core.shprog'
local util = require 'core.util'

local shcolor, shdefault, shtex

function M.init()
    shcolor = shprog.alloc()
    shcolor.attach_frag(util.sync_read('./game/shader/color.frag'))
    shcolor.link()

    shtex = shprog.alloc()
    shtex.attach_frag(util.sync_read('./game/shader/tex.frag'))
    shtex.attach_vertex(util.sync_read('./game/shader/tex.vert'))
    shtex.link()

    shdefault = shprog.alloc()
    shdefault.attach_frag(util.sync_read('./game/shader/default.frag'))
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
