template < typename mediator >
class shy_logic_main_menu_stateless
{
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

public :
    class logic_main_menu_consts_type
    {
    public :
        static const_int_32 max_rows = 5 ;
        static const_int_32 max_letters = 16 ;
    } ;
    
    class logic_main_menu_messages
    {
    public :
        class main_menu_add_letter { public : letter_id letter ; } ;
        class main_menu_add_whitespace { } ;
        class main_menu_finished { } ;
        class main_menu_launch_permit { } ;
        class main_menu_letter_added { public : letter_id letter ; num_whole index ; } ;
        class main_menu_next_row { } ;
        class main_menu_render { } ;
        class main_menu_text_create { } ;
        class main_menu_text_create_finished { } ;
        class main_menu_update { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers ) ;
        void send ( typename logic_main_menu_messages :: main_menu_add_letter msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_add_whitespace msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_finished msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_launch_permit msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_letter_added msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_next_row msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_render msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_text_create msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_text_create_finished msg ) ;
        void send ( typename logic_main_menu_messages :: main_menu_update msg ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_add_letter msg )
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_finished msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_launch_permit msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_render msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_update msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_text_create msg )
{
    _receivers . get ( ) . logic_main_menu_text_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_text_create_finished msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_add_whitespace msg )
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_next_row msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_letter_added msg ) 
{
    _receivers . get ( ) . logic_main_menu_mesh_creator . get ( ) . receive ( msg ) ;
}
