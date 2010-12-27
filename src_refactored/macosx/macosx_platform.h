#ifndef _macosx_platform_included
#define _macosx_platform_included

#include "../platform/conditions.h"
#include "../platform/math_consts.h"
#include "../platform/math_int_float.h"
#include "../platform/matrix_float.h"
#include "../platform/mouse.h"
#include "../platform/pointer.h"
#include "../platform/scheduler_direct_call.h"
#include "../platform/scheduler_random.h"
#include "../platform/static_array.h"
#include "../platform/static_assert.h"
#include "../platform/touch.h"
#include "../platform/vector_float.h"

#include "macosx_platform_render.h"
#include "macosx_platform_sound.h"
#include "macosx_platform_time.h"

class shy_macosx_platform
{
public :
    typedef shy_platform_conditions platform_conditions ;
    typedef shy_platform_math_int_float platform_math ;
    typedef shy_platform_math_consts platform_math_consts ;
    typedef shy_platform_matrix_float platform_matrix ;
    typedef shy_platform_mouse platform_mouse ;
    typedef shy_platform_pointer platform_pointer ;
    typedef shy_macosx_platform_render platform_render ;
    typedef shy_platform_scheduler_random platform_scheduler ;
    typedef shy_macosx_platform_sound platform_sound ;
    typedef shy_platform_static_array platform_static_array ;
    typedef shy_platform_static_assert platform_static_assert ;
    typedef shy_macosx_platform_time platform_time ;
    typedef shy_platform_touch platform_touch ;
    typedef shy_platform_vector_float platform_vector ;

    static const int frames_per_second = 60 ;
} ;

#endif
