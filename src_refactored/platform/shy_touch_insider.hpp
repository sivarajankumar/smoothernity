#include "shy_touch_insider.h"

void shy_platform_touch_insider :: set_enabled ( bool enabled )
{
    so_called_platform_touch :: _enabled = enabled ;
}

void shy_platform_touch_insider :: set_occured ( bool button )
{
    so_called_platform_touch :: _occured = button ;
}

void shy_platform_touch_insider :: set_x ( float x )
{
    so_called_platform_touch :: _x = x ;
}

void shy_platform_touch_insider :: set_y ( float y )
{
    so_called_platform_touch :: _y = y ;
}

