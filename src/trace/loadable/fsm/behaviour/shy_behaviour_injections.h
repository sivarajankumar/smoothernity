#ifndef _shy_trace_loadable_fsm_behaviour_injections_included
#define _shy_trace_loadable_fsm_behaviour_injections_included

#ifdef shy_build_with_trace
    #include "./tracer/shy_tracer_injections.h"
    typedef so_called_trace_loadable_fsm_behaviour_tracer so_called_trace_loadable_fsm_behaviour ;
#endif

#ifdef shy_build_without_trace
    #include "./stub/shy_stub_injections.h"
    typedef so_called_trace_loadable_fsm_behaviour_stub so_called_trace_loadable_fsm_behaviour ;
#endif

#endif
