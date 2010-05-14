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
    NSUInteger              width, height;
    NSURL                   *url = nil;
    CGImageSourceRef        src;
    CGImageRef              image;
    CGContextRef            context = nil;
    CGColorSpaceRef         colorSpace;
    GLubyte                 *data = (GLubyte*) buffer;
    
    url = [NSURL fileURLWithPath: [[NSBundle mainBundle] pathForResource:[ NSString stringWithFormat : @"texture_resource_%i" , resource_index ] ofType:@"png"]];
    src = CGImageSourceCreateWithURL((CFURLRef)url, NULL);
    
    if (!src) {
        NSLog(@"No image");
        return;
    }
    
    image = CGImageSourceCreateImageAtIndex(src, 0, NULL);
    CFRelease(src);
    
    width = CGImageGetWidth(image);
    height = CGImageGetHeight(image);
    
    colorSpace = CGColorSpaceCreateDeviceRGB();
    context = CGBitmapContextCreate(data, width, height, 8, 4 * width, colorSpace, kCGImageAlphaPremultipliedFirst | kCGBitmapByteOrder32Host);
    CGColorSpaceRelease(colorSpace);
    
    // Core Graphics referential is upside-down compared to OpenGL referential
    // Flip the Core Graphics context here
    // An alternative is to use flipped OpenGL texture coordinates when drawing textures
    CGContextTranslateCTM(context, 0.0, height);
    CGContextScaleCTM(context, 1.0, -1.0);
    
    // Set the blend mode to copy before drawing since the previous contents of memory aren't used. This avoids unnecessary blending.
    CGContextSetBlendMode(context, kCGBlendModeCopy);
    
    CGContextDrawImage(context, CGRectMake(0, 0, width, height), image);
    
    CGContextRelease(context);
    CGImageRelease(image);
}

@end
