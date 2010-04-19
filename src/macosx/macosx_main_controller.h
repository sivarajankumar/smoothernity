#import <Cocoa/Cocoa.h>

@class MyOpenGLView ;

@interface MainController : NSResponder
{
    BOOL is_animating ;
    NSTimer * animation_timer ;
    CFAbsoluteTime timeBefore ;

    BOOL stayInFullScreenMode ;
    NSOpenGLContext * fullScreenContext ;

    IBOutlet MyOpenGLView * openGLView ;
}
- ( IBAction ) goFullScreen : ( id ) sender ;
- ( BOOL ) isInFullScreenMode ;
@end
