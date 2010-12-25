#ifndef _module2_sender_included_
#define _module2_sender_included_

class message_from_second_module_to_other_modules ;
class message_my_second_module_function ;
class message_to_second_module_from_other_modules ;

class my_module2_sender
{
public :
    static void send ( message_from_second_module_to_other_modules ) ;
    static void send ( message_my_second_module_function ) ;
    static void send ( message_to_second_module_from_other_modules ) ;
} ;

#endif

