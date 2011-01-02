#include "shy_type_macosx_platform_render_vertex_data.h"

shy_type_macosx_platform_render_vertex_data :: shy_type_macosx_platform_render_vertex_data ( )
{
    for ( int i = 0 ; i < 3 ; i ++ )
        _position [ i ] = so_called_platform_consts_insider :: uninitialized_value ;
    for ( int i = 0 ; i < 2 ; i ++ )
        _tex_coord [ i ] = so_called_platform_consts_insider :: uninitialized_value ;
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) so_called_platform_consts_insider :: uninitialized_value ;
}

