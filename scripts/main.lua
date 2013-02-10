local game = require 'game'
local cfg = require 'config'

function configure()
    return {mpool_sizes = function() return    128, 1024,  8192, 16384, 32768, 1048576, 4194304 end,
            mpool_counts = function() return 10000, 1000,   500,   300,    40,       2,       2 end,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            mesh_count = 1000,
            vbuf_size = 8192,
            vbuf_count = 1000,
            ibuf_size = 65536,
            ibuf_count = 1000,
            text_size = 128,
            text_count = 100,
            vector_count = 100,
            vector_nesting = 20,
            matrix_count = 1000,
            matrix_nesting = 20,
            world_count = 2,
            colshape_count = 100,
            rigidbody_count = 100,
            vehicle_count = 10,
            buf_size = 8192,
            buf_count = 100,
            rop_count = 100,
            storage_key_size = 128,
            storage_data_size = 131072,
            storage_count = 10,
            shuni_count = 1000,
            shprog_count = 10,
            sync_count = 10}
end

function run()
    xpcall(game.run,
        function(msg)
            io.write(string.format('Main\n%s\nError: %s\n', debug.traceback(), msg))
        end)
end
