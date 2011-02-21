#ifndef _shy_common_logic_application_fsm_injections_included
#define _shy_common_logic_application_fsm_injections_included

#include "../message/render/shy_render_injections.h"
#include "../message/update/shy_update_injections.h"

#include "../../amusement/message/created/shy_created_injections.h"
#include "../../amusement/message/finished/shy_finished_injections.h"
#include "../../text/message/prepared/shy_prepared_injections.h"
#include "../../title/message/created/shy_created_injections.h"
#include "../../title/message/finished/shy_finished_injections.h"

#include "../../../message/init/shy_init_injections.h"

#include "../../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_fsm.h"

typedef shy_common_logic_application_fsm_scheduled so_called_common_logic_application_fsm ;

#endif
