#ifndef _shy_trace_loadable_parser_injections_included
#define _shy_trace_loadable_parser_injections_included

#ifdef shy_build_with_trace
    #include "./worker/shy_worker_injections.h"
    typedef so_called_trace_loadable_parser_worker so_called_trace_loadable_parser ;
#endif

#ifdef shy_build_without_trace
    #include "./fribble/shy_fribble_injections.h"
    typedef so_called_trace_loadable_parser_fribble so_called_trace_loadable_parser ;
#endif

#endif
