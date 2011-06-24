#ifndef _shy_iphone_platform_trace_injections_included
#define _shy_iphone_platform_trace_injections_included

#ifdef shy_build_with_trace
    #include "../../../../platform/trace/cerr/shy_cerr_injections.h"
    typedef so_called_platform_trace_cerr so_called_platform_trace ;
#endif

#ifdef shy_build_without_trace
    #include "../../../../platform/trace/stub/shy_stub_injections.h"
    typedef so_called_platform_trace_stub so_called_platform_trace ;
#endif

#endif
