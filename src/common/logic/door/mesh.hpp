template < typename mediator >
class shy_logic_door_mesh
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: logic_door_stateless :: logic_door_stateless_consts_type logic_door_stateless_consts_type ;
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

    class _logic_door_mesh_consts_type
    {
    public :
        _logic_door_mesh_consts_type ( ) ;
    public :
        num_whole mesh_vertices_count ;
        num_whole mesh_triangle_strip_indices_count ;
        num_whole mesh_triangle_fan_indices_count ;
    } ;

    class _engine_render_mesh_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole finalized ;
        engine_render_mesh_id mesh ;
    } ;

    class _logic_door_mesh_create_state_type
    {
    public :
        num_whole requested ;
    } ;

public :
    shy_logic_door_mesh ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_mesh_create ) ;
    void receive ( typename messages :: logic_door_mesh_render_request ) ;
    void receive ( typename messages :: logic_door_mesh_set_transform ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
private :
    shy_logic_door_mesh < mediator > & operator= ( const shy_logic_door_mesh < mediator > & ) ;
    void _proceed_with_creation ( ) ;
    void _request_mesh_create ( ) ;
    void _mesh_created ( ) ;
    void _fill_mesh_contents ( ) ;
    void _finalize_mesh ( ) ;
    void _reply_creation_finished ( ) ;
    void _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_door_stateless_consts_type > _logic_door_stateless_consts ;
    const _logic_door_mesh_consts_type _logic_door_mesh_consts ;

    _engine_render_mesh_create_state_type _engine_render_mesh_create_state ;
    _logic_door_mesh_create_state_type _logic_door_mesh_create_state ;
} ;

template < typename mediator >
shy_logic_door_mesh < mediator > :: _logic_door_mesh_consts_type :: _logic_door_mesh_consts_type ( )
{
    platform_math :: make_num_whole ( mesh_vertices_count , 4 ) ;
    platform_math :: make_num_whole ( mesh_triangle_strip_indices_count , 4 ) ;
    platform_math :: make_num_whole ( mesh_triangle_fan_indices_count , 0 ) ;
}

template < typename mediator >
shy_logic_door_mesh < mediator > :: shy_logic_door_mesh ( )
{
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_door_stateless_consts ( _logic_door_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: receive ( typename messages :: logic_door_mesh_create )
{
    _logic_door_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;    
    _proceed_with_creation ( ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: receive ( typename messages :: logic_door_mesh_render_request )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . finalized ) )
    {
        typename messages :: engine_render_mesh_render msg ;
        msg . mesh = _engine_render_mesh_create_state . mesh ;
        _mediator . get ( ) . send ( msg ) ;
    }
    _mediator . get ( ) . send ( typename messages :: logic_door_mesh_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: receive ( typename messages :: logic_door_mesh_set_transform msg )
{
    typename messages :: engine_render_mesh_set_transform mesh_msg ;
    mesh_msg . transform = msg . transform ;
    mesh_msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( mesh_msg ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
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
void shy_logic_door_mesh < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_mesh_create_state . requested ) )
    {
        _logic_door_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_mesh_create ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . replied ) )
    {
        _engine_render_mesh_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _mesh_created ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: _request_mesh_create ( )
{
    _engine_render_mesh_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    typename messages :: engine_render_mesh_create_request msg ;
    msg . vertices = _logic_door_mesh_consts . mesh_vertices_count ;
    msg . triangle_strip_indices = _logic_door_mesh_consts . mesh_triangle_strip_indices_count ;
    msg . triangle_fan_indices = _logic_door_mesh_consts . mesh_triangle_fan_indices_count ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: _mesh_created ( )
{
    _fill_mesh_contents ( ) ;
    _finalize_mesh ( ) ;
    _reply_creation_finished ( ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: _fill_mesh_contents ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract u_top_left ;
    num_fract v_top_left ;
    num_fract u_top_right ;
    num_fract v_top_right ;
    num_fract u_bottom_left ;
    num_fract v_bottom_left ;
    num_fract u_bottom_right ;
    num_fract v_bottom_right ;
    num_fract z ;
    num_fract color_r ;
    num_fract color_g ;
    num_fract color_b ;
    num_fract color_a ; 
    num_whole current_index ;
    
    x_left = _logic_door_stateless_consts . get ( ) . mesh_x_left ;
    x_right = _logic_door_stateless_consts . get ( ) . mesh_x_right ;
    y_top = _logic_door_stateless_consts . get ( ) . mesh_y_top ; 
    y_bottom = _logic_door_stateless_consts . get ( ) . mesh_y_bottom ; 
    u_top_left = _logic_door_stateless_consts . get ( ) . mesh_u_top_left ;
    v_top_left = _logic_door_stateless_consts . get ( ) . mesh_v_top_left ;
    u_top_right = _logic_door_stateless_consts . get ( ) . mesh_u_top_right ;
    v_top_right = _logic_door_stateless_consts . get ( ) . mesh_v_top_right ;
    u_bottom_left = _logic_door_stateless_consts . get ( ) . mesh_u_bottom_left ;
    v_bottom_left = _logic_door_stateless_consts . get ( ) . mesh_v_bottom_left ;
    u_bottom_right = _logic_door_stateless_consts . get ( ) . mesh_u_bottom_right ;
    v_bottom_right = _logic_door_stateless_consts . get ( ) . mesh_v_bottom_right ;
    z = _logic_door_stateless_consts . get ( ) . mesh_z ;

    color_r = _logic_door_stateless_consts . get ( ) . mesh_color_r ;
    color_g = _logic_door_stateless_consts . get ( ) . mesh_color_g ;
    color_b = _logic_door_stateless_consts . get ( ) . mesh_color_b ;
    color_a = _logic_door_stateless_consts . get ( ) . mesh_color_a ;

    current_index = _platform_math_consts . get ( ) . whole_0 ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z ) ;
    _mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_top_left , v_top_left ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z ) ;
    _mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_bottom_left , v_bottom_left ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z ) ;
    _mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_top_right , v_top_right ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z ) ;
    _mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_bottom_right , v_bottom_right ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: _finalize_mesh ( )
{
    _engine_render_mesh_create_state . finalized = _platform_math_consts . get ( ) . whole_true ;
    typename messages :: engine_render_mesh_finalize msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: _reply_creation_finished ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_door_mesh_creation_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z )
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
void shy_logic_door_mesh < mediator > :: _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v )
{
    typename messages :: engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_door_mesh < mediator > :: _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
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
void shy_logic_door_mesh < mediator > :: _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index )
{
    typename messages :: engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}

