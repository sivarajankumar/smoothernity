#ifndef _shy_trace_loadable_consts_assigner_injections_included
#define _shy_trace_loadable_consts_assigner_injections_included

#ifdef shy_build_with_trace
    #ifdef shy_build_loadable_way
        #include "src/injections/lib/std/char/shy_char.h"
        #include "src/injections/lib/std/int32/t/shy_t.h"
        #include "./shy_assigner.h"
        typedef shy_trace_loadable_consts_assigner so_called_trace_loadable_consts_assigner ;
    #endif
#endif

#endif
