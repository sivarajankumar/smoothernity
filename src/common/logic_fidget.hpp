template < typename mediator >
class shy_logic_fidget
{
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    class _logic_fidget_consts_type
    {
    public :
        _logic_fidget_consts_type ( ) ;
        num_fract fidget_size ;
        num_fract fidget_r ;
        num_fract fidget_g ;
        num_fract fidget_b ;
        num_fract mesh_x ;
        num_fract mesh_y_from_top ;
        num_fract mesh_z ;
        num_fract angle_delta ;
        num_whole fidget_edges ;
        num_whole scale_in_frames ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: fidget_done msg ) ;
    void receive ( typename messages :: fidget_prepare_permit msg ) ;
    void receive ( typename messages :: fidget_render_request msg ) ;
    void receive ( typename messages :: fidget_update msg ) ;
    void receive ( typename messages :: render_mesh_create_reply msg ) ;
    void receive ( typename messages :: render_aspect_reply msg ) ;
    void receive ( typename messages :: render_frame_loss_reply msg ) ;
private :
    void _update_fidget ( ) ;
    void _render_fidget_mesh ( ) ;
    void _create_fidget_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_fidget_consts_type _logic_fidget_consts ;
    num_fract _fidget_angle ;
    num_whole _fidget_prepare_permitted ;
    num_whole _fidget_mesh_created ;
    num_whole _fidget_scale ;
    num_whole _mesh_create_requested ;
    num_whole _render_aspect_requested ;
    num_whole _render_aspect_replied ;
    num_fract _render_aspect_height ;
    num_whole _render_frame_loss_requested ;
    num_whole _render_frame_loss_replied ;
    num_whole _render_frame_loss ;
    mesh_id _fidget_mesh_id ;
} ;

template < typename mediator >
shy_logic_fidget < mediator > :: _logic_fidget_consts_type :: _logic_fidget_consts_type ( )
{
    platform_math :: make_num_fract ( fidget_size , 3 , 10 ) ;
    platform_math :: make_num_fract ( fidget_r , 255 , 255 ) ;
    platform_math :: make_num_fract ( fidget_g , 128 , 255 ) ;
    platform_math :: make_num_fract ( fidget_b , 0 , 255 ) ;
    platform_math :: make_num_fract ( angle_delta , 125 , 1000 ) ;
    platform_math :: make_num_fract ( mesh_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_y_from_top , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_z , - 3 , 1 ) ;
    platform_math :: make_num_whole ( fidget_edges , 3 ) ;
    platform_math :: make_num_whole ( scale_in_frames , 60 ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: init msg )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _fidget_angle = _platform_math_consts . get ( ) . fract_0 ;
    _fidget_prepare_permitted = _platform_math_consts . get ( ) . whole_false ;
    _fidget_mesh_created = _platform_math_consts . get ( ) . whole_false ;
    _fidget_scale = _platform_math_consts . get ( ) . whole_0 ;
    _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_false ;
    _render_aspect_replied = _platform_math_consts . get ( ) . whole_false ;
    _render_frame_loss_requested = _platform_math_consts . get ( ) . whole_false ;
    _render_frame_loss_replied = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_done msg )
{
    if ( platform_conditions :: whole_is_true ( _fidget_mesh_created ) )
    {
        typename messages :: render_mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = _fidget_mesh_id ;
        _mediator . get ( ) . send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_render_request msg )
{
    if ( platform_conditions :: whole_is_true ( _fidget_mesh_created ) )
        _render_fidget_mesh ( ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_prepare_permit msg )
{
    _fidget_prepare_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_requested ) )
    {
        _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
        _fidget_mesh_id = msg . mesh ;
        _create_fidget_mesh ( ) ;
        _fidget_mesh_created = _platform_math_consts . get ( ) . whole_true ;
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
            _mesh_create_requested = _platform_math_consts . get ( ) . whole_true ;
            
            typename messages :: render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = _logic_fidget_consts . fidget_edges ;
            mesh_create_msg . triangle_fan_indices = _logic_fidget_consts . fidget_edges ;
            mesh_create_msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_0 ;
            _mediator . get ( ) . send ( mesh_create_msg ) ;
        }
        else
        {
            _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
            _render_frame_loss_requested = _platform_math_consts . get ( ) . whole_true ;
            _mediator . get ( ) . send ( typename messages :: render_aspect_request ( ) ) ;
            _mediator . get ( ) . send ( typename messages :: render_frame_loss_request ( ) ) ;
        }
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: render_aspect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _render_aspect_requested ) )
    {
        _render_aspect_requested = _platform_math_consts . get ( ) . whole_false ;
        _render_aspect_replied = _platform_math_consts . get ( ) . whole_true ;
        _render_aspect_height = msg . height ;
        _update_fidget ( ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: render_frame_loss_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _render_frame_loss_requested ) )
    {
        _render_frame_loss_requested = _platform_math_consts . get ( ) . whole_false ;
        _render_frame_loss_replied = _platform_math_consts . get ( ) . whole_true ;
        _render_frame_loss = msg . frame_loss ;
        _update_fidget ( ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _update_fidget ( )
{
    if ( platform_conditions :: whole_is_true ( _render_aspect_replied )
      && platform_conditions :: whole_is_true ( _render_frame_loss_replied )
       )
    {
        _render_aspect_replied = _platform_math_consts . get ( ) . whole_false ;
        _render_frame_loss_replied = _platform_math_consts . get ( ) . whole_false ;
    
        matrix_data matrix ;
        num_fract fract_scale_in_frames ;
        num_fract fract_fidget_scale ;
        num_fract scale ;
        num_fract angle_cos ;
        num_fract angle_sin ;
        num_fract cos_by_scale ;
        num_fract sin_by_scale ;
        num_fract neg_sin_by_scale ;
        num_fract mesh_y ;
        
        platform_math :: add_to_fract ( _fidget_angle , _logic_fidget_consts . angle_delta ) ;
        platform_math :: make_fract_from_whole ( fract_scale_in_frames , _logic_fidget_consts . scale_in_frames ) ;
        platform_math :: make_fract_from_whole ( fract_fidget_scale , _fidget_scale ) ;
        platform_math :: div_fracts ( scale , fract_fidget_scale , fract_scale_in_frames ) ;
        platform_math :: cos ( angle_cos , _fidget_angle ) ;
        platform_math :: sin ( angle_sin , _fidget_angle ) ;
        platform_math :: mul_fracts ( cos_by_scale , angle_cos , scale ) ;
        platform_math :: mul_fracts ( sin_by_scale , angle_sin , scale ) ;
        platform_math :: neg_fract ( neg_sin_by_scale , sin_by_scale ) ;
        platform_math :: sub_fracts ( mesh_y , _render_aspect_height , _logic_fidget_consts . mesh_y_from_top ) ;
        platform_matrix :: set_axis_x ( matrix , cos_by_scale , sin_by_scale , _platform_math_consts . get ( ) . fract_0 ) ;
        platform_matrix :: set_axis_y ( matrix , neg_sin_by_scale , cos_by_scale , _platform_math_consts . get ( ) . fract_0 ) ;
        platform_matrix :: set_axis_z ( matrix , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_1 ) ;
        platform_matrix :: set_origin ( matrix , _logic_fidget_consts . mesh_x , mesh_y , _logic_fidget_consts . mesh_z ) ;
        
        typename messages :: render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = _fidget_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        _mediator . get ( ) . send ( mesh_set_transform_msg ) ;

        if ( platform_conditions :: whole_less_than_whole ( _fidget_scale , _logic_fidget_consts . scale_in_frames ) )
            platform_math :: inc_whole ( _fidget_scale ) ;

        if ( platform_conditions :: whole_is_true ( _render_frame_loss ) )
            _fidget_scale = _platform_math_consts . get ( ) . whole_0 ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _render_fidget_mesh ( )
{        
    _mediator . get ( ) . send ( typename messages :: render_texture_unselect ( ) ) ;
    
    typename messages :: render_mesh_render mesh_render_msg ;
    mesh_render_msg . mesh = _fidget_mesh_id ;
    _mediator . get ( ) . send ( mesh_render_msg ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _create_fidget_mesh ( )
{    
    num_fract fract_fidget_edges ;
    
    platform_math :: make_fract_from_whole ( fract_fidget_edges , _logic_fidget_consts . fidget_edges ) ;
    
    for ( num_whole i = _platform_math_consts . get ( ) . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , _logic_fidget_consts . fidget_edges )
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
        platform_math :: mul_fracts ( angle , _platform_math_consts . get ( ) . fract_2pi , fract_i ) ;
        platform_math :: div_fract_by ( angle , fract_fidget_edges ) ;
        platform_math :: cos ( angle_cos , angle ) ;
        platform_math :: sin ( angle_sin , angle ) ;
        platform_math :: mul_fracts ( vertex_x , _logic_fidget_consts . fidget_size , angle_cos ) ;
        platform_math :: mul_fracts ( vertex_y , _logic_fidget_consts . fidget_size , angle_sin ) ;
        vertex_z = _platform_math_consts . get ( ) . fract_0 ;
        vertex_r = _logic_fidget_consts . fidget_r ;
        vertex_g = _logic_fidget_consts . fidget_g ;
        vertex_b = _logic_fidget_consts . fidget_b ;
        vertex_a = _platform_math_consts . get ( ) . fract_1 ;

        typename messages :: render_mesh_set_vertex_position set_pos_msg ;
        set_pos_msg . mesh = _fidget_mesh_id ;
        set_pos_msg . offset = i ;
        set_pos_msg . x = vertex_x ;
        set_pos_msg . y = vertex_y ;
        set_pos_msg . z = vertex_z ;
        _mediator . get ( ) . send ( set_pos_msg ) ;

        typename messages :: render_mesh_set_vertex_color set_col_msg ;
        set_col_msg . mesh = _fidget_mesh_id ;
        set_col_msg . offset = i ;
        set_col_msg . r = vertex_r ;
        set_col_msg . g = vertex_g ;
        set_col_msg . b = vertex_b ;
        set_col_msg . a = vertex_a ;
        _mediator . get ( ) . send ( set_col_msg ) ;
        
        typename messages :: render_mesh_set_triangle_fan_index_value set_index_msg ;
        set_index_msg . mesh = _fidget_mesh_id ;
        set_index_msg . offset = i ;
        set_index_msg . index = i ;
        _mediator . get ( ) . send ( set_index_msg ) ;
    }
    typename messages :: render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _fidget_mesh_id ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
}
