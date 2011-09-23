#ifndef _shy_win_platform_generator_injections_included
#define _shy_win_platform_generator_injections_included

#ifdef shy_build_with_generator
    #include "src/platform/generator/python/shy_python_injections.h"
    typedef so_called_platform_generator_python so_called_platform_generator ;
#endif

#endif
