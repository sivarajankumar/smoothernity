#ifndef _shy_common_logic_amusement_injections_included
#define _shy_common_logic_amusement_injections_included

#include "./message/creation_permit/shy_creation_permit_injections.h"
#include "./message/launch_permit/shy_launch_permit_injections.h"
#include "./message/update/shy_update_injections.h"

#include "../blanket/animation/message/appear_finished/shy_appear_finished_injections.h"
#include "../blanket/animation/message/disappear_finished/shy_disappear_finished_injections.h"
#include "../blanket/message/creation_finished/shy_creation_finished_injections.h"
#include "../door/message/creation_finished/shy_creation_finished_injections.h"
#include "../room/message/creation_finished/shy_creation_finished_injections.h"
#include "../room/message/finished/shy_finished_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_amusement.h"

typedef shy_common_logic_amusement_scheduled so_called_common_logic_amusement ;

#endif 
