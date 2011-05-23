#ifndef _shy_macosx_std_cout_injections_included
#define _shy_macosx_std_cout_injections_included 

#ifdef shy_build_development
    #include "../../../std/cout/shy_cout_injections.h"
    #define so_called_std_cout shy_std_cout
#endif

#endif
