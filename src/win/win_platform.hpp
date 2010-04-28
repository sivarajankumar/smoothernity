#include <math.h>
#include "D3dx9math.h"
#include "DXUT.h"

class shy_win_platform
{
public :
    typedef int int_32 ;
    typedef float float_32 ;
    
    class render_vertex_buffer_id
    {
        friend class shy_win_platform ;
    private :
		IDirect3DVertexBuffer9 * _buffer ;
    } ;
    
    class render_index_buffer_id
    {
        friend class shy_win_platform ;
    private :
		IDirect3DIndexBuffer9 * _buffer ;
    } ;
    
	class render_texture_id
	{
		friend class shy_win_platform ;
	private :
		int _dummy ;
	} ;
	
    class texel_data
    {
        friend class shy_win_platform ;
    private :
        int _dummy ;
    } ;
    
    class vertex_data
    {
        friend class shy_win_platform ;
    private :
		FLOAT _x ;
		FLOAT _y ;
		FLOAT _z ;
		DWORD _color ;
		FLOAT _u ;
		FLOAT _v ;
    } ;
    
    class index_data
    {
        friend class shy_win_platform ;
    private :
		UINT _index ;
    } ;

    class time_data
    {
        friend class shy_win_platform ;
    private :
		int _dummy ;
    } ;
    
    class matrix_data
    {
        friend class shy_win_platform ;
    private :
        float_32 _elements [ 16 ] ;
    } ;
    
    class vector_data
    {
        friend class shy_win_platform ;
    private :
        float_32 _x ;
        float_32 _y ;
        float_32 _z ;
    } ;
    
    class mono_sound_sample
    {
        friend class shy_win_platform ;
    private :
		int _dummy ;
    } ;
    
    class stereo_sound_sample
    {
        friend class shy_win_platform ;
    private :
		int _dummy ;
    } ;
    
    class sound_buffer_id
    {
        friend class shy_win_platform ;
    private :
		int _dummy ;
    } ;
    
    class sound_source_id
    {
        friend class shy_win_platform ;
    private :
		int _dummy ;
    } ;
    
    class stereo_sound_resource_id
    {
        friend class shy_win_platform ;
    private :
		int _dummy ;
    } ;
    
    //
    // constants
    //
    
    static const int_32 frames_per_second = 60 ;
    static const int_32 mono_sound_samples_per_second = 22050 ;
    static const int_32 stereo_sound_samples_per_second = 44100 ;
    
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
    static void render_disable_depth_test ( ) ;
    
    static void render_fog_disable ( ) ;
    static void render_fog_linear ( float_32 near , float_32 far , float_32 r , float_32 g , float_32 b , float_32 a ) ;
    
    static void render_blend_disable ( ) ;
    static void render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    
	static void render_enable_texturing ( ) ;
	static void render_disable_texturing ( ) ;
	static void render_set_modulate_texture_mode ( ) ;
    static void render_use_texture ( const render_texture_id & arg_texture_id ) ;
	static void render_create_texture_id ( render_texture_id & arg_texture_id ) ;
    static void render_set_texel_color ( texel_data & texel , int_32 r , int_32 g , int_32 b , int_32 a ) ;
    static void render_load_texture_data ( const render_texture_id & arg_texture_id , int_32 size_pow2_base , texel_data * data ) ;
    
    static void render_clear_screen ( float_32 r , float_32 g , float_32 b ) ;
    
    static void render_projection_frustum ( float_32 left , float_32 right , float_32 bottom , float_32 top , float_32 near , float_32 far ) ;
    static void render_projection_ortho ( float_32 left , float_32 right , float_32 bottom , float_32 top , float_32 near , float_32 far ) ;
    
    static void render_create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , int_32 elements , vertex_data * data ) ;
    static void render_create_index_buffer ( render_index_buffer_id & arg_buffer_id , int_32 elements , index_data * data ) ;
    static void render_set_vertex_position ( vertex_data & vertex , float_32 x , float_32 y , float_32 z ) ;
    static void render_set_vertex_tex_coord ( vertex_data & vertex , float_32 u , float_32 v ) ;
    static void render_set_vertex_color ( vertex_data & vertex , int_32 r , int_32 g , int_32 b , int_32 a ) ;
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
    
	static float_32 render_get_aspect_width ( ) ;
	static float_32 render_get_aspect_height ( ) ;
    
    //
    // sound
    //
    
    static void sound_set_listener_position ( vector_data position ) ;
    static void sound_set_listener_velocity ( vector_data velocity ) ;
    static void sound_set_listener_orientation ( vector_data look_at , vector_data up ) ;
    static void sound_set_sample_value ( mono_sound_sample & sample , float_32 value ) ;
    static stereo_sound_resource_id sound_create_stereo_resource_id ( int_32 resource_index ) ;
    static void sound_load_stereo_sample_data
        ( stereo_sound_sample * samples 
        , int_32 max_samples_count
        , int_32 & loaded_samples_count
        , const stereo_sound_resource_id & resource_id 
        ) ;
    static int_32 sound_loader_ready ( ) ;
    static sound_buffer_id sound_create_mono_buffer ( mono_sound_sample * samples , int_32 samples_count ) ;
    static sound_buffer_id sound_create_stereo_buffer ( stereo_sound_sample * samples , int_32 samples_count ) ;
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

    //
    // touch
    //
    
    static int_32 touch_occured ( ) ;
    static float_32 touch_x ( ) ;
    static float_32 touch_y ( ) ;

	//
	// mouse
	//

	static int_32 mouse_left_button_down ( ) ;
	static float_32 mouse_x ( ) ;
	static float_32 mouse_y ( ) ;

	//
	// private stuff
	//

	static void _init ( ) ;
	static void _done ( ) ;

	static float_32 _aspect_width ;
	static float_32 _aspect_height ;

private :
	static LPD3DXMATRIXSTACK _matrix_stack ;
} ;

template < typename T >
void swap_values ( T & a , T & b )
{
    T c = b ;
    b = a ;
    a = c ;
}

#include "win_platform_math.hpp"
#include "win_platform_matrix.hpp"
#include "win_platform_mouse.hpp"
#include "win_platform_render.hpp"
#include "win_platform_sound.hpp"
#include "win_platform_time.hpp"
#include "win_platform_touch.hpp"
#include "win_platform_vector.hpp"
