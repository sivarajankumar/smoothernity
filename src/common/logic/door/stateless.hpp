template < typename mediator >
class shy_logic_door_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_door_messages
    {
    public :
        class logic_door_creation_finished { } ;
        class logic_door_creation_permit { } ;
        class logic_door_render { } ;
    } ;

    template < typename receivers >
    class logic_door_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_door_messages :: logic_door_creation_finished ) ;
        void send ( typename logic_door_messages :: logic_door_creation_permit ) ;
        void send ( typename logic_door_messages :: logic_door_render ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_creation_finished msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_creation_permit msg )
{
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_render msg )
{
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
}

