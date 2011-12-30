#include <Cocoa/Cocoa.h>

@class shy_macosx_opengl_view ;

@interface shy_macosx_main_controller : NSResponder
{
    BOOL is_animating ;
    NSTimer * animation_timer ;
    CFAbsoluteTime time_before ;

    BOOL stay_in_full_screen_mode ;
    NSOpenGLContext * full_screen_context ;

    IBOutlet shy_macosx_opengl_view * openGLView ;
}
- ( IBAction ) goFullScreen : ( id ) sender ;
- ( BOOL ) is_in_full_screen_mode ;
@end
