template < typename mediator >
class shy_logic_door_animation
{
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

    class _logic_door_animation_consts_type
    {
    public :
        _logic_door_animation_consts_type ( ) ;
    public :
        num_fract origin_x ;
        num_fract origin_y ;
        num_fract origin_z ;
    } ;

    class _logic_door_animation_transform_state_type
    {
    public :
        num_whole requested ;
        matrix_data transform ;
    } ;

    class _logic_door_animation_appear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract scale ;
    } ;

public :
    shy_logic_door_animation ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_animation_transform_request ) ;
    void receive ( typename messages :: logic_door_animation_appear_transform_reply ) ;
private :
    shy_logic_door_animation < mediator > & operator= ( const shy_logic_door_animation < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _request_appear_transform ( ) ;
    void _reply_computed_transform ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_door_animation_consts_type _logic_door_animation_consts ;

    _logic_door_animation_transform_state_type _logic_door_animation_transform_state ;
    _logic_door_animation_appear_transform_state_type _logic_door_animation_appear_transform_state ;
} ;

template < typename mediator >
shy_logic_door_animation < mediator > :: _logic_door_animation_consts_type :: _logic_door_animation_consts_type ( )
{
    platform_math :: make_num_fract ( origin_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( origin_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( origin_z , - 3 , 1 ) ;
}

template < typename mediator >
shy_logic_door_animation < mediator > :: shy_logic_door_animation ( )
{
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: receive ( typename messages :: logic_door_animation_transform_request )
{
    _logic_door_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: receive ( typename messages :: logic_door_animation_appear_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_animation_appear_transform_state . requested ) )
    {
        _logic_door_animation_appear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_door_animation_appear_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_door_animation_appear_transform_state . scale = msg . scale ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_animation_transform_state . requested ) )
    {
        _logic_door_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_appear_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_door_animation_appear_transform_state . replied ) )
    {
        _logic_door_animation_appear_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_computed_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: _request_appear_transform ( )
{
    _logic_door_animation_appear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_door_animation_appear_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: _reply_computed_transform ( )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: _compute_transform ( )
{
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    num_fract scale ;
    num_fract zero ;
    matrix_data transform ;

    origin_x = _logic_door_animation_consts . origin_x ;
    origin_y = _logic_door_animation_consts . origin_y ;
    origin_z = _logic_door_animation_consts . origin_z ;
    scale = _logic_door_animation_appear_transform_state . scale ;
    zero = _platform_math_consts . get ( ) . fract_0 ;

    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , scale , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , scale , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , scale ) ;
    platform_matrix :: set_origin ( transform , origin_x , origin_y , origin_z ) ;

    _logic_door_animation_transform_state . transform = transform ;
}

template < typename mediator >
void shy_logic_door_animation < mediator > :: _reply_transform ( )
{
    typename messages :: logic_door_animation_transform_reply msg ;
    msg . transform = _logic_door_animation_transform_state . transform ;
    _mediator . get ( ) . send ( msg ) ;
}

