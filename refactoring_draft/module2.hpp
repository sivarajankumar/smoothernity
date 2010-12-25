#ifndef _module2_included_
#define _module2_included_

class message_from_first_module_to_other_modules ;
class message_my_second_module_function ;
class message_to_second_module_from_other_modules ;

class my_module2
{
public :
    static void receive ( message_from_first_module_to_other_modules ) ;
    static void receive ( message_my_second_module_function ) ;
    static void receive ( message_to_second_module_from_other_modules ) ;
} ;

#endif

