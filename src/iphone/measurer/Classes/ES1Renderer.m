//
//  ES1Renderer.m
//  measurer
//
//  Created by Oleg Plakhotnyuk on 23.12.09.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "ES1Renderer.h"

static const int MESH_SPANS = 5000;
static const float PI = 3.141592f;
static const GLubyte colorsR[] = { 255,   0, 0, 255 };
static const GLubyte colorsG[] = { 255, 255, 0,   0 };
static const GLubyte colorsB[] = {   0, 255, 0, 255 };
static const GLubyte colorsA[] = { 255, 255, 0, 255 };

@implementation ES1Renderer

// Create an ES 1.1 context
- (id) init
{
	vertexBuffer = 0;
	indexBuffer = 0;
	indicesCount = 0;
	
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
		
		for ( int i = 0; i < MESH_SPANS + 1; i++ )
		{
			float angle = ((float)i) * PI * 2.0f / (float)MESH_SPANS;
			float x = sinf ( angle );
			float z = cosf ( angle );
			vertices [ indicesCount ] . position [ 0 ] =     x;
			vertices [ indicesCount ] . position [ 1 ] =  1.0f;
			vertices [ indicesCount ] . position [ 2 ] =     z;
			vertices [ indicesCount ] . color [ 0 ] = colorsR [ indicesCount % 4 ];
			vertices [ indicesCount ] . color [ 1 ] = colorsG [ indicesCount % 4 ];
			vertices [ indicesCount ] . color [ 2 ] = colorsB [ indicesCount % 4 ];
			vertices [ indicesCount ] . color [ 3 ] = colorsA [ indicesCount % 4 ];
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
			vertices [ indicesCount ] . color [ 0 ] = colorsR [ indicesCount % 4 ];
			vertices [ indicesCount ] . color [ 1 ] = colorsG [ indicesCount % 4 ];
			vertices [ indicesCount ] . color [ 2 ] = colorsB [ indicesCount % 4 ];
			vertices [ indicesCount ] . color [ 3 ] = colorsA [ indicesCount % 4 ];
			indices [ indicesCount ] = indicesCount;
			indicesCount++;
			if (indicesCount >= VERTEX_BUFFER_MAX_SIZE)
			{
				NSLog(@"vertex buffer too small");
				break;
			}
		}
		NSLog(@"faces in mesh: %i", indicesCount-2);
		
		glGenBuffers(1, &vertexBuffer);
		glGenBuffers(1, &indexBuffer);
		
		glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer);
		glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
		
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
	}
	
	return self;
}

- (void) render
{
	static float transY = 0.0f;
	
	// This application only creates a single context which is already set current at this point.
	// This call is redundant, but needed if dealing with multiple contexts.
    [EAGLContext setCurrentContext:context];
    
	// This application only creates a single default framebuffer which is already bound at this point.
	// This call is redundant, but needed if dealing with multiple framebuffers.
    glBindFramebufferOES(GL_FRAMEBUFFER_OES, defaultFramebuffer);
    glViewport(0, 0, backingWidth, backingHeight);
	glEnable(GL_CULL_FACE);
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
	glFrustumf(-1.0f,1.0f,-1.515f,1.515f,1.0f,10.0f);
    glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(0.0f, 0.0f, -2.0f);
    glRotatef(transY, 0.0f, 1.0f, 0.0f);
	transY += 0.1f;
	
    glClearColor(0.5f, 0.5f, 0.5f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);
    
    glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, sizeof(vertexStruct), (void*)offsetof(vertexStruct,position));
    glEnableClientState(GL_COLOR_ARRAY);
    glColorPointer(4, GL_UNSIGNED_BYTE, sizeof(vertexStruct), (void*)offsetof(vertexStruct,color));
    glDrawElements(GL_TRIANGLE_STRIP, indicesCount, GL_UNSIGNED_SHORT, (void*)0);
	
	CFAbsoluteTime timeBegin = CFAbsoluteTimeGetCurrent ();
	const double desiredDelay = 0.008;
	while ( CFAbsoluteTimeGetCurrent() - timeBegin < ( CFAbsoluteTime ) desiredDelay )
	{
	}
	
	// This application only creates a single color renderbuffer which is already bound at this point.
	// This call is redundant, but needed if dealing with multiple renderbuffers.
    glBindRenderbufferOES(GL_RENDERBUFFER_OES, colorRenderbuffer);
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
