template < typename mediator >
class shy_logic_blanket_animation_disappear
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_blanket_animation_disappear_consts_type
    {
    public :
        _logic_blanket_animation_disappear_consts_type ( ) ;
    public :
        num_fract scale_begin ;
        num_fract scale_end ;
        num_fract rotation_begin ;
        num_fract rotation_end ;
        num_fract time_from_begin_to_end ;
    } ;

    class _logic_blanket_animation_disappear_transform_state_type
    {
    public :
        num_fract scale ;
        num_fract rotation ;
    } ;

    class _logic_blanket_update_state_type
    {
    public :
        num_whole started ;
        num_fract time ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_blanket_update ) ;
    void receive ( typename messages :: logic_blanket_animation_disappear_start ) ;
    void receive ( typename messages :: logic_blanket_animation_disappear_transform_request ) ;
private :
    void _compute_scale ( ) ;
    void _compute_rotation ( ) ;
    void _reply_transform ( ) ; 
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_blanket_animation_disappear_consts_type _logic_blanket_animation_disappear_consts ;

    _logic_blanket_update_state_type _logic_blanket_update_state ;
    _logic_blanket_animation_disappear_transform_state_type _logic_blanket_animation_disappear_transform_state ;
} ;

template < typename mediator >
shy_logic_blanket_animation_disappear < mediator > :: _logic_blanket_animation_disappear_consts_type :: _logic_blanket_animation_disappear_consts_type ( )
{
    platform_math :: make_num_fract ( scale_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( scale_end , 0 , 1 ) ;
    platform_math :: make_num_fract ( rotation_begin , 0 , 1 ) ;
    platform_math :: make_num_fract ( rotation_end , 10 , 1 ) ;
    platform_math :: make_num_fract ( time_from_begin_to_end , 1 , 1 ) ;
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _logic_blanket_update_state . started = _platform_math_consts . get ( ) . whole_false ;
    _logic_blanket_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: receive ( typename messages :: logic_blanket_animation_disappear_start )
{
    _logic_blanket_update_state . started = _platform_math_consts . get ( ) . whole_true ;
    _logic_blanket_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: receive ( typename messages :: logic_blanket_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_update_state . started ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_blanket_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: receive ( typename messages :: logic_blanket_animation_disappear_transform_request )
{
    _compute_scale ( ) ;
    _compute_rotation ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: _compute_scale ( )
{
    num_fract scale ;
    num_fract scale_begin ;
    num_fract scale_end ;
    num_fract time ;
    num_fract time_begin ;
    num_fract time_end ;
    num_fract time_from_begin_to_end ;

    scale_begin = _logic_blanket_animation_disappear_consts . scale_begin ;
    scale_end = _logic_blanket_animation_disappear_consts . scale_end ;
    time_from_begin_to_end = _logic_blanket_animation_disappear_consts . time_from_begin_to_end ;
    time = _logic_blanket_update_state . time ;

    time_begin = _platform_math_consts . get ( ) . fract_0 ;
    time_end = time_from_begin_to_end ;

    engine_math :: lerp ( scale , time , scale_begin , time_begin , scale_end , time_end ) ;

    _logic_blanket_animation_disappear_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: _compute_rotation ( )
{
    num_fract rotation ;
    num_fract rotation_begin ;
    num_fract rotation_end ;
    num_fract time ;
    num_fract time_begin ;
    num_fract time_end ;
    num_fract time_from_begin_to_end ;

    rotation_begin = _logic_blanket_animation_disappear_consts . rotation_begin ;
    rotation_end = _logic_blanket_animation_disappear_consts . rotation_end ;
    time_from_begin_to_end = _logic_blanket_animation_disappear_consts . time_from_begin_to_end ;
    time = _logic_blanket_update_state . time ;

    time_begin = _platform_math_consts . get ( ) . fract_0 ;
    time_end = time_from_begin_to_end ;

    engine_math :: lerp ( rotation , time , rotation_begin , time_begin , rotation_end , time_end ) ;

    _logic_blanket_animation_disappear_transform_state . rotation = rotation ;
}

template < typename mediator >
void shy_logic_blanket_animation_disappear < mediator > :: _reply_transform ( )
{
    typename messages :: logic_blanket_animation_disappear_transform_reply msg ;
    msg . scale = _logic_blanket_animation_disappear_transform_state . scale ;
    msg . rotation = _logic_blanket_animation_disappear_transform_state . rotation ;
    _mediator . get ( ) . send ( msg ) ;
}

