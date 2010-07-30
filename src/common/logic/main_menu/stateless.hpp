template < typename mediator >
class shy_logic_main_menu_stateless
{
    typedef typename mediator :: letter_id letter_id ;

public :
    class logic_main_menu_messages
    {
    public :
        class main_menu_add_letter { public : letter_id letter ; } ;
        class main_menu_add_whitespace { } ;
        class main_menu_next_row { } ;
    } ;
} ;
