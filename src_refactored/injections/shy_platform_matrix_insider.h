#ifndef _shy_injections_platform_matrix_insider_included
#define _shy_injections_platform_matrix_insider_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_macosx_platform_matrix_insider.h"
    typedef shy_macosx_platform_matrix_insider so_called_platform_matrix_insider ;
#endif

#endif
