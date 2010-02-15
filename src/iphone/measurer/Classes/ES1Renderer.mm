//
//  ES1Renderer.m
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "ES1Renderer.h"

static const int BUFFERS_COUNT = 1;
static const int MESH_SPANS = 5000;
static const int COMPUTATION_STEPS = 3;
static const double COMPUTATION_STEP_DELAY = 0.002;
static const double SLEEP_BETWEEN_STEPS = 0.0001;
static const double COMPUTATION_STEP_DELAY_CHECK_ACCURACY = 0.01;
static const float PI = 3.141592f;
static const GLubyte colorsR[] = { 255, 255, 255,   0,   0,   0, 255 };
static const GLubyte colorsG[] = {   0, 128, 255, 255, 255,   0,   0 };
static const GLubyte colorsB[] = {   0,   0,   0,   0, 255, 255, 255 };
static const GLubyte colorsA[] = { 255, 255, 255, 255, 255, 255, 255 };
static const int MAX_FRAMES_WITHOUT_LOSSES = 200;

#define PROFILE_FRAME_LOSSES 1
#define PROFILE_COMPUTATION_DELAY 0

#if ( PROFILE_FRAME_LOSSES && ! PROFILE_COMPUTATION_DELAY )
	#define topR 192
	#define topG 255
	#define topB 192
	#define currentR 64
	#define currentG 255
	#define currentB 64
#elif ( PROFILE_COMPUTATION_DELAY && ! PROFILE_FRAME_LOSSES )
	#define topR 192
	#define topG 192
	#define topB 255
	#define currentR 64
	#define currentG 64
	#define currentB 255
#else
	#define topR 32
	#define topG 192
	#define topB 192
	#define currentR 64
	#define currentG 255
	#define currentB 255
#endif

@implementation ES1Renderer

// Create an ES 1.1 context
- (id) init
{
	meshVertexBuffer = 0;
	meshIndexBuffer = 0;
	topVertexBuffer = 0;
	topIndexBuffer = 0;
	currentVertexBuffer = 0;
	currentIndexBuffer = 0;
	indicesCount = 0;
	
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
		
		for ( int i = 0; i < MESH_SPANS + 1; i++ )
		{
			float angle = ((float)i) * PI * 2.0f / (float)MESH_SPANS;
			float x = sinf ( angle );
			float z = cosf ( angle );
			int color = ( i * 21 / ( MESH_SPANS + 1 ) ) % 7;
			int color1 = color;
			int color2 = ( color + 1 ) % 7;
			vertices [ indicesCount ] . position [ 0 ] =     x;
			vertices [ indicesCount ] . position [ 1 ] =  1.0f;
			vertices [ indicesCount ] . position [ 2 ] =     z;
			vertices [ indicesCount ] . color [ 0 ] = colorsR [ color1 ];
			vertices [ indicesCount ] . color [ 1 ] = colorsG [ color1 ];
			vertices [ indicesCount ] . color [ 2 ] = colorsB [ color1 ];
			vertices [ indicesCount ] . color [ 3 ] = colorsA [ color1 ];
			indices [ indicesCount ] = indicesCount;
			indicesCount++;
			if (indicesCount >= VERTEX_BUFFER_MAX_SIZE)
			{
				NSLog(@"vertex buffer too small");
				break;
			}
			vertices [ indicesCount ] . position [ 0 ] =     x;
			vertices [ indicesCount ] . position [ 1 ] = -1.0f;
			vertices [ indicesCount ] . position [ 2 ] =     z;
			vertices [ indicesCount ] . color [ 0 ] = colorsR [ color2 ];
			vertices [ indicesCount ] . color [ 1 ] = colorsG [ color2 ];
			vertices [ indicesCount ] . color [ 2 ] = colorsB [ color2 ];
			vertices [ indicesCount ] . color [ 3 ] = colorsA [ color2 ];
			indices [ indicesCount ] = indicesCount;
			indicesCount++;
			if (indicesCount >= VERTEX_BUFFER_MAX_SIZE)
			{
				NSLog(@"vertex buffer too small");
				break;
			}
		}
		NSLog(@"faces in mesh: %i", indicesCount-2);

		static const vertexStruct topVertices[] = {
		    -1.0f, -1.0f, 0.0f, topR, topG, topB, 255,
			 1.0f, -1.0f, 0.0f, topR, topG, topB, 255,
			-1.0f,  1.0f, 0.0f, topR, topG, topB, 255,
		     1.0f,  1.0f, 0.0f, topR, topG, topB, 255,
		};
		static const GLushort topIndices[] = { 0, 1, 2, 3 };
		
		static const vertexStruct currentVertices[] = {
		    -1.0f, -1.0f, 0.0f, currentR, currentG, currentB, 255,
			 1.0f, -1.0f, 0.0f, currentR, currentG, currentB, 255,
			-1.0f,  1.0f, 0.0f, currentR, currentG, currentB, 255,
			 1.0f,  1.0f, 0.0f, currentR, currentG, currentB, 255,
		};
		static const GLushort currentIndices[] = { 0, 1, 2, 3 };
		
		for ( int i = 0; i < BUFFERS_COUNT; i++ )
		{
			glGenBuffers(1, &meshVertexBuffer);
			glGenBuffers(1, &meshIndexBuffer);		
			glBindBuffer(GL_ARRAY_BUFFER, meshVertexBuffer);
			glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
			glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, meshIndexBuffer);
			glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
		}

		glGenBuffers(1, &topVertexBuffer);
		glGenBuffers(1, &topIndexBuffer);		
		glBindBuffer(GL_ARRAY_BUFFER, topVertexBuffer);
		glBufferData(GL_ARRAY_BUFFER, sizeof(topVertices), topVertices, GL_STATIC_DRAW);
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, topIndexBuffer);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(topIndices), topIndices, GL_STATIC_DRAW);

		glGenBuffers(1, &currentVertexBuffer);
		glGenBuffers(1, &currentIndexBuffer);		
		glBindBuffer(GL_ARRAY_BUFFER, currentVertexBuffer);
		glBufferData(GL_ARRAY_BUFFER, sizeof(currentVertices), currentVertices, GL_STATIC_DRAW);
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, currentIndexBuffer);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(currentIndices), currentIndices, GL_STATIC_DRAW);
	}
	
	return self;
}

- (void) render :(bool) frameMissed
{
    glViewport(0, 0, backingWidth, backingHeight);
	shyMeasurer . render ( ) ;
	
	static float transY = 0.0f;
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
	
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
	glFrustumf(-1.0f,1.0f,-1.515f,1.515f,1.0f,10.0f);
    glMatrixMode(GL_MODELVIEW);
	
	glLoadIdentity();
	glTranslatef(0.0f, -7.0f + ( 6.0f * topPos ), -2.0f);
	glScalef(4.0f, 4.0f, 4.0f);
    glBindBuffer(GL_ARRAY_BUFFER, topVertexBuffer);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, topIndexBuffer);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, sizeof(vertexStruct), (void*)offsetof(vertexStruct,position));
    glEnableClientState(GL_COLOR_ARRAY);
    glColorPointer(4, GL_UNSIGNED_BYTE, sizeof(vertexStruct), (void*)offsetof(vertexStruct,color));
    glDrawElements(GL_TRIANGLE_STRIP, 4, GL_UNSIGNED_SHORT, (void*)0);
	
	glLoadIdentity();
	glTranslatef(0.0f, -7.0f + ( 6.0f * curPos ), -2.0f);
	glScalef(4.0f, 4.0f, 4.0f);
    glBindBuffer(GL_ARRAY_BUFFER, currentVertexBuffer);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, currentIndexBuffer);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, sizeof(vertexStruct), (void*)offsetof(vertexStruct,position));
    glEnableClientState(GL_COLOR_ARRAY);
    glColorPointer(4, GL_UNSIGNED_BYTE, sizeof(vertexStruct), (void*)offsetof(vertexStruct,color));
    glDrawElements(GL_TRIANGLE_STRIP, 4, GL_UNSIGNED_SHORT, (void*)0);
	
	glLoadIdentity();
	glTranslatef(0.0f, 0.0f, -2.0f);
    glRotatef(transY, 0.0f, 1.0f, 0.0f);
	transY += 2.0f;
    glBindBuffer(GL_ARRAY_BUFFER, meshVertexBuffer);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, meshIndexBuffer);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, sizeof(vertexStruct), (void*)offsetof(vertexStruct,position));
    glEnableClientState(GL_COLOR_ARRAY);
    glColorPointer(4, GL_UNSIGNED_BYTE, sizeof(vertexStruct), (void*)offsetof(vertexStruct,color));
    glDrawElements(GL_TRIANGLE_STRIP, indicesCount, GL_UNSIGNED_SHORT, (void*)0);

	CFAbsoluteTime timeConsumed;
	for ( int i = 0; i < COMPUTATION_STEPS; i++ )
	{
		shyMeasurer . update ( i , COMPUTATION_STEPS ) ;
		CFAbsoluteTime timeBegin = CFAbsoluteTimeGetCurrent ();
		while ( CFAbsoluteTimeGetCurrent() - timeBegin < ( CFAbsoluteTime ) COMPUTATION_STEP_DELAY )
		{
		}
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
