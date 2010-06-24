template < typename mediator >
class shy_logic_fidget
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;

    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _fidget_r = 255 ;
    static const_int_32 _fidget_g = 128 ;
    static const_int_32 _fidget_b = 0 ;    
    static const_int_32 _fidget_edges = 3 ;
    static const num_fract _fidget_size ( ) { num_fract n ; platform_math :: make_num_fract ( n , 3 , 10 ) ; return n ; }
public :
    shy_logic_fidget ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: fidget_done msg ) ;
    void receive ( typename messages :: fidget_prepare_permit msg ) ;
    void receive ( typename messages :: fidget_render msg ) ;
    void receive ( typename messages :: fidget_update msg ) ;
    void receive ( typename messages :: mesh_create_reply msg ) ;
private :
    void _update_fidget ( ) ;
    void _render_fidget_mesh ( ) ;
    void _create_fidget_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_fract _fidget_angle ;
    num_whole _fidget_prepare_permitted ;
    num_whole _fidget_mesh_created ;
    num_whole _fidget_scale ;
    num_whole _mesh_create_requested ;
    mesh_id _fidget_mesh_id ;
} ;

template < typename mediator >
shy_logic_fidget < mediator > :: shy_logic_fidget ( )
{
    platform_math :: make_num_fract ( _fidget_angle , 0 , 1 ) ;
    platform_math :: make_num_whole ( _fidget_prepare_permitted , false ) ;
    platform_math :: make_num_whole ( _fidget_mesh_created , false ) ;
    platform_math :: make_num_whole ( _fidget_scale , 0 ) ;
    _mesh_create_requested = platform :: math_consts . whole_false ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_done msg )
{
    if ( platform_conditions :: whole_is_true ( _fidget_mesh_created ) )
    {
        typename messages :: mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = _fidget_mesh_id ;
        _mediator . get ( ) . send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_render msg )
{
    if ( platform_conditions :: whole_is_true ( _fidget_mesh_created ) )
        _render_fidget_mesh ( ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_prepare_permit msg )
{
    platform_math :: make_num_whole ( _fidget_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_requested ) )
    {
        _mesh_create_requested = platform :: math_consts . whole_false ;
        _fidget_mesh_id = msg . mesh ;
        _create_fidget_mesh ( ) ;
        platform_math :: make_num_whole ( _fidget_mesh_created , true ) ;
        _mediator . get ( ) . send ( typename messages :: fidget_prepared ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_update msg )
{
    if ( platform_conditions :: whole_is_true ( _fidget_prepare_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _fidget_mesh_created ) )
        {
            _mesh_create_requested = platform :: math_consts . whole_true ;
            
            num_whole whole_fidget_edges ;
            platform_math :: make_num_whole ( whole_fidget_edges , _fidget_edges ) ;
            
            typename messages :: mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = whole_fidget_edges ;
            mesh_create_msg . triangle_fan_indices = whole_fidget_edges ;
            mesh_create_msg . triangle_strip_indices = platform :: math_consts . whole_0 ;
            _mediator . get ( ) . send ( mesh_create_msg ) ;
        }
        else
            _update_fidget ( ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _update_fidget ( )
{
    num_fract angle_delta ;
    platform_math :: make_num_fract ( angle_delta , 125 , 1000 ) ;
    platform_math :: add_to_fract ( _fidget_angle , angle_delta ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _render_fidget_mesh ( )
{    
    typename messages :: mesh_set_transform mesh_set_transform_msg ;
    typename messages :: mesh_render mesh_render_msg ;
    matrix_data matrix ;
    num_whole whole_scale_in_frames ;
    num_fract fract_scale_in_frames ;
    num_fract fract_fidget_scale ;
    num_fract scale ;
    num_fract height ;
    num_fract angle_cos ;
    num_fract angle_sin ;
    num_fract cos_by_scale ;
    num_fract sin_by_scale ;
    num_fract neg_sin_by_scale ;
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    num_fract num_half ;
    
    platform_math :: make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform_math :: make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform_math :: make_fract_from_whole ( fract_fidget_scale , _fidget_scale ) ;
    platform_math :: div_fracts ( scale , fract_fidget_scale , fract_scale_in_frames ) ;
    platform_render :: get_aspect_height ( height ) ;
    platform_math :: make_num_fract ( num_half , 1 , 2 ) ;
    platform_math :: cos ( angle_cos , _fidget_angle ) ;
    platform_math :: sin ( angle_sin , _fidget_angle ) ;
    platform_math :: mul_fracts ( cos_by_scale , angle_cos , scale ) ;
    platform_math :: mul_fracts ( sin_by_scale , angle_sin , scale ) ;
    platform_math :: neg_fract ( neg_sin_by_scale , sin_by_scale ) ;
    platform_math :: make_num_fract ( origin_x , 0 , 1 ) ;
    platform_math :: sub_fracts ( origin_y , height , num_half ) ;
    platform_math :: make_num_fract ( origin_z , - 3 , 1 ) ;
    platform_matrix :: set_axis_x ( matrix , cos_by_scale , sin_by_scale , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_y ( matrix , neg_sin_by_scale , cos_by_scale , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_z ( matrix , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_1 ) ;
    platform_matrix :: set_origin ( matrix , origin_x , origin_y , origin_z ) ;
    
    mesh_set_transform_msg . mesh = _fidget_mesh_id ;
    mesh_set_transform_msg . transform = matrix ;
    mesh_render_msg . mesh = _fidget_mesh_id ;
    
    _mediator . get ( ) . send ( typename messages :: texture_unselect ( ) ) ;
    _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
    _mediator . get ( ) . send ( mesh_render_msg ) ;

    if ( platform_conditions :: whole_less_than_whole ( _fidget_scale , whole_scale_in_frames ) )
        platform_math :: inc_whole ( _fidget_scale ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _create_fidget_mesh ( )
{    
    num_whole i ;
    num_whole whole_fidget_edges ;
    num_fract fract_fidget_edges ;
    
    platform_math :: make_num_fract ( fract_fidget_edges , _fidget_edges , 1 ) ;
    platform_math :: make_num_whole ( whole_fidget_edges , _fidget_edges ) ;
    
    for ( platform_math :: make_num_whole ( i , 0 )
        ; platform_conditions :: whole_less_than_whole ( i , whole_fidget_edges )
        ; platform_math :: inc_whole ( i )
        )
    {
        num_fract fract_i ;
        num_fract angle ;
        num_fract angle_cos ;
        num_fract angle_sin ;
        num_fract vertex_x ;
        num_fract vertex_y ;
        num_fract vertex_z ;
        num_fract vertex_r ;
        num_fract vertex_g ;
        num_fract vertex_b ;
        num_fract vertex_a ;
        platform_math :: make_fract_from_whole ( fract_i , i ) ;
        platform_math :: mul_fracts ( angle , platform :: math_consts . fract_2pi , fract_i ) ;
        platform_math :: div_fract_by ( angle , fract_fidget_edges ) ;
        platform_math :: cos ( angle_cos , angle ) ;
        platform_math :: sin ( angle_sin , angle ) ;
        platform_math :: mul_fracts ( vertex_x , _fidget_size ( ) , angle_cos ) ;
        platform_math :: mul_fracts ( vertex_y , _fidget_size ( ) , angle_sin ) ;
        platform_math :: make_num_fract ( vertex_z , 0 , 1 ) ;
        platform_math :: make_num_fract ( vertex_r , _fidget_r , 255 ) ;
        platform_math :: make_num_fract ( vertex_g , _fidget_g , 255 ) ;
        platform_math :: make_num_fract ( vertex_b , _fidget_b , 255 ) ;
        platform_math :: make_num_fract ( vertex_a , 1 , 1 ) ;

        typename messages :: mesh_set_vertex_position set_pos_msg ;
        set_pos_msg . mesh = _fidget_mesh_id ;
        set_pos_msg . offset = i ;
        set_pos_msg . x = vertex_x ;
        set_pos_msg . y = vertex_y ;
        set_pos_msg . z = vertex_z ;
        _mediator . get ( ) . send ( set_pos_msg ) ;

        typename messages :: mesh_set_vertex_color set_col_msg ;
        set_col_msg . mesh = _fidget_mesh_id ;
        set_col_msg . offset = i ;
        set_col_msg . r = vertex_r ;
        set_col_msg . g = vertex_g ;
        set_col_msg . b = vertex_b ;
        set_col_msg . a = vertex_a ;
        _mediator . get ( ) . send ( set_col_msg ) ;
        
        typename messages :: mesh_set_triangle_fan_index_value set_index_msg ;
        set_index_msg . mesh = _fidget_mesh_id ;
        set_index_msg . offset = i ;
        set_index_msg . index = i ;
        _mediator . get ( ) . send ( set_index_msg ) ;
    }
    typename messages :: mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _fidget_mesh_id ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
}
