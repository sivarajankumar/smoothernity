#ifndef _shy_trace_loadable_fsm_behaviour_injections_included
#define _shy_trace_loadable_fsm_behaviour_injections_included

#ifdef shy_build_with_trace
    #ifdef shy_build_loadable_way
        #include "src/injections/lib/std/char/shy_char.h"
        #include "./shy_behaviour.h"
        typedef shy_trace_loadable_fsm_behaviour so_called_trace_loadable_fsm_behaviour ;
    #endif
#endif

#endif
