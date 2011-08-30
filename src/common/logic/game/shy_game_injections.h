#ifndef _shy_common_logic_game_injections_included
#define _shy_common_logic_game_injections_included

#include "common/logic/game/message/launch_permit/shy_launch_permit_injections.h"
#include "common/logic/game/message/render/shy_render_injections.h"
#include "common/logic/game/message/update/shy_update_injections.h"

#include "common/logic/camera/message/matrix_reply/shy_matrix_reply_injections.h"
#include "common/logic/camera/message/prepared/shy_prepared_injections.h"
#include "common/logic/core/message/near_plane_distance_reply/shy_near_plane_distance_reply_injections.h"
#include "common/logic/core/message/use_ortho_projection_reply/shy_use_ortho_projection_reply_injections.h"
#include "common/logic/core/message/use_perspective_projection_reply/shy_use_perspective_projection_reply_injections.h"
#include "common/logic/entities/message/prepared/shy_prepared_injections.h"
#include "common/logic/entities/message/render_reply/shy_render_reply_injections.h"
#include "common/logic/fidget/message/render_reply/shy_render_reply_injections.h"
#include "common/logic/image/message/prepared/shy_prepared_injections.h"
#include "common/logic/image/message/render_reply/shy_render_reply_injections.h"
#include "common/logic/land/message/prepared/shy_prepared_injections.h"
#include "common/logic/land/message/render_reply/shy_render_reply_injections.h"
#include "common/logic/sound/message/prepared/shy_prepared_injections.h"
#include "common/logic/text/message/render_reply/shy_render_reply_injections.h"
#include "common/logic/touch/message/prepared/shy_prepared_injections.h"

#include "common/message/init/shy_init_injections.h"

#include "injections/platform/scheduler/shy_scheduler.h"

#include "./shy_game.h"

typedef shy_common_logic_game_scheduled so_called_common_logic_game ;

#endif
