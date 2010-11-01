template < typename mediator >
class shy_logic_blanket_placement
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_blanket_place_state_type
    {
    public :
        num_whole requested ;
    } ;

    class _logic_blanket_animation_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        matrix_data transform ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_blanket_place ) ;
    void receive ( typename messages :: logic_blanket_animation_transform_reply ) ;
private :
    void _proceed_with_place ( ) ;
    void _request_animation_transform ( ) ;
    void _transform_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_blanket_place_state_type _logic_blanket_place_state ;
    _logic_blanket_animation_transform_state_type _logic_blanket_animation_transform_state ;
} ;

template < typename mediator >
void shy_logic_blanket_placement < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_blanket_placement < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_blanket_placement < mediator > :: receive ( typename messages :: logic_blanket_place )
{
    _logic_blanket_place_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_place ( ) ;
}

template < typename mediator >
void shy_logic_blanket_placement < mediator > :: receive ( typename messages :: logic_blanket_animation_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_animation_transform_state . requested ) )
    {
        _logic_blanket_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_blanket_animation_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_blanket_animation_transform_state . transform = msg . transform ;
        _proceed_with_place ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_placement < mediator > :: _proceed_with_place ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_place_state . requested ) )
    {
        _logic_blanket_place_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_animation_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_blanket_animation_transform_state . replied ) )
    {
        _logic_blanket_animation_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _transform_mesh ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_placement < mediator > :: _request_animation_transform ( )
{
    _logic_blanket_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_blanket_animation_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_blanket_placement < mediator > :: _transform_mesh ( )
{
    typename messages :: logic_blanket_mesh_set_transform msg ;
    msg . transform = _logic_blanket_animation_transform_state . transform ;
    _mediator . get ( ) . send ( msg ) ;
}

