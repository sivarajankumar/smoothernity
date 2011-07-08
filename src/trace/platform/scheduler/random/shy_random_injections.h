#ifndef _shy_trace_platform_scheduler_random_injections_included
#define _shy_trace_platform_scheduler_random_injections_included

#ifdef shy_build_with_trace
    #include "./worker/shy_worker_injections.h"
    typedef so_called_trace_platform_scheduler_random_worker so_called_trace_platform_scheduler_random ;
#endif

#ifdef shy_build_without_trace
    #include "./fribble/shy_fribble_injections.h"
    typedef so_called_trace_platform_scheduler_random_fribble so_called_trace_platform_scheduler_random ;
#endif

#endif
