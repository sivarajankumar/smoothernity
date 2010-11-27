#include "macosx_scene.h"

#include <sstream>
#include <map>
#include <string>
#include <locale>
#include <iostream>

#include "../common/reflection.hpp"
#include "../data/loader.hpp"

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
        _platform_insider -> render_insider . set_texture_loader ( _texture_loader ) ;
        _platform_insider -> sound_insider . set_sound_loader ( _sound_loader ) ;
        _platform_insider -> mouse_insider . set_left_button_down ( false ) ;
        _platform_insider -> mouse_insider . set_enabled ( true ) ;
        
        shy_macosx_platform_insider :: platform_pointer :: pointer < const shy_platform < shy_macosx_platform_insider > > platform_obj ;
        shy_macosx_platform_insider :: platform_pointer :: bind ( platform_obj , _platform_insider -> platform ) ;
        
		_facade = new shy_facade < shy_platform < shy_macosx_platform_insider > > ( platform_obj ) ;
        
        shy_data_loader < shy_data_loader_types < shy_facade < shy_platform < shy_macosx_platform_insider > > , shy_reflection > > loader ;
        loader . bind ( * _facade ) ;
        loader . parse ( "consts logic_fidget_stateless" ) ;
        loader . parse ( "should_render_fidget 1" ) ;
        loader . parse ( "fidget_r 1 / 3" ) ;
        loader . parse ( "fidget_g 1 / 3" ) ;
        loader . parse ( "fidget_b 1 / 1" ) ;
        
        std :: string parsing_error = loader . error ( ) ;
        if ( ! parsing_error . empty ( ) )
            std :: cerr << "parsing error: " << parsing_error << std :: endl ;

		_facade -> init ( ) ;
        NSLog ( @"platform part size = %u bytes" , sizeof ( shy_macosx_platform_insider ) ) ;
        NSLog ( @"common application part size = %u bytes" , sizeof ( shy_facade < shy_platform < shy_macosx_platform_insider > > ) ) ;
	}
    return self ;
}

- ( void ) dealloc
{
	_facade -> done ( ) ;
	delete _facade ;
	_facade = 0 ;
    
    [ _sound_loader thread_stop ] ;
    [ _texture_loader thread_stop ] ;
    _sound_loader = nil ;
    _texture_loader = nil ;
    
    delete _platform_insider ;
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
		_platform_insider -> render_insider . set_aspect_width ( bounds . size . width / bounds . size . height ) ;
		_platform_insider -> render_insider . set_aspect_height ( 1.0f ) ;
	}
	else
	{
		_platform_insider -> render_insider . set_aspect_width ( 1.0f ) ;
		_platform_insider -> render_insider . set_aspect_height ( bounds . size . height / bounds . size . width ) ;
	}
}

- ( void ) set_mouse_position : ( NSPoint ) position
{
	if ( _bounds . size . width > _bounds . size . height )
	{
        _platform_insider -> mouse_insider . set_x 
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . height ) ;
		_platform_insider -> mouse_insider . set_y 
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . height ) ;
	}
	else
	{
        _platform_insider -> mouse_insider . set_x
            ( ( 2.0f * ( position . x - _bounds . origin . x ) - _bounds . size . width ) / _bounds . size . width ) ;
		_platform_insider -> mouse_insider . set_y
            ( ( 2.0f * ( position . y - _bounds . origin . y ) - _bounds . size . height ) / _bounds . size . width ) ;
	}
}

- ( void ) mouse_left_button_down
{
    _platform_insider -> mouse_insider . set_left_button_down ( true ) ;
}

- ( void ) mouse_left_button_up
{
    _platform_insider -> mouse_insider . set_left_button_down ( false ) ;
}

- ( void ) render
{    
	_facade -> update ( ) ;
    _facade -> render ( ) ;
    glFinish ( ) ;
}

- ( void ) video_mode_changed
{
    _facade -> video_mode_changed ( ) ;
}

@end
