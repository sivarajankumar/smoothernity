template < typename mediator >
class shy_engine_rasterizer
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: rasterize_triangle msg ) ;
    void receive ( typename messages :: rasterize_rect msg ) ;
    void receive ( typename messages :: rasterize_ellipse_in_rect msg ) ;
    void receive ( typename messages :: rasterize_use_texture msg ) ;
    void receive ( typename messages :: rasterize_use_texel msg ) ;
    void receive ( typename messages :: rasterize_finalize_request msg ) ;
private :
    void _rasterize_horizontal_line ( num_whole x1 , num_whole x2 , num_whole y ) ;
    void _rasterize_top_triangle_part ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom ) ;
    void _rasterize_bottom_triangle_part ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom ) ;
	void _rasterize_bresenham_ellipse ( num_whole cx , num_whole cy, num_whole x_radius, num_whole y_radius ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    texture_id _texture_id ;
    texel_data _texel ;
    num_whole _origin_x ;
    num_whole _origin_y ;
} ;

template < typename mediator >
void shy_engine_rasterizer < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: receive ( typename messages :: init msg )
{
    _platform_math_consts = _mediator . get ( ) . platform_obj ( ) . math_consts_ptr ;
    platform_math :: make_num_whole ( _origin_x , 0 ) ;
    platform_math :: make_num_whole ( _origin_y , 0 ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: receive ( typename messages :: rasterize_finalize_request msg )
{
    _mediator . get ( ) . send ( typename messages :: rasterize_finalize_reply ( ) ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: receive ( typename messages :: rasterize_triangle msg )
{
    num_whole x1 = msg . x1 ;
    num_whole y1 = msg . y1 ;
    num_whole x2 = msg . x2 ;
    num_whole y2 = msg . y2 ;
    num_whole x3 = msg . x3 ;
    num_whole y3 = msg . y3 ;
    if ( platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y2 ) 
      && platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y3 )
       )
    {
        _rasterize_top_triangle_part    ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
        _rasterize_bottom_triangle_part ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
    }
    else if ( platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y3 ) 
           && platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y2 )
            )
    {
        _rasterize_top_triangle_part    ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
        _rasterize_bottom_triangle_part ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
    }
    else if ( platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y1 )
           && platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y2 )
            )
    {
        _rasterize_top_triangle_part    ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
        _rasterize_bottom_triangle_part ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
    }
    else if ( platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y2 )
           && platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y1 )
            )
    {
        _rasterize_top_triangle_part    ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
        _rasterize_bottom_triangle_part ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
    }
    else if ( platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y1 )
           && platform_conditions :: whole_greater_or_equal_to_whole ( y1 , y3 )
            )
    {
        _rasterize_top_triangle_part    ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
        _rasterize_bottom_triangle_part ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
    }
    else if ( platform_conditions :: whole_greater_or_equal_to_whole ( y2 , y3 ) 
           && platform_conditions :: whole_greater_or_equal_to_whole ( y3 , y1 )
            )
    {
        _rasterize_top_triangle_part    ( x2 , y2 , x3 , y3 , x1 , y1 ) ;
        _rasterize_bottom_triangle_part ( x2 , y2 , x3 , y3 , x1 , y1 ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: receive ( typename messages :: rasterize_ellipse_in_rect msg )
{
    num_whole width ;
    num_whole height ;
    num_whole y_center ;
    num_whole x_center ;
    num_whole x_diff ;
    num_whole y_diff ;
    platform_math :: add_wholes ( y_center , msg . y1 , msg . y2 ) ;
    platform_math :: div_whole_by ( y_center , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: add_wholes ( x_center , msg . x1 , msg . x2 ) ;
    platform_math :: div_whole_by ( x_center , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: sub_wholes ( x_diff , msg . x1 , msg . x2 ) ;
    platform_math :: sub_wholes ( y_diff , msg . y1 , msg . y2 ) ;
    engine_math :: math_abs_whole ( width , x_diff ) ;
    engine_math :: math_abs_whole ( height , y_diff ) ;
    
    num_whole half_width ;
    num_whole half_height ;
    platform_math :: div_wholes ( half_width , width , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: div_wholes ( half_height , height , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_bresenham_ellipse ( x_center , y_center , half_width , half_height ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: receive ( typename messages :: rasterize_rect msg )
{
    num_whole left ;
    num_whole right ;
    num_whole bottom ;
    num_whole top ;
    engine_math :: math_min_whole ( left , msg . x1 , msg . x2 ) ;
    engine_math :: math_max_whole ( right , msg . x1 , msg . x2 ) ;
    engine_math :: math_min_whole ( bottom , msg . y1 , msg . y2 ) ;
    engine_math :: math_max_whole ( top , msg . y1 , msg . y2 ) ;
    platform_math :: add_to_whole ( left , _origin_x ) ;
    platform_math :: add_to_whole ( right , _origin_x ) ;
    platform_math :: add_to_whole ( bottom , _origin_y ) ;
    platform_math :: add_to_whole ( top , _origin_y ) ;
    {
        typename messages :: render_texture_set_texels_rect texture_set_texels_rect_msg ;
        texture_set_texels_rect_msg . left = left ;
        texture_set_texels_rect_msg . right = right ;
        texture_set_texels_rect_msg . bottom = bottom ;
        texture_set_texels_rect_msg . top = top ;
        texture_set_texels_rect_msg . texture = _texture_id ;
        texture_set_texels_rect_msg . texel = _texel ;
        _mediator . get ( ) . send ( texture_set_texels_rect_msg ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: receive ( typename messages :: rasterize_use_texture msg )
{
    _texture_id = msg . texture ;
    _origin_x = msg . origin_x ;
    _origin_y = msg . origin_y ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: receive ( typename messages :: rasterize_use_texel msg )
{
    _texel = msg . texel ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_horizontal_line ( num_whole x1 , num_whole x2 , num_whole y )
{
    num_whole left ;
    num_whole right ;
    engine_math :: math_min_whole ( left , x1 , x2 ) ;
    engine_math :: math_max_whole ( right , x1 , x2 ) ;
    platform_math :: add_to_whole ( left , _origin_x ) ;
    platform_math :: add_to_whole ( right , _origin_x ) ;
    platform_math :: add_to_whole ( y , _origin_y ) ;
    {
        typename messages :: render_texture_set_texels_rect texture_set_texels_rect_msg ;
        texture_set_texels_rect_msg . left = left ;
        texture_set_texels_rect_msg . right = right ;
        texture_set_texels_rect_msg . bottom = y ;
        texture_set_texels_rect_msg . top = y ;
        texture_set_texels_rect_msg . texture = _texture_id ;
        texture_set_texels_rect_msg . texel = _texel ;
        _mediator . get ( ) . send ( texture_set_texels_rect_msg ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_top_triangle_part
    ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom )
{
    for ( num_whole y = y_top 
        ; platform_conditions :: whole_greater_or_equal_to_whole ( y , y_mid ) 
        ; platform_math :: dec_whole ( y )
        )
    {
        num_whole x_top_mid ;
        if ( platform_conditions :: wholes_are_equal ( y_top , y_mid ) ) 
            x_top_mid = x_mid ;
        else
        {
            num_whole y_top_minus_y ;
            num_whole y_top_minus_y_mid ;
            num_whole x_mid_minus_x_top ;
            platform_math :: sub_wholes ( y_top_minus_y , y_top , y ) ;
            platform_math :: sub_wholes ( y_top_minus_y_mid , y_top , y_mid ) ;
            platform_math :: sub_wholes ( x_mid_minus_x_top , x_mid , x_top ) ;
            platform_math :: mul_wholes ( x_top_mid , y_top_minus_y , x_mid_minus_x_top ) ;
            platform_math :: div_whole_by ( x_top_mid , y_top_minus_y_mid ) ;
            platform_math :: add_to_whole ( x_top_mid , x_top ) ;
        }
            
        num_whole x_top_bottom ;
        if ( platform_conditions :: wholes_are_equal ( y_top , y_bottom ) ) 
            x_top_bottom = x_top ;
        else
        {
            num_whole y_top_minus_y ;
            num_whole y_top_minus_y_bottom ;
            num_whole x_bottom_minus_x_top ;
            platform_math :: sub_wholes ( y_top_minus_y , y_top , y ) ;
            platform_math :: sub_wholes ( y_top_minus_y_bottom , y_top , y_bottom ) ;
            platform_math :: sub_wholes ( x_bottom_minus_x_top , x_bottom , x_top ) ;
            platform_math :: mul_wholes ( x_top_bottom , y_top_minus_y , x_bottom_minus_x_top ) ;
            platform_math :: div_whole_by ( x_top_bottom , y_top_minus_y_bottom ) ;
            platform_math :: add_to_whole ( x_top_bottom , x_top ) ;
        }
            
        _rasterize_horizontal_line ( x_top_mid , x_top_bottom , y ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_bottom_triangle_part
    ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom )
{
    for ( num_whole y = y_mid 
        ; platform_conditions :: whole_greater_or_equal_to_whole ( y , y_bottom )
        ; platform_math :: dec_whole ( y )
        )
    {
        num_whole x_mid_bottom ;
        if ( platform_conditions :: wholes_are_equal ( y_mid , y_bottom ) )
            x_mid_bottom = x_mid ;
        else
        {
            num_whole y_mid_minus_y ;
            num_whole y_mid_minus_y_bottom ;
            num_whole x_bottom_minus_x_mid ;
            platform_math :: sub_wholes ( y_mid_minus_y , y_mid , y ) ;
            platform_math :: sub_wholes ( y_mid_minus_y_bottom , y_mid , y_bottom ) ;
            platform_math :: sub_wholes ( x_bottom_minus_x_mid , x_bottom , x_mid ) ;
            platform_math :: mul_wholes ( x_mid_bottom , y_mid_minus_y , x_bottom_minus_x_mid ) ;
            platform_math :: div_whole_by ( x_mid_bottom , y_mid_minus_y_bottom ) ;
            platform_math :: add_to_whole ( x_mid_bottom , x_mid ) ;
        }
        
        num_whole x_top_bottom ;
        if ( platform_conditions :: wholes_are_equal ( y_top , y_bottom ) )
            x_top_bottom = x_bottom ;
        else
        {
            num_whole y_top_minus_y ;
            num_whole y_top_minus_y_bottom ;
            num_whole x_bottom_minus_x_top ;
            platform_math :: sub_wholes ( y_top_minus_y , y_top , y ) ;
            platform_math :: sub_wholes ( y_top_minus_y_bottom , y_top , y_bottom ) ;
            platform_math :: sub_wholes ( x_bottom_minus_x_top , x_bottom , x_top ) ;
            platform_math :: mul_wholes ( x_top_bottom , y_top_minus_y , x_bottom_minus_x_top ) ;
            platform_math :: div_whole_by ( x_top_bottom , y_top_minus_y_bottom ) ;
            platform_math :: add_to_whole ( x_top_bottom , x_top ) ;
        }
        
        _rasterize_horizontal_line ( x_mid_bottom , x_top_bottom , y ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_bresenham_ellipse ( num_whole cx , num_whole cy , num_whole x_radius , num_whole y_radius )
{
    num_whole x , y ;
    num_whole x_change , y_change , ellipse_error , two_a_square , two_b_square , stopping_x , stopping_y ;
    num_whole x_radius_sq ;
    num_whole y_radius_sq ;
    num_whole x_radius_mul_2 ;
    num_whole y_radius_mul_2 ;
    
    platform_math :: mul_wholes ( x_radius_sq , x_radius , x_radius ) ;
    platform_math :: mul_wholes ( y_radius_sq , y_radius , y_radius ) ;
    platform_math :: mul_wholes ( x_radius_mul_2 , x_radius , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: mul_wholes ( y_radius_mul_2 , y_radius , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: mul_wholes ( two_a_square , x_radius_sq , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: mul_wholes ( two_b_square , y_radius_sq , _platform_math_consts . get ( ) . whole_2 ) ;

    x = x_radius ;
    y = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: sub_wholes ( x_change , _platform_math_consts . get ( ) . whole_1 , x_radius_mul_2 ) ;
    platform_math :: mul_whole_by ( x_change , y_radius_sq ) ;
    y_change = x_radius_sq ;
    ellipse_error = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: mul_wholes ( stopping_x , two_b_square , x_radius ) ;    
    stopping_y = _platform_math_consts . get ( ) . whole_0 ;
    
    while ( platform_conditions :: whole_greater_or_equal_to_whole ( stopping_x , stopping_y ) )
    {
        num_whole cx_minus_x ;
        num_whole cx_plus_x ;
        num_whole cy_minus_y ;
        num_whole cy_plus_y ;
        num_whole ellipse_error_mul_2_plus_x_change ;
        platform_math :: sub_wholes ( cx_minus_x , cx , x ) ;
        platform_math :: add_wholes ( cx_plus_x , cx , x ) ;
        platform_math :: sub_wholes ( cy_minus_y , cy , y ) ;
        platform_math :: add_wholes ( cy_plus_y , cy , y ) ;
    
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_minus_y ) ;
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_plus_y ) ;
        
        platform_math :: inc_whole ( y ) ;
        platform_math :: add_to_whole ( stopping_y , two_a_square ) ;
        platform_math :: add_to_whole ( ellipse_error , y_change ) ;
        platform_math :: add_to_whole ( y_change , two_a_square ) ;
        platform_math :: mul_wholes ( ellipse_error_mul_2_plus_x_change , ellipse_error , _platform_math_consts . get ( ) . whole_2 ) ;
        platform_math :: add_to_whole ( ellipse_error_mul_2_plus_x_change , x_change ) ;
        if ( platform_conditions :: whole_greater_than_zero ( ellipse_error_mul_2_plus_x_change ) )
        {
            platform_math :: dec_whole ( x ) ;
            platform_math :: sub_from_whole ( stopping_x , two_b_square ) ;
            platform_math :: add_to_whole ( ellipse_error , x_change ) ;
            platform_math :: add_to_whole ( x_change , two_b_square ) ;
        }
    }
    
    x = _platform_math_consts . get ( ) . whole_0 ;
    y = y_radius ;
    x_change = y_radius_sq ;
    platform_math :: sub_wholes ( y_change , _platform_math_consts . get ( ) . whole_1 , y_radius_mul_2 ) ;
    platform_math :: mul_whole_by ( y_change , x_radius_sq ) ;
    ellipse_error = _platform_math_consts . get ( ) . whole_0 ;
    stopping_x = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: mul_wholes ( stopping_y , two_a_square , y_radius ) ;
    
    while ( platform_conditions :: whole_less_or_equal_to_whole ( stopping_x , stopping_y ) )
    {
        num_whole cx_minus_x ;
        num_whole cx_plus_x ;
        num_whole cy_minus_y ;
        num_whole cy_plus_y ;
        num_whole ellipse_error_mul_2_plus_y_change ;
        platform_math :: sub_wholes ( cx_minus_x , cx , x ) ;
        platform_math :: add_wholes ( cx_plus_x , cx , x ) ;
        platform_math :: sub_wholes ( cy_minus_y , cy , y ) ;
        platform_math :: add_wholes ( cy_plus_y , cy , y ) ;
        
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_minus_y ) ;
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_plus_y ) ;
        
        platform_math :: dec_whole ( x ) ;
        platform_math :: add_to_whole ( stopping_x , two_b_square ) ;
        platform_math :: add_to_whole ( ellipse_error , x_change ) ;
        platform_math :: add_to_whole ( x_change , two_b_square ) ;
        platform_math :: mul_wholes ( ellipse_error_mul_2_plus_y_change , ellipse_error , _platform_math_consts . get ( ) . whole_2 ) ;
        platform_math :: add_to_whole ( ellipse_error_mul_2_plus_y_change , y_change ) ;
        if ( platform_conditions :: whole_greater_than_zero ( ellipse_error_mul_2_plus_y_change ) )
        {
            platform_math :: dec_whole ( y ) ;
            platform_math :: sub_from_whole ( stopping_y , two_a_square ) ;
            platform_math :: add_to_whole ( ellipse_error , y_change ) ;
            platform_math :: add_to_whole ( y_change , two_a_square ) ;
        }
    }
}
