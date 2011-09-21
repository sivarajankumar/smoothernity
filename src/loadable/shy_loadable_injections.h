#ifndef _shy_loadable_injections_included
#define _shy_loadable_injections_included

#ifdef shy_build_loadable_way
    #define so_called_loadable(function) function
#endif

#ifdef shy_build_static_way
    #define so_called_loadable(function) { }
#endif

#endif
