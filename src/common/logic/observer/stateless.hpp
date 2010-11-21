template < typename mediator >
class shy_logic_observer_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_observer_messages
    {
    public :
        class logic_observer_size_reply { public : num_fract size ; } ;
        class logic_observer_size_request { } ;
        class logic_observer_update { } ;
    } ;
    
    template < typename receivers >
    class logic_observer_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_observer_messages :: logic_observer_size_reply ) ;
        void send ( typename logic_observer_messages :: logic_observer_size_request ) ;
        void send ( typename logic_observer_messages :: logic_observer_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_observer_stateless < mediator >
:: logic_observer_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_observer_stateless < mediator >
:: logic_observer_sender < receivers >
:: send ( typename logic_observer_messages :: logic_observer_size_reply msg )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_observer_stateless < mediator >
:: logic_observer_sender < receivers >
:: send ( typename logic_observer_messages :: logic_observer_size_request msg )
{
    _receivers . get ( ) . logic_observer_size . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_observer_stateless < mediator >
:: logic_observer_sender < receivers >
:: send ( typename logic_observer_messages :: logic_observer_update msg )
{
    _receivers . get ( ) . logic_observer_animation_flight . get ( ) . receive ( msg ) ;
}

