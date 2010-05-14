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
    NSUInteger width ;
    NSUInteger height ;
    NSURL * url = nil ;
    CGImageSourceRef src ;
    CGImageRef image ;
    CGContextRef context = nil ;
    CGColorSpaceRef color_space ;
    GLubyte * data = ( GLubyte * ) buffer ;
    url = [ NSURL fileURLWithPath : [ [ NSBundle mainBundle ] pathForResource : 
        [ NSString stringWithFormat : @"texture_resource_%i" , resource_index ] 
        ofType : @"png"
        ] ] ;
    src = CGImageSourceCreateWithURL ( ( CFURLRef ) url , 0 ) ;
    if ( src )
    {
        image = CGImageSourceCreateImageAtIndex ( src , 0 , 0 ) ;
        CFRelease ( src ) ;
        width = CGImageGetWidth ( image ) ;
        height = CGImageGetHeight ( image ) ;
        if ( width == side_size && height == side_size )
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
