#include "shy_macosx_scene.h"
#include "platform/shy_macosx_platform_render_insider.h"
#include "platform/shy_macosx_platform_sound_insider.h"
#include "platform/shy_macosx_platform_mouse_insider.h"
#include "../injections/shy_facade.h"

@implementation shy_macosx_scene

- init
{
    self = [ super init ] ;
    if ( self )
    {
        _sound_loader = [ [ shy_macosx_sound_loader alloc ] init ] ;
        _texture_loader = [ [ shy_macosx_texture_loader alloc ] init ] ;
        [ _sound_loader thread_run ] ;
        [ _texture_loader thread_run ] ;

        shy_macosx_platform_render_insider :: set_texture_loader ( _texture_loader ) ;
        shy_macosx_platform_sound_insider :: set_sound_loader ( _sound_loader ) ;
        shy_macosx_platform_mouse_insider :: set_left_button_down ( false ) ;
        shy_macosx_platform_mouse_insider :: set_enabled ( true ) ;
        
        so_called_facade :: init ( ) ;
        NSLog ( @"facade initialized" ) ;
    }
    return self ;
}

- ( void ) dealloc
{
    so_called_facade :: done ( ) ;

    shy_macosx_platform_render_insider :: set_texture_loader ( 0 ) ;
    shy_macosx_platform_sound_insider :: set_sound_loader ( 0 ) ;

    [ _sound_loader thread_stop ] ;
    [ _texture_loader thread_stop ] ;
    _sound_loader = nil ;
    _texture_loader = nil ;
    
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
        shy_macosx_platform_render_insider :: set_aspect_width ( bounds . size . width / bounds . size . height ) ;
        shy_macosx_platform_render_insider :: set_aspect_height ( 1.0f ) ;
    }
    else
    {
        shy_macosx_platform_render_insider :: set_aspect_width ( 1.0f ) ;
        shy_macosx_platform_render_insider :: set_aspect_height ( bounds . size . height / bounds . size . width ) ;
    }
}

- ( void ) set_mouse_position : ( NSPoint ) position
{
    if ( _bounds . size . width > _bounds . size . height )
    {
        shy_macosx_platform_mouse_insider :: set_x 
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . height ) ;
        shy_macosx_platform_mouse_insider :: set_y 
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . height ) ;
    }
    else
    {
        shy_macosx_platform_mouse_insider :: set_x
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . width ) ;
        shy_macosx_platform_mouse_insider :: set_y
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . width ) ;
    }
}

- ( void ) mouse_left_button_down
{
    shy_macosx_platform_mouse_insider :: set_left_button_down ( true ) ;
}

- ( void ) mouse_left_button_up
{
    shy_macosx_platform_mouse_insider :: set_left_button_down ( false ) ;
}

- ( void ) render
{
    so_called_facade :: update ( ) ;
    so_called_facade :: render ( ) ;
    glFinish ( ) ;
}

- ( void ) video_mode_changed
{
    so_called_facade :: video_mode_changed ( ) ;
}

@end
