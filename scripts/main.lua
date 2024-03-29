local M = {}

local cfg = require 'config'
local buf = require 'core.pool.buf'

function M.configure()
    return {
            main_mpool = function() return
                  128,  1024, 8192, 32768, 2097152,
               200000, 12000,  600,   100,      10 end,
            physics_mpool = function() return
                128,  8192, 1048576, 4194304,
                200,    50,       2,       2 end,
            thread_mpool = function() return
                128, 1024, 2048, 4096, 16384, 65536, 131072, 262144, 524288, 2097152,
              70000, 2000,  200,  200,   400,    40,     10,      5,      5,       5 end,
            thread_count = cfg.THREAD_COUNT,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            full_screen = 1,
            vector_count = cfg.VECTOR_COUNT,
            vector_nesting = 20,
            matrix_count = cfg.MATRIX_COUNT,
            matrix_nesting = 20,
            world_count = cfg.WORLD_COUNT,
            colshape_count = cfg.COLSHAPE_COUNT,
            rigidbody_count = cfg.RIGIDBODY_COUNT,
            vehicle_count = cfg.VEHICLE_COUNT,
            buf_size = buf.size(),
            prog_count = cfg.PROG_COUNT,
            rbuf_count = cfg.RBUF_COUNT,
            vao_count = cfg.VAO_COUNT}
end

function M.run()
    require('core.run').run('game.game', 'run')
end

return M
