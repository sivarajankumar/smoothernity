#pragma once

#import <OpenGLES/ES1/gl.h>
#import <OpenGLES/ES1/glext.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>
#import <QuartzCore/QuartzCore.h>

#define FRAMES_PER_SECOND 60
#define SOUND_FREQUENCY 44100

class shy_iphone_platform
{
public :
    typedef int int_32 ;
    typedef float float_32 ;
    
    class render_buffer_id
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
    
    class vector_data
    {
        friend class shy_iphone_platform ;
    private :
        float_32 _x ;
        float_32 _y ;
        float_32 _z ;
    } ;
    
    class sound_sample
    {
        friend class shy_iphone_platform ;
    private :
        ALubyte _value ;
    } ;
    
    class sound_buffer_id
    {
        friend class shy_iphone_platform ;
    private :
        ALuint _buffer_id ;
    } ;
    
    class sound_source_id
    {
        friend class shy_iphone_platform ;
    private :
        ALuint _source_id ;
    } ;
    
    static int_32 frames_per_second ( )
    {
        return FRAMES_PER_SECOND ;
    }
    
    //
    // vector
    //
    
    static vector_data vector_xyz ( float_32 x , float_32 y , float_32 z ) ;
    static float_32 vector_dot_product ( vector_data v1 , vector_data v2 ) ;
    static vector_data vector_cross_product ( vector_data v1 , vector_data v2 ) ;
    static vector_data vector_add ( vector_data v1 , vector_data v2 ) ;
    static vector_data vector_sub ( vector_data v1 , vector_data v2 ) ;
    static vector_data vector_mul ( vector_data v , float_32 f ) ;
    static float_32 vector_length ( vector_data v ) ;
    static vector_data vector_normalize ( vector_data v ) ;
    
    //
    // matrix
    //
    
    static void matrix_set_axis_x ( matrix_data & matrix , float_32 x , float_32 y , float_32 z ) ;
    static void matrix_set_axis_y ( matrix_data & matrix , float_32 x , float_32 y , float_32 z ) ;
    static void matrix_set_axis_z ( matrix_data & matrix , float_32 x , float_32 y , float_32 z ) ;
    static void matrix_set_origin ( matrix_data & matrix , float_32 x , float_32 y , float_32 z ) ;
    static void matrix_set_axis_x ( matrix_data & matrix , vector_data v ) ;
    static void matrix_set_axis_y ( matrix_data & matrix , vector_data v ) ;
    static void matrix_set_axis_z ( matrix_data & matrix , vector_data v ) ;
    static void matrix_set_origin ( matrix_data & matrix , vector_data v ) ;
    static vector_data matrix_get_axis_x ( const matrix_data & matrix ) ;
    static vector_data matrix_get_axis_y ( const matrix_data & matrix ) ;
    static vector_data matrix_get_axis_z ( const matrix_data & matrix ) ;
    static vector_data matrix_get_origin ( const matrix_data & matrix ) ;
    static void matrix_identity ( matrix_data & matrix ) ;
    static void matrix_inverse_rotation_translation ( matrix_data & matrix ) ;
    
    //
    // render
    //
    
    static void render_enable_face_culling ( ) ;
    static void render_enable_depth_test ( ) ;
    static void render_fog_linear ( float_32 near , float_32 far , float_32 r , float_32 g , float_32 b , float_32 a ) ;
    static void render_clear_screen ( float_32 r , float_32 g , float_32 b ) ;
    static void render_projection_frustum ( float_32 left , float_32 right , float_32 bottom , float_32 top , float_32 near , float_32 far ) ;
    static void render_create_buffer_id ( render_buffer_id & arg_buffer_id ) ;
    static void render_load_vertex_buffer ( const render_buffer_id & arg_buffer_id , int_32 elements , vertex_data * data ) ;
    static void render_set_vertex_position ( vertex_data & vertex , float_32 x , float_32 y , float_32 z ) ;
    static void render_set_vertex_color ( vertex_data & vertex , int_32 r , int_32 g , int_32 b , int_32 a ) ;
    static void render_load_index_buffer ( const render_buffer_id & arg_buffer_id , int_32 elements , index_data * data ) ;
    static void render_set_index_value ( index_data & data , int_32 index ) ;
    static void render_select_modelview_matrix ( ) ;
    static void render_matrix_identity ( ) ;
    static void render_matrix_translate ( float_32 x , float_32 y , float_32 z ) ;
    static void render_matrix_scale ( float_32 x , float_32 y , float_32 z ) ;
    static void render_matrix_rotate ( float_32 angle , float_32 x , float_32 y , float_32 z ) ;
    static void render_matrix_load ( const matrix_data & matrix ) ;
    static void render_matrix_mult ( const matrix_data & matrix ) ;
    static void render_matrix_push ( ) ;
    static void render_matrix_pop ( ) ;
    static void render_draw_triangle_strip 
        ( const render_buffer_id & vertices_buffer 
        , const render_buffer_id & indices_buffer
        , int_32 indices_count
        ) ;
    static void render_draw_triangle_fan
        ( const render_buffer_id & vertices_buffer 
        , const render_buffer_id & indices_buffer
        , int_32 indices_count
        ) ;
    
    //
    // sound
    //
    
    static void sound_set_listener_position ( vector_data position ) ;
    static void sound_set_listener_velocity ( vector_data velocity ) ;
    static void sound_set_listener_orientation ( vector_data look_at , vector_data up ) ;
    static int_32 sound_samples_per_second ( ) ;
    static void sound_set_sample_value ( sound_sample & sample , float_32 value ) ;
    static sound_buffer_id sound_create_buffer ( sound_sample * samples , int_32 samples_count ) ;
    static sound_source_id sound_create_source ( ) ;
    static void sound_set_source_pitch ( const sound_source_id & source_id , float_32 pitch ) ;
    static void sound_set_source_gain ( const sound_source_id & source_id , float_32 gain ) ;
    static void sound_set_source_position ( const sound_source_id & source_id , vector_data position ) ;
    static void sound_set_source_velocity ( const sound_source_id & source_id , vector_data velocity ) ;
    static void sound_set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id ) ;
    static void sound_set_source_playback_looping ( const sound_source_id & source_id ) ;
    static void sound_set_source_playback_once ( const sound_source_id & source_id ) ;
    static void sound_source_play ( const sound_source_id & source_id ) ;
    static void sound_source_stop ( const sound_source_id & source_id ) ;

    //
    // math
    //
    
    static float_32 math_sin ( float_32 a ) ;
    static float_32 math_cos ( float_32 a ) ;
    
    //
    // time
    //
    
    static void time_get_current ( time_data & time ) ;
    static int_32 time_diff_in_microseconds ( const time_data & time1 , const time_data & time2 ) ;
    
private :
    static vertex_data _reference_vertex ;
    static void * _vertex_position_offset ;
    static void * _vertex_color_offset ;
} ;

template < typename T >
void swap_values ( T & a , T & b )
{
    T c = b ;
    b = a ;
    a = c ;
}

#include "iphone_platform_math.hpp"
#include "iphone_platform_matrix.hpp"
#include "iphone_platform_render.hpp"
#include "iphone_platform_sound.hpp"
#include "iphone_platform_time.hpp"
#include "iphone_platform_vector.hpp"
