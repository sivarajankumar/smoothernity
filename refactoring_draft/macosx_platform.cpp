#include "macosx_platform.hpp"
#include <iostream>

macosx_platform :: platform_scheduler :: _scheduled_context_container macosx_platform :: platform_scheduler :: _all_contexts ;

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
    for ( _scheduled_context_container :: iterator context_i = _all_contexts . begin ( )
        ; context_i != _all_contexts . end ( )
        ; ++ context_i
        )
    {
        ( * context_i ) -> run ( ) ;
    }
}

