#ifndef _shy_injections_type_platform_matrix_data_included
#define _shy_injections_type_platform_matrix_data_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_type_macosx_platform_matrix_data.h"
    typedef shy_type_macosx_platform_matrix_data so_called_type_platform_matrix_data ;
#endif

#endif
