#ifdef NDEBUG
    #define shy_build_for_win
    #define shy_build_static_way
    #define shy_build_without_trace
    #define shy_build_without_profile
    #define shy_build_without_generator
    #define shy_scheduling_mode_direct_call
#endif

#ifdef DEBUG
    #define shy_build_for_win
    #define shy_build_loadable_way
    #define shy_build_with_generator
    #define shy_build_with_profile
    #define shy_build_with_stl
    #define shy_build_with_trace
    #define shy_scheduling_mode_random
#endif

#include "src/define/validation/shy_validation.h"

#include <DXUT.h>
