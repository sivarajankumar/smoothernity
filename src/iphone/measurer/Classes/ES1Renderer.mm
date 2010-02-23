//
//  ES1Renderer.m
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "ES1Renderer.h"

shy_iphone_platform :: vertex_data shy_iphone_platform :: _reference_vertex ;
void * shy_iphone_platform :: _vertex_position_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex )
    ) ;
void * shy_iphone_platform :: _vertex_color_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex )
    ) ;

@implementation ES1Renderer

// Create an ES 1.1 context
- (id) init
{		
	if (self = [super init])
	{
		context = [[EAGLContext alloc] initWithAPI:kEAGLRenderingAPIOpenGLES1];
        
        if (!context || ![EAGLContext setCurrentContext:context])
		{
            [self release];
            return nil;
        }
		// Create default framebuffer object. The backing will be allocated for the current layer in -resizeFromLayer
		glGenFramebuffersOES(1, &defaultFramebuffer);
		glGenRenderbuffersOES(1, &colorRenderbuffer);
		glBindFramebufferOES(GL_FRAMEBUFFER_OES, defaultFramebuffer);
		glBindRenderbufferOES(GL_RENDERBUFFER_OES, colorRenderbuffer);
		glFramebufferRenderbufferOES(GL_FRAMEBUFFER_OES, GL_COLOR_ATTACHMENT0_OES, GL_RENDERBUFFER_OES, colorRenderbuffer);
		
		shyMeasurer . init ( ) ;		
	}
	
	return self;
}

- (void) render
{
    glViewport(0, 0, backingWidth, backingHeight);
	shyMeasurer . render ( ) ;
	for ( int i = 0; i < COMPUTATION_STEPS; i++ )
	{
		shyMeasurer . update ( i ) ;		
        [ NSThread sleepForTimeInterval : ( NSTimeInterval ) SLEEP_BETWEEN_STEPS_IN_SECONDS ];
	}
    [context presentRenderbuffer:GL_RENDERBUFFER_OES];	
}

- (BOOL) resizeFromLayer:(CAEAGLLayer *)layer
{	
	// Allocate color buffer backing based on the current layer size
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, colorRenderbuffer);
    [context renderbufferStorage:GL_RENDERBUFFER_OES fromDrawable:layer];
	glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_WIDTH_OES, &backingWidth);
    glGetRenderbufferParameterivOES(GL_RENDERBUFFER_OES, GL_RENDERBUFFER_HEIGHT_OES, &backingHeight);
	
    if (glCheckFramebufferStatusOES(GL_FRAMEBUFFER_OES) != GL_FRAMEBUFFER_COMPLETE_OES)
	{
		NSLog(@"Failed to make complete framebuffer object %x", glCheckFramebufferStatusOES(GL_FRAMEBUFFER_OES));
        return NO;
    }
    
    return YES;
}

- (void) dealloc
{
	shyMeasurer . done ( ) ;
	
	// Tear down GL
	if (defaultFramebuffer)
	{
		glDeleteFramebuffersOES(1, &defaultFramebuffer);
		defaultFramebuffer = 0;
	}

	if (colorRenderbuffer)
	{
		glDeleteRenderbuffersOES(1, &colorRenderbuffer);
		colorRenderbuffer = 0;
	}
	
	// Tear down context
	if ([EAGLContext currentContext] == context)
        [EAGLContext setCurrentContext:nil];
	
	[context release];
	context = nil;
	
	[super dealloc];
}

@end
