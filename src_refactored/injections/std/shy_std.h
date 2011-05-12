#ifndef _shy_injections_std_included
#define _shy_injections_std_included

#ifdef shy_build_loadable_way

    #include <locale>
    #include <sstream>
    #include <stdint.h>
    #include <string>

    typedef char so_called_std_char ;
    typedef int32_t so_called_std_int32_t ;
    typedef std :: istringstream so_called_std_istringstream ;
    typedef std :: locale so_called_std_locale ;
    typedef std :: string so_called_std_string ;

#endif

#endif
