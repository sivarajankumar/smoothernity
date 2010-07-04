#import "macosx_scene.h"

@implementation shy_macosx_scene

- init
{
    self = [ super init ] ;
    if ( self )
	{
		shy_macosx_platform_insider :: sound_loader = [ [ shy_macosx_sound_loader alloc ] init ] ;
        shy_macosx_platform_insider :: texture_loader = [ [ shy_macosx_texture_loader alloc ] init ] ;
        [ shy_macosx_platform_insider :: sound_loader thread_run ] ;
        [ shy_macosx_platform_insider :: texture_loader thread_run ] ;
		_measurer = new shy_facade < shy_macosx_platform > ( ) ;
		_measurer -> init ( ) ;
        NSLog ( @"common application part size = %u bytes" , sizeof ( shy_facade < shy_macosx_platform > ) ) ;
	}
    return self ;
}

- ( void ) dealloc
{
    [ shy_macosx_platform_insider :: sound_loader thread_stop ] ;
    [ shy_macosx_platform_insider :: texture_loader thread_stop ] ;
    shy_macosx_platform_insider :: sound_loader = nil ;
    shy_macosx_platform_insider :: texture_loader = nil ;
	_measurer -> done ( ) ;
	delete _measurer ;
	_measurer = 0 ;
	
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
		shy_macosx_platform_insider :: aspect_width = bounds . size . width / bounds . size . height ;
		shy_macosx_platform_insider :: aspect_height = 1.0f ;
	}
	else
	{
		shy_macosx_platform_insider :: aspect_width = 1.0f ;
		shy_macosx_platform_insider :: aspect_height = bounds . size . height / bounds . size . width ;
	}
}

- ( void ) set_mouse_position : ( NSPoint ) position
{
	if ( _bounds . size . width > _bounds . size . height )
	{
		shy_macosx_platform_insider :: mouse_x = ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . height ;
		shy_macosx_platform_insider :: mouse_y = ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . height ;
	}
	else
	{
		shy_macosx_platform_insider :: mouse_x = ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . width ;
		shy_macosx_platform_insider :: mouse_y = ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . width ;
	}
}

- ( void ) mouse_left_button_down
{
	shy_macosx_platform_insider :: mouse_left_button_down = true ;
}

- ( void ) render
{
	_measurer -> render ( ) ;
	_measurer -> update ( ) ;
	shy_macosx_platform_insider :: mouse_left_button_down = false ;
    glFinish ( ) ;
}

- ( void ) video_mode_changed
{
    _measurer -> video_mode_changed ( ) ;
}

@end
