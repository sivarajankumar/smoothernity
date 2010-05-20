template < typename mediator >
class shy_engine_rasterizer
{
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: texel_data texel_data ;
public :
    shy_engine_rasterizer ( mediator * arg_mediator ) ;
    void rasterize_triangle ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 , num_whole x3 , num_whole y3 ) ;
    void rasterize_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
    void rasterize_ellipse_in_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
    void rasterize_use_texture ( texture_id arg_texture_id , num_whole origin_x , num_whole origin_y ) ;
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
void shy_engine_rasterizer < mediator > :: rasterize_triangle ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 , num_whole x3 , num_whole y3 )
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
void shy_engine_rasterizer < mediator > :: rasterize_ellipse_in_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    num_whole width ;
    num_whole height ;
    num_whole y_center = ( y1 + y2 ) / 2 ;
    num_whole x_center = ( x1 + x2 ) / 2 ;
    _mediator -> math_abs ( width , x1 - x2 ) ;
    _mediator -> math_abs ( height , y1 - y2 ) ;
    _rasterize_bresenham_ellipse ( x_center , y_center , width / 2 , height / 2 ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    rasterize_triangle ( x1 , y1 , x1 , y2 , x2 , y2 ) ;
    rasterize_triangle ( x1 , y1 , x2 , y1 , x2 , y2 ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: rasterize_use_texture ( texture_id arg_texture_id , num_whole origin_x , num_whole origin_y )
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
void shy_engine_rasterizer < mediator > :: _rasterize_horizontal_line ( num_whole x1 , num_whole x2 , num_whole y )
{
    num_whole left ;
    num_whole right ;
    _mediator -> math_min ( left , x1 , x2 ) ;
    _mediator -> math_max ( right , x1 , x2 ) ;
    for ( num_whole x = left ; x <= right ; x ++ )
        _mediator -> texture_set_texel ( _texture_id , x + _origin_x , y + _origin_y , _texel ) ;
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_top_triangle_part
    ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom )
{
    for ( num_whole y = y_top ; y >= y_mid ; y -- )
    {
        num_whole x_top_mid    = ( y_top == y_mid    ) ? x_mid : x_top + ( ( y_top - y ) * ( x_mid    - x_top ) ) / ( y_top - y_mid    ) ;
        num_whole x_top_bottom = ( y_top == y_bottom ) ? x_top : x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
        _rasterize_horizontal_line ( x_top_mid , x_top_bottom , y ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_bottom_triangle_part
    ( num_whole x_top , num_whole y_top , num_whole x_mid , num_whole y_mid , num_whole x_bottom , num_whole y_bottom )
{
    for ( num_whole y = y_mid ; y >= y_bottom ; y -- )
    {
        num_whole x_mid_bottom = ( y_mid == y_bottom ) ? x_mid    : x_mid + ( ( y_mid - y ) * ( x_bottom - x_mid ) ) / ( y_mid - y_bottom ) ;
        num_whole x_top_bottom = ( y_top == y_bottom ) ? x_bottom : x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
        _rasterize_horizontal_line ( x_mid_bottom , x_top_bottom , y ) ;
    }
}

template < typename mediator >
void shy_engine_rasterizer < mediator > :: _rasterize_bresenham_ellipse ( num_whole cx , num_whole cy, num_whole x_radius, num_whole y_radius )
{
    num_whole x , y ;
    num_whole x_change , y_change , ellipse_error , two_a_square , two_b_square , stopping_x , stopping_y ;

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
