template < typename mediator >
class shy_logic_observer_animation_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
public :
    class logic_observer_animation_stateless_consts_type
    {
    public :
        logic_observer_animation_stateless_consts_type ( ) ;
    public :
        num_fract animation_up_x ;
        num_fract animation_up_y ;
        num_fract animation_up_z ;
    } ;

    class logic_observer_animation_messages
    {
    public :
        class logic_observer_animation_flight_transform_reply { public : vector_data eye ; vector_data target ; } ;
        class logic_observer_animation_flight_transform_request { } ;
        class logic_observer_animation_transform_reply { public : matrix_data transform ; } ;
        class logic_observer_animation_transform_request { } ;
    } ;

    template < typename receivers >
    class logic_observer_animation_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_observer_animation_messages :: logic_observer_animation_flight_transform_reply ) ;
        void send ( typename logic_observer_animation_messages :: logic_observer_animation_flight_transform_request ) ;
        void send ( typename logic_observer_animation_messages :: logic_observer_animation_transform_reply ) ;
        void send ( typename logic_observer_animation_messages :: logic_observer_animation_transform_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    const logic_observer_animation_stateless_consts_type logic_observer_animation_stateless_consts ;
} ;

template < typename mediator >
shy_logic_observer_animation_stateless < mediator > :: logic_observer_animation_stateless_consts_type :: logic_observer_animation_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( animation_up_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( animation_up_y , 1 , 1 ) ;
    platform_math :: make_num_fract ( animation_up_z , 0 , 1 ) ;
}

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
:: send ( typename logic_observer_animation_messages :: logic_observer_animation_flight_transform_reply msg )
{
    _receivers . get ( ) . logic_observer_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_observer_animation_stateless < mediator >
:: logic_observer_animation_sender < receivers >
:: send ( typename logic_observer_animation_messages :: logic_observer_animation_flight_transform_request msg )
{
    _receivers . get ( ) . logic_observer_animation_flight . get ( ) . receive ( msg ) ;
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

