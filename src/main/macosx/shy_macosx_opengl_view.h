#include <Cocoa/Cocoa.h>
#include <OpenAL/al.h>
#include <OpenAL/alc.h>

@class shy_macosx_scene ;

@interface shy_macosx_opengl_view : NSOpenGLView
{
    shy_macosx_scene * scene ;
    IBOutlet NSResponder * controller ;
    ALCcontext * _al_context;
    ALCdevice * _al_device;
}
- ( shy_macosx_scene * ) scene ;
- ( void ) render ;
@end
