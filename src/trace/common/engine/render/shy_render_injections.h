#ifndef _shy_trace_common_engine_render_injections_included
#define _shy_trace_common_engine_render_injections_included

#ifdef shy_build_with_trace
    #include "./tracer/shy_tracer_injections.h"
    typedef so_called_trace_common_engine_render_tracer so_called_trace_common_engine_render ;
#endif

#ifdef shy_build_without_trace
    #include "./stub/shy_stub_injections.h"
    typedef so_called_trace_common_engine_render_stub so_called_trace_common_engine_render ;
#endif

#endif
