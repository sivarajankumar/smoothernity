#include <math.h>
#include "D3dx9math.h"
#include "DXUT.h"

#include <new>

#include "../platform/matrix_float.hpp"
#include "../platform/matrix_float_insider.hpp"
#include "../platform/conditions.hpp"
#include "../platform/math_consts.hpp"
#include "../platform/math_int_float.hpp"
#include "../platform/math_int_float_insider.hpp"
#include "../platform/mouse.hpp"
#include "../platform/platform.hpp"
#include "../platform/pointer.hpp"
#include "../platform/scheduler_random.hpp"
#include "../platform/static_array.hpp"
#include "../platform/static_array_insider.hpp"
#include "../platform/static_assert.hpp"
#include "../platform/touch.hpp"
#include "../platform/vector_float.hpp"
#include "../platform/vector_float_insider.hpp"

#include "win_platform_render.hpp"
#include "win_platform_render_insider.hpp"
#include "win_platform_sound.hpp"
#include "win_platform_time.hpp"

class shy_win_platform_insider
{
public :
    typedef shy_platform_math_int_float_insider < shy_win_platform_insider > platform_math_insider ;
    typedef shy_platform_matrix_float_insider < shy_win_platform_insider > platform_matrix_insider ;
    typedef shy_win_platform_render_insider < shy_win_platform_insider > platform_render_insider ;
    typedef shy_platform_static_array_insider < shy_win_platform_insider > platform_static_array_insider ;
    typedef shy_platform_vector_float_insider < shy_win_platform_insider > platform_vector_insider ;

    typedef shy_platform_conditions < shy_win_platform_insider > platform_conditions ;
    typedef shy_platform_math_int_float < shy_win_platform_insider > platform_math ;
    typedef shy_platform_math_consts < shy_win_platform_insider > platform_math_consts ;
    typedef shy_platform_matrix_float < shy_win_platform_insider > platform_matrix ;
    typedef shy_platform_mouse < shy_win_platform_insider > platform_mouse ;
    typedef shy_platform_pointer < shy_win_platform_insider > platform_pointer ;
    typedef shy_win_platform_render < shy_win_platform_insider > platform_render ;
    typedef shy_platform_scheduler_random < shy_win_platform_insider > platform_scheduler ;
    typedef shy_win_platform_sound < shy_win_platform_insider > platform_sound ;
    typedef shy_platform_static_array < shy_win_platform_insider > platform_static_array ;
    typedef shy_platform_static_assert < shy_win_platform_insider > platform_static_assert ;
    typedef shy_win_platform_time < shy_win_platform_insider > platform_time ;
    typedef shy_platform_touch < shy_win_platform_insider > platform_touch ;
    typedef shy_platform_vector_float < shy_win_platform_insider > platform_vector ;

    static const int frames_per_second = 60 ;
    static const int uninitialized_value = 0xC0C0C0C0 ;

    shy_win_platform_insider ( ) ;
    
    platform_render_insider render_insider ;

    platform_math_consts math_consts ;
    platform_mouse mouse ;
    platform_render render ;
    platform_sound sound ;
    platform_touch touch ;
    
    shy_platform < shy_win_platform_insider > platform ;
} ;
