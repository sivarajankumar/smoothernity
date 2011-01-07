bool shy_platform_touch_insider :: _enabled = false ;
bool shy_platform_touch_insider :: _occured = false ;
float shy_platform_touch_insider :: _x = 0.0f ;
float shy_platform_touch_insider :: _y = 0.0f ;

void shy_platform_touch_insider :: set_enabled ( bool enabled )
{
    _enabled = enabled ;
}

void shy_platform_touch_insider :: set_occured ( bool button )
{
    _occured = button ;
}

void shy_platform_touch_insider :: set_x ( float x )
{
    _x = x ;
}

void shy_platform_touch_insider :: set_y ( float y )
{
    _y = y ;
}

