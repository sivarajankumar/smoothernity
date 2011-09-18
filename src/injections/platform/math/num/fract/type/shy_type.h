#ifndef _shy_injections_type_platform_math_num_fract_included
#define _shy_injections_type_platform_math_num_fract_included

#ifdef shy_build_for_iphone
    #include "src/main/iphone/platform/math/num/fract/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "src/main/macosx/platform/math/num/fract/type/shy_type_injections.h"
#endif

#ifdef shy_build_for_win
    #include "src/main/win/platform/math/num/fract/type/shy_type_injections.h"
#endif

#endif
