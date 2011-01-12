#ifndef _shy_injections_facade_included
#define _shy_injections_facade_included

#ifdef shy_build_static_way
    #include "../facade/shy_static_injections.h"
#endif

#ifdef shy_build_loadable_way
    #include "../facade/loadable/shy_loadable_injections.h"
#endif

#endif

