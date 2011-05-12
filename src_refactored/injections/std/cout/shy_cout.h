#ifndef _shy_injections_std_cout_included
#define _shy_injections_std_cout_included

#ifdef shy_build_loadable_way
    #include <iostream>
    #define so_called_std_cout std :: cout
#endif

#endif
