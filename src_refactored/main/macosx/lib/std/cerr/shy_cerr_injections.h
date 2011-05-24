#ifndef _shy_macosx_lib_std_cerr_injections_included
#define _shy_macosx_lib_std_cerr_injections_included 

#ifdef shy_build_development
    #include "../../../../../lib/std/cerr/shy_cerr_injections.h"
    #define so_called_std_cerr shy_std_cerr
#endif

#endif

