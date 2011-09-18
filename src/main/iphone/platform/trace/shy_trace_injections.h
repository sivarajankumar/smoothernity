#ifndef _shy_iphone_platform_trace_injections_included
#define _shy_iphone_platform_trace_injections_included

#ifdef shy_build_with_trace
    #include "src/platform/trace/cerr/shy_cerr_injections.h"
    typedef so_called_platform_trace_cerr so_called_platform_trace ;
#endif

#endif
