template < typename mediator >
class shy_logic_main_menu_selection_mesh
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
    
    class _logic_main_menu_selection_mesh_consts_type
    {
    public :
        _logic_main_menu_selection_mesh_consts_type ( ) ;
    public :
        num_fract color_r ;
        num_fract color_g ;
        num_fract color_b ;
        num_fract color_a ;
        num_fract mesh_size ;
        num_fract position_z ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_create ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_destroy_request ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_render_request ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
private :
    void _bake_mesh ( ) ;
    void _fill_mesh_content ( ) ;
    void _place_mesh ( ) ;
    void _finalize_mesh ( ) ;
    void _render_mesh ( ) ;
    void _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_mesh_consts_type _logic_main_menu_selection_mesh_consts ;
    
    num_whole _creation_requested ;
    engine_render_mesh_id _mesh ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_mesh < mediator > :: _logic_main_menu_selection_mesh_consts_type :: _logic_main_menu_selection_mesh_consts_type ( )
{
    platform_math :: make_num_fract ( color_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( color_a , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_size , 1 , 1 ) ;
    platform_math :: make_num_fract ( position_z , - 3 , 1 ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_create )
{
    _creation_requested = _platform_math_consts . get ( ) . whole_true ;
    typename messages :: engine_render_mesh_create_request msg ;
    msg . vertices = _platform_math_consts . get ( ) . whole_4 ;
    msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_4 ;
    msg . triangle_fan_indices = _platform_math_consts . get ( ) . whole_0 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _creation_requested ) )
    {
        _creation_requested = _platform_math_consts . get ( ) . whole_false ;
        _mesh = msg . mesh ;
        _bake_mesh ( ) ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_create_finished ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_destroy_request )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_destroy_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_render_request )
{
    _render_mesh ( ) ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _bake_mesh ( )
{
    _fill_mesh_content ( ) ;
    _finalize_mesh ( ) ;
    _place_mesh ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _fill_mesh_content ( )
{
    num_fract half_size ;
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_bottom ;
    num_fract y_top ;
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_bottom ;
    num_fract v_top ;
    num_fract z ;
    num_fract color_r ;
    num_fract color_g ;
    num_fract color_b ;
    num_fract color_a ;
    num_whole index_left_top ;
    num_whole index_left_bottom ;
    num_whole index_right_top ;
    num_whole index_right_bottom ;
    
    platform_math :: div_fracts ( half_size , _logic_main_menu_selection_mesh_consts . mesh_size , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: mul_fracts ( x_left , half_size , _platform_math_consts . get ( ) . fract_minus_1 ) ;
    platform_math :: mul_fracts ( y_bottom , half_size , _platform_math_consts . get ( ) . fract_minus_1 ) ;
    platform_math :: mul_fracts ( x_right , half_size , _platform_math_consts . get ( ) . fract_1 ) ;
    platform_math :: mul_fracts ( y_top , half_size , _platform_math_consts . get ( ) . fract_1 ) ;
    z = _platform_math_consts . get ( ) . fract_0 ;
    
    color_r = _logic_main_menu_selection_mesh_consts . color_r ;
    color_g = _logic_main_menu_selection_mesh_consts . color_g ;
    color_b = _logic_main_menu_selection_mesh_consts . color_b ;
    color_a = _logic_main_menu_selection_mesh_consts . color_a ;

    index_left_top = _platform_math_consts . get ( ) . whole_0 ;
    index_left_bottom = _platform_math_consts . get ( ) . whole_1 ;
    index_right_top = _platform_math_consts . get ( ) . whole_2 ;
    index_right_bottom = _platform_math_consts . get ( ) . whole_3 ;
    
    _mesh_set_triangle_strip_index_value ( index_left_top , index_left_top ) ;
    _mesh_set_vertex_color               ( index_left_top , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_position            ( index_left_top , x_left , y_top , z ) ;

    _mesh_set_triangle_strip_index_value ( index_left_bottom , index_left_bottom ) ;
    _mesh_set_vertex_color               ( index_left_bottom , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_position            ( index_left_bottom , x_left , y_bottom , z ) ;

    _mesh_set_triangle_strip_index_value ( index_right_top , index_right_top ) ;
    _mesh_set_vertex_color               ( index_right_top , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_position            ( index_right_top , x_right , y_top , z ) ;

    _mesh_set_triangle_strip_index_value ( index_right_bottom , index_right_bottom ) ;
    _mesh_set_vertex_color               ( index_right_bottom , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_position            ( index_right_bottom , x_right , y_bottom , z ) ;    
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _place_mesh ( )
{
    matrix_data transform ;
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    
    origin_x = _platform_math_consts . get ( ) . fract_0 ;
    origin_y = _platform_math_consts . get ( ) . fract_0 ;
    origin_z = _logic_main_menu_selection_mesh_consts . position_z ;
    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_origin ( transform , origin_x , origin_y , origin_z ) ;

    typename messages :: engine_render_mesh_set_transform msg ;
    msg . mesh = _mesh ;
    msg . transform = transform ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _finalize_mesh ( )
{
    typename messages :: engine_render_mesh_finalize msg ;
    msg . mesh = _mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _render_mesh ( )
{
    typename messages :: engine_render_mesh_render msg ;
    msg . mesh = _mesh ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z )
{
    typename messages :: engine_render_mesh_set_vertex_position msg ;
    msg . mesh = _mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
{
    typename messages :: engine_render_mesh_set_vertex_color msg ;
    msg . mesh = _mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index )
{
    typename messages :: engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = _mesh ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}
