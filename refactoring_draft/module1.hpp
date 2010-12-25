#ifndef _module1_included_
#define _module1_included_

class message_from_second_module_to_other_modules ;
class message_my_first_module_function ;
class message_to_first_module_from_other_modules ;

class my_module1
{
public :
    static void receive ( message_from_second_module_to_other_modules ) ;
    static void receive ( message_my_first_module_function ) ;
    static void receive ( message_to_first_module_from_other_modules ) ;
} ;

#endif

