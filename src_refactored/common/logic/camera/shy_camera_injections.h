#ifndef _shy_common_logic_camera_injections_included
#define _shy_common_logic_camera_injections_included

#include "./message/matrix_request/shy_matrix_request_injections.h"
#include "./message/prepare_permit/shy_prepare_permit_injections.h"
#include "./message/update/shy_update_injections.h"

#include "../core/message/near_plane_distance_reply/shy_near_plane_distance_reply_injections.h"

#include "../../engine/render/message/aspect_reply/shy_aspect_reply_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_camera.h"

typedef shy_common_logic_camera_scheduled so_called_common_logic_camera ;

#endif
