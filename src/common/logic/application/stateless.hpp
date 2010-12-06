template < typename mediator >
class shy_logic_application_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_application_messages
    {
    public :
        class logic_application_render { } ;
        class logic_application_update { } ;
    } ;
    
    template < typename receivers >
    class logic_application_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_application_messages :: logic_application_render ) ;
        void send ( typename logic_application_messages :: logic_application_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_application_stateless < mediator > 
:: logic_application_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_application_stateless < mediator > 
:: logic_application_sender < receivers >
:: send ( typename logic_application_messages :: logic_application_render msg )
{
    _receivers . get ( ) . logic_application_fsm . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_application_stateless < mediator > 
:: logic_application_sender < receivers >
:: send ( typename logic_application_messages :: logic_application_update msg )
{
    _receivers . get ( ) . logic_application_fsm . get ( ) . receive ( msg ) ;
}
