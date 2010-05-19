#import <AudioToolbox/AudioToolbox.h>
#import <AudioToolbox/ExtendedAudioFile.h>
#import <Foundation/NSBundle.h>
#import <OpenAL/al.h>
#import <OpenAL/alc.h>
#import <OpenAL/MacOSX_OALExtensions.h>
#import <OpenGL/gl.h>
#import <OpenGL/glext.h>
#import <QuartzCore/QuartzCore.h>

#import "macosx_sound_loader.h"
#import "macosx_texture_loader.h"

class shy_macosx_platform
{
public :
    typedef int int_32 ;
    typedef float float_32 ;    
    typedef const int const_int_32 ;
    
    class num_whole
    {
        friend class shy_macosx_platform ;
    public :
        num_whole ( )
        : _value ( 0 )
        {
        }
    private :
        int _value ;
    } ;
    
    class num_fract
    {
        friend class shy_macosx_platform ;
    public :
        num_fract ( )
        : _value ( 0 )
        {
        }
    private :
        float _value ;
    } ;
    
    class render_index_buffer_id
    {
        friend class shy_macosx_platform ;
    private :
        GLuint _buffer_id ;
    } ;
    
    class render_vertex_buffer_id
    {
        friend class shy_macosx_platform ;
    private :
        GLuint _buffer_id ;
    } ;
    
	class render_texture_id
	{
		friend class shy_macosx_platform ;
	private :
		GLuint _texture_id ;
	} ;

    class texture_resource_id
    {
        friend class shy_macosx_platform ;
    private :
        int _resource_id ;
    } ;
	
    class texel_data
    {
        friend class shy_macosx_platform ;
    private :
        GLubyte _color [ 4 ] ;
    } ;
    
    class vertex_data
    {
        friend class shy_macosx_platform ;
    private :
        GLfloat _position [ 3 ] ;
        GLfloat _tex_coord [ 2 ] ;
        GLubyte _color [ 4 ] ;
    } ;
    
    class index_data
    {
        friend class shy_macosx_platform ;
    private :
        GLushort _index ;
    } ;

    class time_data
    {
        friend class shy_macosx_platform ;
    private :
        CFAbsoluteTime _time ;
    } ;
    
    class matrix_data
    {
        friend class shy_macosx_platform ;
    private :
        GLfloat _elements [ 16 ] ;
    } ;
    
    class vector_data
    {
        friend class shy_macosx_platform ;
    private :
        float_32 _x ;
        float_32 _y ;
        float_32 _z ;
    } ;
    
    class mono_sound_sample
    {
        friend class shy_macosx_platform ;
    private :
        ALubyte _value ;
    } ;
    
    class stereo_sound_sample
    {
        friend class shy_macosx_platform ;
    private :
        ALushort _left_channel_value ;
        ALushort _right_channel_value ; 
    } ;
    
    class sound_buffer_id
    {
        friend class shy_macosx_platform ;
    private :
        ALuint _buffer_id ;
    } ;
    
    class sound_source_id
    {
        friend class shy_macosx_platform ;
    private :
        ALuint _source_id ;
    } ;
    
    class stereo_sound_resource_id
    {
        friend class shy_macosx_platform ;
    private :
        int _resource_id ;
    } ;
    
    //
    // constants
    //
    
    static const_int_32 frames_per_second = 60 ;
    static const_int_32 mono_sound_samples_per_second = 22050 ;
    static const_int_32 stereo_sound_samples_per_second = 44100 ;
    
    //
    // vector
    //
    
    static void vector_xyz ( vector_data & result , float_32 x , float_32 y , float_32 z ) ;
    static void vector_dot_product ( float_32 & result , vector_data v1 , vector_data v2 ) ;
    static void vector_cross_product ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_add ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_sub ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_mul ( vector_data & result , vector_data v , float_32 f ) ;
    static void vector_length ( float_32 & result , vector_data v ) ;
    static void vector_normalize ( vector_data & result , vector_data v ) ;
    
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
    static void matrix_get_axis_x ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_get_axis_y ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_get_axis_z ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_get_origin ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_identity ( matrix_data & matrix ) ;
    static void matrix_inverse_rotation_translation ( matrix_data & matrix ) ;
    
    //
    // render
    //
    
    static void render_enable_face_culling ( ) ;
    
    static void render_enable_depth_test ( ) ;
    static void render_disable_depth_test ( ) ;
    
    static void render_fog_disable ( ) ;
    static void render_fog_linear ( num_fract near , num_fract far , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    
    static void render_blend_disable ( ) ;
    static void render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    
	static void render_enable_texturing ( ) ;
	static void render_disable_texturing ( ) ;
	static void render_set_modulate_texture_mode ( ) ;
    static void render_use_texture ( const render_texture_id & arg_texture_id ) ;
	static void render_create_texture_id ( render_texture_id & arg_texture_id ) ;
    static void render_set_texel_color ( texel_data & texel , num_whole r , num_whole g , num_whole b , num_whole a ) ;
    static void render_load_texture_data ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , texel_data * data ) ;
    static void render_load_texture_resource ( const texture_resource_id & resource_id , num_whole size_pow2_base , texel_data * data ) ;
    static void render_create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;
    static void render_texture_loader_ready ( num_whole & is_ready ) ;
    
    static void render_clear_screen ( num_fract r , num_fract g , num_fract b ) ;
    
    static void render_projection_frustum ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
    static void render_projection_ortho ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
    
    static void render_create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , vertex_data * data ) ;
    static void render_set_vertex_position ( vertex_data & vertex , float_32 x , float_32 y , float_32 z ) ;
    static void render_set_vertex_tex_coord ( vertex_data & vertex , float_32 u , float_32 v ) ;
    static void render_set_vertex_color ( vertex_data & vertex , int_32 r , int_32 g , int_32 b , int_32 a ) ;

    static void render_create_index_buffer ( render_index_buffer_id & arg_buffer_id , int_32 elements , index_data * data ) ;
    static void render_set_index_value ( index_data & data , int_32 index ) ;
    
    static void render_draw_triangle_strip 
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , int_32 indices_count
        ) ;
    static void render_draw_triangle_fan
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , int_32 indices_count
        ) ;
        
    static void render_matrix_identity ( ) ;
    static void render_matrix_load ( const matrix_data & matrix ) ;
    static void render_matrix_mult ( const matrix_data & matrix ) ;
    static void render_matrix_push ( ) ;
    static void render_matrix_pop ( ) ;
    
	static void render_get_aspect_width ( float_32 & result ) ;
	static void render_get_aspect_height ( float_32 & result ) ;
    
    //
    // sound
    //
    
    static void sound_set_listener_position ( vector_data position ) ;
    static void sound_set_listener_velocity ( vector_data velocity ) ;
    static void sound_set_listener_orientation ( vector_data look_at , vector_data up ) ;
    static void sound_set_sample_value ( mono_sound_sample & sample , num_fract value ) ;
    static void sound_create_stereo_resource_id ( stereo_sound_resource_id & result , num_whole resource_index ) ;
    static void sound_load_stereo_sample_data
        ( stereo_sound_sample * samples 
        , num_whole max_samples_count
        , num_whole & loaded_samples_count
        , const stereo_sound_resource_id & resource_id 
        ) ;
    static void sound_loader_ready ( num_whole & result ) ;
    static void sound_create_mono_buffer ( sound_buffer_id & result , mono_sound_sample * samples , num_whole samples_count ) ;
    static void sound_create_stereo_buffer ( sound_buffer_id & result , stereo_sound_sample * samples , num_whole samples_count ) ;
    static void sound_create_source ( sound_source_id & result ) ;
    static void sound_set_source_pitch ( const sound_source_id & source_id , num_fract pitch ) ;
    static void sound_set_source_gain ( const sound_source_id & source_id , num_fract gain ) ;
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
    
    static void math_sin ( float_32 & result , float_32 a ) ;
    static void math_cos ( float_32 & result , float_32 a ) ;
    static void math_sub_wholes ( num_whole & result , num_whole from , num_whole what ) ;
    static void math_add_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void math_make_num_whole ( num_whole & result , const_int_32 value ) ;
    static void math_make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator ) ;

    //
    // condition
    //
    
    static int condition_equal ( num_whole a , num_whole b ) ;
    static int condition_true ( num_whole num ) ;
    static int condition_false ( num_whole num ) ;
    
    //
    // time
    //
    
    static void time_get_current ( time_data & time ) ;
    static void time_diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 ) ;

    //
    // touch
    //
    
    static void touch_occured ( int_32 & result ) ;
    static void touch_x ( float_32 & result ) ;
    static void touch_y ( float_32 & result ) ;

	//
	// mouse
	//

	static void mouse_left_button_down ( int_32 & result ) ;
	static void mouse_x ( float_32 & result ) ;
	static void mouse_y ( float_32 & result ) ;

	//
	// variables
	//

    static shy_macosx_sound_loader * _sound_loader ;
    static shy_macosx_texture_loader * _texture_loader ;
	
	static float_32 _aspect_width ;
	static float_32 _aspect_height ;
	
	static int_32 _mouse_left_button_down ;
	static float_32 _mouse_x ;
	static float_32 _mouse_y ;

private :
    static vertex_data _reference_vertex ;
    static void * _vertex_position_offset ;
    static void * _vertex_tex_coord_offset ;
    static void * _vertex_color_offset ;
} ;

template < typename type >
void swap_values ( type & a , type & b )
{
    type c = b ;
    b = a ;
    a = c ;
}

#include "macosx_platform_condition.hpp"
#include "macosx_platform_math.hpp"
#include "macosx_platform_matrix.hpp"
#include "macosx_platform_mouse.hpp"
#include "macosx_platform_render.hpp"
#include "macosx_platform_sound.hpp"
#include "macosx_platform_time.hpp"
#include "macosx_platform_touch.hpp"
#include "macosx_platform_vector.hpp"
