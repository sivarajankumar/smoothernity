template < typename platform_insider >
class shy_platform_mouse_insider ;

template < typename platform_insider >
class shy_platform_mouse
{
    friend class shy_platform_mouse_insider < platform_insider > ;
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    shy_platform_mouse ( ) ;
    void enabled ( num_whole & ) ;
	void left_button_down ( num_whole & ) ;
	void x ( num_fract & ) ;
	void y ( num_fract & ) ;
private :
    bool _enabled ;
	bool _left_button_down ;
	float _x ;
	float _y ;
} ;

template < typename platform_insider >
shy_platform_mouse < platform_insider > :: shy_platform_mouse ( )
: _enabled ( false )
, _left_button_down ( false )
, _x ( 0 )
, _y ( 0 )
{
}

template < typename platform_insider >
inline void shy_platform_mouse < platform_insider > :: enabled ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , ( int ) _enabled ) ;
}

template < typename platform_insider >
inline void shy_platform_mouse < platform_insider > :: left_button_down ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , ( int ) _left_button_down ) ;
}

template < typename platform_insider >
inline void shy_platform_mouse < platform_insider > :: x ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _x ) ;
}

template < typename platform_insider >
inline void shy_platform_mouse < platform_insider > :: y ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _y ) ;
}
