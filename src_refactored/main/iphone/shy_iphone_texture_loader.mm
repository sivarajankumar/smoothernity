#include "./iphone_texture_loader.h"

#include "../../injections/lib/std/false/shy_false.h"
#include "../../injections/lib/std/true/shy_true.h"

@implementation shy_iphone_texture_loader

- ( id ) init
{
   	self = [ super init ] ;
    _is_ready = so_called_lib_std_true ;
    _should_quit = so_called_lib_std_false ;
    _resource_index = 0 ;
    _buffer = 0 ;
    _side_size = 0 ;
	return self ;
}

- ( void ) dealloc
{
	[ super dealloc ] ;
}

- ( so_called_lib_std_bool ) loader_ready
{
    return _is_ready ;
}

- ( void ) thread_run
{
    [ self performSelectorInBackground : @selector ( _thread_main_method ) withObject : nil ] ;
}

- ( void ) thread_stop
{
    _should_quit = so_called_lib_std_true ;
}

- ( void ) load_texture_from_png_resource : ( so_called_lib_std_int32_t ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( so_called_lib_std_int32_t ) side_size
{
    if ( _is_ready )
    {
        _resource_index = resource_index ;
        _buffer = buffer ;
        _side_size = side_size ;
        _is_ready = so_called_lib_std_false ;
    }
}

- ( void ) _thread_main_method
{
    NSAutoreleasePool * pool = [ [ NSAutoreleasePool alloc ] init ] ;
    [ NSThread setThreadPriority : 0.0 ] ;
    while ( ! _should_quit )
    {
        [ NSThread sleepForTimeInterval : 0.1 ] ;
        if ( ! _is_ready )
        {
            [ self _perform_load ] ;
            _is_ready = so_called_lib_std_true ;
        }
    }
    [ pool release ] ;
    [ self release ] ;
}

- ( void ) _perform_load
{
    NSUInteger width ;
    NSUInteger height ;
    NSURL * url = nil ;
    CGDataProviderRef src ;
    CGImageRef image ;
    CGContextRef context = nil ;
    CGColorSpaceRef color_space ;
    url = [ NSURL fileURLWithPath : [ [ NSBundle mainBundle ] pathForResource : 
        [ NSString stringWithFormat : @"texture_resource_%i" , ( int ) _resource_index ] 
        ofType : @"png"
        ] ] ;
    src = CGDataProviderCreateWithURL ( ( CFURLRef ) url ) ;
    if ( src )
    {
        image = CGImageCreateWithPNGDataProvider ( src , 0 , false , kCGRenderingIntentDefault ) ;
        CGDataProviderRelease ( src ) ;
        width = CGImageGetWidth ( image ) ;
        height = CGImageGetHeight ( image ) ;
        if ( width == ( NSUInteger ) _side_size && height == ( NSUInteger ) _side_size )
        {
            color_space = CGColorSpaceCreateDeviceRGB ( ) ;
            context = CGBitmapContextCreate 
                ( _buffer 
                , width 
                , height 
                , 8 
                , 4 * width 
                , color_space 
                , kCGImageAlphaPremultipliedFirst | kCGBitmapByteOrder32Host 
                ) ;
            CGColorSpaceRelease ( color_space ) ;
            CGContextTranslateCTM ( context , 0 , height ) ;
            CGContextScaleCTM ( context , 1 , - 1 ) ;
            CGContextSetBlendMode ( context , kCGBlendModeCopy ) ;
            CGContextDrawImage ( context , CGRectMake ( 0 , 0 , width , height ) , image ) ;
            CGContextRelease ( context ) ;
        }
        CGImageRelease ( image ) ;
    }
}

@end
