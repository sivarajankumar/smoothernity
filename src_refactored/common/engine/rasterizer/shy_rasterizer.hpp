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

void shy_guts :: rasterize_top_triangle_part
    ( so_called_type_platform_math_num_whole x_top
    , so_called_type_platform_math_num_whole y_top
    , so_called_type_platform_math_num_whole x_mid
    , so_called_type_platform_math_num_whole y_mid
    , so_called_type_platform_math_num_whole x_bottom
    , so_called_type_platform_math_num_whole y_bottom
    )
{
    for ( so_called_type_platform_math_num_whole y = y_top 
        ; so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y , y_mid ) 
        ; so_called_platform_math :: dec_whole ( y )
        )
    {
        so_called_type_platform_math_num_whole x_top_mid ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_top , y_mid ) ) 
            x_top_mid = x_mid ;
        else
        {
            so_called_type_platform_math_num_whole y_top_minus_y ;
            so_called_type_platform_math_num_whole y_top_minus_y_mid ;
            so_called_type_platform_math_num_whole x_mid_minus_x_top ;

            so_called_platform_math :: sub_wholes ( y_top_minus_y , y_top , y ) ;
            so_called_platform_math :: sub_wholes ( y_top_minus_y_mid , y_top , y_mid ) ;
            so_called_platform_math :: sub_wholes ( x_mid_minus_x_top , x_mid , x_top ) ;
            so_called_platform_math :: mul_wholes ( x_top_mid , y_top_minus_y , x_mid_minus_x_top ) ;
            so_called_platform_math :: div_whole_by ( x_top_mid , y_top_minus_y_mid ) ;
            so_called_platform_math :: add_to_whole ( x_top_mid , x_top ) ;
        }
            
        so_called_type_platform_math_num_whole x_top_bottom ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_top , y_bottom ) ) 
            x_top_bottom = x_top ;
        else
        {
            so_called_type_platform_math_num_whole y_top_minus_y ;
            so_called_type_platform_math_num_whole y_top_minus_y_bottom ;
            so_called_type_platform_math_num_whole x_bottom_minus_x_top ;

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
    ( so_called_type_platform_math_num_whole x_top
    , so_called_type_platform_math_num_whole y_top
    , so_called_type_platform_math_num_whole x_mid
    , so_called_type_platform_math_num_whole y_mid
    , so_called_type_platform_math_num_whole x_bottom
    , so_called_type_platform_math_num_whole y_bottom
    )
{
    for ( so_called_type_platform_math_num_whole y = y_mid 
        ; so_called_platform_conditions :: whole_greater_or_equal_to_whole ( y , y_bottom )
        ; so_called_platform_math :: dec_whole ( y )
        )
    {
        so_called_type_platform_math_num_whole x_mid_bottom ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_mid , y_bottom ) )
            x_mid_bottom = x_mid ;
        else
        {
            so_called_type_platform_math_num_whole y_mid_minus_y ;
            so_called_type_platform_math_num_whole y_mid_minus_y_bottom ;
            so_called_type_platform_math_num_whole x_bottom_minus_x_mid ;

            so_called_platform_math :: sub_wholes ( y_mid_minus_y , y_mid , y ) ;
            so_called_platform_math :: sub_wholes ( y_mid_minus_y_bottom , y_mid , y_bottom ) ;
            so_called_platform_math :: sub_wholes ( x_bottom_minus_x_mid , x_bottom , x_mid ) ;
            so_called_platform_math :: mul_wholes ( x_mid_bottom , y_mid_minus_y , x_bottom_minus_x_mid ) ;
            so_called_platform_math :: div_whole_by ( x_mid_bottom , y_mid_minus_y_bottom ) ;
            so_called_platform_math :: add_to_whole ( x_mid_bottom , x_mid ) ;
        }
        
        so_called_type_platform_math_num_whole x_top_bottom ;
        if ( so_called_platform_conditions :: wholes_are_equal ( y_top , y_bottom ) )
            x_top_bottom = x_bottom ;
        else
        {
            so_called_type_platform_math_num_whole y_top_minus_y ;
            so_called_type_platform_math_num_whole y_top_minus_y_bottom ;
            so_called_type_platform_math_num_whole x_bottom_minus_x_top ;

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
    ( so_called_type_platform_math_num_whole cx
    , so_called_type_platform_math_num_whole cy
    , so_called_type_platform_math_num_whole x_radius
    , so_called_type_platform_math_num_whole y_radius
    )
{
    so_called_type_platform_math_num_whole x ;
    so_called_type_platform_math_num_whole y ;
    so_called_type_platform_math_num_whole x_change ;
    so_called_type_platform_math_num_whole y_change ;
    so_called_type_platform_math_num_whole ellipse_error ;
    so_called_type_platform_math_num_whole two_a_square ;
    so_called_type_platform_math_num_whole two_b_square ;
    so_called_type_platform_math_num_whole stopping_x ;
    so_called_type_platform_math_num_whole stopping_y ;
    so_called_type_platform_math_num_whole x_radius_sq ;
    so_called_type_platform_math_num_whole y_radius_sq ;
    so_called_type_platform_math_num_whole x_radius_mul_2 ;
    so_called_type_platform_math_num_whole y_radius_mul_2 ;
    
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
        so_called_type_platform_math_num_whole cx_minus_x ;
        so_called_type_platform_math_num_whole cx_plus_x ;
        so_called_type_platform_math_num_whole cy_minus_y ;
        so_called_type_platform_math_num_whole cy_plus_y ;
        so_called_type_platform_math_num_whole ellipse_error_mul_2_plus_x_change ;

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
        so_called_type_platform_math_num_whole cx_minus_x ;
        so_called_type_platform_math_num_whole cx_plus_x ;
        so_called_type_platform_math_num_whole cy_minus_y ;
        so_called_type_platform_math_num_whole cy_plus_y ;
        so_called_type_platform_math_num_whole ellipse_error_mul_2_plus_y_change ;

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

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_draw_ellipse_in_rect msg )
{
    so_called_type_platform_math_num_whole width ;
    so_called_type_platform_math_num_whole height ;
    so_called_type_platform_math_num_whole y_center ;
    so_called_type_platform_math_num_whole x_center ;
    so_called_type_platform_math_num_whole x_diff ;
    so_called_type_platform_math_num_whole y_diff ;

    so_called_platform_math :: add_wholes ( y_center , msg . y1 , msg . y2 ) ;
    so_called_platform_math :: div_whole_by ( y_center , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: add_wholes ( x_center , msg . x1 , msg . x2 ) ;
    so_called_platform_math :: div_whole_by ( x_center , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: sub_wholes ( x_diff , msg . x1 , msg . x2 ) ;
    so_called_platform_math :: sub_wholes ( y_diff , msg . y1 , msg . y2 ) ;
    so_called_common_engine_math_stateless :: abs_whole ( width , x_diff ) ;
    so_called_common_engine_math_stateless :: abs_whole ( height , y_diff ) ;
    
    so_called_type_platform_math_num_whole half_width ;
    so_called_type_platform_math_num_whole half_height ;

    so_called_platform_math :: div_wholes ( half_width , width , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: div_wholes ( half_height , height , so_called_platform_math_consts :: whole_2 ) ;

    shy_guts :: rasterize_bresenham_ellipse ( x_center , y_center , half_width , half_height ) ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_draw_rect msg )
{
    so_called_type_platform_math_num_whole left ;
    so_called_type_platform_math_num_whole right ;
    so_called_type_platform_math_num_whole bottom ;
    so_called_type_platform_math_num_whole top ;

    so_called_common_engine_math_stateless :: min_whole ( left , msg . x1 , msg . x2 ) ;
    so_called_common_engine_math_stateless :: max_whole ( right , msg . x1 , msg . x2 ) ;
    so_called_common_engine_math_stateless :: min_whole ( bottom , msg . y1 , msg . y2 ) ;
    so_called_common_engine_math_stateless :: max_whole ( top , msg . y1 , msg . y2 ) ;
    so_called_platform_math :: add_to_whole ( left , shy_guts :: origin_x ) ;
    so_called_platform_math :: add_to_whole ( right , shy_guts :: origin_x ) ;
    so_called_platform_math :: add_to_whole ( bottom , shy_guts :: origin_y ) ;
    so_called_platform_math :: add_to_whole ( top , shy_guts :: origin_y ) ;
    {
        so_called_message_common_engine_render_texture_set_texels_rect texture_set_texels_rect_msg ;
        texture_set_texels_rect_msg . left = left ;
        texture_set_texels_rect_msg . right = right ;
        texture_set_texels_rect_msg . bottom = bottom ;
        texture_set_texels_rect_msg . top = top ;
        texture_set_texels_rect_msg . texture = shy_guts :: texture_id ;
        texture_set_texels_rect_msg . texel = shy_guts :: texel ;
        so_called_sender_common_engine_render_texture_set_texels_rect :: send ( texture_set_texels_rect_msg ) ;
    }
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_draw_triangle msg )
{
    so_called_type_platform_math_num_whole x1 = msg . x1 ;
    so_called_type_platform_math_num_whole y1 = msg . y1 ;
    so_called_type_platform_math_num_whole x2 = msg . x2 ;
    so_called_type_platform_math_num_whole y2 = msg . y2 ;
    so_called_type_platform_math_num_whole x3 = msg . x3 ;
    so_called_type_platform_math_num_whole y3 = msg . y3 ;

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

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_finalize_request )
{
    so_called_sender_common_engine_rasterizer_finalize_reply :: send ( so_called_message_common_engine_rasterizer_finalize_reply ( ) ) ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_init )
{
    shy_guts :: origin_x = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: origin_y = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_use_texel msg )
{
    shy_guts :: texel = msg . texel ;
}

void _shy_common_engine_rasterizer :: receive ( so_called_message_common_engine_rasterizer_use_texture msg )
{
    shy_guts :: texture_id = msg . texture ;
    shy_guts :: origin_x = msg . origin_x ;
    shy_guts :: origin_y = msg . origin_y ;
}
