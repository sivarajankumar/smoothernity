namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_fract final_r = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static const so_called_type_platform_math_num_fract final_g = so_called_platform_math :: init_num_fract ( 1 , 10 ) ;
        static const so_called_type_platform_math_num_fract final_b = so_called_platform_math :: init_num_fract ( 4 , 10 ) ;
        static const so_called_type_platform_math_num_fract fog_far_shift = so_called_platform_math :: init_num_fract ( 20 , 1 ) ;
        static const so_called_type_platform_math_num_fract fog_near_shift = so_called_platform_math :: init_num_fract ( 10 , 1 ) ;
        static const so_called_type_platform_math_num_whole fade_in_frames = so_called_platform_math :: init_num_whole ( 90 ) ;
        static const so_called_type_platform_math_num_whole trace_enabled = so_called_platform_math :: init_num_whole ( so_called_lib_std_true ) ;
    }

    static void clear_screen ( ) ;
    static void update_color ( ) ;
    static void proceed_with_render ( ) ;

    static so_called_type_platform_math_num_fract color_r ;
    static so_called_type_platform_math_num_fract color_g ;
    static so_called_type_platform_math_num_fract color_b ;
    static so_called_type_platform_math_num_whole color_frames ;
    static so_called_type_platform_math_num_whole game_launched ;
    static so_called_type_platform_math_num_whole game_launch_permitted ;
    
    static so_called_type_platform_math_num_whole near_plane_distance_requested ;
    static so_called_type_platform_math_num_whole near_plane_distance_replied ;
    static so_called_type_platform_math_num_fract near_plane_distance ;
    
    static so_called_type_platform_math_num_whole camera_matrix_requested ;
    static so_called_type_platform_math_num_whole camera_matrix_replied ;
    static so_called_type_platform_matrix_data camera_matrix ;
    
    static so_called_type_platform_math_num_whole use_perspective_projection_requested ;
    static so_called_type_platform_math_num_whole use_perspective_projection_replied ;

    static so_called_type_platform_math_num_whole use_ortho_projection_requested ;
    static so_called_type_platform_math_num_whole use_ortho_projection_replied ;
    
    static so_called_type_platform_math_num_whole land_render_requested ;
    static so_called_type_platform_math_num_whole land_render_replied ;
    
    static so_called_type_platform_math_num_whole entities_render_requested ;
    static so_called_type_platform_math_num_whole entities_render_replied ;
    
    static so_called_type_platform_math_num_whole fidget_render_requested ;
    static so_called_type_platform_math_num_whole fidget_render_replied ;
    
    static so_called_type_platform_math_num_whole text_render_requested ;
    static so_called_type_platform_math_num_whole text_render_replied ;

    static so_called_type_platform_math_num_whole image_render_requested ;
    static so_called_type_platform_math_num_whole image_render_replied ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_game > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: clear_screen ( )
{
    so_called_type_platform_math_num_fract fog_a ;
    so_called_type_platform_math_num_fract fog_far ;
    so_called_type_platform_math_num_fract fog_near ;
    fog_a = so_called_platform_math_consts :: fract_0 ;
    so_called_platform_math :: add_fracts ( fog_far , shy_guts :: consts :: fog_far_shift , shy_guts :: near_plane_distance ) ;
    so_called_platform_math :: add_fracts ( fog_near , shy_guts :: consts :: fog_near_shift , shy_guts :: near_plane_distance ) ;
    
    so_called_message_common_engine_render_fog_linear fog_msg ;
    fog_msg . z_near = fog_near ;
    fog_msg . z_far = fog_far ;
    fog_msg . r = shy_guts :: color_r ;
    fog_msg . g = shy_guts :: color_g ;
    fog_msg . b = shy_guts :: color_b ;
    fog_msg . a = fog_a ;
    so_called_sender_common_engine_render_fog_linear :: send ( fog_msg ) ;

    so_called_message_common_engine_render_clear_screen clear_screen_msg ;
    clear_screen_msg . r = shy_guts :: color_r ;
    clear_screen_msg . g = shy_guts :: color_g ;
    clear_screen_msg . b = shy_guts :: color_b ;
    so_called_sender_common_engine_render_clear_screen :: send ( clear_screen_msg ) ;
}

void shy_guts :: update_color ( )
{
    so_called_type_platform_math_num_fract scale ;
    so_called_type_platform_math_num_fract fract_color_frames ;
    so_called_type_platform_math_num_fract fract_fade_in_frames ;

    so_called_platform_math :: make_fract_from_whole ( fract_fade_in_frames , shy_guts :: consts :: fade_in_frames ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_color_frames , shy_guts :: color_frames ) ;
    so_called_platform_math :: div_fracts ( scale , fract_color_frames , fract_fade_in_frames ) ;
    so_called_platform_math :: mul_fracts ( shy_guts :: color_r , scale , shy_guts :: consts :: final_r ) ;
    so_called_platform_math :: mul_fracts ( shy_guts :: color_g , scale , shy_guts :: consts :: final_g ) ;
    so_called_platform_math :: mul_fracts ( shy_guts :: color_b , scale , shy_guts :: consts :: final_b ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: color_frames , shy_guts :: consts :: fade_in_frames ) )
        so_called_platform_math :: inc_whole ( shy_guts :: color_frames ) ;
}

void shy_guts :: proceed_with_render ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: camera_matrix_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: near_plane_distance_replied )
       )
    {
        shy_guts :: camera_matrix_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: near_plane_distance_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: clear_screen ( ) ;
        
        shy_guts :: use_perspective_projection_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_core_use_perspective_projection_request :: send ( so_called_message_common_logic_core_use_perspective_projection_request ( ) ) ;    
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_perspective_projection_replied ) )
    {
        shy_guts :: use_perspective_projection_replied = so_called_platform_math_consts :: whole_false ;
        so_called_sender_common_engine_render_enable_depth_test :: send ( so_called_message_common_engine_render_enable_depth_test ( ) ) ;
        
        so_called_message_common_engine_render_matrix_load matrix_load_msg ;
        matrix_load_msg . matrix = shy_guts :: camera_matrix ;
        so_called_sender_common_engine_render_matrix_load :: send ( matrix_load_msg ) ;
        
        shy_guts :: land_render_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: entities_render_requested = so_called_platform_math_consts :: whole_true ;
        
        so_called_sender_common_logic_land_render_request :: send ( so_called_message_common_logic_land_render_request ( ) ) ;
        so_called_sender_common_logic_entities_render_request :: send ( so_called_message_common_logic_entities_render_request ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_render_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: entities_render_replied )
       )
    {
        shy_guts :: land_render_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: entities_render_replied = so_called_platform_math_consts :: whole_false ;
        
        shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_core_use_ortho_projection_request :: send ( so_called_message_common_logic_core_use_ortho_projection_request ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_ortho_projection_replied ) )
    {
        shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_false ;
        so_called_sender_common_engine_render_disable_depth_test :: send ( so_called_message_common_engine_render_disable_depth_test ( ) ) ;
        so_called_sender_common_engine_render_fog_disable :: send ( so_called_message_common_engine_render_fog_disable ( ) ) ;
        
        shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_fidget_render_request :: send ( so_called_message_common_logic_fidget_render_request ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_render_replied ) )
    {
        shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: text_render_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: image_render_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_text_render_request :: send ( so_called_message_common_logic_text_render_request ( ) ) ;
        so_called_sender_common_logic_image_render_request :: send ( so_called_message_common_logic_image_render_request ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_render_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: image_render_replied )
       )
    {
        shy_guts :: text_render_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: image_render_replied = so_called_platform_math_consts :: whole_false ;
        so_called_sender_common_logic_touch_render :: send ( so_called_message_common_logic_touch_render ( ) ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_init )
{
    shy_guts :: color_r = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: color_g = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: color_b = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: color_frames = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: game_launched = so_called_platform_math_consts :: whole_false ;
    shy_guts :: game_launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: near_plane_distance_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: near_plane_distance_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: camera_matrix_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: camera_matrix_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_perspective_projection_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_perspective_projection_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_render_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_render_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: entities_render_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: entities_render_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: text_render_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: text_render_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: image_render_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: image_render_replied = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_camera_matrix_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: camera_matrix_requested ) )
    {
        shy_guts :: camera_matrix_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: camera_matrix_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: camera_matrix = msg . matrix ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_camera_prepared )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
        so_called_trace ( so_called_trace_common_logic_game :: land_prepare_permitted ( ) ) ;
    so_called_sender_common_logic_land_prepare_permit :: send ( so_called_message_common_logic_land_prepare_permit ( ) ) ;
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_core_near_plane_distance_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: near_plane_distance_requested ) )
    {
        shy_guts :: near_plane_distance_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: near_plane_distance_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: near_plane_distance = msg . distance ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_core_use_ortho_projection_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_ortho_projection_requested ) )
    {
        shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_core_use_perspective_projection_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_perspective_projection_requested ) )
    {
        shy_guts :: use_perspective_projection_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_perspective_projection_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;        
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_entities_prepared )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
        so_called_trace ( so_called_trace_common_logic_game :: image_prepare_permitted ( ) ) ;
    so_called_sender_common_logic_image_prepare_permit :: send ( so_called_message_common_logic_image_prepare_permit ( ) ) ;
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_entities_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entities_render_requested ) )
    {
        shy_guts :: entities_render_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: entities_render_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_fidget_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_render_requested ) )
    {
        shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_game_launch_permit )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
        so_called_trace ( so_called_trace_common_logic_game :: game_launch_permitted ( ) ) ;
    shy_guts :: game_launch_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_game_render )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: game_launched ) )
    {
        shy_guts :: near_plane_distance_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: camera_matrix_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_core_near_plane_distance_request :: send ( so_called_message_common_logic_core_near_plane_distance_request ( ) ) ;
        so_called_sender_common_logic_camera_matrix_request :: send ( so_called_message_common_logic_camera_matrix_request ( ) ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_game_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: game_launch_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: game_launched ) )
        {
            if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
                so_called_trace ( so_called_trace_common_logic_game :: camera_prepare_permitted ( ) ) ;
            so_called_sender_common_logic_camera_prepare_permit :: send ( so_called_message_common_logic_camera_prepare_permit ( ) ) ;
            shy_guts :: game_launched = so_called_platform_math_consts :: whole_true ;
        }
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: game_launched ) )
    {
        shy_guts :: update_color ( ) ;
        so_called_sender_common_logic_camera_update :: send ( so_called_message_common_logic_camera_update ( ) ) ;
        so_called_sender_common_logic_entities_update :: send ( so_called_message_common_logic_entities_update ( ) ) ;
        so_called_sender_common_logic_land_update :: send ( so_called_message_common_logic_land_update ( ) ) ;
        so_called_sender_common_logic_image_update :: send ( so_called_message_common_logic_image_update ( ) ) ;
        so_called_sender_common_logic_sound_update :: send ( so_called_message_common_logic_sound_update ( ) ) ;
        so_called_sender_common_logic_text_update :: send ( so_called_message_common_logic_text_update ( ) ) ;
        so_called_sender_common_logic_touch_update :: send ( so_called_message_common_logic_touch_update ( ) ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_image_prepared )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
        so_called_trace ( so_called_trace_common_logic_game :: touch_prepare_permitted ( ) ) ;
    so_called_sender_common_logic_touch_prepare_permit :: send ( so_called_message_common_logic_touch_prepare_permit ( ) ) ;
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_image_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: image_render_requested ) )
    {
        shy_guts :: image_render_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: image_render_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_land_prepared )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
        so_called_trace ( so_called_trace_common_logic_game :: entities_prepare_permitted ( ) ) ;
    so_called_sender_common_logic_entities_prepare_permit :: send ( so_called_message_common_logic_entities_prepare_permit ( ) ) ;
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_land_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_render_requested ) )
    {
        shy_guts :: land_render_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: land_render_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_sound_prepared )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_text_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_render_requested ) )
    {
        shy_guts :: text_render_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: text_render_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_touch_prepared )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
        so_called_trace ( so_called_trace_common_logic_game :: sound_prepare_permitted ( ) ) ;
    so_called_sender_common_logic_sound_prepare_permit :: send ( so_called_message_common_logic_sound_prepare_permit ( ) ) ;
}

void _shy_common_logic_game :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

