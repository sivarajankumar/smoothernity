#import "macosx_texture_loader.h"

@implementation shy_macosx_texture_loader

- ( id ) init
{
   	self = [ super init ] ;
	return self ;
}

- ( void ) dealloc
{
	[ super dealloc ] ;
}

- ( bool ) loader_ready
{
    return true ;
}

- ( void ) load_texture_from_png_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( int ) side_size
{
}

@end
