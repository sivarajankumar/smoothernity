#import <Cocoa/Cocoa.h>

@class MyOpenGLView ;

@interface MainController : NSResponder
{
    BOOL is_animating ;
    NSTimer * animation_timer ;
    CFAbsoluteTime time_before ;

    BOOL stay_in_full_screen_mode ;
    NSOpenGLContext * fullScreenContext ;

    IBOutlet MyOpenGLView * openGLView ;
}
- ( IBAction ) goFullScreen : ( id ) sender ;
- ( BOOL ) isInFullScreenMode ;
@end
