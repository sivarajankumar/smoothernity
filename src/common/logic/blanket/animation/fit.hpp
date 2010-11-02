template < typename mediator >
class shy_logic_blanket_animation_fit
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_blanket_animation_fit_transform_state_type
    {
    public :
        num_whole requested ;
        num_fract scale ;
    } ;

    class _engine_render_aspect_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract width ;
        num_fract height ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_blanket_animation_fit_transform_request ) ;
    void receive ( typename messages :: engine_render_aspect_reply ) ;
private :
    void _proceed_with_transform ( ) ;
    void _request_aspect_ratio ( ) ;
    void _reply_computed_transform ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _engine_render_aspect_state_type _engine_render_aspect_state ;
    _logic_blanket_animation_fit_transform_state_type _logic_blanket_animation_fit_transform_state ;
} ;

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: receive ( typename messages :: logic_blanket_animation_fit_transform_request )
{
    _logic_blanket_animation_fit_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: receive ( typename messages :: engine_render_aspect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . requested ) )
    {
        _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_aspect_state . width = msg . width ;
        _engine_render_aspect_state . height = msg . height ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_animation_fit_transform_state . requested ) )
    {
        _logic_blanket_animation_fit_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_aspect_ratio ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . replied ) )
    {
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_computed_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: _request_aspect_ratio ( )
{
    _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: _reply_computed_transform ( )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: _compute_transform ( )
{
    num_fract width ;
    num_fract height ;
    num_fract scale ;

    width = _engine_render_aspect_state . width ;
    height = _engine_render_aspect_state . height ;

    platform_math :: add_fracts ( scale , width , height ) ;
    platform_math :: mul_fract_by ( scale , _platform_math_consts . get ( ) . fract_2 ) ;

    _logic_blanket_animation_fit_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_blanket_animation_fit < mediator > :: _reply_transform ( )
{
    typename messages :: logic_blanket_animation_fit_transform_reply msg ;
    msg . scale = _logic_blanket_animation_fit_transform_state . scale ;
    _mediator . get ( ) . send ( msg ) ;
}

