#import <Cocoa/Cocoa.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>

@class shy_macosx_scene ;

@interface MyOpenGLView : NSOpenGLView
{
    shy_macosx_scene * scene ;
    IBOutlet NSResponder * controller ;
	ALCcontext * _al_context;
	ALCdevice * _al_device;
}
- ( shy_macosx_scene * ) scene ;
- ( void ) render ;
@end
