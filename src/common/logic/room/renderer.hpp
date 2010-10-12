template < typename mediator >
class shy_logic_room_renderer
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_room_render_state_type
    {
    public :
        num_whole requested ;
        num_whole render_permitted ;
    } ;

    class _logic_room_mesh_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_room_render ) ;
    void receive ( typename messages :: logic_room_render_permit ) ;
    void receive ( typename messages :: logic_room_mesh_render_reply ) ;
private :
    void _proceed_with_render ( ) ;
    void _request_mesh_render ( ) ;
    void _mesh_rendered ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_room_render_state_type _logic_room_render_state ;
    _logic_room_mesh_render_state_type _logic_room_mesh_render_state ;
} ;

template < typename mediator >
void shy_logic_room_renderer < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_room_renderer < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_room_renderer < mediator > :: receive ( typename messages :: logic_room_render )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_render_state . render_permitted ) )
    {        
        _logic_room_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_renderer < mediator > :: receive ( typename messages :: logic_room_render_permit )
{
    _logic_room_render_state . render_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_room_renderer < mediator > :: receive ( typename messages :: logic_room_mesh_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_mesh_render_state . requested ) )
    {
        _logic_room_mesh_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_room_mesh_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_renderer < mediator > :: _proceed_with_render ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_render_state . requested ) )
    {
        _logic_room_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_mesh_render ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_room_mesh_render_state . replied ) )
    {
        _logic_room_mesh_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _mesh_rendered ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_renderer < mediator > :: _request_mesh_render ( )
{
    _logic_room_mesh_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_room_mesh_render_request ( ) ) ;
}

template < typename mediator >
void shy_logic_room_renderer < mediator > :: _mesh_rendered ( )
{
}

