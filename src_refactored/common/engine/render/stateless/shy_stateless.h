#ifndef _shy_common_engine_render_stateless_included
#define _shy_common_engine_render_stateless_included

class shy_common_engine_render_stateless
{
public :
    static void set_texel_color 
        ( so_called_type_platform_render_texel_data & texel
        , so_called_type_platform_math_num_fract r
        , so_called_type_platform_math_num_fract g
        , so_called_type_platform_math_num_fract b
        , so_called_type_platform_math_num_fract a ) ;
    static void create_texture_resource_id 
        ( so_called_type_platform_render_texture_resource_id & resource_id
        , so_called_type_platform_math_num_whole resource_index
        ) ;
} ;

#endif
