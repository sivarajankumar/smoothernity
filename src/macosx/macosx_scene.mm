#import "macosx_scene.h"

@implementation shy_macosx_scene

- init
{
    self = [ super init ] ;
    if ( self )
	{
		shy_macosx_platform :: _sound_loader = [ [ shy_macosx_sound_loader alloc ] init ] ;
        shy_macosx_platform :: _texture_loader = [ [ shy_macosx_texture_loader alloc ] init ] ;
		_measurer = new shy_facade < shy_macosx_platform > ( ) ;
		_measurer -> init ( ) ;
	}
    return self ;
}

- ( void ) dealloc
{
    [ shy_macosx_platform :: _sound_loader release ] ;
    [ shy_macosx_platform :: _texture_loader release ] ;
    shy_macosx_platform :: _sound_loader = nil ;
    shy_macosx_platform :: _texture_loader = nil ;
	_measurer -> done ( ) ;
	delete _measurer ;
	_measurer = 0 ;
	
    [ super dealloc ] ;
}

- ( void ) set_viewport_rect : ( NSRect ) bounds
{
    glViewport 
		( bounds . origin . x 
		, bounds . origin . y 
		, bounds . size . width 
		, bounds . size . height 
		) ;
	_bounds = bounds ;
	if ( bounds . size . width > bounds . size . height )
	{
		shy_macosx_platform :: _aspect_width = bounds . size . width / bounds . size . height ;
		shy_macosx_platform :: _aspect_height = 1.0f ;
	}
	else
	{
		shy_macosx_platform :: _aspect_width = 1.0f ;
		shy_macosx_platform :: _aspect_height = bounds . size . height / bounds . size . width ;
	}
}

- ( void ) set_mouse_position : ( NSPoint ) position
{
	if ( _bounds . size . width > _bounds . size . height )
	{
		shy_macosx_platform :: _mouse_x = ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . height ;
		shy_macosx_platform :: _mouse_y = ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . height ;
	}
	else
	{
		shy_macosx_platform :: _mouse_x = ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . width ;
		shy_macosx_platform :: _mouse_y = ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . width ;
	}
}

- ( void ) mouse_left_button_down
{
	shy_macosx_platform :: _mouse_left_button_down = true ;
}

- ( void ) render
{
	_measurer -> render ( ) ;
	_measurer -> update ( ) ;
	shy_macosx_platform :: _mouse_left_button_down = false ;
    glFinish ( ) ;
}

- ( void ) video_mode_changed
{
    _measurer -> video_mode_changed ( ) ;
}

@end
