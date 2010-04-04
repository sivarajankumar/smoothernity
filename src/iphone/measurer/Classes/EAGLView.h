#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>
#import <QuartzCore/QuartzCore.h>
#import <UIKit/UIKit.h>

#include "iphone_platform.hpp"
#include "measurer_facade.hpp"

@interface EAGLView : UIView
{    
@private	
	shy_measurer_facade < shy_iphone_platform > _shy_measurer ;
	
	EAGLContext * _gl_context ;
	GLint _gl_backing_width;
	GLint _gl_backing_height;
	GLuint _gl_default_framebuffer;
    GLuint _gl_color_renderbuffer;
    GLuint _gl_depth_renderbuffer;
    
	ALCcontext * _al_context;
	ALCdevice * _al_device;
    
	BOOL _animating;
}

- (void) startAnimation;
- (void) stopAnimation;
- (void) drawView:(id)sender;

@end
