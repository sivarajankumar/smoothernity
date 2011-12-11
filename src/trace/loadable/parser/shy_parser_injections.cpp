#ifdef shy_build_with_trace
    #ifdef shy_build_loadable_way
        #include "./shy_parser_injections.h"
        #include "src/injections/lib/std/bool/shy_bool.h"
        #include "src/injections/lib/std/true/shy_true.h"
        #include "src/injections/platform/trace/shy_trace.h"
        #include "src/loadable/parser/consts/shy_consts_injections.h"
        #include "./shy_parser.hpp"
    #endif
#endif
