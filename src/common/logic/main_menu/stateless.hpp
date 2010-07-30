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
        class main_menu_finished { } ;
        class main_menu_launch_permit { } ;
        class main_menu_next_row { } ;
        class main_menu_render { } ;
        class main_menu_text_create { } ;
        class main_menu_text_create_finished { } ;
        class main_menu_update { } ;
    } ;
} ;
