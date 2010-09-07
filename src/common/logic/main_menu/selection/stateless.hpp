template < typename mediator >
class shy_logic_main_menu_selection_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

public :
    class logic_main_menu_selection_messages
    {
    public :
        class logic_main_menu_selection_mesh_create { } ;
        class logic_main_menu_selection_mesh_create_finished { } ;
        class logic_main_menu_selection_mesh_destroy_reply { } ;
        class logic_main_menu_selection_mesh_destroy_request { } ;
        class logic_main_menu_selection_mesh_render_reply { } ;
        class logic_main_menu_selection_mesh_render_request { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_selection_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create_finished ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_reply ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_request ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_reply ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    shy_logic_main_menu_selection_stateless ( ) ;
private :
    shy_logic_main_menu_selection_stateless < mediator > & operator= ( const shy_logic_main_menu_selection_stateless < mediator > & ) ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_stateless < mediator > :: shy_logic_main_menu_selection_stateless ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create_finished msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_reply msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_reply msg )
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
}
