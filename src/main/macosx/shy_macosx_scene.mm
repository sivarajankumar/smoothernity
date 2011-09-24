#include "./shy_macosx_scene.h"
#include "src/facade/shy_facade_injections.h"
#include "src/injections/lib/std/true/shy_true.h"
#include "src/injections/lib/std/false/shy_false.h"
#include "src/injections/platform/mouse/insider/shy_insider.h"
#include "src/injections/platform/render/insider/shy_insider.h"

@implementation shy_macosx_scene

- init
{
    self = [ super init ] ;
    if ( self )
    {
        so_called_platform_mouse_insider :: set_enabled ( so_called_lib_std_true ) ;
        so_called_facade :: application_init ( ) ;
        so_called_facade :: game_init ( ) ;
    }
    return self ;
}

- ( void ) dealloc
{
    [ super dealloc ] ;
}

- ( void ) set_viewport_rect : ( NSRect ) bounds
{
    glViewport 
        ( GLint ( bounds . origin . x )
        , GLint ( bounds . origin . y )
        , GLsizei ( bounds . size . width )
        , GLsizei ( bounds . size . height )
        ) ;
    _bounds = bounds ;
    if ( bounds . size . width > bounds . size . height )
    {
        so_called_platform_render_insider :: set_aspect_width ( bounds . size . width / bounds . size . height ) ;
        so_called_platform_render_insider :: set_aspect_height ( 1.0f ) ;
    }
    else
    {
        so_called_platform_render_insider :: set_aspect_width ( 1.0f ) ;
        so_called_platform_render_insider :: set_aspect_height ( bounds . size . height / bounds . size . width ) ;
    }
}

- ( void ) set_mouse_position : ( NSPoint ) position
{
    if ( _bounds . size . width > _bounds . size . height )
    {
        so_called_platform_mouse_insider :: set_x 
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . height ) ;
        so_called_platform_mouse_insider :: set_y 
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . height ) ;
    }
    else
    {
        so_called_platform_mouse_insider :: set_x
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . width ) ;
        so_called_platform_mouse_insider :: set_y
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . width ) ;
    }
}

- ( void ) mouse_left_button_down
{
    so_called_platform_mouse_insider :: set_left_button_down ( so_called_lib_std_true ) ;
}

- ( void ) mouse_left_button_up
{
    so_called_platform_mouse_insider :: set_left_button_down ( so_called_lib_std_false ) ;
}

- ( void ) render
{
    so_called_facade :: next_frame ( ) ;
    glFinish ( ) ;
}

- ( void ) video_mode_changed
{
    so_called_facade :: game_done ( ) ;
    so_called_facade :: game_init ( ) ;
}

@end
