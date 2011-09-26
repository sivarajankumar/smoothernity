#ifndef _shy_profile_platform_conditions_injections_included
#define _shy_profile_platform_conditions_injections_included

#ifdef shy_build_with_profile
    #include "./shy_conditions.h"
    typedef shy_profile_platform_conditions so_called_profile_platform_conditions ;
#endif

#endif
