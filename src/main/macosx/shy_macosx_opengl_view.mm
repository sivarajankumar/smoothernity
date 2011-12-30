#include "./shy_macosx_opengl_view.h"
#include "./shy_macosx_scene.h"

@implementation shy_macosx_opengl_view

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
    self = [ super initWithFrame : frameRect pixelFormat : pixel_format ] ;
    if ( self )
    {
        GLint swapInt = 1 ;
        [ [ self openGLContext ] setValues : & swapInt forParameter : NSOpenGLCPSwapInterval ] ;
        
        _al_device = alcOpenDevice ( NULL ) ;
        _al_context = alcCreateContext ( _al_device , NULL ) ;
        alcMakeContextCurrent ( _al_context ) ;
        
        scene = [ [ shy_macosx_scene alloc ] init ] ;
    }
    return self ;
}

- ( void ) dealloc
{
    [ scene release ] ;
    alcDestroyContext ( _al_context ) ;
    alcCloseDevice ( _al_device ) ;
    _al_context = nil ;
    _al_device = nil ;
    [ super dealloc ] ;
}

- ( shy_macosx_scene * ) scene
{
    return scene ;
}

- ( void ) drawRect : ( NSRect ) aRect
{
    [ self render ] ;
}

- ( void ) render
{
    NSPoint window_point = [ [ self window ] mouseLocationOutsideOfEventStream ] ;
    NSPoint view_point = [ self convertPoint : window_point fromView : nil ] ;
    [ scene set_mouse_position : view_point ] ;
    
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

- ( void ) mouseUp : ( NSEvent * ) theEvent
{
    [ controller mouseUp : theEvent ] ;
}

@end
