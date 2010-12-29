#ifndef _shy_injections_platform_matrix_included
#define _shy_injections_platform_matrix_included

#ifdef shy_build_for_macosx
    #include "../macosx/shy_macosx_platform_matrix.h"
    typedef shy_macosx_platform_matrix so_called_platform_matrix ;
#endif

#endif
