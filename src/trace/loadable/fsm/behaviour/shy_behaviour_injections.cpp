#ifdef shy_build_with_trace
    #ifdef shy_build_loadable_way
        #include "./shy_behaviour_injections.h"
        #include "src/injections/lib/std/bool/shy_bool.h"
        #include "src/injections/lib/std/false/shy_false.h"
        #include "src/injections/lib/std/true/shy_true.h"
        #include "src/injections/platform/trace/shy_trace.h"
        #include "./shy_behaviour.hpp"
    #endif
#endif
