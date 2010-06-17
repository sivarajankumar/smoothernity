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
#include "macosx_platform_render.hpp"
#include "macosx_platform_sound.hpp"
#include "macosx_platform_time.hpp"

class shy_macosx_platform_utility ;

class shy_macosx_platform
{
    friend class shy_macosx_platform_mouse < shy_macosx_platform > ;
    friend class shy_macosx_platform_render < shy_macosx_platform > ;
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
    typedef shy_macosx_platform_render < shy_macosx_platform > platform_render ;
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

    static const_int_32 frames_per_second = 60 ;    
    static const shy_platform_math_consts < shy_macosx_platform > math_consts ;
        
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

    static shy_macosx_platform :: platform_render :: vertex_data _reference_vertex ;
    static void * _vertex_position_offset ;
    static void * _vertex_tex_coord_offset ;
    static void * _vertex_color_offset ;
} ;
