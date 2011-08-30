#ifndef _shy_common_logic_core_injections_included
#define _shy_common_logic_core_injections_included

#include "common/logic/core/message/near_plane_distance_request/shy_near_plane_distance_request_injections.h"
#include "common/logic/core/message/use_ortho_projection_request/shy_use_ortho_projection_request_injections.h"
#include "common/logic/core/message/use_perspective_projection_request/shy_use_perspective_projection_request_injections.h"

#include "common/logic/fidget/message/prepared/shy_prepared_injections.h"

#include "common/engine/render/message/aspect_reply/shy_aspect_reply_injections.h"

#include "common/message/init/shy_init_injections.h"
#include "common/message/render/shy_render_injections.h"
#include "common/message/update/shy_update_injections.h"
#include "common/message/video_mode_changed/shy_video_mode_changed_injections.h"

#include "injections/platform/scheduler/shy_scheduler.h"

#include "./shy_core.h"

typedef shy_common_logic_core_scheduled so_called_common_logic_core ;

#endif
