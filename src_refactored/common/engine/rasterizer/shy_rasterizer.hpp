class shy_guts
{
public :
    static void rasterize_horizontal_line 
        ( so_called_type_platform_math_num_whole x1 
        , so_called_type_platform_math_num_whole x2 
        , so_called_type_platform_math_num_whole y 
        ) ;
    static void rasterize_top_triangle_part 
        ( so_called_type_platform_math_num_whole x_top 
        , so_called_type_platform_math_num_whole y_top 
        , so_called_type_platform_math_num_whole x_mid 
        , so_called_type_platform_math_num_whole y_mid 
        , so_called_type_platform_math_num_whole x_bottom 
        , so_called_type_platform_math_num_whole y_bottom 
        ) ;
    static void rasterize_bottom_triangle_part 
        ( so_called_type_platform_math_num_whole x_top 
        , so_called_type_platform_math_num_whole y_top 
        , so_called_type_platform_math_num_whole x_mid 
        , so_called_type_platform_math_num_whole y_mid 
        , so_called_type_platform_math_num_whole x_bottom 
        , so_called_type_platform_math_num_whole y_bottom 
        ) ;
	static void rasterize_bresenham_ellipse 
        ( so_called_type_platform_math_num_whole cx 
        , so_called_type_platform_math_num_whole cy
        , so_called_type_platform_math_num_whole x_radius
        , so_called_type_platform_math_num_whole y_radius 
        ) ;
public :
    static so_called_type_common_engine_render_texture_id texture_id ;
    static so_called_type_platform_render_texel_data texel ;
    static so_called_type_platform_math_num_whole origin_x ;
    static so_called_type_platform_math_num_whole origin_y ;
} ;

so_called_type_common_engine_render_texture_id shy_guts :: texture_id ;
so_called_type_platform_render_texel_data shy_guts :: texel ;
so_called_type_platform_math_num_whole shy_guts :: origin_x ;
so_called_type_platform_math_num_whole shy_guts :: origin_y ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_engine_rasterizer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: rasterize_horizontal_line 
    ( so_called_type_platform_math_num_whole x1
    , so_called_type_platform_math_num_whole x2
    , so_called_type_platform_math_num_whole y
    )
{
    so_called_type_platform_math_num_whole left ;
    so_called_type_platform_math_num_whole right ;

    so_called_common_engine_math_stateless :: min_whole ( left , x1 , x2 ) ;
    so_called_common_engine_math_stateless :: max_whole ( right , x1 , x2 ) ;
    so_called_platform_math :: add_to_whole ( left , origin_x ) ;
    so_called_platform_math :: add_to_whole ( right , origin_x ) ;
    so_called_platform_math :: add_to_whole ( y , origin_y ) ;

    {
        so_called_message_common_engine_render_texture_set_texels_rect texture_set_texels_rect_msg ;
        texture_set_texels_rect_msg . left = left ;
        texture_set_texels_rect_msg . right = right ;
        texture_set_texels_rect_msg . bottom = y ;
        texture_set_texels_rect_msg . top = y ;
        texture_set_texels_rect_msg . texture = texture_id ;
        texture_set_texels_rect_msg . texel = texel ;
        so_called_sender_common_engine_render_texture_set_texels_rect :: send ( texture_set_texels_rect_msg ) ;
    }
}

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
    so_called_sender_common_engine_rasterizer_finalize_reply :: send ( so_called_message_common_engine_rasterizer_finalize_reply ( ) ) ;
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
