#include "shy_mouse.h"

bool shy_platform_mouse :: _enabled = false ;
bool shy_platform_mouse :: _left_button_down = false ;
float shy_platform_mouse :: _x = 0.0f ;
float shy_platform_mouse :: _y = 0.0f ;

void shy_platform_mouse :: enabled ( num_whole & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , ( int ) _enabled ) ;
}

void shy_platform_mouse :: left_button_down ( num_whole & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , ( int ) _left_button_down ) ;
}

void shy_platform_mouse :: x ( num_fract & result )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , _x ) ;
}

void shy_platform_mouse :: y ( num_fract & result )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , _y ) ;
}
