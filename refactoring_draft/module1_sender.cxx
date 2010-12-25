#include "module1_sender.hpp"
#include "module1_messages.hpp"

void my_module1_sender :: send ( message_my_first_module_function msg )
{
    so_called_module1 :: receive ( msg ) ;
}

void my_module1_sender :: send ( message_to_first_module_from_other_modules msg )
{
    so_called_module1 :: receive ( msg ) ;
}

void my_module1_sender :: send ( message_from_first_module_to_other_modules msg )
{
    so_called_module2 :: receive ( msg ) ;
}

