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
    typedef float float_32 ;
    static void render_enable_face_culling ( )
    {
        glEnable ( GL_CULL_FACE ) ;
    }
    static void render_clear_screen ( float_32 r , float_32 g , float_32 b )
    {
        glClearColor ( ( GLfloat ) r , ( GLfloat ) g , ( GLfloat ) b , ( GLfloat ) 1 ) ;
        glClear ( GL_COLOR_BUFFER_BIT ) ;
    }
    static void render_projection_frustum ( float_32 left , float_32 right , float_32 bottom , float_32 top , float_32 near , float_32 far )
    {
        glMatrixMode ( GL_PROJECTION ) ;
        glLoadIdentity ( ) ;
        glFrustumf ( left , right , bottom , top , near , far ) ;
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
