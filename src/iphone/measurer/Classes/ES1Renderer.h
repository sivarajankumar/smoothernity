//
//  ES1Renderer.h
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "ESRenderer.h"

#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>

#include "iphone_platform.hpp"
#include "iphone_sound_loader.h"
#include "measurer_facade.hpp"

@interface ES1Renderer : NSObject <ESRenderer>
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
}

- (void) render;
- (BOOL) resizeFromLayer:(CAEAGLLayer *)layer;

@end
