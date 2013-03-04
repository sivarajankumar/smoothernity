local game = require 'game'
local cfg = require 'config'

function configure()
    return {mpool_sizes = function() return    128,  1024,  8192, 16384, 32768, 1048576, 4194304 end,
            mpool_counts = function() return 50000, 11000,   600,   300,   100,       4,       2 end,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            mesh_count = 1000,
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
            buf_count = cfg.BUF_COUNT,
            storage_key_size = 128,
            storage_data_size = 131072,
            storage_count = 10,
            shuni_count = 1000,
            shprog_count = 10,
            sync_count = 10,
            query_count = 100,
            thread_count = cfg.THREAD_COUNT}
end

function run()
    xpcall(game.run,
        function(msg)
            io.write(string.format('Main run\n%s\nError: %s\n',
                                   debug.traceback(), msg))
        end)
end
