#ifndef _shy_injections_facade_injections_included
#define _shy_injections_facade_injections_included

#ifdef shy_build_static_way
    #include "../facade/shy_static_injections.hpp"
#endif

#ifdef shy_build_loadable_way
    #include "../facade/shy_loadable_injections.hpp"
#endif

#endif

