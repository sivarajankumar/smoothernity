void shy_platform_mouse :: enabled ( so_called_platform_math_num_whole_type & result )
{
    so_called_profile ( so_called_profile_platform_mouse :: enabled ( ) ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , ( so_called_lib_std_int32_t ) so_called_platform_mouse_insider :: _enabled ) ;
}

void shy_platform_mouse :: left_button_down ( so_called_platform_math_num_whole_type & result )
{
    so_called_profile ( so_called_profile_platform_mouse :: buttons ( ) ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , ( so_called_lib_std_int32_t ) so_called_platform_mouse_insider :: _left_button_down ) ;
}

void shy_platform_mouse :: x ( so_called_platform_math_num_fract_type & result )
{
    so_called_profile ( so_called_profile_platform_mouse :: coords ( ) ) ;
    so_called_platform_math_insider :: num_fract_value_set ( result , so_called_platform_mouse_insider :: _x ) ;
}

void shy_platform_mouse :: y ( so_called_platform_math_num_fract_type & result )
{
    so_called_profile ( so_called_profile_platform_mouse :: coords ( ) ) ;
    so_called_platform_math_insider :: num_fract_value_set ( result , so_called_platform_mouse_insider :: _y ) ;
}
