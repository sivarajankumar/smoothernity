#ifndef _shy_common_logic_entities_injections_included
#define _shy_common_logic_entities_injections_included

#include "./message/height_request/shy_height_request_injections.h"
#include "./message/mesh_grid_request/shy_mesh_grid_request_injections.h"
#include "./message/origin_request/shy_origin_request_injections.h"
#include "./message/prepare_permit/shy_prepare_permit_injections.h"
#include "./message/render_request/shy_render_request_injections.h"
#include "./message/update/shy_update_injections.h"

#include "../../engine/render/message/mesh_create_reply/shy_mesh_create_reply_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_entities.h"

typedef shy_common_logic_entities_scheduled so_called_common_logic_entities ;

#endif
