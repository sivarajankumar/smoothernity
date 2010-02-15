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

#import "measurer_facade.hpp"

#define VERTEX_BUFFER_MAX_SIZE 20000
#define MEMORY_POOL_SIZE 48*1024*1024

class shy_iphone_platform
{
public :
    typedef int int_32 ;
    static void render_enable_face_culling ( )
    {
        glEnable ( GL_CULL_FACE ) ;
    }
} ;

typedef struct _vertexStruct
{
	GLfloat position[3];
	GLubyte color[4];
} vertexStruct;

@interface ES1Renderer : NSObject <ESRenderer>
{
@private
	shy_measurer_facade < shy_iphone_platform > shyMeasurer ;
	
	EAGLContext *context;
	
	// The pixel dimensions of the CAEAGLLayer
	GLint backingWidth;
	GLint backingHeight;
	
	// The OpenGL names for the framebuffer and renderbuffer used to render to this view
	GLuint defaultFramebuffer, colorRenderbuffer;
	
	GLuint    meshVertexBuffer;
	GLuint    meshIndexBuffer;	

	GLuint    topVertexBuffer;
	GLuint    topIndexBuffer;
	
	GLuint    currentVertexBuffer;
	GLuint    currentIndexBuffer;
	
	int indicesCount;
	vertexStruct vertices[VERTEX_BUFFER_MAX_SIZE];
	GLushort indices[VERTEX_BUFFER_MAX_SIZE];	
	
	int fakeMemoryPool [ MEMORY_POOL_SIZE / 4 ];
}

- (void) render: (bool) frameMissed;
- (BOOL) resizeFromLayer:(CAEAGLLayer *)layer;

@end
