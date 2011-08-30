#ifndef _shy_common_logic_main_menu_selection_tracking_director_injections_included
#define _shy_common_logic_main_menu_selection_tracking_director_injections_included

#include "common/logic/main_menu/selection/animation/message/appear_finished/shy_appear_finished_injections.h"
#include "common/logic/main_menu/selection/animation/message/select_finished/shy_select_finished_injections.h"
#include "common/logic/main_menu/selection/animation/message/unselect_finished/shy_unselect_finished_injections.h"
#include "common/logic/main_menu/selection/message/track_reply/shy_track_reply_injections.h"
#include "common/logic/main_menu/selection/message/track_row_selected/shy_track_row_selected_injections.h"
#include "common/logic/main_menu/selection/message/track_void_selected/shy_track_void_selected_injections.h"
#include "common/logic/main_menu/selection/message/tracking_director_update/shy_tracking_director_update_injections.h"

#include "common/message/init/shy_init_injections.h"

#include "injections/platform/scheduler/shy_scheduler.h"

#include "./shy_tracking_director.h"

typedef shy_common_logic_main_menu_selection_tracking_director_scheduled so_called_common_logic_main_menu_selection_tracking_director ;

#endif
