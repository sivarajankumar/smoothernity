local M = {}

local shprog = require 'core.shprog'
local util = require 'core.util'

local shcolor, shdefault, shtex

function M.init()
    shcolor = shprog.alloc()
    shcolor.attach_frag(util.sync_read('./game/shader/color.fp'))
    shcolor.link()

    shtex = shprog.alloc()
    shtex.attach_frag(util.sync_read('./game/shader/tex.fp'))
    shtex.link()

    shdefault = shprog.alloc()
    shdefault.attach_frag(util.sync_read('./game/shader/default.fp'))
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
