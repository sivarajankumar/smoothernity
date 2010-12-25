#ifndef _module1_sender_included_
#define _module1_sender_included_

class message_from_first_module_to_other_modules ;
class message_my_first_module_function ;
class message_to_first_module_from_other_modules ;

class my_module1_sender
{
public :
    static void send ( message_from_first_module_to_other_modules ) ;
    static void send ( message_my_first_module_function ) ;
    static void send ( message_to_first_module_from_other_modules ) ;
} ;

#endif

