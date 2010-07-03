template < typename platform_insider >
class shy_win_platform_mouse
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
	static void left_button_down ( num_whole & result ) ;
	static void x ( num_fract & result ) ;
	static void y ( num_fract & result ) ;
} ;

template < typename platform_insider >
inline void shy_win_platform_mouse < platform_insider > :: left_button_down ( num_whole & result )
{
    platform_math_insider :: num_whole_unsafe_value_set ( result , false ) ;
}

template < typename platform_insider >
inline void shy_win_platform_mouse < platform_insider > :: x ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}

template < typename platform_insider >
inline void shy_win_platform_mouse < platform_insider > :: y ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}
