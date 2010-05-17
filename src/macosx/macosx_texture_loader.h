#import <Cocoa/Cocoa.h>

@interface shy_macosx_texture_loader : NSObject
{
@private
    bool _is_ready ;
    bool _should_quit ;
    int _resource_index ;
    void * _buffer ;
    int _side_size ;
}

- ( void ) thread_run ;
- ( void ) thread_stop ;
- ( bool ) loader_ready ;
- ( void ) load_texture_from_png_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( int ) max_samples_count
    ;
- ( void ) _thread_main_method ;
- ( void ) _perform_load ;

@end
