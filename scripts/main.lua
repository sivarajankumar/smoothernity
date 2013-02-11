local game = require 'game'
local cfg = require 'config'

function configure()
    return {mpool_sizes = function() return    128, 1024,  8192, 16384, 32768, 1048576, 4194304 end,
            mpool_counts = function() return 20000, 4000,   500,   300,   100,       2,       2 end,
            screen_width = cfg.SCREEN_WIDTH,
            screen_height = cfg.SCREEN_HEIGHT,
            mesh_count = 1000,
            vbuf_size = cfg.VBUF_SIZE,
            vbuf_count = cfg.VBUF_COUNT,
            ibuf_size = cfg.IBUF_SIZE,
            ibuf_count = cfg.IBUF_COUNT,
            pbuf_size = 1048576,
            pbuf_count = 1,
            tex_size = 1024,
            tex_count = 1,
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
            buf_size = cfg.BUF_SIZE,
            buf_count = cfg.BUF_COUNT,
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
