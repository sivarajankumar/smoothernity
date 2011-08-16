#ifndef _shy_common_logic_image_injections_included
#define _shy_common_logic_image_injections_included

#include "./message/prepare_permit/shy_prepare_permit_injections.h"
#include "./message/render_request/shy_render_request_injections.h"
#include "./message/update/shy_update_injections.h"

#include "../../engine/render/message/mesh_create_reply/shy_mesh_create_reply_injections.h"
#include "../../engine/render/message/texture_create_reply/shy_texture_create_reply_injections.h"
#include "../../engine/render/message/texture_loader_ready_reply/shy_texture_loader_ready_reply_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_image.h"

typedef shy_common_logic_image_scheduled so_called_common_logic_image ;

#endif
