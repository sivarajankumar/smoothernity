template < typename mediator >
class shy_logic_observer_animation_stateless
{
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_observer_animation_messages
    {
    public :
        class logic_observer_animation_transform_reply { public : matrix_data transform ; } ;
        class logic_observer_animation_transform_request { } ;
    } ;

    template < typename receivers >
    class logic_observer_animation_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_observer_animation_messages :: logic_observer_animation_transform_reply ) ;
        void send ( typename logic_observer_animation_messages :: logic_observer_animation_transform_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_observer_animation_stateless < mediator >
:: logic_observer_animation_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_observer_animation_stateless < mediator >
:: logic_observer_animation_sender < receivers >
:: send ( typename logic_observer_animation_messages :: logic_observer_animation_transform_reply msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_observer_animation_stateless < mediator >
:: logic_observer_animation_sender < receivers >
:: send ( typename logic_observer_animation_messages :: logic_observer_animation_transform_request msg )
{
    _receivers . get ( ) . logic_observer_animation . get ( ) . receive ( msg ) ;
}

