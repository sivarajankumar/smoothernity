template < typename mediator >
class shy_logic_land_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_land_messages
    {
    public :
        class logic_land_prepare_permit { } ;
        class logic_land_prepared { } ;
        class logic_land_render_reply { } ;
        class logic_land_render_request { } ;
        class logic_land_update { } ;
    } ;
    
    template < typename receivers >
    class logic_land_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_land_messages :: logic_land_prepare_permit ) ;
        void send ( typename logic_land_messages :: logic_land_prepared ) ;
        void send ( typename logic_land_messages :: logic_land_render_reply ) ;
        void send ( typename logic_land_messages :: logic_land_render_request ) ;
        void send ( typename logic_land_messages :: logic_land_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_land_stateless < mediator >
:: logic_land_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_land_stateless < mediator >
:: logic_land_sender < receivers >
:: send ( typename logic_land_messages :: logic_land_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_land_stateless < mediator >
:: logic_land_sender < receivers >
:: send ( typename logic_land_messages :: logic_land_prepare_permit msg )
{
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_land_stateless < mediator >
:: logic_land_sender < receivers >
:: send ( typename logic_land_messages :: logic_land_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_land_stateless < mediator >
:: logic_land_sender < receivers >
:: send ( typename logic_land_messages :: logic_land_render_request msg )
{
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_land_stateless < mediator >
:: logic_land_sender < receivers >
:: send ( typename logic_land_messages :: logic_land_update msg )
{
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
}
