#ifndef _shy_injections_platform_vector_insider_included
#define _shy_injections_platform_vector_insider_included

#ifdef shy_build_for_macosx
    #include "../macosx/shy_macosx_platform_vector_insider.h"
    typedef shy_macosx_platform_vector_insider so_called_platform_vector_insider ;
#endif

#endif
