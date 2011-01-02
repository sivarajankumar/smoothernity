#include "shy_type_macosx_platform_render_texel_data.h"

shy_type_macosx_platform_render_texel_data :: shy_type_macosx_platform_render_texel_data ( )
{
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) so_called_platform_consts_insider :: uninitialized_value ;
}

