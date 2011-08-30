#ifndef _shy_injections_platform_scheduler_trace_included
#define _shy_injections_platform_scheduler_trace_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/scheduler/trace/shy_trace_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/scheduler/trace/shy_trace_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/scheduler/trace/shy_trace_injections.h"
#endif

#endif
