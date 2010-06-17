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

#include "../platform/matrix_float.hpp"
#include "../platform/matrix_float_insider.hpp"
#include "../platform/conditions.hpp"
#include "../platform/math_consts.hpp"
#include "../platform/math_int_float.hpp"
#include "../platform/math_int_float_insider.hpp"
#include "../platform/pointer.hpp"
#include "../platform/static_array.hpp"
#include "../platform/static_array_insider.hpp"
#include "../platform/touch_dummy.hpp"
#include "../platform/vector_float.hpp"
#include "../platform/vector_float_insider.hpp"

#include "macosx_platform_mouse.hpp"
#include "macosx_platform_sound.hpp"
#include "macosx_platform_time.hpp"

class shy_macosx_platform_utility ;

class shy_macosx_platform
{
    friend class shy_macosx_platform_mouse < shy_macosx_platform > ;
    friend class shy_macosx_platform_sound < shy_macosx_platform > ;
    friend class shy_macosx_platform_time < shy_macosx_platform > ;
    friend class shy_platform_conditions < shy_macosx_platform > ;
    friend class shy_platform_math_consts < shy_macosx_platform > ;
    friend class shy_platform_math_int_float < shy_macosx_platform > ;
    friend class shy_platform_matrix_float < shy_macosx_platform > ;
    friend class shy_platform_pointer < shy_macosx_platform > ;
    friend class shy_platform_static_array < shy_macosx_platform > ;
    friend class shy_platform_touch_dummy < shy_macosx_platform > ;
    friend class shy_platform_vector_float < shy_macosx_platform > ;
private :
    typedef shy_macosx_platform_utility _platform_insider ;
    typedef shy_platform_math_int_float_insider < shy_macosx_platform > _platform_math_insider ;
    typedef shy_platform_matrix_float_insider < shy_macosx_platform > _platform_matrix_insider ;
    typedef shy_platform_static_array_insider < shy_macosx_platform > _platform_static_array_insider ;
    typedef shy_platform_vector_float_insider < shy_macosx_platform > _platform_vector_insider ;
public :
    typedef shy_platform_conditions < shy_macosx_platform > platform_conditions ;
    typedef shy_platform_math_int_float < shy_macosx_platform > platform_math ;
    typedef shy_platform_matrix_float < shy_macosx_platform > platform_matrix ;
    typedef shy_macosx_platform_mouse < shy_macosx_platform > platform_mouse ;
    typedef shy_platform_pointer < shy_macosx_platform > platform_pointer ;
    typedef shy_macosx_platform_sound < shy_macosx_platform > platform_sound ;
    typedef shy_platform_static_array < shy_macosx_platform > platform_static_array ;
    typedef shy_macosx_platform_time < shy_macosx_platform > platform_time ;
    typedef shy_platform_touch_dummy < shy_macosx_platform > platform_touch ;
    typedef shy_platform_vector_float < shy_macosx_platform > platform_vector ;
        
    typedef const int const_int_32 ;
    typedef platform_math :: num_fract num_fract ;
    typedef platform_math :: num_whole num_whole ;
    typedef platform_matrix :: matrix_data matrix_data ;
    typedef platform_vector :: vector_data vector_data ;

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
        friend class shy_macosx_platform_utility ;
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

    //
    // constants
    //
    
    static const_int_32 frames_per_second = 60 ;
    
    static const shy_platform_math_consts < shy_macosx_platform > math_consts ;
    
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
    static void render_set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void render_create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;
    static void render_texture_loader_ready ( num_whole & is_ready ) ;

    static void render_clear_screen ( num_fract r , num_fract g , num_fract b ) ;    
    static void render_projection_frustum ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
    static void render_projection_ortho ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
    
    static void render_set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z ) ;
    static void render_set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v ) ;
    static void render_set_vertex_color ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void render_set_index_value ( index_data & data , num_whole index ) ;
    
    static void render_matrix_identity ( ) ;
    static void render_matrix_load ( const matrix_data & matrix ) ;
    static void render_matrix_mult ( const matrix_data & matrix ) ;
    static void render_matrix_push ( ) ;
    static void render_matrix_pop ( ) ;
    
	static void render_get_aspect_width ( num_fract & result ) ;
	static void render_get_aspect_height ( num_fract & result ) ;
    
    static void render_delete_vertex_buffer ( const render_vertex_buffer_id & arg_buffer_id ) ;
    static void render_delete_index_buffer ( const render_index_buffer_id & arg_buffer_id ) ;
    
    template < typename texels_array >
    static void render_load_texture_data ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , const texels_array & data ) ;
    
    template < typename texels_array >
    static void render_load_texture_resource ( const texture_resource_id & resource_id , num_whole size_pow2_base , const texels_array & data ) ;
    
    template < typename vertices_array >
    static void render_create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , const vertices_array & data ) ;
    
    template < typename indices_array >
    static void render_create_index_buffer ( render_index_buffer_id & arg_buffer_id , num_whole elements , const indices_array & data ) ;
    
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
    
private :
    static const int _uninitialized_value = 0xC0C0C0C0 ;
} ;

class shy_macosx_platform_utility
{
public :
    static const int _uninitialized_value = 0xC0C0C0C0 ;
    
    static shy_macosx_sound_loader * _sound_loader ;
    static shy_macosx_texture_loader * _texture_loader ;
	
	static float _aspect_width ;
	static float _aspect_height ;
	
	static int _mouse_left_button_down ;
	static float _mouse_x ;
	static float _mouse_y ;

    static shy_macosx_platform :: vertex_data _reference_vertex ;
    static void * _vertex_position_offset ;
    static void * _vertex_tex_coord_offset ;
    static void * _vertex_color_offset ;
} ;

#include "macosx_platform_render.hpp"
