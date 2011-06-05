#ifndef _shy_facade_injections_included
#define _shy_facade_injections_included

#ifdef shy_build_static_way
    #include "./static/shy_static_injections.h"
#endif

#ifdef shy_build_loadable_way
    #include "./loadable/shy_loadable_injections.h"
#endif

#endif

