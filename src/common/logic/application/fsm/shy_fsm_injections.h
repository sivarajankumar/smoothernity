#ifndef _shy_common_logic_application_fsm_injections_included
#define _shy_common_logic_application_fsm_injections_included

#include "../message/render/shy_render_injections.h"
#include "../message/update/shy_update_injections.h"

#include "../../amusement/message/created/shy_created_injections.h"
#include "../../amusement/message/finished/shy_finished_injections.h"
#include "../../main_menu/message/created/shy_created_injections.h"
#include "../../main_menu/message/finished/shy_finished_injections.h"
#include "../../salutation/message/created/shy_created_injections.h"
#include "../../salutation/message/finished/shy_finished_injections.h"
#include "../../salutation/letters/meshes/generator/message/generate_finished/shy_generate_finished_injections.h"
#include "../../salutation/letters/text/generator/message/generate_finished/shy_generate_finished_injections.h"
#include "../../salutation/timer/disappear/message/run_finished/shy_run_finished_injections.h"
#include "../../text/message/prepared/shy_prepared_injections.h"
#include "../../title/message/created/shy_created_injections.h"
#include "../../title/message/finished/shy_finished_injections.h"

#include "../../../message/init/shy_init_injections.h"

#include "../../../../injections/platform/math/type/num_whole/shy_num_whole.h"
#include "../../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_fsm.h"

typedef shy_common_logic_application_fsm_scheduled so_called_common_logic_application_fsm ;

#endif
