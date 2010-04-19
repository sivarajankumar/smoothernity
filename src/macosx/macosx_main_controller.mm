#import "macosx_main_controller.h"
#import "macosx_opengl_view.h"
#import "macosx_scene.h"

#import <OpenGL/OpenGL.h>

@interface MainController ( AnimationMethods )
- ( BOOL ) is_animating ;
- ( void ) start_animation ;
- ( void ) stop_animation ;

- ( void ) start_animation_timer ;
- ( void ) stop_animation_timer ;
- ( void ) animation_timer_fired : ( NSTimer * ) timer ;
@end

@implementation MainController

- ( void ) awakeFromNib
{
    is_animating = NO ;
    [ self start_animation ] ;
}

- ( IBAction ) goFullScreen : ( id ) sender
{
    shy_macosx_scene * scene = [ openGLView scene ] ;
    CGLContextObj cgl_context ;
    CGDisplayErr err ;
    GLint old_swap_interval ;
    GLint new_swap_interval ;

    NSOpenGLPixelFormatAttribute attrs [ ] =
	{
        NSOpenGLPFAFullScreen ,
        NSOpenGLPFAScreenMask , CGDisplayIDToOpenGLDisplayMask ( kCGDirectMainDisplay ) ,
        NSOpenGLPFAColorSize , 24 ,
        NSOpenGLPFADepthSize , 16 ,
        NSOpenGLPFADoubleBuffer ,
        NSOpenGLPFAAccelerated ,
        0
    } ;
    GLint renderer_id ;
    NSOpenGLPixelFormat * pixel_format = [ [ NSOpenGLPixelFormat alloc ] initWithAttributes : attrs ] ;
    [ pixel_format getValues : & renderer_id forAttribute : NSOpenGLPFARendererID forVirtualScreen : 0 ] ;
    NSLog ( @"FullScreen pixel_format renderer_id = %08x" , ( unsigned ) renderer_id ) ;
    full_screen_context = [ [ NSOpenGLContext alloc ] 
		initWithFormat : pixel_format 
		shareContext : [ openGLView openGLContext ]
		] ;
    [ pixel_format release ] ;
    pixel_format = nil ;

    if ( full_screen_context == nil )
	{
        NSLog ( @"Failed to create full_screen_context" ) ;
        return ;
    }

    if ( [ self is_animating ] )
        [ self stop_animation_timer ] ;

    err = CGCaptureAllDisplays ( ) ;
    if ( err != CGDisplayNoErr )
	{
        [ full_screen_context release ] ;
        full_screen_context = nil ;
        return ;
    }

    [ full_screen_context setFullScreen ] ;
    [ full_screen_context makeCurrentContext ] ;

    cgl_context = CGLGetCurrentContext ( ) ;
    CGLGetParameter ( cgl_context , kCGLCPSwapInterval , & old_swap_interval ) ;
    new_swap_interval = 1 ;
    CGLSetParameter ( cgl_context , kCGLCPSwapInterval , & new_swap_interval ) ;

    [ scene set_viewport_rect : NSMakeRect 
		( 0 
		, 0 
		, CGDisplayPixelsWide ( kCGDirectMainDisplay ) 
		, CGDisplayPixelsHigh ( kCGDirectMainDisplay ) 
		) 
	] ;

    stay_in_full_screen_mode = YES ;
    while ( stay_in_full_screen_mode )
	{
        NSAutoreleasePool * pool = [ [ NSAutoreleasePool alloc ] init ] ;

        NSEvent * event ;
        while ( event = [ NSApp 
			nextEventMatchingMask : NSAnyEventMask 
			untilDate : [ NSDate distantPast ] 
			inMode : NSDefaultRunLoopMode 
			dequeue : YES
			] )
		{
            switch ( [ event type ] )
			{
                case NSLeftMouseDown :
                    [ self mouseDown : event ] ;
                    break ;
                case NSLeftMouseUp :
                    [ self mouseUp : event ] ;
                    break ;
                case NSLeftMouseDragged :
                    [ self mouseDragged : event ] ;
                    break ;
                case NSKeyDown :
                    [ self keyDown : event ] ;
                    break ;
                default :
                    break ;
            }
        }

        [ scene render ] ;
        [ full_screen_context flushBuffer ] ;

        [ pool release ] ;
    }
    
    glClearColor ( 0.0 , 0.0 , 0.0 , 0.0 ) ;
    glClear ( GL_COLOR_BUFFER_BIT ) ;
    [ full_screen_context flushBuffer ] ;
    glClear ( GL_COLOR_BUFFER_BIT ) ;
    [ full_screen_context flushBuffer ] ;

    CGLSetParameter ( cgl_context , kCGLCPSwapInterval , & old_swap_interval ) ;

    [ NSOpenGLContext clearCurrentContext ] ;
    [ full_screen_context clearDrawable ] ;
    [ full_screen_context release ] ;
    full_screen_context = nil ;

    CGReleaseAllDisplays ( ) ;

    [ openGLView setNeedsDisplay : YES ] ;

    if ( [ self is_animating ] )
        [ self start_animation_timer ] ;
}

- ( void ) keyDown : ( NSEvent * ) event
{
    unichar c = [ [ event charactersIgnoringModifiers ] characterAtIndex : 0 ] ;
    switch ( c )
	{
        case 27 :
            stay_in_full_screen_mode = NO ;
            break ;
        default :
            break ;
    }
}

- ( void ) mouseDown : ( NSEvent * ) the_event
{
//    shy_macosx_scene * scene = [ openGLView scene ] ;
//    NSPoint window_point = [ the_event locationInWindow ] ;
}

- (BOOL) is_in_full_screen_mode
{
    return full_screen_context != nil ;
}

@end

@implementation MainController ( AnimationMethods )

- ( BOOL ) is_animating
{
    return is_animating ;
}

- ( void ) start_animation
{
    if ( ! is_animating )
	{
        is_animating = YES ;
        if ( ! [ self is_in_full_screen_mode ] )
            [ self start_animation_timer ] ;
    }
}

- ( void ) stop_animation
{
    if ( is_animating )
        is_animating = NO ;
}

- ( void ) start_animation_timer
{
    [ NSTimer
		scheduledTimerWithTimeInterval : 0
		target : self
		selector : @selector ( animation_timer_fired : )
		userInfo : nil
		repeats : NO
	] ;
}

- ( void ) stop_animation_timer
{
}

- ( void ) animation_timer_fired : ( NSTimer * ) timer
{
	if ( is_animating )
	{
		[ openGLView render ] ;
		[ NSTimer
			scheduledTimerWithTimeInterval : 0
			target : self
			selector : @selector ( animation_timer_fired : )
			userInfo : nil
			repeats : NO
		] ;
	}
}

@end
