#ifndef _shy_common_logic_text_injections_included
#define _shy_common_logic_text_injections_included

#include "./message/letter_big_tex_coords_request/shy_letter_big_tex_coords_request_injections.h"
#include "./message/letter_small_tex_coords_request/shy_letter_small_tex_coords_request_injections.h"
#include "./message/prepare_permit/shy_prepare_permit_injections.h"
#include "./message/render_request/shy_render_request_injections.h"
#include "./message/update/shy_update_injections.h"
#include "./message/use_text_texture_request/shy_use_text_texture_request_injections.h"

#include "../../engine/rasterizer/message/finalize_reply/shy_finalize_reply_injections.h"
#include "../../engine/render/message/mesh_create_reply/shy_mesh_create_reply_injections.h"
#include "../../engine/render/message/texture_create_reply/shy_texture_create_reply_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_text.h"

typedef shy_common_logic_text_scheduled so_called_common_logic_text ;

#endif
