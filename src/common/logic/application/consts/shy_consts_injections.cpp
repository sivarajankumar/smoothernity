#include "./shy_consts_injections.h"

#ifdef shy_build_static_way
    #include "common/logic/application/consts/autogenerated/shy_autogenerated_injections.hpp"
#endif

#ifdef shy_build_loadable_way
    #include "./shy_consts.hpp"
#endif
