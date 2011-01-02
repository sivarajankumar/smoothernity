#ifndef _shy_macosx_platform_scheduler_included
#define _shy_macosx_platform_scheduler_included

#ifdef shy_scheduling_mode_random
    #include "../../platform/shy_scheduler_random.h"
    typedef shy_platform_scheduler_random shy_macosx_platform_scheduler ;
#endif

#ifdef shy_scheduling_mode_direct_call
    #include "../../platform/shy_scheduler_direct_call.h"
    typedef shy_platform_scheduler_direct_call shy_macosx_platform_scheduler ;
#endif

#endif
