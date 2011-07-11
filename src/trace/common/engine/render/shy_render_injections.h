#ifndef _shy_trace_common_engine_render_injections_included
#define _shy_trace_common_engine_render_injections_included

#ifdef shy_build_with_trace
    #include "./worker/shy_worker_injections.h"
    typedef so_called_trace_common_engine_render_worker so_called_trace_common_engine_render ;
#endif

#endif
