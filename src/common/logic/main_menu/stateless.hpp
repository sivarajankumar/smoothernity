template < typename mediator >
class shy_logic_main_menu_mesh_creator ;

template < typename mediator >
class shy_logic_main_menu_stateless
{
    typedef typename mediator :: letter_id letter_id ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

public :
    class logic_main_menu_mesh_id
    {
        friend class shy_logic_main_menu_mesh_creator < mediator > ;
    private :
        num_whole _mesh_id ;
    } ;

    class logic_main_menu_stateless_consts_type
    {
    public :
        static const_int_32 max_rows = 5 ;
        static const_int_32 max_cols = 16 ;
    } ;
    
    class logic_main_menu_messages
    {
    public :
        class logic_main_menu_add_letter { public : letter_id letter ; } ;
        class logic_main_menu_cols_reply { public : num_whole row ; num_whole cols ; } ;
        class logic_main_menu_cols_request { public : num_whole row ; } ;
        class logic_main_menu_finished { } ;
        class main_menu_launch_permit { } ;
        class main_menu_letter_reply { public : num_whole row ; num_whole col ; letter_id letter ; } ;
        class main_menu_letter_request { public : num_whole row ; num_whole col ; } ;
        class main_menu_mesh_create { } ;
        class main_menu_mesh_create_finished { } ;
        class main_menu_mesh_has_been_created { public : num_whole row ; num_whole col ; logic_main_menu_mesh_id mesh ; } ;
        class main_menu_next_row { } ;
        class main_menu_render { } ;
        class main_menu_rows_reply { public : num_whole rows ; } ;
        class main_menu_rows_request { } ;
        class main_menu_text_create { } ;
        class main_menu_text_create_finished { } ;
        class main_menu_update { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_add_letter ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_cols_reply ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_cols_request ) ;
        void send ( typename logic_main_menu_messages :: logic_main_menu_finished ) ;
        void send ( typename logic_main_menu_messages :: main_menu_launch_permit ) ;
        void send ( typename logic_main_menu_messages :: main_menu_letter_reply ) ;
        void send ( typename logic_main_menu_messages :: main_menu_letter_request ) ;
        void send ( typename logic_main_menu_messages :: main_menu_mesh_create ) ;
        void send ( typename logic_main_menu_messages :: main_menu_mesh_create_finished ) ;
        void send ( typename logic_main_menu_messages :: main_menu_mesh_has_been_created ) ;
        void send ( typename logic_main_menu_messages :: main_menu_next_row ) ;
        void send ( typename logic_main_menu_messages :: main_menu_render ) ;
        void send ( typename logic_main_menu_messages :: main_menu_rows_reply ) ;
        void send ( typename logic_main_menu_messages :: main_menu_rows_request ) ;
        void send ( typename logic_main_menu_messages :: main_menu_text_create ) ;
        void send ( typename logic_main_menu_messages :: main_menu_text_create_finished ) ;
        void send ( typename logic_main_menu_messages :: main_menu_update ) ;
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
:: send ( typename logic_main_menu_messages :: logic_main_menu_add_letter msg )
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_finished msg )
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
    _receivers . get ( ) . logic_main_menu_mesh_creator . get ( ) . receive ( msg ) ;
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
:: send ( typename logic_main_menu_messages :: main_menu_next_row msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_mesh_create msg ) 
{
    _receivers . get ( ) . logic_main_menu_mesh_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_mesh_create_finished msg ) 
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator >
:: logic_main_menu_sender < receivers >
:: send ( typename logic_main_menu_messages :: main_menu_mesh_has_been_created msg )
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_cols_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_mesh_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: logic_main_menu_cols_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_letter_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_mesh_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_letter_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_rows_reply msg ) 
{
    _receivers . get ( ) . logic_main_menu_mesh_creator . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_stateless < mediator > 
:: logic_main_menu_sender < receivers > 
:: send ( typename logic_main_menu_messages :: main_menu_rows_request msg ) 
{
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
}

