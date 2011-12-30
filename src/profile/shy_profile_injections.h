#ifndef _shy_profile_injections_included
#define _shy_profile_injections_included

#ifdef shy_build_with_profile
    #define so_called_profile(function) function
#endif

#ifdef shy_build_without_profile
    #define so_called_profile(function) { }
#endif

#endif
