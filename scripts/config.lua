local M = {}

M.SCREEN_WIDTH = 1920
M.SCREEN_HEIGHT = 1080
M.CAMERA_DIST = 2
M.LAND_HEIGHT = 500
M.FRAME_TIME = 1 / 60
M.TWINS = 1
M.COPIES = 300
M.CPU_CORES = 1
M.THREAD_COUNT = 1
M.BUF_POOL = {[128] = 64, [8192] = 255, [65536] = 32}
M.VBUF_POOL = {[128] = 64, [8192] = 255}
M.IBUF_POOL = {[128] = 512, [65536] = 255}
M.PBUF_SIZE = 1024*1024
M.PBUF_COUNT = 1
M.PBUF_POOL = {[1024*1024] = 1}
M.TEX_POOL = {[256] = 5, [512] = 5, [1024] = 5}
M.NOISE_SIZE = 256
M.QUERY_COUNT = 100
M.SYNC_COUNT = 10
M.SHPROG_COUNT = 10
M.SHUNI_COUNT = 1000
M.MESH_COUNT = 1000
M.WORLD_COUNT = 2
M.RIGIDBODY_COUNT = 100
M.COLSHAPE_COUNT = 100
M.VEHICLE_COUNT = 10
M.MATRIX_COUNT = 1000
M.VECTOR_COUNT = 300
M.SAVE_NUMS_PER_ROW = 10

return M
