#ifndef _shy_injections_platform_vector_included
#define _shy_injections_platform_vector_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_vector.h"
    typedef shy_macosx_platform_vector so_called_platform_vector ;
#endif

#endif
