#ifndef _shy_iphone_platform_scheduler_injections_included
#define _shy_iphone_platform_scheduler_injections_included

#ifdef shy_scheduling_mode_random
    #include "platform/scheduler/random/shy_random_injections.h"
    typedef so_called_platform_scheduler_random so_called_platform_scheduler ;
#endif

#ifdef shy_scheduling_mode_direct_call
    #include "platform/scheduler/direct/call/shy_call_injections.h"
    typedef so_called_platform_scheduler_direct_call so_called_platform_scheduler ;
#endif

#endif

