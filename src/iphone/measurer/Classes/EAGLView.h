//
//  EAGLView.h
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>
#import <QuartzCore/QuartzCore.h>
#import <UIKit/UIKit.h>

#include "iphone_platform.hpp"
#include "iphone_sound_loader.h"
#include "measurer_facade.hpp"

// This class wraps the CAEAGLLayer from CoreAnimation into a convenient UIView subclass.
// The view content is basically an EAGL surface you render your OpenGL scene into.
// Note that setting the view non-opaque will only work if the EAGL surface has an alpha channel.
@interface EAGLView : UIView
{    
@private	
	shy_measurer_facade < shy_iphone_platform > shyMeasurer ;
	
	EAGLContext *context;
	
	// The pixel dimensions of the CAEAGLLayer
	GLint backingWidth;
	GLint backingHeight;
	
	// The OpenGL names for the framebuffer and renderbuffer used to render to this view
	GLuint defaultFramebuffer, colorRenderbuffer, depthRenderbuffer;
    
    // OpenAL 
	ALCcontext * mContext;
	ALCdevice * mDevice;
	BOOL animating;
}

@property (readonly, nonatomic, getter=isAnimating) BOOL animating;

- (void) startAnimation;
- (void) stopAnimation;
- (void) drawView:(id)sender;

@end
