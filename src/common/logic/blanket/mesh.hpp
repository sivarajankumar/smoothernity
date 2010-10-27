template < typename mediator >
class shy_logic_blanket_mesh
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_blanket_mesh_consts_type
    {
    public :
        _logic_blanket_mesh_consts_type ( ) ;
    public :
        num_fract vertex_x_left ;
        num_fract vertex_x_right ;
        num_fract vertex_y_bottom ;
        num_fract vertex_y_top ;
        num_fract color_r ;
        num_fract color_g ;
        num_fract color_b ;
        num_fract color_a ;
        num_whole vertices ;
        num_whole triangle_strip_indices ;
        num_whole triangle_fan_indices ;
    } ;

    class _logic_blanket_mesh_create_state_type
    {
    public :
        num_whole requested ;
    } ;

    class _engine_render_mesh_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        engine_render_mesh_id mesh ;
    } ;

public :
    shy_logic_blanket_mesh ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_blanket_mesh_create ) ;
    void receive ( typename messages :: logic_blanket_mesh_render_request ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
private :
    shy_logic_blanket_mesh < mediator > & operator= ( const shy_logic_blanket_mesh < mediator > & ) ;
    void _proceed_with_creation ( ) ;
    void _request_mesh_create ( ) ;
    void _mesh_created ( ) ;
    void _fill_mesh_contents ( ) ;
    void _transform_mesh ( ) ;
    void _finalize_mesh ( ) ;
    void _reply_creation_finished ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_blanket_mesh_consts_type _logic_blanket_mesh_consts ;

    _logic_blanket_mesh_create_state_type _logic_blanket_mesh_create_state ;
    _engine_render_mesh_create_state_type _engine_render_mesh_create_state ;
} ;

template < typename mediator >
shy_logic_blanket_mesh < mediator > :: _logic_blanket_mesh_consts_type :: _logic_blanket_mesh_consts_type ( )
{
    platform_math :: make_num_fract ( vertex_x_left , - 1 , 1 ) ;
    platform_math :: make_num_fract ( vertex_x_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( vertex_y_bottom , -1 , 1 ) ;
    platform_math :: make_num_fract ( vertex_y_top , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_a , 1 , 1 ) ;
    platform_math :: make_num_whole ( vertices , 4 ) ;
    platform_math :: make_num_whole ( triangle_strip_indices , 4 ) ;
    platform_math :: make_num_whole ( triangle_fan_indices , 0 ) ;
}

template < typename mediator >
shy_logic_blanket_mesh < mediator > :: shy_logic_blanket_mesh ( )
{
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: receive ( typename messages :: logic_blanket_mesh_create )
{
    _logic_blanket_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_creation ( ) ;
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: receive ( typename messages :: logic_blanket_mesh_render_request )
{
    _mediator . get ( ) . send ( typename messages :: logic_blanket_mesh_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . requested ) )
    {
        _engine_render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_mesh_create_state . mesh = msg . mesh ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_mesh_create_state . requested ) )
    {
        _logic_blanket_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_mesh_create ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . replied ) )
    {
        _engine_render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _mesh_created ( ) ;
    }
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: _request_mesh_create ( )
{
    _engine_render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    typename messages :: engine_render_mesh_create_request msg ;
    msg . vertices = _logic_blanket_mesh_consts . vertices ;
    msg . triangle_strip_indices = _logic_blanket_mesh_consts . triangle_strip_indices ;
    msg . triangle_fan_indices = _logic_blanket_mesh_consts . triangle_fan_indices ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: _mesh_created ( )
{
    _fill_mesh_contents ( ) ;
    _finalize_mesh ( ) ;
    _transform_mesh ( ) ;
    _reply_creation_finished ( ) ;
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: _fill_mesh_contents ( )
{
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: _transform_mesh ( )
{
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: _finalize_mesh ( )
{
    typename messages :: engine_render_mesh_finalize msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_blanket_mesh < mediator > :: _reply_creation_finished ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_blanket_mesh_creation_finished ( ) ) ;
}

