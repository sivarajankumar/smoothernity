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

#define VERTEX_BUFFER_MAX_SIZE 100000

typedef struct _vertexStruct
{
	GLfloat position[3];
	GLubyte color[4];
} vertexStruct;

@interface ES1Renderer : NSObject <ESRenderer>
{
@private
	EAGLContext *context;
	
	// The pixel dimensions of the CAEAGLLayer
	GLint backingWidth;
	GLint backingHeight;
	
	// The OpenGL names for the framebuffer and renderbuffer used to render to this view
	GLuint defaultFramebuffer, colorRenderbuffer;
	
	GLuint    vertexBuffer;
	GLuint    indexBuffer;	

	int indicesCount;
	vertexStruct vertices[VERTEX_BUFFER_MAX_SIZE];
	GLushort indices[VERTEX_BUFFER_MAX_SIZE];	
}

- (void) render;
- (BOOL) resizeFromLayer:(CAEAGLLayer *)layer;

@end
