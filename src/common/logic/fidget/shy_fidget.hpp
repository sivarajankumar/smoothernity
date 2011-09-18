namespace shy_guts
{
    static void update_fidget ( ) ;
    static void render_fidget_mesh ( ) ;
    static void create_fidget_mesh ( ) ;

    static so_called_platform_math_num_fract_type fidget_angle ;
    static so_called_platform_math_num_whole_type fidget_prepare_permitted ;
    static so_called_platform_math_num_whole_type fidget_mesh_created ;
    static so_called_platform_math_num_whole_type fidget_scale ;
    static so_called_platform_math_num_whole_type mesh_create_requested ;
    static so_called_platform_math_num_whole_type render_aspect_requested ;
    static so_called_platform_math_num_whole_type render_aspect_replied ;
    static so_called_platform_math_num_fract_type render_aspect_height ;
    static so_called_platform_math_num_whole_type render_frame_loss_requested ;
    static so_called_platform_math_num_whole_type render_frame_loss_replied ;
    static so_called_platform_math_num_whole_type render_frame_loss ;
    static so_called_common_engine_render_mesh_id_type fidget_mesh_id ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_fidget > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: update_fidget ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_aspect_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: render_frame_loss_replied )
       )
    {
        shy_guts :: render_aspect_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_frame_loss_replied = so_called_platform_math_consts :: whole_false ;
    
        so_called_platform_matrix_data_type matrix ;
        so_called_platform_math_num_fract_type fract_scale_in_frames ;
        so_called_platform_math_num_fract_type fract_fidget_scale ;
        so_called_platform_math_num_fract_type scale ;
        so_called_platform_math_num_fract_type angle_cos ;
        so_called_platform_math_num_fract_type angle_sin ;
        so_called_platform_math_num_fract_type cos_by_scale ;
        so_called_platform_math_num_fract_type sin_by_scale ;
        so_called_platform_math_num_fract_type neg_sin_by_scale ;
        so_called_platform_math_num_fract_type mesh_y ;
        
        so_called_platform_math :: add_to_fract ( shy_guts :: fidget_angle , so_called_common_logic_fidget_consts :: angle_delta ) ;
        so_called_platform_math :: make_fract_from_whole ( fract_scale_in_frames , so_called_common_logic_fidget_consts :: scale_in_frames ) ;
        so_called_platform_math :: make_fract_from_whole ( fract_fidget_scale , shy_guts :: fidget_scale ) ;
        so_called_platform_math :: div_fracts ( scale , fract_fidget_scale , fract_scale_in_frames ) ;
        so_called_platform_math :: cos ( angle_cos , shy_guts :: fidget_angle ) ;
        so_called_platform_math :: sin ( angle_sin , shy_guts :: fidget_angle ) ;
        so_called_platform_math :: mul_fracts ( cos_by_scale , angle_cos , scale ) ;
        so_called_platform_math :: mul_fracts ( sin_by_scale , angle_sin , scale ) ;
        so_called_platform_math :: neg_fract ( neg_sin_by_scale , sin_by_scale ) ;
        so_called_platform_math :: sub_fracts ( mesh_y , shy_guts :: render_aspect_height , so_called_common_logic_fidget_consts :: mesh_y_from_top ) ;
        so_called_platform_matrix :: set_axis_x ( matrix , cos_by_scale , sin_by_scale , so_called_platform_math_consts :: fract_0 ) ;
        so_called_platform_matrix :: set_axis_y ( matrix , neg_sin_by_scale , cos_by_scale , so_called_platform_math_consts :: fract_0 ) ;
        so_called_platform_matrix :: set_axis_z ( matrix , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_1 ) ;
        so_called_platform_matrix :: set_origin ( matrix , so_called_common_logic_fidget_consts :: mesh_x , mesh_y , so_called_common_logic_fidget_consts :: mesh_z ) ;
        
        so_called_common_engine_render_mesh_set_transform_message mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = shy_guts :: fidget_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_common_engine_render_mesh_set_transform_sender :: send ( mesh_set_transform_msg ) ;

        if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: fidget_scale , so_called_common_logic_fidget_consts :: scale_in_frames ) )
            so_called_platform_math :: inc_whole ( shy_guts :: fidget_scale ) ;

        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_frame_loss ) )
            shy_guts :: fidget_scale = so_called_platform_math_consts :: whole_0 ;
    }
}

void shy_guts :: render_fidget_mesh ( )
{
    so_called_common_engine_render_texture_unselect_sender :: send ( so_called_common_engine_render_texture_unselect_message ( ) ) ;
    
    so_called_common_engine_render_mesh_render_message mesh_render_msg ;
    mesh_render_msg . mesh = shy_guts :: fidget_mesh_id ;
    so_called_common_engine_render_mesh_render_sender :: send ( mesh_render_msg ) ;
}

void shy_guts :: create_fidget_mesh ( )
{
    so_called_platform_math_num_fract_type fract_fidget_edges ;
    
    so_called_platform_math :: make_fract_from_whole ( fract_fidget_edges , so_called_common_logic_fidget_consts :: fidget_edges ) ;
    
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , so_called_common_logic_fidget_consts :: fidget_edges )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_math_num_fract_type fract_i ;
        so_called_platform_math_num_fract_type angle ;
        so_called_platform_math_num_fract_type angle_cos ;
        so_called_platform_math_num_fract_type angle_sin ;
        so_called_platform_math_num_fract_type vertex_x ;
        so_called_platform_math_num_fract_type vertex_y ;
        so_called_platform_math_num_fract_type vertex_z ;
        so_called_platform_math_num_fract_type vertex_r ;
        so_called_platform_math_num_fract_type vertex_g ;
        so_called_platform_math_num_fract_type vertex_b ;
        so_called_platform_math_num_fract_type vertex_a ;

        so_called_platform_math :: make_fract_from_whole ( fract_i , i ) ;
        so_called_platform_math :: mul_fracts ( angle , so_called_platform_math_consts :: fract_2pi , fract_i ) ;
        so_called_platform_math :: div_fract_by ( angle , fract_fidget_edges ) ;
        so_called_platform_math :: cos ( angle_cos , angle ) ;
        so_called_platform_math :: sin ( angle_sin , angle ) ;
        so_called_platform_math :: mul_fracts ( vertex_x , so_called_common_logic_fidget_consts :: fidget_size , angle_cos ) ;
        so_called_platform_math :: mul_fracts ( vertex_y , so_called_common_logic_fidget_consts :: fidget_size , angle_sin ) ;
        vertex_z = so_called_platform_math_consts :: fract_0 ;
        vertex_r = so_called_common_logic_fidget_consts :: fidget_r ;
        vertex_g = so_called_common_logic_fidget_consts :: fidget_g ;
        vertex_b = so_called_common_logic_fidget_consts :: fidget_b ;
        vertex_a = so_called_platform_math_consts :: fract_1 ;

        so_called_common_engine_render_mesh_set_vertex_position_message set_pos_msg ;
        set_pos_msg . mesh = shy_guts :: fidget_mesh_id ;
        set_pos_msg . offset = i ;
        set_pos_msg . x = vertex_x ;
        set_pos_msg . y = vertex_y ;
        set_pos_msg . z = vertex_z ;
        so_called_common_engine_render_mesh_set_vertex_position_sender :: send ( set_pos_msg ) ;

        so_called_common_engine_render_mesh_set_vertex_color_message set_col_msg ;
        set_col_msg . mesh = shy_guts :: fidget_mesh_id ;
        set_col_msg . offset = i ;
        set_col_msg . r = vertex_r ;
        set_col_msg . g = vertex_g ;
        set_col_msg . b = vertex_b ;
        set_col_msg . a = vertex_a ;
        so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( set_col_msg ) ;
        
        so_called_common_engine_render_mesh_set_triangle_fan_index_value_message set_index_msg ;
        set_index_msg . mesh = shy_guts :: fidget_mesh_id ;
        set_index_msg . offset = i ;
        set_index_msg . index = i ;
        so_called_common_engine_render_mesh_set_triangle_fan_index_value_sender :: send ( set_index_msg ) ;
    }
    so_called_common_engine_render_mesh_finalize_message mesh_finalize_msg ;
    mesh_finalize_msg . mesh = shy_guts :: fidget_mesh_id ;
    so_called_common_engine_render_mesh_finalize_sender :: send ( mesh_finalize_msg ) ;
}

void _shy_common_logic_fidget :: receive ( so_called_common_engine_render_aspect_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_aspect_requested ) )
    {
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_aspect_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: render_aspect_height = msg . height ;
        shy_guts :: update_fidget ( ) ;
    }
}

void _shy_common_logic_fidget :: receive ( so_called_common_engine_render_frame_loss_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_frame_loss_requested ) )
    {
        shy_guts :: render_frame_loss_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_frame_loss_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: render_frame_loss = msg . frame_loss ;
        shy_guts :: update_fidget ( ) ;
    }
}

void _shy_common_logic_fidget :: receive ( so_called_common_engine_render_mesh_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fidget_mesh_id = msg . mesh ;
        shy_guts :: create_fidget_mesh ( ) ;
        shy_guts :: fidget_mesh_created = so_called_platform_math_consts :: whole_true ;
        so_called_common_logic_fidget_prepared_sender :: send ( so_called_common_logic_fidget_prepared_message ( ) ) ;
    }
}

void _shy_common_logic_fidget :: receive ( so_called_common_init_message )
{
    shy_guts :: fidget_angle = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: fidget_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_scale = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_aspect_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_frame_loss_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_frame_loss_replied = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_fidget :: receive ( so_called_common_logic_fidget_prepare_permit_message )
{
    shy_guts :: fidget_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_fidget :: receive ( so_called_common_logic_fidget_render_request_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( so_called_common_logic_fidget_consts :: should_render_fidget ) )
    {
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_mesh_created ) )
            shy_guts :: render_fidget_mesh ( ) ;
    }
    so_called_common_logic_fidget_render_reply_sender :: send ( so_called_common_logic_fidget_render_reply_message ( ) ) ;
}

void _shy_common_logic_fidget :: receive ( so_called_common_logic_fidget_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: fidget_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
            
            so_called_common_engine_render_mesh_create_request_message mesh_create_msg ;
            mesh_create_msg . vertices = so_called_common_logic_fidget_consts :: fidget_edges ;
            mesh_create_msg . triangle_fan_indices = so_called_common_logic_fidget_consts :: fidget_edges ;
            mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_common_engine_render_mesh_create_request_sender :: send ( mesh_create_msg ) ;
        }
        else
        {
            shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
            shy_guts :: render_frame_loss_requested = so_called_platform_math_consts :: whole_true ;
            so_called_common_engine_render_aspect_request_sender :: send ( so_called_common_engine_render_aspect_request_message ( ) ) ;
            so_called_common_engine_render_frame_loss_request_sender :: send ( so_called_common_engine_render_frame_loss_request_message ( ) ) ;
        }
    }
}

void _shy_common_logic_fidget :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

