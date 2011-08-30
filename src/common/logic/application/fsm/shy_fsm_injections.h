#ifndef _shy_common_logic_application_fsm_injections_included
#define _shy_common_logic_application_fsm_injections_included

#include "common/logic/application/message/render/shy_render_injections.h"
#include "common/logic/application/message/update/shy_update_injections.h"

#include "common/logic/amusement/message/created/shy_created_injections.h"
#include "common/logic/amusement/message/finished/shy_finished_injections.h"
#include "common/logic/main_menu/message/created/shy_created_injections.h"
#include "common/logic/main_menu/message/finished/shy_finished_injections.h"
#include "common/logic/salutation/letters/meshes/cleaner/clean/finished/message/shy_message_injections.h"
#include "common/logic/salutation/letters/meshes/generator/generate/finished/message/shy_message_injections.h"
#include "common/logic/salutation/letters/text/cleaner/clean/finished/message/shy_message_injections.h"
#include "common/logic/salutation/letters/text/generator/generate/finished/message/shy_message_injections.h"
#include "common/logic/salutation/timer/appear/run/finished/message/shy_message_injections.h"
#include "common/logic/salutation/timer/disappear/run/finished/message/shy_message_injections.h"
#include "common/logic/text/message/prepared/shy_prepared_injections.h"
#include "common/logic/title/message/created/shy_created_injections.h"
#include "common/logic/title/message/finished/shy_finished_injections.h"

#include "common/message/init/shy_init_injections.h"

#include "injections/platform/math/type/num_whole/shy_num_whole.h"
#include "injections/platform/scheduler/shy_scheduler.h"

#include "./shy_fsm.h"

typedef shy_common_logic_application_fsm_scheduled so_called_common_logic_application_fsm ;

#endif
