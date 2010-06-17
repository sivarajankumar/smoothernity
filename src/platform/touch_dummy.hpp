template < typename platform >
class shy_platform_touch_dummy
{
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: num_fract num_fract ;
    typedef typename platform :: num_whole num_whole ;
public :
    static void touch_occured ( num_whole & result ) ;
    static void touch_x ( num_fract & result ) ;
    static void touch_y ( num_fract & result ) ;
} ;

template < typename platform >
inline void shy_platform_touch_dummy < platform > :: touch_occured ( num_whole & result )
{
    _platform_math_insider :: num_whole_unsafe_value_set ( result , false ) ;
}

template < typename platform >
inline void shy_platform_touch_dummy < platform > :: touch_x ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}

template < typename platform >
inline void shy_platform_touch_dummy < platform > :: touch_y ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}
