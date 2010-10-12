template < typename mediator >
class shy_logic_room_mesh
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

    class _logic_room_mesh_consts_type
    {
    public :
        _logic_room_mesh_consts_type ( ) ;
    public :
        num_fract color_r ;
        num_fract color_g ;
        num_fract color_b ;
        num_fract color_a ;
    } ;

    class _logic_room_mesh_create_state_type
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
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
    void receive ( typename messages :: logic_room_mesh_create ) ;
private :
    void _proceed_with_creation ( ) ;
    void _request_mesh_creation ( ) ;
    void _mesh_created ( ) ;
    void _fill_mesh_contents ( ) ;
    void _reply_mesh_creation_finished ( ) ;
    void _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    _logic_room_mesh_consts_type _logic_room_mesh_consts ;

    _logic_room_mesh_create_state_type _logic_room_mesh_create_state ;
    _engine_render_mesh_create_state_type _engine_render_mesh_create_state ;
} ;

template < typename mediator >
shy_logic_room_mesh < mediator > :: _logic_room_mesh_consts_type :: _logic_room_mesh_consts_type ( )
{
    platform_math :: make_num_fract ( color_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_a , 1 , 1 ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
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
void shy_logic_room_mesh < mediator > :: receive ( typename messages :: logic_room_mesh_create )
{
    _logic_room_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_creation ( ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_mesh_create_state . requested ) )
    {
        _logic_room_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_mesh_creation ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . replied ) )
    {
        _engine_render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _mesh_created ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _request_mesh_creation ( )
{
    _engine_render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    typename messages :: engine_render_mesh_create_request msg ;
    msg . vertices = _platform_math_consts . get ( ) . whole_4 ;
    msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_4 ;
    msg . triangle_fan_indices = _platform_math_consts . get ( ) . whole_0 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _mesh_created ( )
{
    _fill_mesh_contents ( ) ;
    _reply_mesh_creation_finished ( ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _fill_mesh_contents ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z ;
    num_fract color_r ;
    num_fract color_g ;
    num_fract color_b ;
    num_fract color_a ;
    num_whole index ;
    
    x_left = _platform_math_consts . get ( ) . fract_minus_1 ;
    x_right = _platform_math_consts . get ( ) . fract_1 ;
    y_top = _platform_math_consts . get ( ) . fract_1 ;
    y_bottom = _platform_math_consts . get ( ) . fract_minus_1 ;
    u_left = _platform_math_consts . get ( ) . fract_0 ;
    u_right = _platform_math_consts . get ( ) . fract_1 ;
    v_top = _platform_math_consts . get ( ) . fract_1 ;
    v_bottom = _platform_math_consts . get ( ) . fract_0 ;
    z = _platform_math_consts . get ( ) . fract_0 ;
    color_r = _logic_room_mesh_consts . color_r ;
    color_g = _logic_room_mesh_consts . color_g ;
    color_b = _logic_room_mesh_consts . color_b ;
    color_a = _logic_room_mesh_consts . color_a ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_0 , x_left , y_top , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_0 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_0 , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 ) ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_1 , x_left , y_bottom , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_1 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_1 , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_1 , _platform_math_consts . get ( ) . whole_1 ) ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_2 , x_right , y_top , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_2 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_2 , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_2 , _platform_math_consts . get ( ) . whole_2 ) ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_3 , x_right , y_bottom , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_3 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_3 , u_right , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_3 , _platform_math_consts . get ( ) . whole_3 ) ;

    typename messages :: engine_render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _reply_mesh_creation_finished ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_room_mesh_creation_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z )
{
    typename messages :: engine_render_mesh_set_vertex_position msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v )
{
    typename messages :: engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
{
    typename messages :: engine_render_mesh_set_vertex_color msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index )
{
    typename messages :: engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}

