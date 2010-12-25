#include "facade.hpp"
#include "module1_messages.hpp"
#include "module2_messages.hpp"

void my_facade :: my_first_module_function ( int arg )
{
    message_my_first_module_function msg ;
    msg . arg . value = arg ;
    so_called_mediator :: send ( msg ) ;
    so_called_platform :: platform_scheduler :: run ( ) ;
}

void my_facade :: my_second_module_function ( int arg1 , int arg2 )
{
    message_my_second_module_function msg ;
    msg . arg1 . value = arg1 ;
    msg . arg2 . value = arg2 ;
    so_called_mediator :: send ( msg ) ;
    so_called_platform :: platform_scheduler :: run ( ) ;
}

