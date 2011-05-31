#include <Foundation/NSBundle.h>

#include "../../injections/lib/std/bool/shy_bool.h"
#include "../../injections/lib/std/int32_t/shy_int32_t.h"

@interface shy_iphone_texture_loader : NSObject
{
@private
    so_called_lib_std_bool _is_ready ;
    so_called_lib_std_bool _should_quit ;
    so_called_lib_std_int32_t _resource_index ;
    void * _buffer ;
    so_called_lib_std_int32_t _side_size ;
}

- ( void ) thread_run ;
- ( void ) thread_stop ;
- ( so_called_lib_std_bool ) loader_ready ;
- ( void ) load_texture_from_png_resource : ( so_called_lib_std_int32_t ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( so_called_lib_std_int32_t ) max_samples_count
    ;
- ( void ) _thread_main_method ;
- ( void ) _perform_load ;

@end
