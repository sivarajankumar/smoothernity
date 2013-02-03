local game = require 'game'
local cfg = require 'config'

function configure()
    return {mpool_sizes = function() return    100, 1000, 10000, 100000, 1000000, 5000000 end,
            mpool_counts = function() return 10000, 1000,  2000,      2,       2,       2 end,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            mesh_count = 1000,
            vbuf_size = math.pow(2, 13),
            vbuf_count = 1000,
            ibuf_size = math.pow(2, 16),
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
            buf_size = math.pow(2, 13),
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
