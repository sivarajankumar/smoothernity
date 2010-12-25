#include "mediator.hpp"
#include "module1_messages.hpp"
#include "module2_messages.hpp"

void my_mediator :: send ( message_my_first_module_function msg )
{
    so_called_module1 :: receive ( msg ) ;
}

void my_mediator :: send ( message_my_second_module_function msg )
{
    so_called_module2 :: receive ( msg ) ;
}

void my_mediator :: send ( message_to_first_module_from_other_modules msg )
{
    so_called_module1 :: receive ( msg ) ;
}

void my_mediator :: send ( message_to_second_module_from_other_modules msg )
{
    so_called_module2 :: receive ( msg ) ;
}

void my_mediator :: send ( message_from_first_module_to_other_modules msg )
{
    so_called_module2 :: receive ( msg ) ;
}

void my_mediator :: send ( message_from_second_module_to_other_modules msg )
{
    so_called_module1 :: receive ( msg ) ;
}

