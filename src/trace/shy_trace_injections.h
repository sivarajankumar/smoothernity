#ifndef _shy_trace_injections_included
#define _shy_trace_injections_included

#ifdef shy_build_with_trace
    #define so_called_trace(function) function
#endif

#ifdef shy_build_without_trace
    #define so_called_trace(function) { }
#endif

#endif
