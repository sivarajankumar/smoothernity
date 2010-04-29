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
    void rasterize_circle 
        ( texel_data * starting_texel
        , const texel_data & filler 
        , int_32 texels_in_row 
        , int_32 x1
        , int_32 y1 
        , int_32 x2
        , int_32 y2
        )
    {
        _rasterize_circle ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 ) ;
    }
private :
    void _rasterize_horizontal_line
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x1
        , int_32 x2
        , int_32 y
        )
    {
        int_32 left  = _mediator -> math_min ( x1 , x2 ) ;
        int_32 right = _mediator -> math_max ( x1 , x2 ) ;
        for ( int_32 x = left ; x <= right ; x ++ )
            starting_texel [ x + texels_in_row * y ] = filler ;
    }
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
            _rasterize_horizontal_line ( starting_texel , filler , texels_in_row , x_top_mid , x_top_bottom , y ) ;
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
            _rasterize_horizontal_line ( starting_texel , filler , texels_in_row , x_mid_bottom , x_top_bottom , y ) ;
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
    void _rasterize_circle 
        ( texel_data * starting_texel
        , const texel_data & filler 
        , int_32 texels_in_row 
        , int_32 x1
        , int_32 y1 
        , int_32 x2
        , int_32 y2
        )
    {
        int_32 top    = _mediator -> math_max ( y1 , y2 ) ;
        int_32 bottom = _mediator -> math_min ( y1 , y2 ) ;
        int_32 left   = _mediator -> math_min ( x1 , x2 ) ;
        int_32 right  = _mediator -> math_max ( x1 , x2 ) ;
        int_32 y_center = ( y1 + y2 ) / 2 ;
        int_32 x_center = ( x1 + x2 ) / 2 ;
        _ellipse ( starting_texel , filler , texels_in_row , x_center , y_center , ( right - left ) / 2 , ( top - bottom ) / 2 ) ;
    }
	void _ellipse ( texel_data * starting_texel , const texel_data & filler , int_32 texels_in_row , int_32 cx , int_32 cy, int_32 x_radius, int_32 y_radius )
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
			_plot_4_ellipse_points ( starting_texel , filler , texels_in_row , cx , cy , x , y ) ;
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
			_plot_4_ellipse_points ( starting_texel , filler , texels_in_row , cx , cy , x , y ) ;
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
	void _plot_4_ellipse_points ( texel_data * starting_texel , const texel_data & filler , int_32 texels_in_row , int_32 cx , int_32 cy , int_32 x , int_32 y )
    {
        _rasterize_horizontal_line ( starting_texel , filler , texels_in_row , cx - x , cx + x , cy - y ) ;
        _rasterize_horizontal_line ( starting_texel , filler , texels_in_row , cx - x , cx + x , cy + y ) ;
	}

private :
    mediator * _mediator ;
} ;
