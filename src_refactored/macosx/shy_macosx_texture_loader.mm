#include "./shy_macosx_texture_loader.h"

@implementation shy_macosx_texture_loader

- ( id ) init
{
    self = [ super init ] ;
    _is_ready = true ;
    _should_quit = false ;
    _resource_index = 0 ;
    _buffer = 0 ;
    _side_size = 0 ;
    return self ;
}

- ( void ) dealloc
{
    [ super dealloc ] ;
}

- ( bool ) loader_ready
{
    return _is_ready ;
}

- ( void ) thread_run
{
    [ self performSelectorInBackground : @selector ( _thread_main_method ) withObject : nil ] ;
}

- ( void ) thread_stop
{
    _should_quit = true ;
}

- ( void ) load_texture_from_png_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( int ) side_size
{
    if ( _is_ready )
    {
        _resource_index = resource_index ;
        _buffer = buffer ;
        _side_size = side_size ;
        _is_ready = false ;
    }
}

- ( void ) _thread_main_method
{
    NSAutoreleasePool * pool = [ [ NSAutoreleasePool alloc ] init ] ;
    while ( ! _should_quit )
    {
        [ NSThread sleepForTimeInterval : 0.1 ] ;
        if ( ! _is_ready )
        {
            [ self _perform_load ] ;
            _is_ready = true ;
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
    CGImageSourceRef src ;
    CGImageRef image ;
    CGContextRef context = nil ;
    CGColorSpaceRef color_space ;
    GLubyte * data = ( GLubyte * ) _buffer ;
    url = [ NSURL fileURLWithPath : [ [ NSBundle mainBundle ] pathForResource : 
        [ NSString stringWithFormat : @"texture_resource_%i" , _resource_index ] 
        ofType : @"png"
        ] ] ;
    src = CGImageSourceCreateWithURL ( ( CFURLRef ) url , 0 ) ;
    if ( src )
    {
        image = CGImageSourceCreateImageAtIndex ( src , 0 , 0 ) ;
        CFRelease ( src ) ;
        width = CGImageGetWidth ( image ) ;
        height = CGImageGetHeight ( image ) ;
        if ( width == ( NSUInteger ) _side_size && height == ( NSUInteger ) _side_size )
        {
            color_space = CGColorSpaceCreateDeviceRGB ( ) ;
            context = CGBitmapContextCreate 
                ( data 
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
