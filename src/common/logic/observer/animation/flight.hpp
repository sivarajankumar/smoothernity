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

    class _logic_observer_animation_flight_consts_type
    {
    public :
        _logic_observer_animation_flight_consts_type ( ) ;
    public :
        num_fract rotation_period ;
        num_fract vertical_offset_period ;
        num_fract vertical_offset_amplitude ;
    } ;

    class _logic_observer_animation_flight_transform_state_type
    {
    public :
        vector_data eye ;
        vector_data target ;
        num_fract vertical_offset ;
    } ;

    class _logic_observer_update_state_type
    {
    public :
        num_fract time ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_observer_animation_flight_transform_request ) ;
    void receive ( typename messages :: logic_observer_update ) ;
private :
    void _compute_vertical_offset ( ) ;
    void _compute_eye ( ) ;
    void _compute_target ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_observer_animation_flight_consts_type _logic_observer_animation_flight_consts ;

    _logic_observer_update_state_type _logic_observer_update_state ;
    _logic_observer_animation_flight_transform_state_type _logic_observer_animation_flight_transform_state ;
} ;

template < typename mediator >
shy_logic_observer_animation_flight < mediator > :: _logic_observer_animation_flight_consts_type :: _logic_observer_animation_flight_consts_type ( )
{
    platform_math :: make_num_fract ( rotation_period , 10 , 1 ) ;
    platform_math :: make_num_fract ( vertical_offset_period , 2 , 1 ) ;
    platform_math :: make_num_fract ( vertical_offset_amplitude , 1 , 1 ) ;
}

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
    _logic_observer_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: receive ( typename messages :: logic_observer_update )
{
    num_fract time_step ;
    platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
    platform_math :: add_to_fract ( _logic_observer_update_state . time , time_step ) ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: receive ( typename messages :: logic_observer_animation_flight_transform_request )
{
    _compute_vertical_offset ( ) ;
    _compute_eye ( ) ;
    _compute_target ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: _compute_vertical_offset ( )
{
    num_fract time ;
    num_fract vertical_offset ;
    num_fract vertical_offset_period ;
    num_fract vertical_offset_amplitude ;
    num_fract vertical_offset_phase ;

    time = _logic_observer_update_state . time ;
    vertical_offset_period = _logic_observer_animation_flight_consts . vertical_offset_period ;
    vertical_offset_amplitude = _logic_observer_animation_flight_consts . vertical_offset_amplitude ;

    platform_math :: mul_fracts ( vertical_offset_phase , time , _platform_math_consts . get ( ) . fract_2pi ) ;
    platform_math :: div_fract_by ( vertical_offset_phase , vertical_offset_period ) ;

    platform_math :: sin ( vertical_offset , vertical_offset_phase ) ;
    platform_math :: mul_fract_by ( vertical_offset , vertical_offset_amplitude ) ;

    _logic_observer_animation_flight_transform_state . vertical_offset = vertical_offset ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: _compute_eye ( )
{
    num_fract vertical_offset ;
    num_fract zero ;
    vector_data eye ;

    vertical_offset = _logic_observer_animation_flight_transform_state . vertical_offset ;
    zero = _platform_math_consts . get ( ) . fract_0 ;

    platform_vector :: xyz ( eye , zero , vertical_offset , zero ) ;

    _logic_observer_animation_flight_transform_state . eye = eye ;
}

template < typename mediator >
void shy_logic_observer_animation_flight < mediator > :: _compute_target ( )
{
    num_fract time ;
    num_fract rotation_period ;
    num_fract rotation_phase ;
    num_fract vertical_offset ;
    num_fract target_x ;
    num_fract target_y ;
    num_fract target_z ;
    vector_data target ;

    time = _logic_observer_update_state . time ;
    rotation_period = _logic_observer_animation_flight_consts . rotation_period ;
    vertical_offset = _logic_observer_animation_flight_transform_state . vertical_offset ;

    platform_math :: mul_fracts ( rotation_phase , time , _platform_math_consts . get ( ) . fract_2pi ) ;
    platform_math :: div_fract_by ( rotation_phase , rotation_period ) ;

    target_y = vertical_offset ;
    platform_math :: sin ( target_x , rotation_phase ) ;
    platform_math :: cos ( target_z , rotation_phase ) ;

    platform_vector :: xyz ( target , target_x , target_y , target_z ) ;

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

