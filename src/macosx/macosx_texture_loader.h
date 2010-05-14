#import <Cocoa/Cocoa.h>

@interface shy_macosx_texture_loader : NSObject
{
}

- ( bool ) loader_ready ;
- ( void ) load_texture_from_png_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( int ) max_samples_count
    ;

@end
