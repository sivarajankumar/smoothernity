#ifndef _shy_injections_type_platform_render_vertex_data_included
#define _shy_injections_type_platform_render_vertex_data_included

#ifdef shy_build_for_macosx
    #include "../macosx/platform/shy_type_macosx_platform_render_vertex_data.h"
    typedef shy_type_macosx_platform_render_vertex_data so_called_type_platform_render_vertex_data ;
#endif

#endif
