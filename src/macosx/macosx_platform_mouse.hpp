inline void shy_macosx_platform :: mouse_left_button_down ( num_whole & result )
{
    result . _value = ( _mouse_left_button_down != false ) ;
}

inline void shy_macosx_platform :: mouse_x ( num_fract & result )
{
    result . _value = _mouse_x ;
}

inline void shy_macosx_platform :: mouse_y ( num_fract & result )
{
    result . _value = _mouse_y ;
}
