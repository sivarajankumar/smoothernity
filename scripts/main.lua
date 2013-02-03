local game = require 'game'
local cfg = require 'config'

function configure()
    return {mpool_aligns = function() return    16,   16,    16,    128,     128,    1024 end,
            mpool_sizes = function() return    128, 1024,  8192, 131072, 1048576, 4194304 end,
            mpool_counts = function() return 10000, 2000,  2000,      2,       2,       2 end,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            mesh_count = 1000,
            vbuf_size = 8192,
            vbuf_count = 1000,
            ibuf_size = 65536,
            ibuf_count = 1000,
            text_size = 100,
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
            storage_size = 100000,
            storage_count = 1}
end

function run()
    xpcall(game.run,
        function(msg)
            io.write(string.format('Main\n%s\nError: %s\n', debug.traceback(), msg))
        end)
end
