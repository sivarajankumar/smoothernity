#ifndef _shy_common_logic_door_injections_included
#define _shy_common_logic_door_injections_included

#include "./message/creation_permit/shy_creation_permit_injections.h"
#include "./message/launch_permit/shy_launch_permit_injections.h"
#include "./message/mesh_creation_finished/shy_mesh_creation_finished_injections.h"
#include "./message/texture_creation_finished/shy_texture_creation_finished_injections.h"
#include "./message/update/shy_update_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_door.h"

typedef shy_common_logic_door_scheduled so_called_common_logic_door ;

#endif
