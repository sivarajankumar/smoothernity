#ifndef _shy_injections_std_isspace_included
#define _shy_injections_std_isspace_included

#ifdef shy_build_loadable_way
    #include <locale>
    #define so_called_std_isspace std :: isspace
#endif

#endif
