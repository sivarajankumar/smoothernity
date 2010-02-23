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
        
static const int COMPUTATION_STEPS = 3;
static const double COMPUTATION_STEP_DELAY = 0.002;
static const double SLEEP_BETWEEN_STEPS = 0.0001;
static const double COMPUTATION_STEP_DELAY_CHECK_ACCURACY = 0.01;
static const int MAX_FRAMES_WITHOUT_LOSSES = 200;

@implementation ES1Renderer

// Create an ES 1.1 context
- (id) init
{	
	for ( int i = 0; i < ( MEMORY_POOL_SIZE ) / sizeof(int); i++ )
		fakeMemoryPool [ i ] = i;
	
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

- (void) render :(bool) frameMissed
{
    glViewport(0, 0, backingWidth, backingHeight);
	shyMeasurer . render ( ) ;
	
	static int maxFramesWithoutLosses = 0;
	static int framesWithoutLosses = 0;
	static int bestResultExpirationFrames = 0;
	
	framesWithoutLosses++;
#if PROFILE_FRAME_LOSSES
	if ( frameMissed )
		framesWithoutLosses = 0;
#endif
	if ( framesWithoutLosses > maxFramesWithoutLosses )
	{
		maxFramesWithoutLosses = framesWithoutLosses;
		bestResultExpirationFrames = 0;
	}
	else
		bestResultExpirationFrames++;
	if ( bestResultExpirationFrames > MAX_FRAMES_WITHOUT_LOSSES )
		maxFramesWithoutLosses = 0;
	
	float curPos = ((float)framesWithoutLosses) / (float)MAX_FRAMES_WITHOUT_LOSSES;
	float topPos = ((float)maxFramesWithoutLosses) / (float)MAX_FRAMES_WITHOUT_LOSSES;
	if ( curPos > 1.0f )
		curPos = 1.0f;
	if ( topPos > 1.0f )
		topPos = 1.0f;
        
	CFAbsoluteTime timeConsumed;
	for ( int i = 0; i < COMPUTATION_STEPS; i++ )
	{
		CFAbsoluteTime timeBegin = CFAbsoluteTimeGetCurrent ();
		shyMeasurer . update ( i , COMPUTATION_STEPS ) ;
		timeConsumed += CFAbsoluteTimeGetCurrent() - timeBegin;
		
		if ( SLEEP_BETWEEN_STEPS > 0.0 )
			[ NSThread sleepForTimeInterval : ( NSTimeInterval ) SLEEP_BETWEEN_STEPS ];
	}
	
#if PROFILE_COMPUTATION_DELAY
	if ( timeConsumed > ( 1.0 + COMPUTATION_STEP_DELAY_CHECK_ACCURACY ) * COMPUTATION_STEP_DELAY * ( double ) COMPUTATION_STEPS )
		framesWithoutLosses = 0;
#endif
	
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
