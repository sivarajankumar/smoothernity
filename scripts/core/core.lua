local M = {}

local world = require 'core.world'
local rigidbody = require 'core.rigidbody'
local colshape = require 'core.colshape'
local vehicle = require 'core.vehicle'
local matrix = require 'core.matrix'
local vector = require 'core.vector'
local query = require 'core.query'
local mesh = require 'core.mesh'
local tex = require 'core.tex'
local shprog = require 'core.shprog'
local shuni = require 'core.shuni'
local thread = require 'core.thread'
local sync = require 'core.sync'
local key = require 'core.key'
local buf = require 'core.pool.buf'
local pbuf = require 'core.pool.pbuf'
local render = require 'core.render.render'
local ibuf = require 'core.render.ibuf'
local vbuf = require 'core.render.vbuf'

function M.init()
    matrix.init()
    vector.init()
    world.init()
    vehicle.init()
    colshape.init()
    rigidbody.init()
    shprog.init()
    shuni.init()
    mesh.init()
    query.init()
    sync.init()
    thread.init()
    buf.init()
    pbuf.init()
    ibuf.init()
    vbuf.init()
    tex.init()
    render.init()
end

function M.done()
    matrix.done()
    vector.done()
    world.done()
    vehicle.done()
    colshape.done()
    rigidbody.done()
    shprog.done()
    shuni.done()
    mesh.done()
    query.done()
    sync.done()
    thread.done()
    buf.done()
    pbuf.done()
    ibuf.done()
    vbuf.done()
    tex.done()
    render.done()
end

return M
