inline void shy_macosx_platform :: touch_occured ( num_whole & result )
{
    _platform_math_insider :: num_whole_unsafe_value_set ( result , false ) ;
}

inline void shy_macosx_platform :: touch_x ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}

inline void shy_macosx_platform :: touch_y ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , 0 ) ;
}
