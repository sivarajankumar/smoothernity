namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_fract z_far = so_called_platform_math :: init_num_fract ( 50 , 1 ) ;
        static const so_called_type_platform_math_num_fract z_near = so_called_platform_math :: init_num_fract ( 1 , 1 ) ;
    }

    static void init_render ( ) ;
    static void get_near_plane_distance ( so_called_type_platform_math_num_fract & ) ;

    static so_called_type_platform_math_num_whole fidget_prepared ;
    
    static so_called_type_platform_math_num_whole render_aspect_requested ;
    static so_called_type_platform_math_num_fract render_aspect_width ;
    static so_called_type_platform_math_num_fract render_aspect_height ;
    
    static so_called_type_platform_math_num_whole handling_near_plane_distance_request ;
    static so_called_type_platform_math_num_whole handling_use_ortho_projection_request ;
    static so_called_type_platform_math_num_whole handling_use_perspective_projection_request ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_core > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: init_render ( )
{
    so_called_sender_common_engine_render_blend_disable :: send ( so_called_message_common_engine_render_blend_disable ( ) ) ;
    so_called_sender_common_engine_render_enable_face_culling :: send ( so_called_message_common_engine_render_enable_face_culling ( ) ) ;
    so_called_sender_common_engine_render_texture_mode_modulate :: send ( so_called_message_common_engine_render_texture_mode_modulate ( ) ) ;
}

void shy_guts :: get_near_plane_distance ( so_called_type_platform_math_num_fract & result )
{
    so_called_platform_math :: add_fracts ( result , shy_guts :: render_aspect_width , shy_guts :: render_aspect_height ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_engine_render_aspect_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_aspect_requested ) )
    {
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_aspect_width = msg . width ;
        shy_guts :: render_aspect_height = msg . height ;
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: handling_near_plane_distance_request ) )
        {
            shy_guts :: handling_near_plane_distance_request = so_called_platform_math_consts :: whole_false ;
            so_called_message_common_logic_core_near_plane_distance_reply near_plane_distance_reply_msg ;
            shy_guts :: get_near_plane_distance ( near_plane_distance_reply_msg . distance ) ;
            so_called_sender_common_logic_core_near_plane_distance_reply :: send ( near_plane_distance_reply_msg ) ;
        }
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: handling_use_ortho_projection_request ) )
        {
            shy_guts :: handling_use_ortho_projection_request = so_called_platform_math_consts :: whole_false ;
            
            so_called_type_platform_math_num_fract width = shy_guts :: render_aspect_width ;
            so_called_type_platform_math_num_fract height = shy_guts :: render_aspect_height ;
            so_called_type_platform_math_num_fract neg_width ;
            so_called_type_platform_math_num_fract neg_height ;
            so_called_platform_math :: neg_fract ( neg_width , width ) ;
            so_called_platform_math :: neg_fract ( neg_height , height ) ;
            
            so_called_message_common_engine_render_projection_ortho proj_msg ;
            proj_msg . x_left = neg_width ;
            proj_msg . x_right = width ;
            proj_msg . y_bottom = neg_height ;
            proj_msg . y_top = height ;
            proj_msg . z_near = shy_guts :: consts :: z_near ;
            proj_msg . z_far = shy_guts :: consts :: z_far ;
            so_called_sender_common_engine_render_projection_ortho :: send ( proj_msg ) ;
            
            so_called_sender_common_engine_render_matrix_identity :: send ( so_called_message_common_engine_render_matrix_identity ( ) ) ;
            so_called_sender_common_logic_core_use_ortho_projection_reply :: send ( so_called_message_common_logic_core_use_ortho_projection_reply ( ) ) ;
        }
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: handling_use_perspective_projection_request ) )
        {
            shy_guts :: handling_use_perspective_projection_request = so_called_platform_math_consts :: whole_false ;
        
            so_called_type_platform_math_num_fract width = shy_guts :: render_aspect_width ;
            so_called_type_platform_math_num_fract height = shy_guts :: render_aspect_height ;
            so_called_type_platform_math_num_fract neg_width ;
            so_called_type_platform_math_num_fract neg_height ;
            so_called_type_platform_math_num_fract z_near ;
            shy_guts :: get_near_plane_distance ( z_near ) ;
            so_called_platform_math :: neg_fract ( neg_width , width ) ;
            so_called_platform_math :: neg_fract ( neg_height , height ) ;
            
            so_called_message_common_engine_render_projection_frustum proj_msg ;
            proj_msg . x_left = neg_width ;
            proj_msg . x_right = width ;
            proj_msg . y_bottom = neg_height ;
            proj_msg . y_top = height ;
            proj_msg . z_near = z_near ;
            proj_msg . z_far = shy_guts :: consts :: z_far ;
            so_called_sender_common_engine_render_projection_frustum :: send ( proj_msg ) ;
            
            so_called_sender_common_engine_render_matrix_identity :: send ( so_called_message_common_engine_render_matrix_identity ( ) ) ;
            so_called_sender_common_logic_core_use_perspective_projection_reply :: send ( so_called_message_common_logic_core_use_perspective_projection_reply ( ) ) ;
        }
    }
}

void _shy_common_logic_core :: receive ( so_called_message_common_init )
{
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: handling_near_plane_distance_request = so_called_platform_math_consts :: whole_false ;
    shy_guts :: handling_use_ortho_projection_request = so_called_platform_math_consts :: whole_false ;
    shy_guts :: handling_use_perspective_projection_request = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_prepared = so_called_platform_math_consts :: whole_false ;
    shy_guts :: init_render ( ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_logic_core_near_plane_distance_request )
{
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: handling_near_plane_distance_request = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_engine_render_aspect_request :: send ( so_called_message_common_engine_render_aspect_request ( ) ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_logic_core_use_ortho_projection_request )
{
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: handling_use_ortho_projection_request = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_engine_render_aspect_request :: send ( so_called_message_common_engine_render_aspect_request ( ) ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_logic_core_use_perspective_projection_request )
{
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: handling_use_perspective_projection_request = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_engine_render_aspect_request :: send ( so_called_message_common_engine_render_aspect_request ( ) ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_logic_fidget_prepared )
{
    shy_guts :: fidget_prepared = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_render )
{
    so_called_sender_common_logic_application_render :: send ( so_called_message_common_logic_application_render ( ) ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_prepared ) )
        so_called_sender_common_logic_application_update :: send ( so_called_message_common_logic_application_update ( ) ) ;
    else
        so_called_sender_common_logic_fidget_prepare_permit :: send ( so_called_message_common_logic_fidget_prepare_permit ( ) ) ;
    so_called_sender_common_logic_fidget_update :: send ( so_called_message_common_logic_fidget_update ( ) ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_video_mode_changed )
{
    shy_guts :: init_render ( ) ;
}

void _shy_common_logic_core :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

