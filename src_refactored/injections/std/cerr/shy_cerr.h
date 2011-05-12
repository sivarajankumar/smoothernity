#ifndef _shy_injections_std_cerr_included
#define _shy_injections_std_cerr_included

#ifdef shy_build_loadable_way
    #include <iostream>
    #define so_called_std_cerr std :: cerr
#endif

#endif
