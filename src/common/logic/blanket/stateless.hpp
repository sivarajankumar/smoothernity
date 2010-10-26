template < typename mediator >
class shy_logic_blanket_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_blanket_messages
    {
    public :
        class logic_blanket_creation_finished { } ;
        class logic_blanket_creation_permit { } ;
        class logic_blanket_render_reply { } ;
        class logic_blanket_render_request { } ;
    } ;
    
    template < typename receivers >
    class logic_blanket_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_creation_finished ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_creation_permit ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_render_reply ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_render_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_creation_finished msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_creation_permit msg )
{
    _receivers . get ( ) . logic_blanket . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_render_reply msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_render_request msg )
{
    _receivers . get ( ) . logic_blanket . get ( ) . receive ( msg ) ;
}

