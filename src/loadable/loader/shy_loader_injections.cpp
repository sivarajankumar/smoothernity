#ifdef shy_build_loadable_way
    #include "./shy_loader_injections.h"

    #include "src/loadable/consts/assigner/shy_assigner_injections.h"
    #include "src/loadable/consts/reflection/shy_reflection_injections.h"
    #include "src/loadable/fsm/assigner/shy_assigner_injections.h"
    #include "src/loadable/fsm/reflection/shy_reflection_injections.h"
    #include "src/loadable/generator/shy_generator_injections.h"
    #include "src/loadable/parser/shy_parser_injections.h"

    #include "src/injections/lib/std/cin/shy_cin.h"
    #include "src/injections/lib/std/cout/shy_cout.h"
    #include "src/injections/lib/std/endl/shy_endl.h"
    #include "src/injections/lib/std/false/shy_false.h"
    #include "src/injections/lib/std/getline/shy_getline.h"

    #include "./shy_loader.hpp"
#endif
