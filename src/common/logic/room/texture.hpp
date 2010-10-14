template < typename mediator >
class shy_logic_room_texture
{
    typedef typename mediator :: engine_render_stateless :: engine_render_texture_id engine_render_texture_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_room_texture_consts
    {
    public :
        _logic_room_texture_consts ( ) ;
    public :
        num_fract pen_intensity ;
        num_fract paper_intensity ;
        num_fract alpha ;
    } ;

    class _logic_room_texture_create_state_type
    {
    public :
        num_whole requested ;
    } ;

    class _engine_render_texture_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        engine_render_texture_id texture ;
    } ;

    class _engine_rasterizer_finalize_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_room_texture_create ) ;
    void receive ( typename messages :: logic_room_texture_select_request ) ;
    void receive ( typename messages :: engine_render_texture_create_reply ) ;
    void receive ( typename messages :: engine_rasterizer_finalize_reply ) ;
private :
    void _proceed_with_creation ( ) ;
    void _request_texture_create ( ) ;
    void _texture_received ( ) ;
    void _rasterizer_finalized ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_room_texture_create_state_type _logic_room_texture_create_state ;
    _engine_render_texture_create_state_type _engine_render_texture_create_state ;
    _engine_rasterizer_finalize_state_type _engine_rasterizer_finalize_state ;
} ;

template < typename mediator >
shy_logic_room_texture < mediator > :: _logic_room_texture_consts :: _logic_room_texture_consts ( )
{
    platform_math :: make_num_fract ( pen_intensity , 1 , 1 ) ;
    platform_math :: make_num_fract ( paper_intensity , 1 , 2 ) ;
    platform_math :: make_num_fract ( alpha , 1 , 1 ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: logic_room_texture_create )
{
    _logic_room_texture_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_creation ( ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: logic_room_texture_select_request )
{
    _mediator . get ( ) . send ( typename messages :: logic_room_texture_select_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: engine_render_texture_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_texture_create_state . requested ) )
    {
        _engine_render_texture_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_texture_create_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_texture_create_state . texture = msg . texture ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: engine_rasterizer_finalize_reply )
{
    if ( platform_conditions :: whole_is_true ( _engine_rasterizer_finalize_state . requested ) )
    {
        _engine_rasterizer_finalize_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_rasterizer_finalize_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_texture_create_state . requested ) )
    {
        _logic_room_texture_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_texture_create ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_texture_create_state . replied ) )
    {
        _engine_render_texture_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _texture_received ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_rasterizer_finalize_state . replied ) )
    {
        _engine_rasterizer_finalize_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _rasterizer_finalized ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _request_texture_create ( )
{
    _engine_render_texture_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_texture_create_request ( ) ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _texture_received ( )
{
    _engine_rasterizer_finalize_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_rasterizer_finalize_request ( ) ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _rasterizer_finalized ( )
{
    typename messages :: engine_render_texture_finalize msg ;
    msg . texture = _engine_render_texture_create_state . texture ;
    _mediator . get ( ) . send ( msg ) ;

    _mediator . get ( ) . send ( typename messages :: logic_room_texture_creation_finished ( ) ) ;
}

