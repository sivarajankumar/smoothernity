class shy_guts
{
public :
    static so_called_type_common_engine_render_texture_id texture_id ;
    static so_called_type_platform_render_texel_data texel ;
    static so_called_type_platform_math_num_whole origin_x ;
    static so_called_type_platform_math_num_whole origin_y ;
} ;

so_called_type_platform_math_num_whole shy_guts :: origin_x ;
so_called_type_platform_math_num_whole shy_guts :: origin_y ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_engine_rasterizer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_draw_ellipse_in_rect )
{
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_draw_rect )
{
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_draw_triangle )
{
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_finalize_request )
{
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_init )
{
    shy_guts :: origin_x = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: origin_y = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_use_texel )
{
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_use_texture )
{
}
