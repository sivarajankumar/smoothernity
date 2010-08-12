template < typename mediator >
class shy_logic_fidget_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_fidget_messages
    {
    public :
        class logic_fidget_prepare_permit { } ;
        class logic_fidget_prepared { } ;
        class logic_fidget_render_reply { } ;
        class logic_fidget_render_request { } ;
        class logic_fidget_update { } ;
    } ;
    
    template < typename receivers >
    class logic_fidget_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_fidget_messages :: logic_fidget_prepare_permit ) ;
        void send ( typename logic_fidget_messages :: logic_fidget_prepared ) ;
        void send ( typename logic_fidget_messages :: logic_fidget_render_reply ) ;
        void send ( typename logic_fidget_messages :: logic_fidget_render_request ) ;
        void send ( typename logic_fidget_messages :: logic_fidget_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_fidget_stateless < mediator >
:: logic_fidget_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_fidget_stateless < mediator >
:: logic_fidget_sender < receivers >
:: send ( typename logic_fidget_messages :: logic_fidget_prepared msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_fidget_stateless < mediator >
:: logic_fidget_sender < receivers >
:: send ( typename logic_fidget_messages :: logic_fidget_prepare_permit msg )
{
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_fidget_stateless < mediator >
:: logic_fidget_sender < receivers >
:: send ( typename logic_fidget_messages :: logic_fidget_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_fidget_stateless < mediator >
:: logic_fidget_sender < receivers >
:: send ( typename logic_fidget_messages :: logic_fidget_render_request msg )
{
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_fidget_stateless < mediator >
:: logic_fidget_sender < receivers >
:: send ( typename logic_fidget_messages :: logic_fidget_update msg )
{
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
}
