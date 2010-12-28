#ifndef _shy_injections_facade_included
#define _shy_injections_facade_included

#ifdef build_static_way
    #include "../facade/shy_static.h"
    typedef shy_facade_static so_called_facade ;
#endif

#ifdef build_loadable_way
    #include "../facade/shy_loadable.h"
    typedef shy_facade_loadable so_called_facade ;
#endif

#endif

