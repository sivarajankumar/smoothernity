#import "macosx_scene.h"

@implementation shy_macosx_scene

- init
{
    self = [ super init ] ;
    if ( self )
	{
		measurer = new shy_facade < shy_macosx_platform > ( ) ;
		shy_macosx_platform :: _sound_loader = [ [ shy_macosx_sound_loader alloc ] init ] ;
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
	measurer -> init ( ) ;
}

- ( void ) render
{
	measurer -> render ( ) ;
	measurer -> update ( ) ;
    glFinish ( ) ;
}

@end
