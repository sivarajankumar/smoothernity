#ifndef _facade_included
#define _facade_included

#ifdef build_static_way
    #include "static.h"
    typedef shy_facade_static so_called_facade ;
#endif

#ifdef build_loadable_way
    #include "loadable.h"
    typedef shy_facade_loadable so_called_facade ;
#endif

#endif

