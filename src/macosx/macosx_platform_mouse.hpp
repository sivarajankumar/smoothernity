inline void shy_macosx_platform :: mouse_left_button_down ( num_whole & result )
{
    result . _value = ( _mouse_left_button_down != false ) ;
}

inline void shy_macosx_platform :: mouse_x ( float_32 & result )
{
    result = _mouse_x ;
}

inline void shy_macosx_platform :: mouse_y ( float_32 & result )
{
    result = _mouse_y ;
}
