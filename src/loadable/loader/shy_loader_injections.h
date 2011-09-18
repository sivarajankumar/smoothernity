#ifndef _shy_loadable_loader_injections_included
#define _shy_loadable_loader_injections_included

#ifdef shy_build_loadable_way
    #include "src/loadable/loader/worker/shy_worker_injections.h"
    typedef so_called_loadable_loader_worker so_called_loadable_loader ;
#endif

#ifdef shy_build_static_way
    #include "src/loadable/loader/fribble/shy_fribble_injections.h"
    typedef so_called_loadable_loader_fribble so_called_loadable_loader ;
#endif

#endif
