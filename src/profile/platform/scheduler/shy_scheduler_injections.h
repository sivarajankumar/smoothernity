#ifndef _shy_profile_platform_scheduler_injections_included
#define _shy_profile_platform_scheduler_injections_included

#ifdef shy_build_with_profile
    #include "./shy_scheduler.h"
    typedef shy_profile_platform_scheduler so_called_profile_platform_scheduler ;
#endif

#endif
