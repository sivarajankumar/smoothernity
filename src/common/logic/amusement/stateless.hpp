template < typename mediator >
class shy_logic_amusement_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_amusement_messages
    {
    public :
        class logic_amusement_creation_permit { } ;
        class logic_amusement_finished { } ;
        class logic_amusement_launch_permit { } ;
        class logic_amusement_render { } ;
        class logic_amusement_update { } ;
    } ;

    template < typename receivers >
    class logic_amusement_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_creation_permit ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_finished ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_launch_permit ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_render ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_creation_permit msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_finished msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_launch_permit msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_render msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_update msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

