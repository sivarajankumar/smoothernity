#include "macosx_scene.h"

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
        _platform_insider = new shy_macosx_platform_insider ( ) ;
        _platform = new shy_platform < shy_macosx_platform_insider > ( ) ;
        _platform_insider -> render_insider . unsafe_set_texture_loader ( _texture_loader ) ;
        _platform_insider -> sound_insider . unsafe_set_sound_loader ( _sound_loader ) ;
        _platform_insider -> register_platform_modules ( * _platform ) ;
		_measurer = new shy_facade < shy_platform < shy_macosx_platform_insider > > ( * _platform ) ;
		_measurer -> init ( ) ;
        NSLog ( @"platform part size = %u bytes" , sizeof ( shy_macosx_platform_insider ) ) ;
        NSLog ( @"common application part size = %u bytes" , sizeof ( shy_facade < shy_platform < shy_macosx_platform_insider > > ) ) ;
	}
    return self ;
}

- ( void ) dealloc
{
	_measurer -> done ( ) ;
	delete _measurer ;
	_measurer = 0 ;
    
    [ _sound_loader thread_stop ] ;
    [ _texture_loader thread_stop ] ;
    _sound_loader = nil ;
    _texture_loader = nil ;
    
    delete _platform ;
    delete _platform_insider ;
    _platform = 0 ;
    _platform_insider = 0 ;
	
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
		_platform_insider -> render_insider . unsafe_set_aspect_width ( bounds . size . width / bounds . size . height ) ;
		_platform_insider -> render_insider . unsafe_set_aspect_height ( 1.0f ) ;
	}
	else
	{
		_platform_insider -> render_insider . unsafe_set_aspect_width ( 1.0f ) ;
		_platform_insider -> render_insider . unsafe_set_aspect_height ( bounds . size . height / bounds . size . width ) ;
	}
}

- ( void ) set_mouse_position : ( NSPoint ) position
{
	if ( _bounds . size . width > _bounds . size . height )
	{
        _platform_insider -> mouse_insider . unsafe_set_x 
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . height ) ;
		_platform_insider -> mouse_insider . unsafe_set_y 
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . height ) ;
	}
	else
	{
        _platform_insider -> mouse_insider . unsafe_set_x
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . width ) ;
		_platform_insider -> mouse_insider . unsafe_set_y
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . width ) ;
	}
}

- ( void ) mouse_left_button_down
{
    _platform_insider -> mouse_insider . unsafe_set_left_button_down ( true ) ;
}

- ( void ) render
{
	_measurer -> render ( ) ;
	_measurer -> update ( ) ;
    _platform_insider -> mouse_insider . unsafe_set_left_button_down ( false ) ;
    glFinish ( ) ;
}

- ( void ) video_mode_changed
{
    _measurer -> video_mode_changed ( ) ;
}

@end
