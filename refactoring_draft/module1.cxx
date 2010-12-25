#include "module1.hpp"
#include "module1_messages.hpp"
#include "module2_messages.hpp"

typedef so_called_platform :: platform_scheduler :: scheduled_context < my_module1 > my_module1_scheduled_context ;
template < > my_module1_scheduled_context my_module1_scheduled_context :: _singleton = my_module1_scheduled_context ( ) ;

void my_module1 :: receive ( message_my_first_module_function msg )
{
    so_called_platform :: platform_print :: print_string ( "my first module function (arg = " ) ;
    so_called_platform :: platform_print :: print_int ( msg . arg . value ) ;
    so_called_platform :: platform_print :: print_string ( ")\n" ) ;

    so_called_mediator :: send ( message_to_second_module_from_other_modules ( ) ) ;
}

void my_module1 :: receive ( message_from_second_module_to_other_modules msg )
{
    so_called_platform :: platform_print :: print_string ( "from second module to other modules\n" ) ;
}

void my_module1 :: receive ( message_to_first_module_from_other_modules msg )
{
    so_called_platform :: platform_print :: print_string ( "to first module from other modules\n" ) ;
    so_called_mediator :: send ( message_from_first_module_to_other_modules ( ) ) ;
}

