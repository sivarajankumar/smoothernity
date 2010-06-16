inline void shy_macosx_platform :: mouse_left_button_down ( num_whole & result )
{
    _platform_math_insider :: num_whole_unsafe_value_set ( result , shy_macosx_platform_utility :: _mouse_left_button_down != false ) ;
}

inline void shy_macosx_platform :: mouse_x ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , shy_macosx_platform_utility :: _mouse_x ) ;
}

inline void shy_macosx_platform :: mouse_y ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , shy_macosx_platform_utility :: _mouse_y ) ;
}
