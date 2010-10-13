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
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_room_mesh_consts_type
    {
    public :
        _logic_room_mesh_consts_type ( ) ;
    public :
        num_fract color_right_r ;
        num_fract color_right_g ;
        num_fract color_right_b ;
        num_fract color_right_a ;
        num_fract color_left_r ;
        num_fract color_left_g ;
        num_fract color_left_b ;
        num_fract color_left_a ;
        num_fract color_near_r ;
        num_fract color_near_g ;
        num_fract color_near_b ;
        num_fract color_near_a ;
        num_fract color_far_r ;
        num_fract color_far_g ;
        num_fract color_far_b ;
        num_fract color_far_a ;
        num_fract color_top_r ;
        num_fract color_top_g ;
        num_fract color_top_b ;
        num_fract color_top_a ;
        num_fract color_bottom_r ;
        num_fract color_bottom_g ;
        num_fract color_bottom_b ;
        num_fract color_bottom_a ;
        num_fract position_x ;
        num_fract position_y ;
        num_fract position_z ;
        num_fract rotation_period ;
        num_fract vertical_offset_period ;
        num_fract vertical_offset_amplitude ;
        num_fract x_left ;
        num_fract x_right ;
        num_fract y_top ;
        num_fract y_bottom ;
        num_fract z_near ;
        num_fract z_far ;
        num_fract u_left ;
        num_fract u_right ;
        num_fract v_top ;
        num_fract v_bottom ;
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
        engine_render_mesh_id mesh ;
    } ;

    class _logic_room_update_state_type
    {
    public :
        num_fract time ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
    void receive ( typename messages :: logic_room_mesh_create ) ;
    void receive ( typename messages :: logic_room_mesh_render_request ) ;
    void receive ( typename messages :: logic_room_update ) ;
private :
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
    void _finalize_mesh ( ) ;
    void _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    _logic_room_mesh_consts_type _logic_room_mesh_consts ;

    _logic_room_mesh_create_state_type _logic_room_mesh_create_state ;
    _logic_room_update_state_type _logic_room_update_state ;
    _engine_render_mesh_create_state_type _engine_render_mesh_create_state ;
} ;

template < typename mediator >
shy_logic_room_mesh < mediator > :: _logic_room_mesh_consts_type :: _logic_room_mesh_consts_type ( )
{
    platform_math :: make_num_fract ( color_left_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_left_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_left_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_left_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( color_right_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_right_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_right_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_right_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( color_near_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_near_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_near_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_near_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( color_far_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_far_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_far_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_far_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( color_top_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_top_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_top_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_top_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( color_bottom_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_bottom_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_bottom_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_bottom_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( position_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( position_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( position_z , - 10 , 1 ) ;
    platform_math :: make_num_fract ( rotation_period , 1 , 1 ) ;
    platform_math :: make_num_fract ( vertical_offset_period , 2 , 1 ) ;
    platform_math :: make_num_fract ( vertical_offset_amplitude , 3 , 1 ) ;

    platform_math :: make_num_fract ( x_left , - 1 , 1 ) ;
    platform_math :: make_num_fract ( x_right , 1 , 1 ) ;

    platform_math :: make_num_fract ( y_top , 1 , 1 ) ; 
    platform_math :: make_num_fract ( y_bottom , - 1 , 1 ) ;

    platform_math :: make_num_fract ( z_near , 1 , 1 ) ;
    platform_math :: make_num_fract ( z_far , - 1 , 1 ) ;

    platform_math :: make_num_fract ( u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( u_right , 1 , 1 ) ;

    platform_math :: make_num_fract ( v_top , 1 , 1 ) ;
    platform_math :: make_num_fract ( v_bottom , 0 , 1 ) ;

    platform_math :: make_num_whole ( vertices_count , 22 ) ;
    platform_math :: make_num_whole ( triangle_strip_indices_count , 22 ) ;
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

    _logic_room_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
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
    typename messages :: engine_render_mesh_render render_msg ;
    render_msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( render_msg ) ;

    _mediator . get ( ) . send ( typename messages :: logic_room_mesh_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: receive ( typename messages :: logic_room_update )
{
    num_fract time_step ;
    platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
    platform_math :: add_to_fract ( _logic_room_update_state . time , time_step ) ;
    _transform_mesh ( ) ;
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
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _add_near_side ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z_near ;
    num_fract color_near_r ;
    num_fract color_near_g ;
    num_fract color_near_b ;
    num_fract color_near_a ; 
    num_whole current_index ;
    
    x_left = _logic_room_mesh_consts . x_left ;
    x_right = _logic_room_mesh_consts . x_right ;
    y_top = _logic_room_mesh_consts . y_top ; 
    y_bottom = _logic_room_mesh_consts . y_bottom ; 
    u_left = _logic_room_mesh_consts . u_left ;
    u_right = _logic_room_mesh_consts . u_right ;
    v_top = _logic_room_mesh_consts . v_top ;
    v_bottom = _logic_room_mesh_consts . v_bottom ;
    z_near = _logic_room_mesh_consts . z_near ;

    color_near_r = _logic_room_mesh_consts . color_near_r ;
    color_near_g = _logic_room_mesh_consts . color_near_g ;
    color_near_b = _logic_room_mesh_consts . color_near_b ;
    color_near_a = _logic_room_mesh_consts . color_near_a ;

    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_bottom ) ;
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
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z_near ;
    num_fract z_far ;
    num_fract color_right_r ;
    num_fract color_right_g ;
    num_fract color_right_b ;
    num_fract color_right_a ;
    num_whole current_index ;
    
    x_right = _logic_room_mesh_consts . x_right ;
    y_top = _logic_room_mesh_consts . y_top ; 
    y_bottom = _logic_room_mesh_consts . y_bottom ; 
    u_left = _logic_room_mesh_consts . u_left ;
    u_right = _logic_room_mesh_consts . u_right ;
    v_top = _logic_room_mesh_consts . v_top ;
    v_bottom = _logic_room_mesh_consts . v_bottom ;
    z_near = _logic_room_mesh_consts . z_near ;
    z_far = _logic_room_mesh_consts . z_far ;

    color_right_r = _logic_room_mesh_consts . color_right_r ;
    color_right_g = _logic_room_mesh_consts . color_right_g ;
    color_right_b = _logic_room_mesh_consts . color_right_b ;
    color_right_a = _logic_room_mesh_consts . color_right_a ;

    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_bottom ) ;
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
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z_far ;
    num_fract color_far_r ;
    num_fract color_far_g ;
    num_fract color_far_b ;
    num_fract color_far_a ; 
    num_whole current_index ;
    
    x_left = _logic_room_mesh_consts . x_left ;
    x_right = _logic_room_mesh_consts . x_right ;
    y_top = _logic_room_mesh_consts . y_top ; 
    y_bottom = _logic_room_mesh_consts . y_bottom ; 
    u_left = _logic_room_mesh_consts . u_left ;
    u_right = _logic_room_mesh_consts . u_right ;
    v_top = _logic_room_mesh_consts . v_top ;
    v_bottom = _logic_room_mesh_consts . v_bottom ;
    z_far = _logic_room_mesh_consts . z_far ;

    color_far_r = _logic_room_mesh_consts . color_far_r ;
    color_far_g = _logic_room_mesh_consts . color_far_g ;
    color_far_b = _logic_room_mesh_consts . color_far_b ;
    color_far_a = _logic_room_mesh_consts . color_far_a ;

    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_bottom ) ;
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
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z_near ;
    num_fract z_far ;
    num_fract color_left_r ;
    num_fract color_left_g ;
    num_fract color_left_b ;
    num_fract color_left_a ;
    num_whole current_index ;
    
    x_left = _logic_room_mesh_consts . x_left ;
    y_top = _logic_room_mesh_consts . y_top ; 
    y_bottom = _logic_room_mesh_consts . y_bottom ; 
    u_left = _logic_room_mesh_consts . u_left ;
    u_right = _logic_room_mesh_consts . u_right ;
    v_top = _logic_room_mesh_consts . v_top ;
    v_bottom = _logic_room_mesh_consts . v_bottom ;
    z_near = _logic_room_mesh_consts . z_near ;
    z_far = _logic_room_mesh_consts . z_far ;

    color_left_r = _logic_room_mesh_consts . color_left_r ;
    color_left_g = _logic_room_mesh_consts . color_left_g ;
    color_left_b = _logic_room_mesh_consts . color_left_b ;
    color_left_a = _logic_room_mesh_consts . color_left_a ;
    current_index = _logic_room_mesh_create_state . current_index ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_bottom ) ;
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
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z_near ;
    num_fract z_far ;
    num_fract color_top_r ;
    num_fract color_top_g ;
    num_fract color_top_b ;
    num_fract color_top_a ;
    num_whole current_index ;
    
    x_left = _logic_room_mesh_consts . x_left ;
    x_right = _logic_room_mesh_consts . x_right ;
    y_top = _logic_room_mesh_consts . y_top ; 
    y_bottom = _logic_room_mesh_consts . y_bottom ; 
    u_left = _logic_room_mesh_consts . u_left ;
    u_right = _logic_room_mesh_consts . u_right ;
    v_top = _logic_room_mesh_consts . v_top ;
    v_bottom = _logic_room_mesh_consts . v_bottom ;
    z_near = _logic_room_mesh_consts . z_near ;
    z_far = _logic_room_mesh_consts . z_far ;

    color_top_r = _logic_room_mesh_consts . color_top_r ;
    color_top_g = _logic_room_mesh_consts . color_top_g ;
    color_top_b = _logic_room_mesh_consts . color_top_b ;
    color_top_a = _logic_room_mesh_consts . color_top_a ;
    current_index = _logic_room_mesh_create_state . current_index ;

    //
    // connection
    //

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    //
    // side
    //

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;
    
    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    _mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    _mesh_set_vertex_tex_coord           ( current_index , u_right , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    platform_math :: inc_whole           ( current_index ) ;

    _logic_room_mesh_create_state . current_index = current_index ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _finalize_mesh ( )
{
    typename messages :: engine_render_mesh_finalize msg ;
    msg . mesh = _engine_render_mesh_create_state . mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_mesh < mediator > :: _transform_mesh ( )
{
    num_fract rotation_phase ;
    num_fract rotation_period ;
    num_fract axis_x_x ;
    num_fract axis_x_y ;
    num_fract axis_x_z ;
    num_fract axis_z_x ;
    num_fract axis_z_y ;
    num_fract axis_z_z ;
    num_fract position_x ;
    num_fract position_y ;
    num_fract position_z ;
    num_fract vertical_offset ;
    num_fract vertical_offset_period ;
    num_fract vertical_offset_phase ;
    num_fract vertical_offset_amplitude ;
    num_fract time ;
    matrix_data transform ;

    axis_x_y = _platform_math_consts . get ( ) . fract_0 ;
    axis_z_y = _platform_math_consts . get ( ) . fract_0 ; 

    position_x = _logic_room_mesh_consts . position_x ;
    position_y = _logic_room_mesh_consts . position_y ;
    position_z = _logic_room_mesh_consts . position_z ;

    time = _logic_room_update_state . time ;
    rotation_period = _logic_room_mesh_consts . rotation_period ;
    vertical_offset_period = _logic_room_mesh_consts . vertical_offset_period ;
    vertical_offset_amplitude = _logic_room_mesh_consts . vertical_offset_amplitude ;

    platform_math :: mul_fracts ( vertical_offset_phase , time , _platform_math_consts . get ( ) . fract_2pi ) ;
    platform_math :: div_fract_by ( vertical_offset_phase , vertical_offset_period ) ;
    platform_math :: sin ( vertical_offset , vertical_offset_phase ) ;
    platform_math :: mul_fract_by ( vertical_offset , vertical_offset_amplitude ) ;

    platform_math :: add_to_fract ( position_y , vertical_offset ) ;

    platform_math :: mul_fracts ( rotation_phase , time , _platform_math_consts . get ( ) . fract_2pi ) ;
    platform_math :: div_fract_by ( rotation_phase , rotation_period ) ;
    platform_math :: cos ( axis_x_x , rotation_phase ) ;
    platform_math :: sin ( axis_x_z , rotation_phase ) ;
    platform_math :: mul_fracts ( axis_z_x , axis_x_z , _platform_math_consts . get ( ) . fract_minus_1 ) ;
    platform_math :: mul_fracts ( axis_z_z , axis_x_x , _platform_math_consts . get ( ) . fract_1 ) ;

    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , axis_x_x , axis_x_y , axis_x_z ) ;
    platform_matrix :: set_axis_z ( transform , axis_z_x , axis_z_y , axis_z_z ) ;
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

