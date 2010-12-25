#include "iphone_platform.hpp"
#include <iostream>

void iphone_platform :: platform_print :: print_string ( const char * s )
{
    std :: cout << s ;
}

void iphone_platform :: platform_print :: print_int ( int i )
{
    std :: cout << i ;
}

void iphone_platform :: platform_scheduler :: run ( )
{
    std :: cout << "iphone scheduler run" << std :: endl ;
}

