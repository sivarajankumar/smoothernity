#include "./shy_consts_injections.h"

#ifdef shy_build_static_way
    #include "src/common/logic/perspective/consts/autogenerated/shy_autogenerated_injections.hpp"
#endif

#ifdef shy_build_loadable_way
    #include "./shy_consts.hpp"
#endif
