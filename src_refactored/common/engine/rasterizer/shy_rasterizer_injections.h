#ifndef _shy_common_engine_rasterizer_injections_included
#define _shy_common_engine_rasterizer_injections_included

#include "./message/draw_ellipse_in_rect/shy_draw_ellipse_in_rect_injections.h"
#include "./message/draw_rect/shy_draw_rect_injections.h"
#include "./message/draw_triangle/shy_draw_triangle_injections.h"
#include "./message/finalize_request/shy_finalize_request_injections.h"
#include "./message/init/shy_init_injections.h"
#include "./message/use_texel/shy_use_texel_injections.h"
#include "./message/use_texture/shy_use_texture_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_rasterizer.h"

typedef shy_common_engine_rasterizer_scheduled so_called_common_engine_rasterizer ;

#endif
