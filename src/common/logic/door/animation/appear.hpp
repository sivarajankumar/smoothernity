template < typename mediator >
class shy_logic_door_animation_appear
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: logic_door_animation_stateless :: logic_door_animation_stateless_consts_type logic_door_animation_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_door_animation_appear_transform_state_type
    {
    public :
        num_fract scale ;
    } ;

    class _logic_door_update_state_type
    {
    public :
        num_whole started ;
        num_fract time ;
    } ;

public :
    shy_logic_door_animation_appear ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_update ) ;
    void receive ( typename messages :: logic_door_animation_appear_start ) ;
    void receive ( typename messages :: logic_door_animation_appear_transform_request ) ;
private :
    shy_logic_door_animation_appear < mediator > & operator= ( const shy_logic_door_animation_appear < mediator > & ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_door_animation_stateless_consts_type > _logic_door_animation_stateless_consts ;

    _logic_door_update_state_type _logic_door_update_state ;
    _logic_door_animation_appear_transform_state_type _logic_door_animation_appear_transform_state ;
} ;

template < typename mediator >
shy_logic_door_animation_appear < mediator > :: shy_logic_door_animation_appear ( )
{
}

template < typename mediator >
void shy_logic_door_animation_appear < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door_animation_appear < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_door_animation_stateless_consts ( _logic_door_animation_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _logic_door_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_door_animation_appear < mediator > :: receive ( typename messages :: logic_door_animation_appear_start )
{
    _logic_door_update_state . started = _platform_math_consts . get ( ) . whole_true ;
    _logic_door_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_door_animation_appear < mediator > :: receive ( typename messages :: logic_door_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_update_state . started ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_door_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_door_animation_appear < mediator > :: receive ( typename messages :: logic_door_animation_appear_transform_request )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_door_animation_appear < mediator > :: _compute_transform ( )
{
    num_fract scale_begin ;
    num_fract scale_end ;
    num_fract scale ;
    num_fract time_from_begin_to_end ;
    num_fract time_begin ;
    num_fract time_end ;
    num_fract time ;

    scale_begin = _logic_door_animation_stateless_consts . get ( ) . appear_scale_begin ;
    scale_end = _logic_door_animation_stateless_consts . get ( ) . appear_scale_end ;
    time_from_begin_to_end = _logic_door_animation_stateless_consts . get ( ) . appear_time_from_begin_to_end ;
    time = _logic_door_update_state . time ;

    time_begin = _platform_math_consts . get ( ) . fract_0 ;
    time_end = time_from_begin_to_end ;
    
    engine_math :: hard_in_easy_out
        ( scale
        , time
        , scale_begin
        , time_begin
        , scale_end
        , time_end
        ) ;

    _logic_door_animation_appear_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_door_animation_appear < mediator > :: _reply_transform ( )
{
    typename messages :: logic_door_animation_appear_transform_reply msg ;
    msg . scale = _logic_door_animation_appear_transform_state . scale ;
    _mediator . get ( ) . send ( msg ) ;
}

