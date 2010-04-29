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
        ellipse ( starting_texel , filler , texels_in_row , x_center , y_center , ( right - left ) / 2 , ( top - bottom ) / 2 ) ;
    }
	void ellipse ( texel_data * starting_texel , const texel_data & filler , int_32 texels_in_row , int CX, int CY, int XRadius, int YRadius )
    {
		int x,y;
		int XChange, YChange, EllipseError, TwoASquare, TwoBSquare, StoppingX, StoppingY;
	
		TwoASquare = 2*XRadius*XRadius;
		TwoBSquare = 2*YRadius*YRadius;
		
		x = XRadius;
		y = 0;
		XChange = YRadius*YRadius*(1-2*XRadius);
		YChange = XRadius*XRadius;
		EllipseError = 0;
		StoppingX = TwoBSquare*XRadius;
		StoppingY = 0;
		
		while ( StoppingX >= StoppingY ) {
			plot4EllipsePoints(starting_texel, filler, texels_in_row, CX, CY, x,y); // nakresli 4 body do 4 kvadrantov
			y++;
			StoppingY += TwoASquare;
			EllipseError += YChange;
		    YChange += TwoASquare;
				if ((2*EllipseError + XChange) > 0 ) {
					x--;
					StoppingX -= TwoBSquare;
					EllipseError += XChange;
					XChange += TwoBSquare;
				}	
		}
		
		x = 0;
		y = YRadius;
		XChange = YRadius*YRadius;
		YChange = XRadius*XRadius*(1-2*YRadius);
		EllipseError = 0;
		StoppingX = 0;
		StoppingY = TwoASquare*YRadius;
		
		while ( StoppingX <= StoppingY ) {
			plot4EllipsePoints(starting_texel, filler, texels_in_row, CX, CY, x,y);
			x--;
			StoppingX += TwoBSquare;
			EllipseError += XChange;
			XChange += TwoBSquare;
			if ((2*EllipseError + YChange) > 0 ) {
			  y--;
			  StoppingY -= TwoASquare;
			  EllipseError += YChange;
			  YChange += TwoASquare;
			}
		}
	}

	void plot4EllipsePoints(texel_data * starting_texel , const texel_data & filler , int_32 texels_in_row , int CX, int CY,int x, int y)
    {
		putPixel(starting_texel, filler, texels_in_row, CX+x, CY+y); // prvy kvadrant
		putPixel(starting_texel, filler, texels_in_row, CX-x, CY+y); // druhy
		putPixel(starting_texel, filler, texels_in_row, CX-x, CY-y); // treti
		putPixel(starting_texel, filler, texels_in_row, CX+x, CY-y); // stvrty		
	}
    
	void putPixel(texel_data * starting_texel , const texel_data & filler , int_32 texels_in_row , int x0, int y0)
    {
        starting_texel [ x0 + texels_in_row * y0 ] = filler ;
	}
	
private :
    mediator * _mediator ;
} ;
