template < typename mediator >
class shy_logic_observer_animation
{
    typedef typename mediator :: engine_camera engine_camera ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_observer_animation_consts_type
    {
    public :
        _logic_observer_animation_consts_type ( ) ;
    public :
        num_fract up_x ;
        num_fract up_y ;
        num_fract up_z ;
    } ;

    class _logic_observer_animation_transform_state_type
    {
    public :
        num_whole requested ;
        matrix_data transform ;
    } ;

    class _logic_observer_animation_flight_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        vector_data eye ;
        vector_data target ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_observer_animation_transform_request ) ;
    void receive ( typename messages :: logic_observer_animation_flight_transform_reply ) ;
private :
    void _proceed_with_transform ( ) ;
    void _request_flight_transform ( ) ;
    void _reply_computed_transform ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_observer_animation_consts_type _logic_observer_animation_consts ;

    _logic_observer_animation_transform_state_type _logic_observer_animation_transform_state ;
    _logic_observer_animation_flight_transform_state_type _logic_observer_animation_flight_transform_state ;
} ;

template < typename mediator >
shy_logic_observer_animation < mediator > :: _logic_observer_animation_consts_type :: _logic_observer_animation_consts_type ( )
{
    platform_math :: make_num_fract ( up_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( up_y , 1 , 1 ) ;
    platform_math :: make_num_fract ( up_z , 0 , 1 ) ;
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: receive ( typename messages :: logic_observer_animation_transform_request )
{
    _logic_observer_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: receive ( typename messages :: logic_observer_animation_flight_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_observer_animation_flight_transform_state . requested ) )
    {
        _logic_observer_animation_flight_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_observer_animation_flight_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_observer_animation_flight_transform_state . eye = msg . eye ;
        _logic_observer_animation_flight_transform_state . target = msg . target ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_observer_animation_transform_state . requested ) )
    {
        _logic_observer_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_flight_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_observer_animation_flight_transform_state . replied ) )
    {
        _logic_observer_animation_flight_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_computed_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: _request_flight_transform ( )
{
    _logic_observer_animation_flight_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_observer_animation_flight_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: _reply_computed_transform ( )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: _compute_transform ( )
{
    num_fract up_x ;
    num_fract up_y ;
    num_fract up_z ;
    vector_data up ;
    vector_data eye ;
    vector_data target ;
    matrix_data transform ;

    up_x = _logic_observer_animation_consts . up_x ;
    up_y = _logic_observer_animation_consts . up_y ;
    up_z = _logic_observer_animation_consts . up_z ;
    eye = _logic_observer_animation_flight_transform_state . eye ;
    target = _logic_observer_animation_flight_transform_state . target ;

    platform_vector :: xyz ( up , up_x , up_y , up_z ) ;
    engine_camera :: camera_matrix_look_at ( transform , eye , target , up ) ;

    _logic_observer_animation_transform_state . transform = transform ;
}

template < typename mediator >
void shy_logic_observer_animation < mediator > :: _reply_transform ( )
{
    typename messages :: logic_observer_animation_transform_reply msg ;
    msg . transform = _logic_observer_animation_transform_state . transform ;
    _mediator . get ( ) . send ( msg ) ;
}

