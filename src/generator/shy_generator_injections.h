#ifndef _shy_generator_injections_included
#define _shy_generator_injections_included

#ifdef shy_build_with_generator
    #define so_called_generator(function) function
#endif

#ifdef shy_build_without_generator
    #define so_called_generator(function) { }
#endif

#endif
