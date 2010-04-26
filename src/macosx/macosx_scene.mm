#import "macosx_scene.h"

@implementation shy_macosx_scene

- init
{
    self = [ super init ] ;
    if ( self )
	{
		shy_macosx_platform :: _sound_loader = [ [ shy_macosx_sound_loader alloc ] init ] ;
		measurer = new shy_facade < shy_macosx_platform > ( ) ;
		measurer -> init ( ) ;
	}
    return self ;
}

- ( void ) dealloc
{
    [ shy_macosx_platform :: _sound_loader release ] ;
    shy_macosx_platform :: _sound_loader = nil ;
	measurer -> done ( ) ;
	delete measurer ;
    [ super dealloc ] ;
}

- ( void ) set_viewport_rect : ( NSRect ) bounds
{
    glViewport ( bounds . origin . x , bounds . origin . y , bounds . size . width , bounds . size . height ) ;
	float width = bounds . size . width ;
	float height = bounds . size . height ;
	if ( width > height )
	{
		shy_macosx_platform :: _aspect_width = width / height ;
		shy_macosx_platform :: _aspect_height = 1.0f ;
	}
	else
	{
		shy_macosx_platform :: _aspect_width = 1.0f ;
		shy_macosx_platform :: _aspect_height = height / width ;
	}
}

- ( void ) render
{
	measurer -> render ( ) ;
	measurer -> update ( ) ;
    glFinish ( ) ;
}

@end
