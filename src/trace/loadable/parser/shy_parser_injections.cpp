#ifdef shy_build_loadable_way

    #ifdef shy_build_with_trace
        #include "./worker/shy_worker_injections.hpp"
    #endif

    #ifdef shy_build_without_trace
        #include "./fribble/shy_fribble_injections.hpp"
    #endif

#endif
