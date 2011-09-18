#ifndef _shy_trace_loadable_fsm_assigner_injections_included
#define _shy_trace_loadable_fsm_assigner_injections_included

#ifdef shy_build_with_trace
    #ifdef shy_build_loadable_way
        #include "src/injections/lib/std/char/shy_char.h"
        #include "./shy_assigner.h"
        typedef shy_trace_loadable_fsm_assigner so_called_trace_loadable_fsm_assigner ;
    #endif
#endif

#endif
