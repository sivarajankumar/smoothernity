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
    static const int _uninitialized_value = 0xC0C0C0C0 ;    
public :
    typedef const int const_int_32 ;

    template < typename data_type , int size >
    class static_array
    {
        friend class shy_macosx_platform ;
    private :
        static const int _array_size = size ;
        data_type _elements [ _array_size ] ;
    } ;
    
    class num_whole
    {
        friend class shy_macosx_platform ;
    public :
        num_whole ( ) ;
    private :
        num_whole ( int arg_value ) ;
    private :
        int _value ;
    } ;
    
    class num_fract
    {
        friend class shy_macosx_platform ;
    public :
        num_fract ( ) ;
    private :
        num_fract ( float arg_value ) ;
    private :
        float _value ;
    } ;
    
    class matrix_data
    {
        friend class shy_macosx_platform ;
    public :
        matrix_data ( ) ;
    private :
        GLfloat _elements [ 16 ] ;
    } ;
    
    class vector_data
    {
        friend class shy_macosx_platform ;
    public :
        vector_data ( ) ;
    private :
        float _x ;
        float _y ;
        float _z ;
    } ;
    
    class render_index_buffer_id
    {
        friend class shy_macosx_platform ;
    public :
        render_index_buffer_id ( ) ;
    private :
        GLuint _buffer_id ;
    } ;
    
    class render_vertex_buffer_id
    {
        friend class shy_macosx_platform ;
    public :
        render_vertex_buffer_id ( ) ;
    private :
        GLuint _buffer_id ;
    } ;
    
	class render_texture_id
	{
		friend class shy_macosx_platform ;
    public :
        render_texture_id ( ) ;
	private :
		GLuint _texture_id ;
	} ;

    class texture_resource_id
    {
        friend class shy_macosx_platform ;
    public :
        texture_resource_id ( ) ;
    private :
        int _resource_id ;
    } ;
	
    class texel_data
    {
        friend class shy_macosx_platform ;
    public :
        texel_data ( ) ;
    private :
        GLubyte _color [ 4 ] ;
    } ;
    
    class vertex_data
    {
        friend class shy_macosx_platform ;
    public :
        vertex_data ( ) ;
    private :
        GLfloat _position [ 3 ] ;
        GLfloat _tex_coord [ 2 ] ;
        GLubyte _color [ 4 ] ;
    } ;
    
    class index_data
    {
        friend class shy_macosx_platform ;
    public :
        index_data ( ) ;
    private :
        GLushort _index ;
    } ;

    class time_data
    {
        friend class shy_macosx_platform ;
    public :
        time_data ( ) ;
    private :
        CFAbsoluteTime _time ;
    } ;
    
    class mono_sound_sample
    {
        friend class shy_macosx_platform ;
    public :
        mono_sound_sample ( ) ;
    private :
        ALubyte _value ;
    } ;
    
    class stereo_sound_sample
    {
        friend class shy_macosx_platform ;
    public :
        stereo_sound_sample ( ) ;
    private :
        ALushort _left_channel_value ;
        ALushort _right_channel_value ; 
    } ;
    
    class sound_buffer_id
    {
        friend class shy_macosx_platform ;
    public :
        sound_buffer_id ( ) ;
    private :
        ALuint _buffer_id ;
    } ;
    
    class sound_source_id
    {
        friend class shy_macosx_platform ;
    public :
        sound_source_id ( ) ;
    private :
        ALuint _source_id ;
    } ;
    
    class stereo_sound_resource_id
    {
        friend class shy_macosx_platform ;
    public :
        stereo_sound_resource_id ( ) ;
    private :
        int _resource_id ;
    } ;
    
    //
    // constants
    //
    
    static const_int_32 frames_per_second = 60 ;
    static const_int_32 mono_sound_samples_per_second = 22050 ;
    static const_int_32 stereo_sound_samples_per_second = 44100 ;
    static const num_fract fract_pi ;
    static const num_fract fract_2pi ;
    static const num_fract fract_0 ;
    static const num_fract fract_1 ;
    static const num_fract fract_2 ;
    static const num_fract fract_3 ;
    static const num_fract fract_4 ;
    static const num_fract fract_5 ;
    static const num_fract fract_6 ;
    static const num_fract fract_7 ;
    static const num_fract fract_8 ;
    static const num_fract fract_9 ;
    static const num_whole whole_0 ;
    static const num_whole whole_1 ;
    static const num_whole whole_2 ;
    static const num_whole whole_3 ;
    static const num_whole whole_4 ;
    static const num_whole whole_5 ;
    static const num_whole whole_6 ;
    static const num_whole whole_7 ;
    static const num_whole whole_8 ;
    static const num_whole whole_9 ;
    
    //
    // vector
    //
    
    static void vector_xyz ( vector_data & result , num_fract x , num_fract y , num_fract z ) ;
    static void vector_dot_product ( num_fract & result , vector_data v1 , vector_data v2 ) ;
    static void vector_cross_product ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_add ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_sub ( vector_data & result , vector_data v1 , vector_data v2 ) ;
    static void vector_mul ( vector_data & result , vector_data v , num_fract f ) ;
    static void vector_length ( num_fract & result , vector_data v ) ;
    static void vector_normalize ( vector_data & result , vector_data v ) ;
    
    //
    // matrix
    //
    
    static void matrix_set_axis_x ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void matrix_set_axis_y ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void matrix_set_axis_z ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void matrix_set_origin ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
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
    static void render_set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z ) ;
    static void render_set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v ) ;
    static void render_set_vertex_color ( vertex_data & vertex , num_whole r , num_whole g , num_whole b , num_whole a ) ;

    static void render_create_index_buffer ( render_index_buffer_id & arg_buffer_id , num_whole elements , index_data * data ) ;
    static void render_set_index_value ( index_data & data , num_whole index ) ;
    
    static void render_draw_triangle_strip 
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;
    static void render_draw_triangle_fan
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;
        
    static void render_matrix_identity ( ) ;
    static void render_matrix_load ( const matrix_data & matrix ) ;
    static void render_matrix_mult ( const matrix_data & matrix ) ;
    static void render_matrix_push ( ) ;
    static void render_matrix_pop ( ) ;
    
	static void render_get_aspect_width ( num_fract & result ) ;
	static void render_get_aspect_height ( num_fract & result ) ;
    
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
        , const stereo_sound_resource_id & resource_id 
        ) ;
    static void sound_loader_ready ( num_whole & result ) ;
    static void sound_loaded_samples_count ( num_whole & result ) ;
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
    
    static void math_add_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_add_to_whole ( num_whole & a , num_whole b ) ;
    static void math_sub_wholes ( num_whole & result , num_whole from , num_whole what ) ;
    static void math_sub_from_whole ( num_whole & a , num_whole b ) ;
    static void math_mul_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_mul_whole_by ( num_whole & a , num_whole b ) ;
    static void math_mod_wholes ( num_whole & result , num_whole value , num_whole modulator ) ;
    static void math_mod_whole_by ( num_whole & a , num_whole b ) ;
    static void math_div_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_div_whole_by ( num_whole & a , num_whole b ) ;
    static void math_inc_whole ( num_whole & a ) ;
    static void math_dec_whole ( num_whole & a ) ;
    static void math_xor_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void math_neg_whole ( num_whole & result , num_whole a ) ;

    static void math_sin ( num_fract & result , num_fract a ) ;
    static void math_cos ( num_fract & result , num_fract a ) ;    
    static void math_sub_fracts ( num_fract & result , num_fract from , num_fract what ) ;
    static void math_sub_from_fract ( num_fract & from , num_fract what ) ;
    static void math_add_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void math_add_to_fract ( num_fract & a , num_fract b ) ;
    static void math_mul_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void math_mul_fract_by ( num_fract & a , num_fract b ) ;
    static void math_div_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void math_div_fract_by ( num_fract & a , num_fract b ) ;
    static void math_neg_fract ( num_fract & a ) ;
    static void math_neg_fract ( num_fract & result , num_fract a ) ;
    
    static void math_make_whole_from_fract ( num_whole & result , num_fract fract ) ;
    static void math_make_fract_from_whole ( num_fract & result , num_whole whole ) ;
    
    static void math_make_num_whole ( num_whole & result , const_int_32 value ) ;
    static void math_make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator ) ;

    //
    // condition
    //
    
    static int condition_true ( num_whole num ) ;
    static int condition_false ( num_whole num ) ;

    static int condition_fract_less_than_fract ( num_fract a , num_fract b ) ;
    static int condition_fract_greater_than_fract ( num_fract a , num_fract b ) ;
    
    static int condition_wholes_are_equal ( num_whole a , num_whole b ) ;
    static int condition_whole_greater_or_equal_to_whole ( num_whole a , num_whole b ) ;
    static int condition_whole_greater_than_whole ( num_whole a , num_whole b ) ;
    static int condition_whole_greater_than_zero ( num_whole num ) ;
    static int condition_whole_less_than_whole ( num_whole a , num_whole b ) ;
    static int condition_whole_less_than_zero ( num_whole a ) ;
    static int condition_whole_less_or_equal_to_zero ( num_whole a ) ;
    static int condition_whole_less_or_equal_to_whole ( num_whole a , num_whole b ) ;
    static int condition_whole_is_zero ( num_whole num ) ;
    static int condition_whole_is_even ( num_whole num ) ;
    
    //
    // memory
    //
    
    template < typename type >
    static void memory_pointer_offset ( type * & result , type * base , num_whole offset ) ;
        
    //
    // array
    //
    
    template < typename data_type , int size >
    static data_type & array_element ( static_array < data_type , size > & array , num_whole index ) ;
    template < typename data_type , int size >
    static const data_type & array_element ( const static_array < data_type , size > & array , num_whole index ) ;
        
    //
    // time
    //
    
    static void time_get_current ( time_data & time ) ;
    static void time_diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 ) ;

    //
    // touch
    //
    
    static void touch_occured ( num_whole & result ) ;
    static void touch_x ( num_fract & result ) ;
    static void touch_y ( num_fract & result ) ;

	//
	// mouse
	//

	static void mouse_left_button_down ( num_whole & result ) ;
	static void mouse_x ( num_fract & result ) ;
	static void mouse_y ( num_fract & result ) ;

	//
	// variables
	//

    static shy_macosx_sound_loader * _sound_loader ;
    static shy_macosx_texture_loader * _texture_loader ;
	
	static float _aspect_width ;
	static float _aspect_height ;
	
	static int _mouse_left_button_down ;
	static float _mouse_x ;
	static float _mouse_y ;

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

#include "macosx_platform_array.hpp"
#include "macosx_platform_condition.hpp"
#include "macosx_platform_math.hpp"
#include "macosx_platform_matrix.hpp"
#include "macosx_platform_memory.hpp"
#include "macosx_platform_mouse.hpp"
#include "macosx_platform_render.hpp"
#include "macosx_platform_sound.hpp"
#include "macosx_platform_time.hpp"
#include "macosx_platform_touch.hpp"
#include "macosx_platform_vector.hpp"
