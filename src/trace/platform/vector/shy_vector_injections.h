#ifndef _shy_trace_platform_vector_injections_included
#define _shy_trace_platform_vector_injections_included

#ifdef shy_build_with_trace
    #include "src/injections/platform/vector/data/type/shy_type.h"
    #include "./shy_vector.h"
    typedef shy_trace_platform_vector so_called_trace_platform_vector ;
#endif

#endif
