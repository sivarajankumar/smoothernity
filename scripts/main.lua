local M = {}

local game = require 'game.game'
local cfg = require 'config'

function M.configure()
    return {
            main_mpool = function() return
                  128,  1024, 8192, 32768, 2097152,
                60000, 11000,  600,   100,      10 end,
            physics_mpool = function() return
                128,  8192, 1048576, 4194304,
                200,    50,       2,       2 end,
            thread_mpool = function() return
                128, 1024, 2048, 4096, 16384, 65536, 131072, 262144, 524288, 2097152,
              10000, 1000,  200,  200,   100,    10,      5,      5,      5,       5 end,
            thread_count = cfg.THREAD_COUNT,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            full_screen = 1,
            mesh_count = cfg.MESH_COUNT,
            vbuf_size = cfg.VBUF_SIZE,
            vbuf_count = cfg.VBUF_COUNT,
            ibuf_size = cfg.IBUF_SIZE,
            ibuf_count = cfg.IBUF_COUNT,
            pbuf_size = cfg.PBUF_SIZE,
            pbuf_count = cfg.PBUF_COUNT,
            tex = function()
                local t = {}
                for i, p in ipairs(cfg.TEX_POOL) do
                    local size, layers = unpack(p)
                    table.insert(t, size)
                    table.insert(t, layers)
                end
                return unpack(t)
            end,
            vector_count = 300,
            vector_nesting = 20,
            matrix_count = 1000,
            matrix_nesting = 20,
            world_count = 2,
            colshape_count = 100,
            rigidbody_count = 100,
            vehicle_count = 10,
            buf_size = cfg.BUF_SIZE,
            shuni_count = cfg.SHUNI_COUNT,
            shprog_count = cfg.SHPROG_COUNT,
            sync_count = cfg.SYNC_COUNT,
            query_count = cfg.QUERY_COUNT}
end

function M.run()
    xpcall(game.run,
        function(msg)
            io.write(string.format('Main run\n%s\nError: %s\n',
                                   debug.traceback(), msg))
        end)
end

return M
