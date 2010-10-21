template < typename mediator >
class shy_logic_door_renderer
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_door_render_state_type
    {
    public :
        num_whole requested ;
    } ;

    class _logic_door_mesh_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

    class _logic_door_texture_select_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_render_request ) ;
    void receive ( typename messages :: logic_door_mesh_render_reply ) ;
    void receive ( typename messages :: logic_door_texture_select_reply ) ;
private :
    void _proceed_with_render ( ) ;
    void _render_requested ( ) ;
    void _prepare_render_state ( ) ;
    void _request_mesh_render ( ) ;
    void _request_texture_select ( ) ;
    void _reply_door_render ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_door_render_state_type _logic_door_render_state ;
    _logic_door_mesh_render_state_type _logic_door_mesh_render_state ;
    _logic_door_texture_select_state_type _logic_door_texture_select_state ;
} ;

template < typename mediator >
void shy_logic_door_renderer < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: receive ( typename messages :: logic_door_render_request )
{
    _logic_door_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_render ( ) ;
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: receive ( typename messages :: logic_door_mesh_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_mesh_render_state . requested ) )
    {
        _logic_door_mesh_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_door_mesh_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: receive ( typename messages :: logic_door_texture_select_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_texture_select_state . requested ) )
    {
        _logic_door_texture_select_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_door_texture_select_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: _proceed_with_render ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_render_state . requested ) )
    {
        _logic_door_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _render_requested ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_door_texture_select_state . replied ) )
    {
        _logic_door_texture_select_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _request_mesh_render ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_door_mesh_render_state . replied ) )
    {
        _logic_door_mesh_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_door_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: _render_requested ( )
{
    _prepare_render_state ( ) ;
    _request_texture_select ( ) ;
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: _prepare_render_state ( )
{
    _mediator . get ( ) . send ( typename messages :: engine_render_blend_disable ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: engine_render_texture_unselect ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: engine_render_disable_depth_test ( ) ) ;
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: _request_mesh_render ( )
{
    _logic_door_mesh_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_door_mesh_render_request ( ) ) ;
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: _request_texture_select ( )
{
    _logic_door_texture_select_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_door_texture_select_request ( ) ) ;
}

template < typename mediator >
void shy_logic_door_renderer < mediator > :: _reply_door_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_door_render_reply ( ) ) ;
}

