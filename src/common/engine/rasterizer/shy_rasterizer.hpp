namespace shy_guts
{
    static void rasterize_horizontal_line 
        ( so_called_platform_math_num_whole_type x1 
        , so_called_platform_math_num_whole_type x2 
        , so_called_platform_math_num_whole_type y 
        ) ;
    static void rasterize_top_triangle_part 
        ( so_called_platform_math_num_whole_type x_top 
        , so_called_platform_math_num_whole_type y_top 
        , so_called_platform_math_num_whole_type x_mid 
        , so_called_platform_math_num_whole_type y_mid 
        , so_called_platform_math_num_whole_type x_bottom 
        , so_called_platform_math_num_whole_type y_bottom 
        ) ;
    static void rasterize_bottom_triangle_part 
        ( so_called_platform_math_num_whole_type x_top 
        , so_called_platform_math_num_whole_type y_top 
        , so_called_platform_math_num_whole_type x_mid 
        , so_called_platform_math_num_whole_type y_mid 
        , so_called_platform_math_num_whole_type x_bottom 
        , so_called_platform_math_num_whole_type y_bottom 
        ) ;
    static void rasterize_bresenham_ellipse 
        ( so_called_platform_math_num_whole_type cx 
        , so_called_platform_math_num_whole_type cy
        , so_called_platform_math_num_whole_type x_radius
        , so_called_platform_math_num_whole_type y_radius 
        ) ;
    static void to_global_space
        ( so_called_platform_math_num_whole_type & x
        , so_called_platform_math_num_whole_type & y
        ) ;

    static so_called_common_engine_render_texture_id_type texture_id ;
    static so_called_platform_render_texel_data_type texel ;
    static so_called_platform_math_num_whole_type origin_x ;
    static so_called_platform_math_num_whole_type origin_y ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_engine_rasterizer , 1000 > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: to_global_space
    ( so_called_platform_math_num_whole_type & x
    , so_called_platform_math_num_whole_type & y
    )
{
    so_called_platform_math_num_whole_type x_new ;
    so_called_platform_math_num_whole_type y_new ;
    so_called_platform_math :: add_wholes ( x , x , shy_guts :: origin_x ) ;
    so_called_platform_math :: add_wholes ( y , y , shy_guts :: origin_y ) ;
    x_new = x ;
    y_new = y ;
    so_called_common_engine_render_stateless :: clamp_texture_coords ( x_new , y_new ) ;
    if ( ! so_called_platform_conditions :: wholes_are_equal ( x , x_new )
      || ! so_called_platform_conditions :: wholes_are_equal ( y , y_new )
       )
    {
        so_called_trace ( so_called_trace_common_engine_rasterizer :: coords_out_of_range_error ( x , y ) ) ;
    }
    x = x_new ;
    y = y_new ;
}

void shy_guts :: rasterize_horizontal_line 
    ( so_called_platform_math_num_whole_type x1
    , so_called_platform_math_num_whole_type x2
    , so_called_platform_math_num_whole_type y
    )
{
    so_called_platform_math_num_whole_type left ;
    so_called_platform_math_num_whole_type right ;

    so_called_common_engine_math_stateless :: min_whole ( left , x1 , x2 ) ;
    so_called_common_engine_math_stateless :: max_whole ( right , x1 , x2 ) ;
    so_called_platform_math :: add_to_whole ( left , origin_x ) ;
    so_called_platform_math :: add_to_whole ( right , origin_x ) ;
    so_called_platform_math :: add_to_whole ( y , origin_y ) ;

    {
        so_called_common_engine_render_texture_set_texels_rect_message texture_set_texels_rect_msg ;
        texture_set_texels_rect_msg . left = left ;
        texture_set_texels_rect_msg . right = right ;
        texture_set_texels_rect_msg . bottom = y ;
        texture_set_texels_rect_msg . top = y ;
        texture_set_texels_rect_msg . texture = texture_id ;
        texture_set_texels_rect_msg . texel = texel ;
        so_called_common_engine_render_texture_set_texels_rect_sender :: send ( texture_set_texels_rect_msg ) ;
    }
}

void shy_guts :: rasterize_top_triangle_part
    ( so_called_platform_math_num_whole_type x_top
    , so_called_platform_math_num_whole_type y_top
    , so_called_platform_math_num_whole_type x_mid
    , so_called_platform_math_num_whole_type y_mid
    , so_called_platform_math_num_whole_type x_bottom
    , so_called_platform_math_num_whole_type y_bottom
    )
{
    for ( so_called_platform_math_num_whole_type y = y_top 
        ; so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y , y_mid ) 
        ; so_called_platform_math :: dec_whole ( y )
        )
    {
        so_called_platform_math_num_whole_type x_top_mid ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_top , y_mid ) ) 
            x_top_mid = x_mid ;
        else
        {
            so_called_platform_math_num_whole_type y_top_minus_y ;
            so_called_platform_math_num_whole_type y_top_minus_y_mid ;
            so_called_platform_math_num_whole_type x_mid_minus_x_top ;

            so_called_platform_math :: sub_wholes ( y_top_minus_y , y_top , y ) ;
            so_called_platform_math :: sub_wholes ( y_top_minus_y_mid , y_top , y_mid ) ;
            so_called_platform_math :: sub_wholes ( x_mid_minus_x_top , x_mid , x_top ) ;
            so_called_platform_math :: mul_wholes ( x_top_mid , y_top_minus_y , x_mid_minus_x_top ) ;
            so_called_platform_math :: div_whole_by ( x_top_mid , y_top_minus_y_mid ) ;
            so_called_platform_math :: add_to_whole ( x_top_mid , x_top ) ;
        }
            
        so_called_platform_math_num_whole_type x_top_bottom ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_top , y_bottom ) ) 
            x_top_bottom = x_top ;
        else
        {
            so_called_platform_math_num_whole_type y_top_minus_y ;
            so_called_platform_math_num_whole_type y_top_minus_y_bottom ;
            so_called_platform_math_num_whole_type x_bottom_minus_x_top ;

            so_called_platform_math :: sub_wholes ( y_top_minus_y , y_top , y ) ;
            so_called_platform_math :: sub_wholes ( y_top_minus_y_bottom , y_top , y_bottom ) ;
            so_called_platform_math :: sub_wholes ( x_bottom_minus_x_top , x_bottom , x_top ) ;
            so_called_platform_math :: mul_wholes ( x_top_bottom , y_top_minus_y , x_bottom_minus_x_top ) ;
            so_called_platform_math :: div_whole_by ( x_top_bottom , y_top_minus_y_bottom ) ;
            so_called_platform_math :: add_to_whole ( x_top_bottom , x_top ) ;
        }
            
        rasterize_horizontal_line ( x_top_mid , x_top_bottom , y ) ;
    }
}

void shy_guts :: rasterize_bottom_triangle_part
    ( so_called_platform_math_num_whole_type x_top
    , so_called_platform_math_num_whole_type y_top
    , so_called_platform_math_num_whole_type x_mid
    , so_called_platform_math_num_whole_type y_mid
    , so_called_platform_math_num_whole_type x_bottom
    , so_called_platform_math_num_whole_type y_bottom
    )
{
    for ( so_called_platform_math_num_whole_type y = y_mid 
        ; so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y , y_bottom )
        ; so_called_platform_math :: dec_whole ( y )
        )
    {
        so_called_platform_math_num_whole_type x_mid_bottom ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_mid , y_bottom ) )
            x_mid_bottom = x_mid ;
        else
        {
            so_called_platform_math_num_whole_type y_mid_minus_y ;
            so_called_platform_math_num_whole_type y_mid_minus_y_bottom ;
            so_called_platform_math_num_whole_type x_bottom_minus_x_mid ;

            so_called_platform_math :: sub_wholes ( y_mid_minus_y , y_mid , y ) ;
            so_called_platform_math :: sub_wholes ( y_mid_minus_y_bottom , y_mid , y_bottom ) ;
            so_called_platform_math :: sub_wholes ( x_bottom_minus_x_mid , x_bottom , x_mid ) ;
            so_called_platform_math :: mul_wholes ( x_mid_bottom , y_mid_minus_y , x_bottom_minus_x_mid ) ;
            so_called_platform_math :: div_whole_by ( x_mid_bottom , y_mid_minus_y_bottom ) ;
            so_called_platform_math :: add_to_whole ( x_mid_bottom , x_mid ) ;
        }
        
        so_called_platform_math_num_whole_type x_top_bottom ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_top , y_bottom ) )
            x_top_bottom = x_bottom ;
        else
        {
            so_called_platform_math_num_whole_type y_top_minus_y ;
            so_called_platform_math_num_whole_type y_top_minus_y_bottom ;
            so_called_platform_math_num_whole_type x_bottom_minus_x_top ;

            so_called_platform_math :: sub_wholes ( y_top_minus_y , y_top , y ) ;
            so_called_platform_math :: sub_wholes ( y_top_minus_y_bottom , y_top , y_bottom ) ;
            so_called_platform_math :: sub_wholes ( x_bottom_minus_x_top , x_bottom , x_top ) ;
            so_called_platform_math :: mul_wholes ( x_top_bottom , y_top_minus_y , x_bottom_minus_x_top ) ;
            so_called_platform_math :: div_whole_by ( x_top_bottom , y_top_minus_y_bottom ) ;
            so_called_platform_math :: add_to_whole ( x_top_bottom , x_top ) ;
        }
        
        rasterize_horizontal_line ( x_mid_bottom , x_top_bottom , y ) ;
    }
}

void shy_guts :: rasterize_bresenham_ellipse
    ( so_called_platform_math_num_whole_type cx
    , so_called_platform_math_num_whole_type cy
    , so_called_platform_math_num_whole_type x_radius
    , so_called_platform_math_num_whole_type y_radius
    )
{
    so_called_platform_math_num_whole_type x ;
    so_called_platform_math_num_whole_type y ;
    so_called_platform_math_num_whole_type x_change ;
    so_called_platform_math_num_whole_type y_change ;
    so_called_platform_math_num_whole_type ellipse_error ;
    so_called_platform_math_num_whole_type two_a_square ;
    so_called_platform_math_num_whole_type two_b_square ;
    so_called_platform_math_num_whole_type stopping_x ;
    so_called_platform_math_num_whole_type stopping_y ;
    so_called_platform_math_num_whole_type x_radius_sq ;
    so_called_platform_math_num_whole_type y_radius_sq ;
    so_called_platform_math_num_whole_type x_radius_mul_2 ;
    so_called_platform_math_num_whole_type y_radius_mul_2 ;
    
    so_called_platform_math :: mul_wholes ( x_radius_sq , x_radius , x_radius ) ;
    so_called_platform_math :: mul_wholes ( y_radius_sq , y_radius , y_radius ) ;
    so_called_platform_math :: mul_wholes ( x_radius_mul_2 , x_radius , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: mul_wholes ( y_radius_mul_2 , y_radius , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: mul_wholes ( two_a_square , x_radius_sq , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: mul_wholes ( two_b_square , y_radius_sq , so_called_platform_math_consts :: whole_2 ) ;

    x = x_radius ;
    y = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: sub_wholes ( x_change , so_called_platform_math_consts :: whole_1 , x_radius_mul_2 ) ;
    so_called_platform_math :: mul_whole_by ( x_change , y_radius_sq ) ;
    y_change = x_radius_sq ;
    ellipse_error = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: mul_wholes ( stopping_x , two_b_square , x_radius ) ;    
    stopping_y = so_called_platform_math_consts :: whole_0 ;
    
    while ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( stopping_x , stopping_y ) )
    {
        so_called_platform_math_num_whole_type cx_minus_x ;
        so_called_platform_math_num_whole_type cx_plus_x ;
        so_called_platform_math_num_whole_type cy_minus_y ;
        so_called_platform_math_num_whole_type cy_plus_y ;
        so_called_platform_math_num_whole_type ellipse_error_mul_2_plus_x_change ;

        so_called_platform_math :: sub_wholes ( cx_minus_x , cx , x ) ;
        so_called_platform_math :: add_wholes ( cx_plus_x , cx , x ) ;
        so_called_platform_math :: sub_wholes ( cy_minus_y , cy , y ) ;
        so_called_platform_math :: add_wholes ( cy_plus_y , cy , y ) ;
    
        rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_minus_y ) ;
        rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_plus_y ) ;
        
        so_called_platform_math :: inc_whole ( y ) ;
        so_called_platform_math :: add_to_whole ( stopping_y , two_a_square ) ;
        so_called_platform_math :: add_to_whole ( ellipse_error , y_change ) ;
        so_called_platform_math :: add_to_whole ( y_change , two_a_square ) ;
        so_called_platform_math :: mul_wholes ( ellipse_error_mul_2_plus_x_change , ellipse_error , so_called_platform_math_consts :: whole_2 ) ;
        so_called_platform_math :: add_to_whole ( ellipse_error_mul_2_plus_x_change , x_change ) ;
        if ( so_called_platform_conditions :: whole_greater_than_zero ( ellipse_error_mul_2_plus_x_change ) )
        {
            so_called_platform_math :: dec_whole ( x ) ;
            so_called_platform_math :: sub_from_whole ( stopping_x , two_b_square ) ;
            so_called_platform_math :: add_to_whole ( ellipse_error , x_change ) ;
            so_called_platform_math :: add_to_whole ( x_change , two_b_square ) ;
        }
    }
    
    x = so_called_platform_math_consts :: whole_0 ;
    y = y_radius ;
    x_change = y_radius_sq ;
    so_called_platform_math :: sub_wholes ( y_change , so_called_platform_math_consts :: whole_1 , y_radius_mul_2 ) ;
    so_called_platform_math :: mul_whole_by ( y_change , x_radius_sq ) ;
    ellipse_error = so_called_platform_math_consts :: whole_0 ;
    stopping_x = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: mul_wholes ( stopping_y , two_a_square , y_radius ) ;
    
    while ( so_called_platform_conditions :: whole_less_or_equal_to_whole ( stopping_x , stopping_y ) )
    {
        so_called_platform_math_num_whole_type cx_minus_x ;
        so_called_platform_math_num_whole_type cx_plus_x ;
        so_called_platform_math_num_whole_type cy_minus_y ;
        so_called_platform_math_num_whole_type cy_plus_y ;
        so_called_platform_math_num_whole_type ellipse_error_mul_2_plus_y_change ;

        so_called_platform_math :: sub_wholes ( cx_minus_x , cx , x ) ;
        so_called_platform_math :: add_wholes ( cx_plus_x , cx , x ) ;
        so_called_platform_math :: sub_wholes ( cy_minus_y , cy , y ) ;
        so_called_platform_math :: add_wholes ( cy_plus_y , cy , y ) ;
        
        rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_minus_y ) ;
        rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_plus_y ) ;
        
        so_called_platform_math :: dec_whole ( x ) ;
        so_called_platform_math :: add_to_whole ( stopping_x , two_b_square ) ;
        so_called_platform_math :: add_to_whole ( ellipse_error , x_change ) ;
        so_called_platform_math :: add_to_whole ( x_change , two_b_square ) ;
        so_called_platform_math :: mul_wholes ( ellipse_error_mul_2_plus_y_change , ellipse_error , so_called_platform_math_consts :: whole_2 ) ;
        so_called_platform_math :: add_to_whole ( ellipse_error_mul_2_plus_y_change , y_change ) ;
        if ( so_called_platform_conditions :: whole_greater_than_zero ( ellipse_error_mul_2_plus_y_change ) )
        {
            so_called_platform_math :: dec_whole ( y ) ;
            so_called_platform_math :: sub_from_whole ( stopping_y , two_a_square ) ;
            so_called_platform_math :: add_to_whole ( ellipse_error , y_change ) ;
            so_called_platform_math :: add_to_whole ( y_change , two_a_square ) ;
        }
    }
}

void _shy_common_engine_rasterizer :: receive ( so_called_common_engine_rasterizer_draw_ellipse_in_rect_message msg )
{
    so_called_platform_math_num_whole_type width ;
    so_called_platform_math_num_whole_type height ;
    so_called_platform_math_num_whole_type y_center ;
    so_called_platform_math_num_whole_type x_center ;
    so_called_platform_math_num_whole_type x_diff ;
    so_called_platform_math_num_whole_type y_diff ;

    so_called_platform_math :: add_wholes ( y_center , msg . y1 , msg . y2 ) ;
    so_called_platform_math :: div_whole_by ( y_center , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: add_wholes ( x_center , msg . x1 , msg . x2 ) ;
    so_called_platform_math :: div_whole_by ( x_center , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: sub_wholes ( x_diff , msg . x1 , msg . x2 ) ;
    so_called_platform_math :: sub_wholes ( y_diff , msg . y1 , msg . y2 ) ;
    so_called_common_engine_math_stateless :: abs_whole ( width , x_diff ) ;
    so_called_common_engine_math_stateless :: abs_whole ( height , y_diff ) ;
    
    so_called_platform_math_num_whole_type half_width ;
    so_called_platform_math_num_whole_type half_height ;

    so_called_platform_math :: div_wholes ( half_width , width , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: div_wholes ( half_height , height , so_called_platform_math_consts :: whole_2 ) ;

    shy_guts :: rasterize_bresenham_ellipse ( x_center , y_center , half_width , half_height ) ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_common_engine_rasterizer_draw_rect_message msg )
{
    so_called_platform_math_num_whole_type left ;
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math_num_whole_type bottom ;
    so_called_platform_math_num_whole_type top ;

    so_called_common_engine_math_stateless :: min_whole ( left , msg . x1 , msg . x2 ) ;
    so_called_common_engine_math_stateless :: max_whole ( right , msg . x1 , msg . x2 ) ;
    so_called_common_engine_math_stateless :: min_whole ( bottom , msg . y1 , msg . y2 ) ;
    so_called_common_engine_math_stateless :: max_whole ( top , msg . y1 , msg . y2 ) ;

    shy_guts :: to_global_space ( left , bottom ) ;
    shy_guts :: to_global_space ( right , top ) ;

    {
        so_called_common_engine_render_texture_set_texels_rect_message texture_set_texels_rect_msg ;
        texture_set_texels_rect_msg . left = left ;
        texture_set_texels_rect_msg . right = right ;
        texture_set_texels_rect_msg . bottom = bottom ;
        texture_set_texels_rect_msg . top = top ;
        texture_set_texels_rect_msg . texture = shy_guts :: texture_id ;
        texture_set_texels_rect_msg . texel = shy_guts :: texel ;
        so_called_common_engine_render_texture_set_texels_rect_sender :: send ( texture_set_texels_rect_msg ) ;
    }
}

void _shy_common_engine_rasterizer :: receive ( so_called_common_engine_rasterizer_draw_triangle_message msg )
{
    so_called_platform_math_num_whole_type x1 = msg . x1 ;
    so_called_platform_math_num_whole_type y1 = msg . y1 ;
    so_called_platform_math_num_whole_type x2 = msg . x2 ;
    so_called_platform_math_num_whole_type y2 = msg . y2 ;
    so_called_platform_math_num_whole_type x3 = msg . x3 ;
    so_called_platform_math_num_whole_type y3 = msg . y3 ;

    if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y2 ) 
      && so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y3 )
       )
    {
        shy_guts :: rasterize_top_triangle_part    ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
        shy_guts :: rasterize_bottom_triangle_part ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
    }
    else if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y3 ) 
           && so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y2 )
            )
    {
        shy_guts :: rasterize_top_triangle_part    ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
        shy_guts :: rasterize_bottom_triangle_part ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
    }
    else if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y1 )
           && so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y2 )
            )
    {
        shy_guts :: rasterize_top_triangle_part    ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
        shy_guts :: rasterize_bottom_triangle_part ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
    }
    else if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y2 )
           && so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y1 )
            )
    {
        shy_guts :: rasterize_top_triangle_part    ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
        shy_guts :: rasterize_bottom_triangle_part ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
    }
    else if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y1 )
           && so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y3 )
            )
    {
        shy_guts :: rasterize_top_triangle_part    ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
        shy_guts :: rasterize_bottom_triangle_part ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
    }
    else if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y3 ) 
           && so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y1 )
            )
    {
        shy_guts :: rasterize_top_triangle_part    ( x2 , y2 , x3 , y3 , x1 , y1 ) ;
        shy_guts :: rasterize_bottom_triangle_part ( x2 , y2 , x3 , y3 , x1 , y1 ) ;
    }
}

void _shy_common_engine_rasterizer :: receive ( so_called_common_engine_rasterizer_finalize_request_message )
{
    so_called_common_engine_rasterizer_finalize_reply_sender :: send ( so_called_common_engine_rasterizer_finalize_reply_message ( ) ) ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_common_init_message )
{
    shy_guts :: texture_id = so_called_common_engine_render_texture_id_type ( ) ;
    shy_guts :: texel = so_called_platform_render_texel_data_type ( ) ;
    shy_guts :: origin_x = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: origin_y = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_common_engine_rasterizer_use_texel_message msg )
{
    shy_guts :: texel = msg . texel ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_common_engine_rasterizer_use_texture_message msg )
{
    shy_guts :: texture_id = msg . texture ;
    shy_guts :: origin_x = msg . origin_x ;
    shy_guts :: origin_y = msg . origin_y ;
}

void _shy_common_engine_rasterizer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
