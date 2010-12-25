#include "macosx_platform.hpp"
#include <iostream>

void macosx_platform :: platform_print :: print_string ( const char * s )
{
    std :: cout << s ;
}

void macosx_platform :: platform_print :: print_int ( int i )
{
    std :: cout << i ;
}

void macosx_platform :: platform_scheduler :: run ( )
{
    std :: cout << "macosx scheduler run" << std :: endl ;
}

