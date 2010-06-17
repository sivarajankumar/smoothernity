template < typename platform_insider >
class shy_platform_touch_dummy
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    static void touch_occured ( num_whole & result ) ;
    static void touch_x ( num_fract & result ) ;
    static void touch_y ( num_fract & result ) ;
} ;

template < typename platform_insider >
inline void shy_platform_touch_dummy < platform_insider > :: touch_occured ( num_whole & result )
{
    platform_math_insider :: num_whole_unsafe_value_set ( result , false ) ;
}

template < typename platform_insider >
inline void shy_platform_touch_dummy < platform_insider > :: touch_x ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}

template < typename platform_insider >
inline void shy_platform_touch_dummy < platform_insider > :: touch_y ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}
