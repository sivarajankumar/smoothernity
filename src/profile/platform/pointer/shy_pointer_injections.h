#ifndef _shy_profile_platform_pointer_injections_included
#define _shy_profile_platform_pointer_injections_included

#ifdef shy_build_with_profile
    #include "./shy_pointer.h"
    typedef shy_profile_platform_pointer so_called_profile_platform_pointer ;
#endif

#endif
