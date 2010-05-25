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
    void _rasterize_horizontal_line ( int_32 x1 , int_32 x2 , int_32 y ) ;
    void _rasterize_top_triangle_part ( int_32 x_top , int_32 y_top , int_32 x_mid , int_32 y_mid , int_32 x_bottom , int_32 y_bottom ) ;
    void _rasterize_bottom_triangle_part ( int_32 x_top , int_32 y_top , int_32 x_mid , int_32 y_mid , int_32 x_bottom , int_32 y_bottom ) ;
	void _rasterize_bresenham_ellipse ( int_32 cx , int_32 cy, int_32 x_radius, int_32 y_radius ) ;
private :
    mediator * _mediator ;
    texture_id _texture_id ;
    texel_data _texel ;
    int_32 _origin_x ;
    int_32 _origin_y ;
} ;

template < typename mediator >
shy_engine_rasterizer < mediator > :: shy_engine_rasterizer ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _origin_x ( 0 )
, _origin_y ( 0 )
{
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_triangle ( int_32 x1 , int_32 y1 , int_32 x2 , int_32 y2 , int_32 x3 , int_32 y3 )
{
    if ( y1 >= y2 && y2 >= y3 )
    {
        _rasterize_top_triangle_part    ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
        _rasterize_bottom_triangle_part ( x1 , y1 , x2 , y2 , x3 , y3 ) ;
    }
    else if ( y1 >= y3 && y3 >= y2 )
    {
        _rasterize_top_triangle_part    ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
        _rasterize_bottom_triangle_part ( x1 , y1 , x3 , y3 , x2 , y2 ) ;
    }
    else if ( y3 >= y1 && y1 >= y2 )
    {
        _rasterize_top_triangle_part    ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
        _rasterize_bottom_triangle_part ( x3 , y3 , x1 , y1 , x2 , y2 ) ;
    }
    else if ( y3 >= y2 && y2 >= y1 )
    {
        _rasterize_top_triangle_part    ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
        _rasterize_bottom_triangle_part ( x3 , y3 , x2 , y2 , x1 , y1 ) ;
    }
    else if ( y2 >= y1 && y1 >= y3 )
    {
        _rasterize_top_triangle_part    ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
        _rasterize_bottom_triangle_part ( x2 , y2 , x1 , y1 , x3 , y3 ) ;
    }
    else if ( y2 >= y3 && y3 >= y1 )
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
    _rasterize_bresenham_ellipse ( x_center . debug_to_int_32 ( ) , y_center . debug_to_int_32 ( ) , half_width . debug_to_int_32 ( ) , half_height . debug_to_int_32 ( ) ) ;
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
    _origin_x = origin_x ;
    _origin_y = origin_y ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_use_texel ( const texel_data & texel )
{
    _texel = texel ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_horizontal_line ( int_32 x1_int_32 , int_32 x2_int_32 , int_32 y_int_32 )
{
    num_whole num_origin_x ;
    num_whole num_origin_y ;
    num_whole left ;
    num_whole right ;
    num_whole x1 ;
    num_whole x2 ;
    num_whole y ;
    platform :: math_make_num_whole ( x1 , x1_int_32 ) ;
    platform :: math_make_num_whole ( x2 , x2_int_32 ) ;
    platform :: math_make_num_whole ( y , y_int_32 ) ;
    platform :: math_make_num_whole ( num_origin_x , _origin_x ) ;
    platform :: math_make_num_whole ( num_origin_y , _origin_y ) ;
    _mediator -> math_min_whole ( left , x1 , x2 ) ;
    _mediator -> math_max_whole ( right , x1 , x2 ) ;
    for ( num_whole x = left 
        ; platform :: condition_whole_less_or_equal_to_whole ( x , right )
        ; platform :: math_inc_whole ( x )
        )
    {
        num_whole x_plus_origin_x ;
        num_whole y_plus_origin_y ;
        platform :: math_add_wholes ( x_plus_origin_x , x , num_origin_x ) ;
        platform :: math_add_wholes ( y_plus_origin_y , y , num_origin_y ) ;
        _mediator -> texture_set_texel ( _texture_id , x_plus_origin_x . debug_to_int_32 ( ) , y_plus_origin_y . debug_to_int_32 ( ) , _texel ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_top_triangle_part
    ( int_32 x_top , int_32 y_top , int_32 x_mid , int_32 y_mid , int_32 x_bottom , int_32 y_bottom )
{
    for ( int_32 y = y_top ; y >= y_mid ; y -- )
    {
        int_32 x_top_mid    = ( y_top == y_mid    ) ? x_mid : x_top + ( ( y_top - y ) * ( x_mid    - x_top ) ) / ( y_top - y_mid    ) ;
        int_32 x_top_bottom = ( y_top == y_bottom ) ? x_top : x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
        _rasterize_horizontal_line ( x_top_mid , x_top_bottom , y ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_bottom_triangle_part
    ( int_32 x_top , int_32 y_top , int_32 x_mid , int_32 y_mid , int_32 x_bottom , int_32 y_bottom )
{
    for ( int_32 y = y_mid ; y >= y_bottom ; y -- )
    {
        int_32 x_mid_bottom = ( y_mid == y_bottom ) ? x_mid    : x_mid + ( ( y_mid - y ) * ( x_bottom - x_mid ) ) / ( y_mid - y_bottom ) ;
        int_32 x_top_bottom = ( y_top == y_bottom ) ? x_bottom : x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
        _rasterize_horizontal_line ( x_mid_bottom , x_top_bottom , y ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_bresenham_ellipse ( int_32 cx , int_32 cy, int_32 x_radius, int_32 y_radius )
{
    int_32 x , y ;
    int_32 x_change , y_change , ellipse_error , two_a_square , two_b_square , stopping_x , stopping_y ;

    two_a_square = 2 * x_radius * x_radius ;
    two_b_square = 2 * y_radius * y_radius ;
    
    x = x_radius ;
    y = 0 ;
    x_change = y_radius * y_radius * ( 1 - 2 * x_radius ) ;
    y_change = x_radius * x_radius;
    ellipse_error = 0 ;
    stopping_x = two_b_square * x_radius ;
    stopping_y = 0 ;
    
    while ( stopping_x >= stopping_y )
    {
        _rasterize_horizontal_line ( cx - x , cx + x , cy - y ) ;
        _rasterize_horizontal_line ( cx - x , cx + x , cy + y ) ;
        y ++ ;
        stopping_y += two_a_square ;
        ellipse_error += y_change ;
        y_change += two_a_square ;
        if ( 2 * ellipse_error + x_change > 0 )
        {
            x -- ;
            stopping_x -= two_b_square ;
            ellipse_error += x_change ;
            x_change += two_b_square ;
        }
    }
    
    x = 0 ;
    y = y_radius ;
    x_change = y_radius * y_radius ;
    y_change = x_radius * x_radius * ( 1 - 2 * y_radius ) ;
    ellipse_error = 0 ;
    stopping_x = 0 ;
    stopping_y = two_a_square * y_radius ;
    
    while ( stopping_x <= stopping_y )
    {
        _rasterize_horizontal_line ( cx - x , cx + x , cy - y ) ;
        _rasterize_horizontal_line ( cx - x , cx + x , cy + y ) ;
        x -- ;
        stopping_x += two_b_square ;
        ellipse_error += x_change ;
        x_change += two_b_square ;
        if ( 2 * ellipse_error + y_change > 0 )
        {
            y -- ;
            stopping_y -= two_a_square ;
            ellipse_error += y_change ;
            y_change += two_a_square ;
        }
    }
}
