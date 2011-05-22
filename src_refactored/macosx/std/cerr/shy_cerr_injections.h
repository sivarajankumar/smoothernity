#ifndef _shy_macosx_std_cerr_injections_included
#define _shy_macosx_std_cerr_injections_included 

#ifdef shy_build_loadable_way
    #include "../../../std/cerr/shy_cerr_injections.h"
    #define so_called_std_cerr shy_std_cerr
#endif

#endif

