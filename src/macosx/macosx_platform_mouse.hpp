template < typename platform_insider >
class shy_macosx_platform_mouse
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
	static void mouse_left_button_down ( num_whole & result ) ;
	static void mouse_x ( num_fract & result ) ;
	static void mouse_y ( num_fract & result ) ;
} ;

template < typename platform_insider >
inline void shy_macosx_platform_mouse < platform_insider > :: mouse_left_button_down ( num_whole & result )
{
    platform_math_insider :: num_whole_unsafe_value_set ( result , platform_insider :: mouse_left_button_down != false ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_mouse < platform_insider > :: mouse_x ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , platform_insider :: mouse_x ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_mouse < platform_insider > :: mouse_y ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , platform_insider :: mouse_y ) ;
}
