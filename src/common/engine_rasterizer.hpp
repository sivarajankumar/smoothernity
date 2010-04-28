template < typename mediator >
class shy_engine_rasterizer
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: texel_data texel_data ;
public :
    shy_engine_rasterizer ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    {
    }
    void rasterize_triangle
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x1
        , int_32 y1
        , int_32 x2
        , int_32 y2
        , int_32 x3
        , int_32 y3
        )
    {
        _rasterize_triangle ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 , x3 , y3 ) ;
    }
private :
    void _rasterize_top_triangle_part
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x_top
        , int_32 y_top
        , int_32 x_mid
        , int_32 y_mid
        , int_32 x_bottom
        , int_32 y_bottom
        )
    {
        for ( int_32 y = y_top ; y >= y_mid ; y -- )
        {
            int_32 x_top_mid    = ( y_top == y_mid    ) ? x_mid : x_top + ( ( y_top - y ) * ( x_mid    - x_top ) ) / ( y_top - y_mid    ) ;
            int_32 x_top_bottom = ( y_top == y_bottom ) ? x_top : x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
            int_32 x_left  = _mediator -> math_min ( x_top_mid , x_top_bottom ) ;
            int_32 x_right = _mediator -> math_max ( x_top_mid , x_top_bottom ) ;
            for ( int_32 x = x_left ; x <= x_right ; x ++ )
                starting_texel [ x + texels_in_row * y ] = filler ;
        }
    }
    void _rasterize_bottom_triangle_part
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x_top
        , int_32 y_top
        , int_32 x_mid
        , int_32 y_mid
        , int_32 x_bottom
        , int_32 y_bottom
        )
    {
        for ( int_32 y = y_mid ; y >= y_bottom ; y -- )
        {
            int_32 x_mid_bottom = ( y_mid == y_bottom ) ? x_mid    : x_mid + ( ( y_mid - y ) * ( x_bottom - x_mid ) ) / ( y_mid - y_bottom ) ;
            int_32 x_top_bottom = ( y_top == y_bottom ) ? x_bottom : x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
            int_32 x_left  = _mediator -> math_min ( x_mid_bottom , x_top_bottom ) ;
            int_32 x_right = _mediator -> math_max ( x_mid_bottom , x_top_bottom ) ;
            for ( int_32 x = x_left ; x <= x_right ; x ++ )
                starting_texel [ x + texels_in_row * y ] = filler ;
        }
    }
    void _rasterize_triangle
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x1
        , int_32 y1
        , int_32 x2
        , int_32 y2
        , int_32 x3
        , int_32 y3
        )
    {
        if ( y1 >= y2 && y2 >= y3 )
        {
            _rasterize_top_triangle_part    ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 , x3 , y3 ) ;
            _rasterize_bottom_triangle_part ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 , x3 , y3 ) ;
        }
        else if ( y1 >= y3 && y3 >= y2 )
        {
            _rasterize_top_triangle_part    ( starting_texel , filler , texels_in_row , x1 , y1 , x3 , y3 , x2 , y2 ) ;
            _rasterize_bottom_triangle_part ( starting_texel , filler , texels_in_row , x1 , y1 , x3 , y3 , x2 , y2 ) ;
        }
        else if ( y3 >= y1 && y1 >= y2 )
        {
            _rasterize_top_triangle_part    ( starting_texel , filler , texels_in_row , x3 , y3 , x1 , y1 , x2 , y2 ) ;
            _rasterize_bottom_triangle_part ( starting_texel , filler , texels_in_row , x3 , y3 , x1 , y1 , x2 , y2 ) ;
        }
        else if ( y3 >= y2 && y2 >= y1 )
        {
            _rasterize_top_triangle_part    ( starting_texel , filler , texels_in_row , x3 , y3 , x2 , y2 , x1 , y1 ) ;
            _rasterize_bottom_triangle_part ( starting_texel , filler , texels_in_row , x3 , y3 , x2 , y2 , x1 , y1 ) ;
        }
        else if ( y2 >= y1 && y1 >= y3 )
        {
            _rasterize_top_triangle_part    ( starting_texel , filler , texels_in_row , x2 , y2 , x1 , y1 , x3 , y3 ) ;
            _rasterize_bottom_triangle_part ( starting_texel , filler , texels_in_row , x2 , y2 , x1 , y1 , x3 , y3 ) ;
        }
        else if ( y2 >= y3 && y3 >= y1 )
        {
            _rasterize_top_triangle_part    ( starting_texel , filler , texels_in_row , x2 , y2 , x3 , y3 , x1 , y1 ) ;
            _rasterize_bottom_triangle_part ( starting_texel , filler , texels_in_row , x2 , y2 , x3 , y3 , x1 , y1 ) ;
        }
    }
private :
    mediator * _mediator ;
} ;
