#import <Cocoa/Cocoa.h>

@class shy_macosx_scene ;

@interface MyOpenGLView : NSOpenGLView
{
    shy_macosx_scene * scene ;
    IBOutlet NSResponder * controller ;
}
- ( shy_macosx_scene * ) scene ;
- ( void ) render ;
@end
