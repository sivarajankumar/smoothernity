template < typename mediator >
class shy_logic_observer_animation_flight
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_observer_animation_flight_transform_request ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
} ;

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: receive ( typename messages :: logic_observer_animation_flight_transform_request )
{
    typename messages :: logic_observer_animation_flight_transform_reply msg ;
    platform_vector :: xyz 
        ( msg . eye
        , _platform_math_consts . get ( ) . fract_0
        , _platform_math_consts . get ( ) . fract_0
        , _platform_math_consts . get ( ) . fract_0
        ) ;
    platform_vector :: xyz 
        ( msg . target
        , _platform_math_consts . get ( ) . fract_0
        , _platform_math_consts . get ( ) . fract_0
        , _platform_math_consts . get ( ) . fract_minus_1
        ) ;
    _mediator . get ( ) . send ( msg ) ;
}

