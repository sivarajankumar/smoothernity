#include "module2.hpp"

#include "module1_messages.hpp"
#include "module2_messages.hpp"

typedef so_called_platform :: platform_scheduler :: scheduled_context < my_module2 > my_module2_scheduled_context ;
template < > my_module2_scheduled_context my_module2_scheduled_context :: _singleton = my_module2_scheduled_context ( ) ;

void my_module2 :: receive ( message_my_second_module_function msg )
{
    so_called_platform :: platform_print :: print_string ( "my second module function (arg1 = " ) ;
    so_called_platform :: platform_print :: print_int ( msg . arg1 . value ) ;
    so_called_platform :: platform_print :: print_string ( ", arg2 = " ) ;
    so_called_platform :: platform_print :: print_int ( msg . arg2 . value ) ;
    so_called_platform :: platform_print :: print_string ( ")\n" ) ;

    message_my_first_module_function msg1 ;
    msg1 . arg . value = msg . arg1 . value + msg . arg2 . value ;
    so_called_mediator :: send ( msg1 ) ;

    so_called_mediator :: send ( message_to_first_module_from_other_modules ( ) ) ;
}

void my_module2 :: receive ( message_from_first_module_to_other_modules msg )
{
    so_called_platform :: platform_print :: print_string ( "from first module to other modules\n" ) ;
}

void my_module2 :: receive ( message_to_second_module_from_other_modules msg )
{
    so_called_platform :: platform_print :: print_string ( "to second module from other modules\n" ) ;
    so_called_mediator :: send ( message_from_second_module_to_other_modules ( ) ) ;
}

