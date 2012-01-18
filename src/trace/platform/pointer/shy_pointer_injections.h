#ifndef _shy_trace_platform_pointer_injections_included
#define _shy_trace_platform_pointer_injections_included

#ifdef shy_build_with_trace
    #include "src/injections/lib/std/false/shy_false.h"
    #include "src/injections/platform/pointer/insider/shy_insider.h"
    #include "./shy_pointer.h"
    typedef shy_trace_platform_pointer so_called_trace_platform_pointer ;
#endif

#endif
