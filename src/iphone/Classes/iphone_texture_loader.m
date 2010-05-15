#import "iphone_texture_loader.h"

@implementation shy_iphone_texture_loader

- ( id ) init
{
   	self = [ super init ] ;
    _is_ready = true ;
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

- ( void ) load_texture_from_png_resource : ( int ) resource_index
    to_buffer : ( void * ) buffer
    with_side_size_of : ( int ) side_size
{
    if ( _is_ready )
    {
        _is_ready = false ;
        _resource_index = resource_index ;
        _buffer = buffer ;
        _side_size = side_size ;
        [ self performSelectorInBackground : @selector ( _thread_main_method ) withObject : nil ] ;
    }
}

- ( void ) _thread_main_method
{
	[ NSThread sleepForTimeInterval : 0.1 ] ;
    NSAutoreleasePool * pool = [ [ NSAutoreleasePool alloc ] init ] ;
    
    NSUInteger width ;
    NSUInteger height ;
    NSURL * url = nil ;
    CGDataProviderRef src ;
    CGImageRef image ;
    CGContextRef context = nil ;
    CGColorSpaceRef color_space ;
    url = [ NSURL fileURLWithPath : [ [ NSBundle mainBundle ] pathForResource : 
        [ NSString stringWithFormat : @"texture_resource_%i" , _resource_index ] 
        ofType : @"png"
        ] ] ;
    src = CGDataProviderCreateWithURL ( ( CFURLRef ) url ) ;
    if ( src )
    {
        image = CGImageCreateWithPNGDataProvider ( src , 0 , false , kCGRenderingIntentDefault ) ;
        CGDataProviderRelease ( src ) ;
        width = CGImageGetWidth ( image ) ;
        height = CGImageGetHeight ( image ) ;
        if ( width == _side_size && height == _side_size )
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
    
    [ pool release ] ;
    _is_ready = true ;
}

@end
