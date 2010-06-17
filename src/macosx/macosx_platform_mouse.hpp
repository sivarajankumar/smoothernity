template < typename platform >
class shy_macosx_platform_mouse
{
    typedef typename platform :: _platform_insider _platform_insider ;
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: num_fract num_fract ;
    typedef typename platform :: num_whole num_whole ;
public :
	static void mouse_left_button_down ( num_whole & result ) ;
	static void mouse_x ( num_fract & result ) ;
	static void mouse_y ( num_fract & result ) ;
} ;

template < typename platform >
inline void shy_macosx_platform_mouse < platform > :: mouse_left_button_down ( num_whole & result )
{
    _platform_math_insider :: num_whole_unsafe_value_set ( result , _platform_insider :: _mouse_left_button_down != false ) ;
}

template < typename platform >
inline void shy_macosx_platform_mouse < platform > :: mouse_x ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , _platform_insider :: _mouse_x ) ;
}

template < typename platform >
inline void shy_macosx_platform_mouse < platform > :: mouse_y ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , _platform_insider :: _mouse_y ) ;
}
