#ifndef _shy_common_logic_game_injections_included
#define _shy_common_logic_game_injections_included

#include "../camera/message/matrix_reply/shy_matrix_reply_injections.h"
#include "../camera/message/prepared/shy_prepared_injections.h"
#include "../core/message/near_plane_distance_reply/shy_near_plane_distance_reply_injections.h"
#include "../core/message/use_ortho_projection_reply/shy_use_ortho_projection_reply_injections.h"
#include "../core/message/use_perspective_projection_reply/shy_use_perspective_projection_reply_injections.h"
#include "../entities/message/prepared/shy_prepared_injections.h"
#include "../entities/message/render_reply/shy_render_reply_injections.h"
#include "../fidget/message/render_reply/shy_render_reply_injections.h"
#include "../land/message/prepared/shy_prepared_injections.h"
#include "../land/message/render_reply/shy_render_reply_injections.h"
#include "../sound/message/prepared/shy_prepared_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_game.h"

typedef shy_common_logic_game_scheduled so_called_common_logic_game ;

#endif
