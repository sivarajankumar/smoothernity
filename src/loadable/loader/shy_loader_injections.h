#ifndef _shy_loadable_loader_injections_included
#define _shy_loadable_loader_injections_included

#ifdef shy_build_loadable_way
    #include "./active/shy_active_injections.h"
    typedef so_called_loadable_loader_active so_called_loadable_loader ;
#endif

#ifdef shy_build_static_way
    #include "./stub/shy_stub_injections.h"
    typedef so_called_loadable_loader_stub so_called_loadable_loader ;
#endif

#endif
