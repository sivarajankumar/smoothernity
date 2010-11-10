template < typename mediator >
class shy_logic_observer_animation_flight
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_observer_animation_flight_transform_state_type
    {
    public :
        vector_data eye ;
        vector_data target ;
        num_fract offset_y ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_observer_animation_flight_transform_request ) ;
    void receive ( typename messages :: logic_observer_update ) ;
private :
    void _compute_offset_y ( ) ;
    void _compute_eye ( ) ;
    void _compute_target ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_observer_animation_flight_transform_state_type _logic_observer_animation_flight_transform_state ;
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
void shy_logic_observer_animation_flight < mediator > :: receive ( typename messages :: logic_observer_update )
{
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: receive ( typename messages :: logic_observer_animation_flight_transform_request )
{
    _compute_offset_y ( ) ;
    _compute_eye ( ) ;
    _compute_target ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: _compute_offset_y ( )
{
    _logic_observer_animation_flight_transform_state . offset_y = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: _compute_eye ( )
{
    num_fract offset_y ;
    num_fract zero ;
    vector_data eye ;

    offset_y = _logic_observer_animation_flight_transform_state . offset_y ;
    zero = _platform_math_consts . get ( ) . fract_0 ;

    platform_vector :: xyz ( eye , zero , offset_y , zero ) ;

    _logic_observer_animation_flight_transform_state . eye = eye ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: _compute_target ( )
{
    num_fract offset_y ;
    num_fract zero ;
    num_fract minus_1 ;
    vector_data target ;

    offset_y = _logic_observer_animation_flight_transform_state . offset_y ;
    zero = _platform_math_consts . get ( ) . fract_0 ;
    minus_1 = _platform_math_consts . get ( ) . fract_minus_1 ;

    platform_vector :: xyz ( target , zero , offset_y , minus_1 ) ;

    _logic_observer_animation_flight_transform_state . target = target ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: _reply_transform ( )
{
    typename messages :: logic_observer_animation_flight_transform_reply msg ;
    msg . eye = _logic_observer_animation_flight_transform_state . eye ;
    msg . target = _logic_observer_animation_flight_transform_state . target ;
    _mediator . get ( ) . send ( msg ) ;
}

