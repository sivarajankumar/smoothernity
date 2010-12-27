#ifndef _macosx_platform_insider_included
#define _macosx_platform_insider_included

#include "../platform/math_int_float_insider.h"
#include "../platform/matrix_float_insider.h"
#include "../platform/mouse_insider.h"
#include "../platform/static_array_insider.h"
#include "../platform/vector_float_insider.h"

#include "macosx_platform_render_insider.h"
#include "macosx_platform_sound_insider.h"

class shy_macosx_platform_insider
{
public :
    typedef shy_platform_math_int_float_insider platform_math_insider ;
    typedef shy_platform_matrix_float_insider platform_matrix_insider ;
    typedef shy_platform_mouse_insider platform_mouse_insider ;
    typedef shy_macosx_platform_render_insider platform_render_insider ;
    typedef shy_macosx_platform_sound_insider platform_sound_insider ;
    typedef shy_platform_static_array_insider platform_static_array_insider ;
    typedef shy_platform_vector_float_insider platform_vector_insider ;

    static const int uninitialized_value = 0xC0C0C0C0 ;
} ;

#endif
