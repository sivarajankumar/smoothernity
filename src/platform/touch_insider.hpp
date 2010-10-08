template < typename platform_insider >
class shy_platform_touch_insider
{
public :
    shy_platform_touch_insider ( ) ;
    void set_platform_insider ( platform_insider * ) ;
    void set_enabled ( bool ) ;
	void set_occured ( bool ) ;
	void set_x ( float ) ;
	void set_y ( float ) ;
private :
    platform_insider * _platform_insider ;
} ;

template < typename platform_insider >
shy_platform_touch_insider < platform_insider > :: shy_platform_touch_insider ( )
: _platform_insider ( 0 )
{
}

template < typename platform_insider >
inline void shy_platform_touch_insider < platform_insider > :: set_platform_insider ( platform_insider * arg_platform_insider )
{
    _platform_insider = arg_platform_insider ;
}

template < typename platform_insider >
inline void shy_platform_touch_insider < platform_insider > :: set_enabled ( bool enabled )
{
    _platform_insider -> touch . _enabled = enabled ;
}

template < typename platform_insider >
inline void shy_platform_touch_insider < platform_insider > :: set_occured ( bool button )
{
    _platform_insider -> touch . _occured = button ;
}

template < typename platform_insider >
inline void shy_platform_touch_insider < platform_insider > :: set_x ( float x )
{
    _platform_insider -> touch . _x = x ;
}

template < typename platform_insider >
inline void shy_platform_touch_insider < platform_insider > :: set_y ( float y )
{
    _platform_insider -> touch . _y = y ;
}
