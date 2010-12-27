#include "macosx_scene.h"

#include <iostream>
#include <locale>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#include "../facade/loadable.hpp"
#include "../facade/static.hpp"

@implementation shy_macosx_scene

- init
{
    typedef shy_platform < shy_macosx_platform_insider > macosx_platform_type ;
    typedef shy_facade_static < macosx_platform_type > facade_static_type ;
    typedef shy_facade_loadable < macosx_platform_type > facade_loadable_type ;
    typedef shy_macosx_platform_insider :: platform_pointer platform_pointer ;

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
        
        platform_pointer :: pointer < const macosx_platform_type > platform_obj ;
        platform_pointer :: bind ( platform_obj , _platform_insider -> platform ) ;
        
        NSUserDefaults * args = [ NSUserDefaults standardUserDefaults ] ;

        if ( [ args boolForKey : @"load" ] )
        {
            NSLog ( @"loading data" ) ;
            facade_loadable_type * facade_loadable = new facade_loadable_type ( platform_obj ) ;
            std :: string loader_error = facade_loadable -> error ( ) ;
            if ( loader_error . empty ( ) )
                NSLog ( @"data loaded, code generated" ) ;
            else
                NSLog ( @"loader error: %s" , loader_error . c_str ( ) ) ;

            _facade = facade_loadable ;
        }
        else
		    _facade = new facade_static_type ( platform_obj ) ;

		_facade -> init ( ) ;
        NSLog ( @"platform object size = %u bytes" , sizeof ( shy_macosx_platform_insider ) ) ;
        NSLog ( @"loadable facade object size = %u bytes" , sizeof ( facade_loadable_type ) ) ;
        NSLog ( @"static facade object size = %u bytes" , sizeof ( facade_static_type ) ) ;
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
