template < typename mediator >
class shy_logic_controls_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_controls_messages
    {
    public :
        class logic_controls_dummy_message { } ;
    } ;

    template < typename receivers >
    class logic_controls_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_controls_messages :: logic_controls_dummy_message ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_controls_stateless < mediator > 
:: logic_controls_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_controls_stateless < mediator >
:: logic_controls_sender < receivers >
:: send ( typename logic_controls_messages :: logic_controls_dummy_message )
{
}

