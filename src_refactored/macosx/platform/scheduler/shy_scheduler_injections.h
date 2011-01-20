#ifndef _shy_macosx_platform_scheduler_injections_included
#define _shy_macosx_platform_scheduler_injections_included

#ifdef shy_scheduling_mode_random
    #include "../../../platform/shy_scheduler_random_injections.h"
    typedef shy_platform_scheduler_random so_called_platform_scheduler ;
#endif

#ifdef shy_scheduling_mode_direct_call
    #include "../../../platform/scheduler/direct_call/shy_direct_call_injections.h"
    typedef shy_platform_scheduler_direct_call so_called_platform_scheduler ;
#endif

#endif

