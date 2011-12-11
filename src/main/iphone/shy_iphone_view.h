#include <OpenGLES/ES1/gl.h>
#include <OpenGLES/ES1/glext.h>
#include <OpenAL/al.h>
#include <OpenAL/alc.h>
#include <QuartzCore/QuartzCore.h>
#include <UIKit/UIKit.h>

@interface EAGLView : UIView
{    
@private	
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
- ( void ) _update_touch_position : ( NSSet * ) touches ;

@end
