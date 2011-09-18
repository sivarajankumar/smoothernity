#ifndef _shy_injections_platform_trace_included
#define _shy_injections_platform_trace_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/trace/shy_trace_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/trace/shy_trace_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/trace/shy_trace_injections.h"
#endif

#endif
