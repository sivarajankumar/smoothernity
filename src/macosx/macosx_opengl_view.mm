#import "macosx_opengl_view.h"
#import "macosx_scene.h"

@implementation MyOpenGLView

- initWithFrame : ( NSRect ) frameRect
{
    NSOpenGLPixelFormatAttribute attrs [ ] = 
	{
        NSOpenGLPFANoRecovery ,
        NSOpenGLPFAColorSize , 24 ,
        NSOpenGLPFADepthSize , 16 ,
        NSOpenGLPFADoubleBuffer ,
        NSOpenGLPFAAccelerated ,
        0
    } ;
    GLint renderer_id ;
    NSOpenGLPixelFormat * pixel_format = [ [ NSOpenGLPixelFormat alloc ] initWithAttributes : attrs ] ;
    [ pixel_format getValues : & renderer_id forAttribute : NSOpenGLPFARendererID forVirtualScreen : 0 ] ;
    NSLog ( @"NSOpenGLView pixelFormat RendererID = %08x" , ( unsigned ) renderer_id ) ;
    self = [ super initWithFrame : frameRect pixelFormat : pixel_format ] ;
    if ( self )
        scene = [ [ shy_macosx_scene alloc ] init ] ;
    return self ;
}

- ( void ) dealloc
{
    [ scene release ] ;
    [ super dealloc ] ;
}

- ( shy_macosx_scene * ) scene
{
    return scene ;
}

- ( void ) drawRect : ( NSRect ) aRect
{
    [ scene render ] ;
    [ [ self openGLContext ] flushBuffer ] ;
}

- ( void ) reshape
{
    [ scene set_viewport_rect : [ self bounds ] ] ;
}

- ( BOOL ) acceptsFirstResponder
{
    return YES ;
}

- ( void ) keyDown : ( NSEvent * ) theEvent
{
    [ controller keyDown : theEvent ] ;
}

- ( void ) mouseDown : ( NSEvent * ) theEvent
{
    [ controller mouseDown : theEvent ] ;
}

@end
