#ifndef _shy_injections_std_included
#define _shy_injections_std_included

#ifdef shy_build_loadable_way

    #include <locale>
    #include <map>
    #include <set>
    #include <sstream>
    #include <stdint.h>
    #include <string>
    #include <vector>

    #define so_called_std_isdigit std :: isdigit
    #define so_called_std_isspace std :: isspace
    #define so_called_std_map std :: map
    #define so_called_std_set std :: set
    #define so_called_std_true true
    #define so_called_std_vector std :: vector

    typedef bool so_called_std_bool ;
    typedef char so_called_std_char ;
    typedef int32_t so_called_std_int32_t ;
    typedef std :: istringstream so_called_std_istringstream ;
    typedef std :: locale so_called_std_locale ;
    typedef std :: string so_called_std_string ;

#endif

#endif
