template < typename mediator >
class shy_logic_blanket_animation
{
    typedef typename mediator :: engine_math engine_math ;
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

    class _logic_blanket_animation_consts_type
    {
    public :
        _logic_blanket_animation_consts_type ( ) ;
    public :
        num_fract origin_x ;
        num_fract origin_y ;
        num_fract origin_z ;
    } ;

    class _logic_blanket_animation_transform_state_type
    {
    public :
        num_whole requested ;
        matrix_data transform ;
    } ;

    class _logic_blanket_animation_disappear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract scale ;
        num_fract rotation ;
    } ;

public :
    shy_logic_blanket_animation ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_blanket_animation_transform_request ) ;
    void receive ( typename messages :: logic_blanket_animation_disappear_transform_reply ) ;
private :
    shy_logic_blanket_animation < mediator > & operator= ( const shy_logic_blanket_animation < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _request_disappear_transform ( ) ;
    void _reply_computed_transform ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_blanket_animation_consts_type _logic_blanket_animation_consts ;

    _logic_blanket_animation_transform_state_type _logic_blanket_animation_transform_state ;
    _logic_blanket_animation_disappear_transform_state_type _logic_blanket_animation_disappear_transform_state ;
} ;

template < typename mediator >
shy_logic_blanket_animation < mediator > :: _logic_blanket_animation_consts_type :: _logic_blanket_animation_consts_type ( )
{
    platform_math :: make_num_fract ( origin_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( origin_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( origin_z , - 3 , 1 ) ;
}

template < typename mediator >
shy_logic_blanket_animation < mediator > :: shy_logic_blanket_animation ( )
{
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: receive ( typename messages :: logic_blanket_animation_transform_request )
{
    _logic_blanket_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: receive ( typename messages :: logic_blanket_animation_disappear_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_animation_disappear_transform_state . requested ) )
    {
        _logic_blanket_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_blanket_animation_disappear_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_blanket_animation_disappear_transform_state . scale = msg . scale ;
        _logic_blanket_animation_disappear_transform_state . rotation = msg . rotation ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_animation_transform_state . requested ) )
    {
        _logic_blanket_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_disappear_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_blanket_animation_disappear_transform_state . replied ) )
    {
        _logic_blanket_animation_disappear_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_computed_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: _request_disappear_transform ( )
{
    _logic_blanket_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_blanket_animation_disappear_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: _reply_computed_transform ( )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: _compute_transform ( )
{
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    num_fract disappear_scale ;
    num_fract disappear_rotation ;
    num_fract one ;
    num_fract zero ;
    num_fract scale ;
    num_fract rotation ;
    vector_data axis_x ;
    vector_data axis_y ;
    vector_data axis_z ;
    matrix_data transform ;

    origin_x = _logic_blanket_animation_consts . origin_x ;
    origin_y = _logic_blanket_animation_consts . origin_y ;
    origin_z = _logic_blanket_animation_consts . origin_z ;
    one = _platform_math_consts . get ( ) . fract_1 ;
    zero = _platform_math_consts . get ( ) . fract_0 ;
    disappear_scale = _logic_blanket_animation_disappear_transform_state . scale ;
    disappear_rotation = _logic_blanket_animation_disappear_transform_state . rotation ;

    scale = disappear_scale ;
    rotation = disappear_rotation ;

    engine_math :: rotation_z ( axis_x , axis_y , rotation ) ;
    platform_vector :: xyz ( axis_z , zero , zero , one ) ;

    platform_vector :: mul_by ( axis_x , scale ) ;
    platform_vector :: mul_by ( axis_y , scale ) ;

    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , axis_x ) ;
    platform_matrix :: set_axis_y ( transform , axis_y ) ;
    platform_matrix :: set_axis_z ( transform , axis_z ) ;
    platform_matrix :: set_origin ( transform , origin_x , origin_y , origin_z ) ;

    _logic_blanket_animation_transform_state . transform = transform ;
}

template < typename mediator >
void shy_logic_blanket_animation < mediator > :: _reply_transform ( )
{
    typename messages :: logic_blanket_animation_transform_reply msg ;
    msg . transform = _logic_blanket_animation_transform_state . transform ;
    _mediator . get ( ) . send ( msg ) ;
}

