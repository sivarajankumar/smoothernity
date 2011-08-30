#ifndef _shy_injections_type_platform_math_num_fract_included
#define _shy_injections_type_platform_math_num_fract_included

#ifdef shy_build_for_iphone
    #include "main/iphone/platform/math/type/num_fract/shy_num_fract_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "main/macosx/platform/math/type/num_fract/shy_num_fract_injections.h"
#endif

#ifdef shy_build_for_win
    #include "main/win/platform/math/type/num_fract/shy_num_fract_injections.h"
#endif

#endif
