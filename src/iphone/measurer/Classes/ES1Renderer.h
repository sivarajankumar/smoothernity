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

#define COMPUTATION_STEPS 1
#define FRAMES_PER_SECOND 60
#define SLEEP_BETWEEN_STEPS_IN_SECONDS 0.004

template < typename T >
void swap_values ( T & a , T & b )
{
    T c = b ;
    b = a ;
    a = c ;
}

class shy_iphone_platform
{
public :
    typedef int int_32 ;
    typedef float float_32 ;
    
    class buffer_id
    {
        friend class shy_iphone_platform ;
    private :
        GLuint _buffer_id ;
    } ;
    
    class vertex_data
    {
        friend class shy_iphone_platform ;
    private :
        GLfloat _position [ 3 ] ;
        GLubyte _color [ 4 ] ;
    } ;
    
    class index_data
    {
        friend class shy_iphone_platform ;
    private :
        GLushort _index ;
    } ;

    class time_data
    {
        friend class shy_iphone_platform ;
    private :
        CFAbsoluteTime _time ;
    } ;
    
    class matrix_data
    {
        friend class shy_iphone_platform ;
    private :
        GLfloat _elements [ 16 ] ;
    } ;
    
    static void matrix_set_axis_x ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
    {
        matrix . _elements [ 0 ] = x ;
        matrix . _elements [ 1 ] = y ;
        matrix . _elements [ 2 ] = z ;
        matrix . _elements [ 3 ] = 0 ;
    }
    static void matrix_set_axis_y ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
    {
        matrix . _elements [ 4 ] = x ;
        matrix . _elements [ 5 ] = y ;
        matrix . _elements [ 6 ] = z ;
        matrix . _elements [ 7 ] = 0 ;
    }
    static void matrix_set_axis_z ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
    {
        matrix . _elements [  8 ] = x ;
        matrix . _elements [  9 ] = y ;
        matrix . _elements [ 10 ] = z ;
        matrix . _elements [ 11 ] = 0 ;
    }
    static void matrix_set_origin ( matrix_data & matrix , float_32 x , float_32 y , float_32 z )
    {
        matrix . _elements [ 12 ] = x ;
        matrix . _elements [ 13 ] = y ;
        matrix . _elements [ 14 ] = z ;
        matrix . _elements [ 15 ] = 1 ;
    }
    static void matrix_identity ( matrix_data & matrix )
    {
        for ( int i = 0 ; i < 16 ; i ++ )
        {
            if ( i == 0 || i == 5 || i == 10 || i == 15 )
                matrix . _elements [ i ] = 1 ;
            else
                matrix . _elements [ i ] = 0 ;
        }
    }
    static void matrix_inverse_rotation_translation ( matrix_data & matrix )
    {
        swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
        swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
        swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
        matrix . _elements [ 12 ] = - matrix . _elements [ 12 ] ;
        matrix . _elements [ 13 ] = - matrix . _elements [ 13 ] ;
        matrix . _elements [ 14 ] = - matrix . _elements [ 14 ] ;
    }
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
    static void render_create_buffer_id ( buffer_id & arg_buffer_id )
    {
        glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    }
    static void render_load_vertex_buffer ( const buffer_id & arg_buffer_id , int_32 elements , vertex_data * data )
    {
		glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
		glBufferData
            ( GL_ARRAY_BUFFER 
            , ( GLsizeiptr ) ( sizeof ( vertex_data ) * ( unsigned int ) elements ) 
            , data
            , GL_STATIC_DRAW 
            ) ;
    }
    static void render_set_vertex_position ( vertex_data & vertex , float_32 x , float_32 y , float_32 z )
    {
        vertex . _position [ 0 ] = ( GLfloat ) x ;
        vertex . _position [ 1 ] = ( GLfloat ) y ;
        vertex . _position [ 2 ] = ( GLfloat ) z ;
    }
    static void render_set_vertex_color ( vertex_data & vertex , int_32 r , int_32 g , int_32 b , int_32 a )
    {
        vertex . _color [ 0 ] = ( GLubyte ) r ;
        vertex . _color [ 1 ] = ( GLubyte ) g ;
        vertex . _color [ 2 ] = ( GLubyte ) b ;
        vertex . _color [ 3 ] = ( GLubyte ) a ;
    }
    static void render_load_index_buffer ( const buffer_id & arg_buffer_id , int_32 elements , index_data * data )
    {
		glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
		glBufferData
            ( GL_ELEMENT_ARRAY_BUFFER
            , ( GLsizeiptr ) ( sizeof ( index_data ) * ( unsigned int ) elements )
            , data
            , GL_STATIC_DRAW
            ) ;
    }
    static void render_set_index_value ( index_data & data , int_32 index )
    {
        data . _index = ( GLushort ) index ;
    }
    static void render_select_modelview_matrix ( )
    {
        glMatrixMode ( GL_MODELVIEW ) ;
    }
    static void render_matrix_identity ( )
    {
        glLoadIdentity ( ) ;
    }
    static void render_matrix_translate ( float_32 x , float_32 y , float_32 z )
    {
        glTranslatef ( ( GLfloat ) x , ( GLfloat ) y , ( GLfloat ) z ) ;
    }
    static void render_matrix_scale ( float_32 x , float_32 y , float_32 z )
    {
        glScalef ( ( GLfloat ) x , ( GLfloat ) y , ( GLfloat ) z ) ;
    }
    static void render_matrix_rotate ( float_32 angle , float_32 x , float_32 y , float_32 z )
    {
        glRotatef ( ( GLfloat ) angle , ( GLfloat ) x , ( GLfloat ) y , ( GLfloat ) z ) ;
    }
    static void render_matrix_load ( const matrix_data & matrix )
    {
        glLoadMatrixf ( matrix . _elements ) ;
    }
    static void render_draw_triangle_strip 
        ( const buffer_id & vertices_buffer 
        , const buffer_id & indices_buffer
        , int_32 indices_count
        )
    {
        glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
        glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
        glEnableClientState ( GL_VERTEX_ARRAY ) ;
        glVertexPointer ( 3 , GL_FLOAT , sizeof ( vertex_data ) , _vertex_position_offset ) ;
        glEnableClientState ( GL_COLOR_ARRAY ) ;
        glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( vertex_data ) , _vertex_color_offset ) ;
        glDrawElements ( GL_TRIANGLE_STRIP , ( GLsizei ) indices_count , GL_UNSIGNED_SHORT , ( void * ) 0 ) ;
    }
    static float_32 math_sin ( float_32 a )
    {
        return sinf ( a ) ;
    }
    static float_32 math_cos ( float_32 a )
    {
        return cosf ( a ) ;
    }
    static void time_get_current ( time_data & time )
    {
        time . _time = CFAbsoluteTimeGetCurrent ( ) ;
    }
    static int_32 time_diff_in_microseconds ( const time_data & time1 , const time_data & time2 )
    {
        CFAbsoluteTime diff = 0 ;
        if ( time1 . _time > time2 . _time )
            diff = time1 . _time - time2 . _time ;
        else
            diff = time2 . _time - time1 . _time ;
        return ( int_32 ) ( diff * ( CFAbsoluteTime ) 1000000 ) ;
    }
    static double debug_time_diff_in_seconds ( const time_data & time1 , const time_data & time2 )
    {
        if ( time1 . _time > time2 . _time )
            return time1 . _time - time2 . _time ;
        else
            return time2 . _time - time1 . _time ;
    }
    static int_32 max_update_steps ( )
    {
        return COMPUTATION_STEPS ;
    }
    static int_32 frames_per_second ( )
    {
        return FRAMES_PER_SECOND ;
    }
private :
    static vertex_data _reference_vertex ;
    static void * _vertex_position_offset ;
    static void * _vertex_color_offset ;
} ;

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
}

- (void) render;
- (BOOL) resizeFromLayer:(CAEAGLLayer *)layer;

@end
