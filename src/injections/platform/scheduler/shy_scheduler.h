#ifndef _shy_injections_platform_scheduler_included
#define _shy_injections_platform_scheduler_included

#ifdef shy_build_for_iphone
    #include "../../../main/iphone/platform/scheduler/shy_scheduler_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../main/macosx/platform/scheduler/shy_scheduler_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../main/win/platform/scheduler/shy_scheduler_injections.h"
#endif

#endif