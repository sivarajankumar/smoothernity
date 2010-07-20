#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>
#import <QuartzCore/QuartzCore.h>
#import <UIKit/UIKit.h>

#include "iphone_platform.hpp"
#include "../common/facade.hpp"

@interface EAGLView : UIView
{    
@private	
    shy_iphone_sound_loader * _sound_loader ;
    shy_iphone_texture_loader * _texture_loader ;
    shy_iphone_platform_insider * _platform_insider ;
	shy_facade < shy_platform < shy_iphone_platform_insider > > * _facade ;
	
	EAGLContext * _gl_context ;
	GLint _gl_backing_width;
	GLint _gl_backing_height;
	GLuint _gl_default_framebuffer;
    GLuint _gl_color_renderbuffer;
    GLuint _gl_depth_renderbuffer;
 
    CFAbsoluteTime _frame_time ;
          
	ALCcontext * _al_context;
	ALCdevice * _al_device;
    
	BOOL _animating;
}

- ( void ) start_animation ;
- ( void ) stop_animation ;
- ( void ) draw_view : ( id ) sender ;
- ( void ) _init_platform ;
- ( void ) _done_platform ;
- ( void ) _init_game ;
- ( void ) _done_game ;
- ( void ) _schedule_draw ;

@end
