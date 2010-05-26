template < typename mediator >
class shy_engine_rasterizer
{
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: texel_data texel_data ;
public :
    shy_engine_rasterizer ( mediator * arg_mediator ) ;
    void rasterize_triangle ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 , int_32 x3 , int_32 y3 ) ;
    void rasterize_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 ) ;
    void rasterize_ellipse_in_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 ) ;
    void rasterize_use_texture ( texture_id arg_texture_id , int_32 origin_x , int_32 origin_y ) ;
    void rasterize_use_texel ( const texel_data & texel ) ;
private :
    void _rasterize_horizontal_line ( num_whole x1 , num_whole x2 , num_whole y ) ;
    void _rasterize_top_triangle_part ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom ) ;
    void _rasterize_bottom_triangle_part ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom ) ;
	void _rasterize_bresenham_ellipse ( num_whole cx , num_whole cy, num_whole x_radius, num_whole y_radius ) ;
private :
    mediator * _mediator ;
    texture_id _texture_id ;
    texel_data _texel ;
    num_whole _origin_x ;
    num_whole _origin_y ;
} ;

template < typename mediator >
shy_engine_rasterizer < mediator > :: shy_engine_rasterizer ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_whole ( _origin_x , 0 ) ;
    platform :: math_make_num_whole ( _origin_y , 0 ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_triangle ( int_32 x1_int_32 , int_32 y1_int_32 , int_32 x2_int_32 , int_32 y2_int_32 , int_32 x3_int_32 , int_32 y3_int_32 )
{
    num_whole x1 ;
    num_whole y1 ;
    num_whole x2 ;
    num_whole y2 ;
    num_whole x3 ;
    num_whole y3 ;
    platform :: math_make_num_whole ( x1 , x1_int_32 ) ;
    platform :: math_make_num_whole ( y1 , y1_int_32 ) ;
    platform :: math_make_num_whole ( x2 , x2_int_32 ) ;
    platform :: math_make_num_whole ( y2 , y2_int_32 ) ;
    platform :: math_make_num_whole ( x3 , x3_int_32 ) ;
    platform :: math_make_num_whole ( y3 , y3_int_32 ) ;
    if ( platform :: condition_whole_greater_or_equal_to_whole ( y1 , y2 ) 
      && platform :: condition_whole_greater_or_equal_to_whole ( y2 , y3 )
       )
    {
        _rasterize_top_triangle_part    ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
        _rasterize_bottom_triangle_part ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
    }
    else if ( platform :: condition_whole_greater_or_equal_to_whole ( y1 , y3 ) 
           && platform :: condition_whole_greater_or_equal_to_whole ( y3 , y2 )
            )
    {
        _rasterize_top_triangle_part    ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
        _rasterize_bottom_triangle_part ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
    }
    else if ( platform :: condition_whole_greater_or_equal_to_whole ( y3 , y1 )
           && platform :: condition_whole_greater_or_equal_to_whole ( y1 , y2 )
            )
    {
        _rasterize_top_triangle_part    ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
        _rasterize_bottom_triangle_part ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
    }
    else if ( platform :: condition_whole_greater_or_equal_to_whole ( y3 , y2 )
           && platform :: condition_whole_greater_or_equal_to_whole ( y2 , y1 )
            )
    {
        _rasterize_top_triangle_part    ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
        _rasterize_bottom_triangle_part ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
    }
    else if ( platform :: condition_whole_greater_or_equal_to_whole ( y2 , y1 )
           && platform :: condition_whole_greater_or_equal_to_whole ( y1 , y3 )
            )
    {
        _rasterize_top_triangle_part    ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
        _rasterize_bottom_triangle_part ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
    }
    else if ( platform :: condition_whole_greater_or_equal_to_whole ( y2 , y3 ) 
           && platform :: condition_whole_greater_or_equal_to_whole ( y3 , y1 )
            )
    {
        _rasterize_top_triangle_part    ( x2 , y2 , x3 , y3 , x1 , y1 ) ;
        _rasterize_bottom_triangle_part ( x2 , y2 , x3 , y3 , x1 , y1 ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_ellipse_in_rect ( int_32 x1_int_32 , int_32 y1_int_32 , int_32 x2_int_32 , int_32 y2_int_32 )
{
    num_whole x1 ;
    num_whole x2 ;
    num_whole y1 ;
    num_whole y2 ;
    num_whole width ;
    num_whole height ;
    num_whole y_center ;
    num_whole x_center ;
    num_whole x_diff ;
    num_whole y_diff ;
    platform :: math_make_num_whole ( x1 , x1_int_32 ) ;
    platform :: math_make_num_whole ( x2 , x2_int_32 ) ;
    platform :: math_make_num_whole ( y1 , y1_int_32 ) ;
    platform :: math_make_num_whole ( y2 , y2_int_32 ) ;
    platform :: math_add_wholes ( y_center , y1 , y2 ) ;
    platform :: math_div_whole_by ( y_center , platform :: whole_2 ) ;
    platform :: math_add_wholes ( x_center , x1 , x2 ) ;
    platform :: math_div_whole_by ( x_center , platform :: whole_2 ) ;
    platform :: math_sub_wholes ( x_diff , x1 , x2 ) ;
    platform :: math_sub_wholes ( y_diff , y1 , y2 ) ;
    _mediator -> math_abs_whole ( width , x_diff ) ;
    _mediator -> math_abs_whole ( height , y_diff ) ;
    
    num_whole half_width ;
    num_whole half_height ;
    platform :: math_div_wholes ( half_width , width , platform :: whole_2 ) ;    
    platform :: math_div_wholes ( half_height , height , platform :: whole_2 ) ;
    _rasterize_bresenham_ellipse ( x_center , y_center , half_width , half_height ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_rect ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 )
{
    rasterize_triangle ( x1 , y1 , x1 , y2 , x2 , y2 ) ;
    rasterize_triangle ( x1 , y1 , x2 , y1 , x2 , y2 ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_use_texture ( texture_id arg_texture_id , int_32 origin_x , int_32 origin_y )
{
    _texture_id = arg_texture_id ;
    platform :: math_make_num_whole ( _origin_x , origin_x ) ;
    platform :: math_make_num_whole ( _origin_y , origin_y ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_use_texel ( const texel_data & texel )
{
    _texel = texel ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_horizontal_line ( num_whole x1 , num_whole x2 , num_whole y )
{
    num_whole left ;
    num_whole right ;
    _mediator -> math_min_whole ( left , x1 , x2 ) ;
    _mediator -> math_max_whole ( right , x1 , x2 ) ;
    for ( num_whole x = left 
        ; platform :: condition_whole_less_or_equal_to_whole ( x , right )
        ; platform :: math_inc_whole ( x )
        )
    {
        num_whole x_plus_origin_x ;
        num_whole y_plus_origin_y ;
        platform :: math_add_wholes ( x_plus_origin_x , x , _origin_x ) ;
        platform :: math_add_wholes ( y_plus_origin_y , y , _origin_y ) ;
        _mediator -> texture_set_texel ( _texture_id , x_plus_origin_x , y_plus_origin_y , _texel ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_top_triangle_part
    ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom )
{
    for ( num_whole y = y_top 
        ; platform :: condition_whole_greater_or_equal_to_whole ( y , y_mid ) 
        ; platform :: math_dec_whole ( y )
        )
    {
        num_whole x_top_mid ;
        if ( platform :: condition_wholes_are_equal ( y_top , y_mid ) ) 
            x_top_mid = x_mid ;
        else
        {
            num_whole y_top_minus_y ;
            num_whole y_top_minus_y_mid ;
            num_whole x_mid_minus_x_top ;
            platform :: math_sub_wholes ( y_top_minus_y , y_top , y ) ;
            platform :: math_sub_wholes ( y_top_minus_y_mid , y_top , y_mid ) ;
            platform :: math_sub_wholes ( x_mid_minus_x_top , x_mid , x_top ) ;
            platform :: math_mul_wholes ( x_top_mid , y_top_minus_y , x_mid_minus_x_top ) ;
            platform :: math_div_whole_by ( x_top_mid , y_top_minus_y_mid ) ;
            platform :: math_add_to_whole ( x_top_mid , x_top ) ;
        }
            
        num_whole x_top_bottom ;
        if ( platform :: condition_wholes_are_equal ( y_top , y_bottom ) ) 
            x_top_bottom = x_top ;
        else
        {
            num_whole y_top_minus_y ;
            num_whole y_top_minus_y_bottom ;
            num_whole x_bottom_minus_x_top ;
            platform :: math_sub_wholes ( y_top_minus_y , y_top , y ) ;
            platform :: math_sub_wholes ( y_top_minus_y_bottom , y_top , y_bottom ) ;
            platform :: math_sub_wholes ( x_bottom_minus_x_top , x_bottom , x_top ) ;
            platform :: math_mul_wholes ( x_top_bottom , y_top_minus_y , x_bottom_minus_x_top ) ;
            platform :: math_div_whole_by ( x_top_bottom , y_top_minus_y_bottom ) ;
            platform :: math_add_to_whole ( x_top_bottom , x_top ) ;
        }
            
        _rasterize_horizontal_line ( x_top_mid , x_top_bottom , y ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_bottom_triangle_part
    ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom )
{
    for ( num_whole y = y_mid 
        ; platform :: condition_whole_greater_or_equal_to_whole ( y , y_bottom )
        ; platform :: math_dec_whole ( y )
        )
    {
        num_whole x_mid_bottom ;
        if ( platform :: condition_wholes_are_equal ( y_mid , y_bottom ) )
            x_mid_bottom = x_mid ;
        else
        {
            num_whole y_mid_minus_y ;
            num_whole y_mid_minus_y_bottom ;
            num_whole x_bottom_minus_x_mid ;
            platform :: math_sub_wholes ( y_mid_minus_y , y_mid , y ) ;
            platform :: math_sub_wholes ( y_mid_minus_y_bottom , y_mid , y_bottom ) ;
            platform :: math_sub_wholes ( x_bottom_minus_x_mid , x_bottom , x_mid ) ;
            platform :: math_mul_wholes ( x_mid_bottom , y_mid_minus_y , x_bottom_minus_x_mid ) ;
            platform :: math_div_whole_by ( x_mid_bottom , y_mid_minus_y_bottom ) ;
            platform :: math_add_to_whole ( x_mid_bottom , x_mid ) ;
        }
        
        num_whole x_top_bottom ;
        if ( platform :: condition_wholes_are_equal ( y_top , y_bottom ) )
            x_top_bottom = x_bottom ;
        else
        {
            num_whole y_top_minus_y ;
            num_whole y_top_minus_y_bottom ;
            num_whole x_bottom_minus_x_top ;
            platform :: math_sub_wholes ( y_top_minus_y , y_top , y ) ;
            platform :: math_sub_wholes ( y_top_minus_y_bottom , y_top , y_bottom ) ;
            platform :: math_sub_wholes ( x_bottom_minus_x_top , x_bottom , x_top ) ;
            platform :: math_mul_wholes ( x_top_bottom , y_top_minus_y , x_bottom_minus_x_top ) ;
            platform :: math_div_whole_by ( x_top_bottom , y_top_minus_y_bottom ) ;
            platform :: math_add_to_whole ( x_top_bottom , x_top ) ;
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
    
    platform :: math_mul_wholes ( x_radius_sq , x_radius , x_radius ) ;
    platform :: math_mul_wholes ( y_radius_sq , y_radius , y_radius ) ;
    platform :: math_mul_wholes ( x_radius_mul_2 , x_radius , platform :: whole_2 ) ;
    platform :: math_mul_wholes ( y_radius_mul_2 , y_radius , platform :: whole_2 ) ;
    platform :: math_mul_wholes ( two_a_square , x_radius_sq , platform :: whole_2 ) ;
    platform :: math_mul_wholes ( two_b_square , y_radius_sq , platform :: whole_2 ) ;

    x = x_radius ;
    y = platform :: whole_0 ;
    platform :: math_sub_wholes ( x_change , platform :: whole_1 , x_radius_mul_2 ) ;
    platform :: math_mul_whole_by ( x_change , y_radius_sq ) ;
    y_change = x_radius_sq ;
    ellipse_error = platform :: whole_0 ;
    platform :: math_mul_wholes ( stopping_x , two_b_square , x_radius ) ;    
    stopping_y = platform :: whole_0 ;
    
    while ( platform :: condition_whole_greater_or_equal_to_whole ( stopping_x , stopping_y ) )
    {
        num_whole cx_minus_x ;
        num_whole cx_plus_x ;
        num_whole cy_minus_y ;
        num_whole cy_plus_y ;
        num_whole ellipse_error_mul_2_plus_x_change ;
        platform :: math_sub_wholes ( cx_minus_x , cx , x ) ;
        platform :: math_add_wholes ( cx_plus_x , cx , x ) ;
        platform :: math_sub_wholes ( cy_minus_y , cy , y ) ;
        platform :: math_add_wholes ( cy_plus_y , cy , y ) ;
    
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_minus_y ) ;
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_plus_y ) ;
        
        platform :: math_inc_whole ( y ) ;
        platform :: math_add_to_whole ( stopping_y , two_a_square ) ;
        platform :: math_add_to_whole ( ellipse_error , y_change ) ;
        platform :: math_add_to_whole ( y_change , two_a_square ) ;
        platform :: math_mul_wholes ( ellipse_error_mul_2_plus_x_change , ellipse_error , platform :: whole_2 ) ;
        platform :: math_add_to_whole ( ellipse_error_mul_2_plus_x_change , x_change ) ;
        if ( platform :: condition_whole_greater_than_zero ( ellipse_error_mul_2_plus_x_change ) )
        {
            platform :: math_dec_whole ( x ) ;
            platform :: math_sub_from_whole ( stopping_x , two_b_square ) ;
            platform :: math_add_to_whole ( ellipse_error , x_change ) ;
            platform :: math_add_to_whole ( x_change , two_b_square ) ;
        }
    }
    
    x = platform :: whole_0 ;
    y = y_radius ;
    x_change = y_radius_sq ;
    platform :: math_sub_wholes ( y_change , platform :: whole_1 , y_radius_mul_2 ) ;
    platform :: math_mul_whole_by ( y_change , x_radius_sq ) ;
    ellipse_error = platform :: whole_0 ;
    stopping_x = platform :: whole_0 ;
    platform :: math_mul_wholes ( stopping_y , two_a_square , y_radius ) ;
    
    while ( platform :: condition_whole_less_or_equal_to_whole ( stopping_x , stopping_y ) )
    {
        num_whole cx_minus_x ;
        num_whole cx_plus_x ;
        num_whole cy_minus_y ;
        num_whole cy_plus_y ;
        num_whole ellipse_error_mul_2_plus_y_change ;
        platform :: math_sub_wholes ( cx_minus_x , cx , x ) ;
        platform :: math_add_wholes ( cx_plus_x , cx , x ) ;
        platform :: math_sub_wholes ( cy_minus_y , cy , y ) ;
        platform :: math_add_wholes ( cy_plus_y , cy , y ) ;
        
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_minus_y ) ;
        _rasterize_horizontal_line ( cx_minus_x , cx_plus_x , cy_plus_y ) ;
        
        platform :: math_dec_whole ( x ) ;
        platform :: math_add_to_whole ( stopping_x , two_b_square ) ;
        platform :: math_add_to_whole ( ellipse_error , x_change ) ;
        platform :: math_add_to_whole ( x_change , two_b_square ) ;
        platform :: math_mul_wholes ( ellipse_error_mul_2_plus_y_change , ellipse_error , platform :: whole_2 ) ;
        platform :: math_add_to_whole ( ellipse_error_mul_2_plus_y_change , y_change ) ;
        if ( platform :: condition_whole_greater_than_zero ( ellipse_error_mul_2_plus_y_change ) )
        {
            platform :: math_dec_whole ( y ) ;
            platform :: math_sub_from_whole ( stopping_y , two_a_square ) ;
            platform :: math_add_to_whole ( ellipse_error , y_change ) ;
            platform :: math_add_to_whole ( y_change , two_a_square ) ;
        }
    }
}
