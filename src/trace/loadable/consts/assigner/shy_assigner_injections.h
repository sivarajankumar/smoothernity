#ifndef _shy_trace_loadable_consts_assigner_injections_included
#define _shy_trace_loadable_consts_assigner_injections_included

#ifdef shy_build_with_trace
    #include "./worker/shy_worker_injections.h"
    typedef so_called_trace_loadable_consts_assigner_worker so_called_trace_loadable_consts_assigner ;
#endif

#ifdef shy_build_without_trace
    #include "./fribble/shy_fribble_injections.h"
    typedef so_called_trace_loadable_consts_assigner_fribble so_called_trace_loadable_consts_assigner ;
#endif

#endif
