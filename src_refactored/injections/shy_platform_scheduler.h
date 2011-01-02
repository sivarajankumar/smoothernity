#ifndef _shy_injections_platform_scheduler_included
#define _shy_injections_platform_scheduler_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_scheduler.h"
    typedef shy_macosx_platform_scheduler so_called_platform_scheduler ;
#endif

#endif
