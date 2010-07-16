template < typename platform_insider >
class shy_platform_mouse_dummy
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
	void left_button_down ( num_whole & result ) ;
    void x ( num_fract & result ) ;
    void y ( num_fract & result ) ;
} ;

template < typename platform_insider >
inline void shy_platform_mouse_dummy < platform_insider > :: left_button_down ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , false ) ;
}

template < typename platform_insider >
inline void shy_platform_mouse_dummy < platform_insider > :: x ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , 0 ) ;
}

template < typename platform_insider >
inline void shy_platform_mouse_dummy < platform_insider > :: y ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , 0 ) ;
}
