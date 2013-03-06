local M = {}

M.SCREEN_WIDTH = 1024
M.SCREEN_HEIGHT = 768
M.CAMERA_DIST = 2
M.LAND_HEIGHT = 500
M.FRAME_TIME = 1 / 60
M.TWINS = 2
M.THREAD_COUNT = 1
M.BUF_SIZE = 1048576
M.BUF_POOL = {[128] = 64, [8192] = 127}
M.VBUF_SIZE = 2097152
M.VBUF_COUNT = M.TWINS
M.VBUF_POOL = {[128] = 64, [8192] = 255}
M.IBUF_SIZE = 16777216
M.IBUF_COUNT = M.TWINS
M.IBUF_POOL = {[128] = 512, [65536] = 255}
M.PBUF_SIZE = 1048576
M.PBUF_COUNT = 1
M.PBUF_POOL = {[1048576] = 1}
M.TEX_POOL = {{8, 5}, {9, 5}, {10, 5}}
M.NOISE_SIZE = 256

return M
