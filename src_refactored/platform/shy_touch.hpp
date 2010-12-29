#include "shy_touch.h"

bool shy_platform_touch :: _enabled = false ;
bool shy_platform_touch :: _occured = false ;
float shy_platform_touch :: _x = 0.0f ;
float shy_platform_touch :: _y = 0.0f ;

void shy_platform_touch :: enabled ( num_whole & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , ( int ) _enabled ) ;
}

void shy_platform_touch :: occured ( num_whole & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , ( int ) _occured ) ;
}

void shy_platform_touch :: x ( num_fract & result )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , _x ) ;
}

void shy_platform_touch :: y ( num_fract & result )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , _y ) ;
}

