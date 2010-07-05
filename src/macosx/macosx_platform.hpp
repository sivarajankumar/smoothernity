#include <AudioToolbox/AudioToolbox.h>
#include <AudioToolbox/ExtendedAudioFile.h>
#include <Foundation/NSBundle.h>
#include <OpenAL/al.h>
#include <OpenAL/alc.h>
#include <OpenAL/MacOSX_OALExtensions.h>
#include <OpenGL/gl.h>
#include <OpenGL/glext.h>
#include <QuartzCore/QuartzCore.h>

#include "macosx_sound_loader.h"
#include "macosx_texture_loader.h"

#include <new>

#include "../platform/matrix_float.hpp"
#include "../platform/matrix_float_insider.hpp"
#include "../platform/conditions.hpp"
#include "../platform/math_consts.hpp"
#include "../platform/math_int_float.hpp"
#include "../platform/math_int_float_insider.hpp"
#include "../platform/pointer.hpp"
#include "../platform/scheduler_random.hpp"
#include "../platform/static_array.hpp"
#include "../platform/static_array_insider.hpp"
#include "../platform/static_assert.hpp"
#include "../platform/touch_dummy.hpp"
#include "../platform/vector_float.hpp"
#include "../platform/vector_float_insider.hpp"

#include "macosx_platform_mouse.hpp"
#include "macosx_platform_mouse_insider.hpp"
#include "macosx_platform_render.hpp"
#include "macosx_platform_render_insider.hpp"
#include "macosx_platform_sound.hpp"
#include "macosx_platform_sound_insider.hpp"
#include "macosx_platform_time.hpp"

class shy_macosx_platform ;

class shy_macosx_platform_insider
{
public :
    typedef shy_platform_math_int_float_insider < shy_macosx_platform_insider > platform_math_insider ;
    typedef shy_platform_matrix_float_insider < shy_macosx_platform_insider > platform_matrix_insider ;
    typedef shy_macosx_platform_mouse_insider < shy_macosx_platform_insider > platform_mouse_insider ;
    typedef shy_macosx_platform_render_insider < shy_macosx_platform_insider > platform_render_insider ;
    typedef shy_macosx_platform_sound_insider < shy_macosx_platform_insider > platform_sound_insider ;
    typedef shy_platform_static_array_insider < shy_macosx_platform_insider > platform_static_array_insider ;
    typedef shy_platform_vector_float_insider < shy_macosx_platform_insider > platform_vector_insider ;

    typedef shy_platform_conditions < shy_macosx_platform_insider > platform_conditions ;
    typedef shy_platform_math_int_float < shy_macosx_platform_insider > platform_math ;
    typedef shy_platform_math_consts < shy_macosx_platform_insider > platform_math_consts ;
    typedef shy_platform_matrix_float < shy_macosx_platform_insider > platform_matrix ;
    typedef shy_macosx_platform_mouse < shy_macosx_platform_insider > platform_mouse ;
    typedef shy_platform_pointer < shy_macosx_platform_insider > platform_pointer ;
    typedef shy_macosx_platform_render < shy_macosx_platform_insider > platform_render ;
    typedef shy_platform_scheduler_random < shy_macosx_platform_insider > platform_scheduler ;
    typedef shy_macosx_platform_sound < shy_macosx_platform_insider > platform_sound ;
    typedef shy_platform_static_array < shy_macosx_platform_insider > platform_static_array ;
    typedef shy_platform_static_assert < shy_macosx_platform_insider > platform_static_assert ;
    typedef shy_macosx_platform_time < shy_macosx_platform_insider > platform_time ;
    typedef shy_platform_touch_dummy < shy_macosx_platform_insider > platform_touch ;
    typedef shy_platform_vector_float < shy_macosx_platform_insider > platform_vector ;

    static const int uninitialized_value = 0xC0C0C0C0 ;

    shy_macosx_platform_insider ( ) ;
    void register_platform_modules ( shy_macosx_platform & platform ) ;
    
    platform_mouse_insider mouse_insider ;
    platform_render_insider render_insider ;
    platform_sound_insider sound_insider ;

    platform_math_consts math_consts ;
    platform_mouse mouse ;
    platform_render render ;
    platform_sound sound ;
} ;

class shy_macosx_platform
{
public :
    typedef shy_platform_conditions < shy_macosx_platform_insider > platform_conditions ;
    typedef shy_platform_math_int_float < shy_macosx_platform_insider > platform_math ;
    typedef shy_platform_math_consts < shy_macosx_platform_insider > platform_math_consts ;
    typedef shy_platform_matrix_float < shy_macosx_platform_insider > platform_matrix ;
    typedef shy_macosx_platform_mouse < shy_macosx_platform_insider > platform_mouse ;
    typedef shy_platform_pointer < shy_macosx_platform_insider > platform_pointer ;
    typedef shy_macosx_platform_render < shy_macosx_platform_insider > platform_render ;
    typedef shy_platform_scheduler_random < shy_macosx_platform_insider > platform_scheduler ;
    typedef shy_macosx_platform_sound < shy_macosx_platform_insider > platform_sound ;
    typedef shy_platform_static_array < shy_macosx_platform_insider > platform_static_array ;
    typedef shy_platform_static_assert < shy_macosx_platform_insider > platform_static_assert ;
    typedef shy_macosx_platform_time < shy_macosx_platform_insider > platform_time ;
    typedef shy_platform_touch_dummy < shy_macosx_platform_insider > platform_touch ;
    typedef shy_platform_vector_float < shy_macosx_platform_insider > platform_vector ;

    static platform_math :: const_int_32 frames_per_second = 60 ;    
    static const shy_platform_math_consts < shy_macosx_platform_insider > math_consts ;
    
    platform_pointer :: pointer < const platform_math_consts > math_consts_ptr ;
    platform_pointer :: pointer < platform_mouse > mouse ;
    platform_pointer :: pointer < platform_render > render ;
    platform_pointer :: pointer < platform_sound > sound ;
} ;
