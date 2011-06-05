#ifndef _shy_common_logic_fidget_injections_included
#define _shy_common_logic_fidget_injections_included

#include "./message/prepare_permit/shy_prepare_permit_injections.h"
#include "./message/render_request/shy_render_request_injections.h"
#include "./message/update/shy_update_injections.h"

#include "../../engine/render/message/aspect_reply/shy_aspect_reply_injections.h"
#include "../../engine/render/message/frame_loss_reply/shy_frame_loss_reply_injections.h"
#include "../../engine/render/message/mesh_create_reply/shy_mesh_create_reply_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_fidget.h"

typedef shy_common_logic_fidget_scheduled so_called_common_logic_fidget ;

#endif
