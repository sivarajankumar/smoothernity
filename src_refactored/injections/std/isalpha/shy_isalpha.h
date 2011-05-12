#ifndef _shy_injections_std_isalpha_included
#define _shy_injections_std_isalpha_included

#ifdef shy_build_loadable_way
    #include <locale>
    #define so_called_std_isalpha std :: isalpha
#endif

#endif
