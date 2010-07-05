template < typename platform_insider >
class shy_macosx_platform_mouse_insider
{
public :
    shy_macosx_platform_mouse_insider ( ) ;
    void set_platform_insider ( platform_insider * arg_platform_insider ) ;
	void set_left_button_down ( bool button ) ;
	void set_x ( float x ) ;
	void set_y ( float y ) ;
private :
    platform_insider * _platform_insider ;
} ;

template < typename platform_insider >
shy_macosx_platform_mouse_insider < platform_insider > :: shy_macosx_platform_mouse_insider ( )
: _platform_insider ( 0 )
{
}

template < typename platform_insider >
inline void shy_macosx_platform_mouse_insider < platform_insider > :: set_platform_insider ( platform_insider * arg_platform_insider )
{
    _platform_insider = arg_platform_insider ;
}

template < typename platform_insider >
inline void shy_macosx_platform_mouse_insider < platform_insider > :: set_left_button_down ( bool button )
{
    _platform_insider -> mouse . _left_button_down = button ;
}

template < typename platform_insider >
inline void shy_macosx_platform_mouse_insider < platform_insider > :: set_x ( float x )
{
    _platform_insider -> mouse . _x = x ;
}

template < typename platform_insider >
inline void shy_macosx_platform_mouse_insider < platform_insider > :: set_y ( float y )
{
    _platform_insider -> mouse . _y = y ;
}
