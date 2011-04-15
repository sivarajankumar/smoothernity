#ifndef _shy_injections_std_included
#define _shy_injections_std_included

#ifdef shy_build_loadable_way

    #include <iostream>
    #include <map>
    #include <set>
    #include <string>
    #include <vector>

    #define so_called_std_cerr std :: cerr
    #define so_called_std_cin std :: cin
    #define so_called_std_cout std :: cout
    #define so_called_std_endl std :: endl
    #define so_called_std_getline std :: getline
    #define so_called_std_map std :: map
    #define so_called_std_set std :: set
    #define so_called_std_vector std :: vector

    typedef std :: string so_called_std_string ;

#endif

#endif
