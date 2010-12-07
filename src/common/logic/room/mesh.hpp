template < typename mediator >
class shy_logic_room_mesh
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: logic_room_stateless :: logic_room_stateless_consts_type logic_room_stateless_consts_type ;
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

    class _logic_room_mesh_consts_type
    {
    public :
        _logic_room_mesh_consts_type ( ) ;
    public :
        num_whole vertices_count ;
        num_whole triangle_strip_indices_count ;
    } ;

    class _logic_room_mesh_create_state_type
    {
    public :
        num_whole requested ;
        num_whole current_index ;
    } ;

    class _engine_render_mesh_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole finalized ;
        engine_render_mesh_id mesh ;
    } ;

public :
    shy_logic_room_mesh ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
    void receive ( typename messages :: logic_room_mesh_create ) ;
    void receive ( typename messages :: logic_room_mesh_render_request ) ;
private :
    shy_logic_room_mesh < mediator > & operator= ( const shy_logic_room_mesh < mediator > & ) ;
    void _proceed_with_creation ( ) ;
    void _request_mesh_creation ( ) ;
    void _mesh_created ( ) ;
    void _fill_mesh_contents ( ) ;
    void _transform_mesh ( ) ;
    void _reply_mesh_creation_finished ( ) ;
    void _add_cube_sides ( ) ;
    void _add_near_side ( ) ;
    void _add_far_side ( ) ;
    void _add_left_side ( ) ;
    void _add_right_side ( ) ;
    void _add_top_side ( ) ;
    void _add_bottom_side ( ) ;
    void _finalize_mesh ( ) ;
    void _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_room_stateless_consts_type > _logic_room_stateless_consts ;
    const _logic_room_mesh_consts_type _logic_room_mesh_consts ;

    _logic_room_mesh_create_state_type _logic_room_mesh_create_state ;
    _engine_render_mesh_create_state_type _engine_render_mesh_create_state ;
} ;

template < typename mediator >
shy_logic_room_mesh < mediator > :: _logic_room_mesh_consts_type :: _logic_room_mesh_consts_type ( )
{
    platform_math :: make_num_whole ( vertices_count , 27 ) ;
    platform_math :: make_num_whole ( triangle_strip_indices_count , 27 ) ;
}

template < typename mediator >
shy_logic_room_mesh < mediator > :: shy_logic_room_mesh ( )
{
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
    _mediator . get ( ) . logic_room_stateless_consts ( _logic_room_stateless_consts ) ;
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
void shy_logic_room_mesh < mediator > :: receive ( typename messages :: logic_room_mesh_render_request )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_mesh_create_state . finalized ) )
    {
        typename messages :: engine_render_mesh_render render_msg ;
        render_msg . mesh = _engine_render_mesh_create_state . mesh ;
        _mediator . get ( ) . send ( render_msg ) ;
    }
    _mediator . get ( ) . send ( typename messages :: logic_room_mesh_render_reply ( ) ) ;
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
    msg . vertices = _logic_room_mesh_consts . vertices_count ;
    msg . triangle_strip_indices = _logic_room_mesh_consts . triangle_strip_indices_count ;
    msg . triangle_fan_indices = _platform_math_consts . get ( ) . whole_0 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _mesh_created ( )
{
    _fill_mesh_contents ( ) ;
    _transform_mesh ( ) ;
    _reply_mesh_creation_finished ( ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _fill_mesh_contents ( )
{
    _add_cube_sides ( ) ;
    _finalize_mesh ( ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_cube_sides ( )
{
    _logic_room_mesh_create_state . current_index = _platform_math_consts . get ( ) . whole_0 ;
    _add_near_side ( ) ;
    _add_right_side ( ) ;
    _add_far_side ( ) ;
    _add_left_side ( ) ;
    _add_top_side ( ) ;
    _add_bottom_side ( ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_near_side ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract near_side_u_left ;
    num_fract near_side_u_right ;
    num_fract near_side_v_top ;
    num_fract near_side_v_bottom ;
    num_fract z_near ;
    num_fract color_near_r ;
    num_fract color_near_g ;
    num_fract color_near_b ;
    num_fract color_near_a ; 
    num_whole current_index ;
    
    x_left = _logic_room_stateless_consts . get ( ) . mesh_x_left ;
    x_right = _logic_room_stateless_consts . get ( ) . mesh_x_right ;
    y_top = _logic_room_stateless_consts . get ( ) . mesh_y_top ; 
    y_bottom = _logic_room_stateless_consts . get ( ) . mesh_y_bottom ; 
    near_side_u_left = _logic_room_stateless_consts . get ( ) . mesh_near_side_u_left ;
    near_side_u_right = _logic_room_stateless_consts . get ( ) . mesh_near_side_u_right ;
    near_side_v_top = _logic_room_stateless_consts . get ( ) . mesh_near_side_v_top ;
    near_side_v_bottom = _logic_room_stateless_consts . get ( ) . mesh_near_side_v_bottom ;
    z_near = _logic_room_stateless_consts . get ( ) . mesh_z_near ;

    color_near_r = _logic_room_stateless_consts . get ( ) . mesh_color_near_r ;
    color_near_g = _logic_room_stateless_consts . get ( ) . mesh_color_near_g ;
    color_near_b = _logic_room_stateless_consts . get ( ) . mesh_color_near_b ;
    color_near_a = _logic_room_stateless_consts . get ( ) . mesh_color_near_a ;

    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , near_side_u_left , near_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , near_side_u_left , near_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , near_side_u_right , near_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , near_side_u_right , near_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _logic_room_mesh_create_state . current_index = current_index ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_right_side ( )
{
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract right_side_u_left ;
    num_fract right_side_u_right ;
    num_fract right_side_v_top ;
    num_fract right_side_v_bottom ;
    num_fract z_near ;
    num_fract z_far ;
    num_fract color_right_r ;
    num_fract color_right_g ;
    num_fract color_right_b ;
    num_fract color_right_a ;
    num_whole current_index ;
    
    x_right = _logic_room_stateless_consts . get ( ) . mesh_x_right ;
    y_top = _logic_room_stateless_consts . get ( ) . mesh_y_top ; 
    y_bottom = _logic_room_stateless_consts . get ( ) . mesh_y_bottom ; 
    right_side_u_left = _logic_room_stateless_consts . get ( ) . mesh_right_side_u_left ;
    right_side_u_right = _logic_room_stateless_consts . get ( ) . mesh_right_side_u_right ;
    right_side_v_top = _logic_room_stateless_consts . get ( ) . mesh_right_side_v_top ;
    right_side_v_bottom = _logic_room_stateless_consts . get ( ) . mesh_right_side_v_bottom ;
    z_near = _logic_room_stateless_consts . get ( ) . mesh_z_near ;
    z_far = _logic_room_stateless_consts . get ( ) . mesh_z_far ;

    color_right_r = _logic_room_stateless_consts . get ( ) . mesh_color_right_r ;
    color_right_g = _logic_room_stateless_consts . get ( ) . mesh_color_right_g ;
    color_right_b = _logic_room_stateless_consts . get ( ) . mesh_color_right_b ;
    color_right_a = _logic_room_stateless_consts . get ( ) . mesh_color_right_a ;

    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , right_side_u_left , right_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , right_side_u_left , right_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , right_side_u_right , right_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , right_side_u_right , right_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _logic_room_mesh_create_state . current_index = current_index ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_far_side ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract far_side_u_left ;
    num_fract far_side_u_right ;
    num_fract far_side_v_top ;
    num_fract far_side_v_bottom ;
    num_fract z_far ;
    num_fract color_far_r ;
    num_fract color_far_g ;
    num_fract color_far_b ;
    num_fract color_far_a ; 
    num_whole current_index ;
    
    x_left = _logic_room_stateless_consts . get ( ) . mesh_x_left ;
    x_right = _logic_room_stateless_consts . get ( ) . mesh_x_right ;
    y_top = _logic_room_stateless_consts . get ( ) . mesh_y_top ; 
    y_bottom = _logic_room_stateless_consts . get ( ) . mesh_y_bottom ; 
    far_side_u_left = _logic_room_stateless_consts . get ( ) . mesh_far_side_u_left ;
    far_side_u_right = _logic_room_stateless_consts . get ( ) . mesh_far_side_u_right ;
    far_side_v_top = _logic_room_stateless_consts . get ( ) . mesh_far_side_v_top ;
    far_side_v_bottom = _logic_room_stateless_consts . get ( ) . mesh_far_side_v_bottom ;
    z_far = _logic_room_stateless_consts . get ( ) . mesh_z_far ;

    color_far_r = _logic_room_stateless_consts . get ( ) . mesh_color_far_r ;
    color_far_g = _logic_room_stateless_consts . get ( ) . mesh_color_far_g ;
    color_far_b = _logic_room_stateless_consts . get ( ) . mesh_color_far_b ;
    color_far_a = _logic_room_stateless_consts . get ( ) . mesh_color_far_a ;

    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , far_side_u_left , far_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , far_side_u_left , far_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , far_side_u_right , far_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , far_side_u_right , far_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _logic_room_mesh_create_state . current_index = current_index ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_left_side ( )
{
    num_fract x_left ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract left_side_u_left ;
    num_fract left_side_u_right ;
    num_fract left_side_v_top ;
    num_fract left_side_v_bottom ;
    num_fract z_near ;
    num_fract z_far ;
    num_fract color_left_r ;
    num_fract color_left_g ;
    num_fract color_left_b ;
    num_fract color_left_a ;
    num_whole current_index ;
    
    x_left = _logic_room_stateless_consts . get ( ) . mesh_x_left ;
    y_top = _logic_room_stateless_consts . get ( ) . mesh_y_top ; 
    y_bottom = _logic_room_stateless_consts . get ( ) . mesh_y_bottom ; 
    left_side_u_left = _logic_room_stateless_consts . get ( ) . mesh_left_side_u_left ;
    left_side_u_right = _logic_room_stateless_consts . get ( ) . mesh_left_side_u_right ;
    left_side_v_top = _logic_room_stateless_consts . get ( ) . mesh_left_side_v_top ;
    left_side_v_bottom = _logic_room_stateless_consts . get ( ) . mesh_left_side_v_bottom ;
    z_near = _logic_room_stateless_consts . get ( ) . mesh_z_near ;
    z_far = _logic_room_stateless_consts . get ( ) . mesh_z_far ;

    color_left_r = _logic_room_stateless_consts . get ( ) . mesh_color_left_r ;
    color_left_g = _logic_room_stateless_consts . get ( ) . mesh_color_left_g ;
    color_left_b = _logic_room_stateless_consts . get ( ) . mesh_color_left_b ;
    color_left_a = _logic_room_stateless_consts . get ( ) . mesh_color_left_a ;
    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , left_side_u_left , left_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , left_side_u_left , left_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , left_side_u_right , left_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , left_side_u_right , left_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _logic_room_mesh_create_state . current_index = current_index ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_top_side ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract top_side_u_left ;
    num_fract top_side_u_right ;
    num_fract top_side_v_top ;
    num_fract top_side_v_bottom ;
    num_fract z_near ;
    num_fract z_far ;
    num_fract color_top_r ;
    num_fract color_top_g ;
    num_fract color_top_b ;
    num_fract color_top_a ;
    num_whole current_index ;
    
    x_left = _logic_room_stateless_consts . get ( ) . mesh_x_left ;
    x_right = _logic_room_stateless_consts . get ( ) . mesh_x_right ;
    y_top = _logic_room_stateless_consts . get ( ) . mesh_y_top ; 
    y_bottom = _logic_room_stateless_consts . get ( ) . mesh_y_bottom ; 
    top_side_u_left = _logic_room_stateless_consts . get ( ) . mesh_top_side_u_left ;
    top_side_u_right = _logic_room_stateless_consts . get ( ) . mesh_top_side_u_right ;
    top_side_v_top = _logic_room_stateless_consts . get ( ) . mesh_top_side_v_top ;
    top_side_v_bottom = _logic_room_stateless_consts . get ( ) . mesh_top_side_v_bottom ;
    z_near = _logic_room_stateless_consts . get ( ) . mesh_z_near ;
    z_far = _logic_room_stateless_consts . get ( ) . mesh_z_far ;

    color_top_r = _logic_room_stateless_consts . get ( ) . mesh_color_top_r ;
    color_top_g = _logic_room_stateless_consts . get ( ) . mesh_color_top_g ;
    color_top_b = _logic_room_stateless_consts . get ( ) . mesh_color_top_b ;
    color_top_a = _logic_room_stateless_consts . get ( ) . mesh_color_top_a ;
    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , top_side_u_left , top_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , top_side_u_left , top_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , top_side_u_right , top_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , top_side_u_right , top_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _logic_room_mesh_create_state . current_index = current_index ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_bottom_side ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract bottom_side_u_left ;
    num_fract bottom_side_u_right ;
    num_fract bottom_side_v_top ;
    num_fract bottom_side_v_bottom ;
    num_fract z_near ;
    num_fract z_far ;
    num_fract color_bottom_r ;
    num_fract color_bottom_g ;
    num_fract color_bottom_b ;
    num_fract color_bottom_a ;
    num_whole current_index ;
    
    x_left = _logic_room_stateless_consts . get ( ) . mesh_x_left ;
    x_right = _logic_room_stateless_consts . get ( ) . mesh_x_right ;
    y_top = _logic_room_stateless_consts . get ( ) . mesh_y_top ; 
    y_bottom = _logic_room_stateless_consts . get ( ) . mesh_y_bottom ; 
    bottom_side_u_left = _logic_room_stateless_consts . get ( ) . mesh_bottom_side_u_left ;
    bottom_side_u_right = _logic_room_stateless_consts . get ( ) . mesh_bottom_side_u_right ;
    bottom_side_v_top = _logic_room_stateless_consts . get ( ) . mesh_bottom_side_v_top ;
    bottom_side_v_bottom = _logic_room_stateless_consts . get ( ) . mesh_bottom_side_v_bottom ;
    z_near = _logic_room_stateless_consts . get ( ) . mesh_z_near ;
    z_far = _logic_room_stateless_consts . get ( ) . mesh_z_far ;

    color_bottom_r = _logic_room_stateless_consts . get ( ) . mesh_color_bottom_r ;
    color_bottom_g = _logic_room_stateless_consts . get ( ) . mesh_color_bottom_g ;
    color_bottom_b = _logic_room_stateless_consts . get ( ) . mesh_color_bottom_b ;
    color_bottom_a = _logic_room_stateless_consts . get ( ) . mesh_color_bottom_a ;
    current_index = _logic_room_mesh_create_state . current_index ;

    //
    // connection from top side
    //

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    //
    // bottom side
    //

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_left , bottom_side_v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_left , bottom_side_v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _logic_room_mesh_create_state . current_index = current_index ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _finalize_mesh ( )
{
    _engine_render_mesh_create_state . finalized = _platform_math_consts . get ( ) . whole_true ;
    typename messages :: engine_render_mesh_finalize msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _transform_mesh ( )
{
    num_fract position_x ;
    num_fract position_y ;
    num_fract position_z ;
    matrix_data transform ;

    position_x = _logic_room_stateless_consts . get ( ) . mesh_position_x ;
    position_y = _logic_room_stateless_consts . get ( ) . mesh_position_y ;
    position_z = _logic_room_stateless_consts . get ( ) . mesh_position_z ;

    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_origin ( transform , position_x , position_y , position_z ) ;

    typename messages :: engine_render_mesh_set_transform msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    msg . transform = transform ;
    _mediator . get ( ) . send ( msg ) ;
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

