#import "macosx_main_controller.h"
#import "macosx_opengl_view.h"
#import "macosx_scene.h"

#import <OpenGL/OpenGL.h>

@interface MainController (AnimationMethods)
- (BOOL) is_animating;
- (void) startAnimation;
- (void) stopAnimation;
- (void) toggleAnimation;

- (void) startAnimationTimer;
- (void) stopAnimationTimer;
- (void) animationTimerFired:(NSTimer *)timer;
@end

@implementation MainController

- (void) awakeFromNib
{
    is_animating = NO;
    [self startAnimation];
}

// Action method wired up to fire when the user clicks the "Go FullScreen" button.  We remain in this method until the user exits FullScreen mode.
- (IBAction) goFullScreen:(id)sender
{
    shy_macosx_scene *scene = [openGLView scene];
    CFAbsoluteTime timeNow;
    CGLContextObj cglContext;
    CGDisplayErr err;
    GLint oldSwapInterval;
    GLint newSwapInterval;

    // Pixel Format Attributes for the FullScreen NSOpenGLContext
    NSOpenGLPixelFormatAttribute attrs[] = {

        // Specify that we want a full-screen OpenGL context.
        NSOpenGLPFAFullScreen,

        // We may be on a multi-display system (and each screen may be driven by a different renderer), so we need to specify which screen we want to take over.  For this demo, we'll specify the main screen.
        NSOpenGLPFAScreenMask, CGDisplayIDToOpenGLDisplayMask(kCGDirectMainDisplay),

        // Attributes Common to FullScreen and non-FullScreen
        NSOpenGLPFAColorSize, 24,
        NSOpenGLPFADepthSize, 16,
        NSOpenGLPFADoubleBuffer,
        NSOpenGLPFAAccelerated,
        0
    };
    GLint rendererID;

    // Create the FullScreen NSOpenGLContext with the attributes listed above.
    NSOpenGLPixelFormat *pixelFormat = [[NSOpenGLPixelFormat alloc] initWithAttributes:attrs];
    
    // Just as a diagnostic, report the renderer ID that this pixel format binds to.  CGLRenderers.h contains a list of known renderers and their corresponding RendererID codes.
    [pixelFormat getValues:&rendererID forAttribute:NSOpenGLPFARendererID forVirtualScreen:0];
    NSLog(@"FullScreen pixelFormat RendererID = %08x", (unsigned)rendererID);

    // Create an NSOpenGLContext with the FullScreen pixel format.  By specifying the non-FullScreen context as our "shareContext", we automatically inherit all of the textures, display lists, and other OpenGL objects it has defined.
    full_screen_context = [[NSOpenGLContext alloc] initWithFormat:pixelFormat shareContext:[openGLView openGLContext]];
    [pixelFormat release];
    pixelFormat = nil;

    if (full_screen_context == nil) {
        NSLog(@"Failed to create full_screen_context");
        return;
    }

    // Pause animation in the OpenGL view.  While we're in full-screen mode, we'll drive the animation actively instead of using a timer callback.
    if ([self is_animating]) {
        [self stopAnimationTimer];
    }

    // Take control of the display where we're about to go FullScreen.
    err = CGCaptureAllDisplays();
    if (err != CGDisplayNoErr) {
        [full_screen_context release];
        full_screen_context = nil;
        return;
    }

    // Enter FullScreen mode and make our FullScreen context the active context for OpenGL commands.
    [full_screen_context setFullScreen];
    [full_screen_context makeCurrentContext];

    // Save the current swap interval so we can restore it later, and then set the new swap interval to lock us to the display's refresh rate.
    cglContext = CGLGetCurrentContext();
    CGLGetParameter(cglContext, kCGLCPSwapInterval, &oldSwapInterval);
    newSwapInterval = 1;
    CGLSetParameter(cglContext, kCGLCPSwapInterval, &newSwapInterval);

    // Tell the scene the dimensions of the area it's going to render to, so it can set up an appropriate viewport and viewing transformation.
    [scene set_viewport_rect:NSMakeRect(0, 0, CGDisplayPixelsWide(kCGDirectMainDisplay), CGDisplayPixelsHigh(kCGDirectMainDisplay))];

    // Now that we've got the screen, we enter a loop in which we alternately process input events and computer and render the next frame of our animation.  The shift here is from a model in which we passively receive events handed to us by the AppKit to one in which we are actively driving event processing.
    time_before = CFAbsoluteTimeGetCurrent();
    stay_in_full_screen_mode = YES;
    while (stay_in_full_screen_mode) {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

        // Check for and process input events.
        NSEvent *event;
        while (event = [NSApp nextEventMatchingMask:NSAnyEventMask untilDate:[NSDate distantPast] inMode:NSDefaultRunLoopMode dequeue:YES]) {
            switch ([event type]) {
                case NSLeftMouseDown:
                    [self mouseDown:event];
                    break;

                case NSLeftMouseUp:
                    [self mouseUp:event];
                    break;

                case NSLeftMouseDragged:
                    [self mouseDragged:event];
                    break;

                case NSKeyDown:
                    [self keyDown:event];
                    break;

                default:
                    break;
            }
        }

        // Update our animation.
        timeNow = CFAbsoluteTimeGetCurrent();
        time_before = timeNow;

        // Render a frame, and swap the front and back buffers.
        [scene render];
        [full_screen_context flushBuffer];

        // Clean up any autoreleased objects that were created this time through the loop.
        [pool release];
    }
    
    // Clear the front and back framebuffers before switching out of FullScreen mode.  (This is not strictly necessary, but avoids an untidy flash of garbage.)
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT);
    [full_screen_context flushBuffer];
    glClear(GL_COLOR_BUFFER_BIT);
    [full_screen_context flushBuffer];

    // Restore the previously set swap interval.
    CGLSetParameter(cglContext, kCGLCPSwapInterval, &oldSwapInterval);

    // Exit fullscreen mode and release our FullScreen NSOpenGLContext.
    [NSOpenGLContext clearCurrentContext];
    [full_screen_context clearDrawable];
    [full_screen_context release];
    full_screen_context = nil;

    // Release control of the display.
    CGReleaseAllDisplays();

    // Mark our view as needing drawing.  (The animation has advanced while we were in FullScreen mode, so its current contents are stale.)
    [openGLView setNeedsDisplay:YES];

    // Resume animation timer firings.
    if ([self is_animating]) {
        [self startAnimationTimer];
    }
}

- (void) keyDown:(NSEvent *)event
{
    unichar c = [[event charactersIgnoringModifiers] characterAtIndex:0];
    switch (c) {

        // [Esc] exits FullScreen mode.
        case 27:
            stay_in_full_screen_mode = NO;
            break;

        // [space] toggles rotation of the globe.
        case 32:
            [self toggleAnimation];
            break;

        default:
            break;
    }
}

// Holding the mouse button and dragging the mouse changes the "roll" angle (y-axis) and the direction from which sunlight is coming (x-axis).
- (void)mouseDown:(NSEvent *)theEvent
{
    shy_macosx_scene *scene = [openGLView scene];
    BOOL wasAnimating = [self is_animating];
    BOOL dragging = YES;
    NSPoint windowPoint;
    NSPoint lastWindowPoint = [theEvent locationInWindow];
    float dx, dy;

    if (wasAnimating) {
        [self stopAnimation];
    }
    while (dragging) {
        theEvent = [[openGLView window] nextEventMatchingMask:NSLeftMouseUpMask | NSLeftMouseDraggedMask];
        windowPoint = [theEvent locationInWindow];
        switch ([theEvent type]) {
            case NSLeftMouseUp:
                dragging = NO;
                break;

            case NSLeftMouseDragged:
                dx = windowPoint.x - lastWindowPoint.x;
                dy = windowPoint.y - lastWindowPoint.y;
                lastWindowPoint = windowPoint;

                // Render a frame.
                if (full_screen_context) {
                    [scene render];
                    [full_screen_context flushBuffer];
                } else {
                    [openGLView display];
                }
                break;

            default:
                break;
        }
    }
    if (wasAnimating) {
        [self startAnimation];
        time_before = CFAbsoluteTimeGetCurrent();
    }
}

- (BOOL) isInFullScreenMode
{
    return full_screen_context != nil;
}

@end

@implementation MainController (AnimationMethods)

- (BOOL) is_animating
{
    return is_animating;
}

- (void) startAnimation
{
    if (!is_animating) {
        is_animating = YES;
        if (![self isInFullScreenMode]) {
            [self startAnimationTimer];
        }
    }
}

- (void) stopAnimation
{
    if (is_animating) {
        if (animation_timer != nil) {
            [self stopAnimationTimer];
        }
        is_animating = NO;
    }
}

- (void) toggleAnimation
{
    if ([self is_animating]) {
        [self stopAnimation];
    } else {
        [self startAnimation];
    }
}

- (void) startAnimationTimer
{
    if (animation_timer == nil) {
        animation_timer = [[NSTimer scheduledTimerWithTimeInterval:0.017 target:self selector:@selector(animationTimerFired:) userInfo:nil repeats:YES] retain];
    }
}

- (void) stopAnimationTimer
{
    if (animation_timer != nil) {
        [animation_timer invalidate];
        [animation_timer release];
        animation_timer = nil;
    }
}

- (void) animationTimerFired:(NSTimer *)timer
{
    [openGLView setNeedsDisplay:YES];
}

@end

