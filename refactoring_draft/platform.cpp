#include "platform.hpp"
#include <iostream>

void my_platform :: platform_print :: print_string ( const char * s )
{
    std :: cout << s ;
}

void my_platform :: platform_print :: print_int ( int i )
{
    std :: cout << i ;
}

void my_platform :: platform_scheduler :: run ( )
{
    std :: cout << "scheduler run" << std :: endl ;
}

