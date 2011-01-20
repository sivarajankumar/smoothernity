bool shy_platform_mouse_insider :: _enabled = false ;
bool shy_platform_mouse_insider :: _left_button_down = false ;
float shy_platform_mouse_insider :: _x = 0.0f ;
float shy_platform_mouse_insider :: _y = 0.0f ;

void shy_platform_mouse_insider :: set_left_button_down ( bool left_button_down )
{
    _left_button_down = left_button_down ;
}

void shy_platform_mouse_insider :: set_enabled ( bool enabled )
{
    _enabled = enabled ;
}

void shy_platform_mouse_insider :: set_x ( float x )
{
    _x = x ;
}

void shy_platform_mouse_insider :: set_y ( float y )
{
    _y = y ;
}

