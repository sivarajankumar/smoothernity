namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_whole change_origin_in_frames = so_called_platform_math :: init_num_whole ( 139 ) ;
        static const so_called_type_platform_math_num_whole change_target_in_frames = so_called_platform_math :: init_num_whole ( 181 ) ;
        static const so_called_type_platform_math_num_whole random_const_1 = so_called_platform_math :: init_num_whole ( 181 ) ;
        static const so_called_type_platform_math_num_whole random_const_2 = so_called_platform_math :: init_num_whole ( 139 ) ;
    }

    static void proceed_with_update ( ) ;
    static void proceed_with_fill_camera_schedules ( ) ;
    static void proceed_with_camera_update ( ) ;
    static void proceed_with_update_desired_camera_target ( ) ;
    static void proceed_with_update_desired_camera_origin ( ) ;
    static void fill_next_camera_schedule ( ) ;
    static void reset_camera_rubber ( ) ;
    static void update_camera ( ) ;
    static void update_desired_camera_origin ( ) ;
    static void update_desired_camera_target ( ) ;
    static void update_current_camera_origin ( ) ;
    static void update_current_camera_target ( ) ;
    static void update_camera_matrix ( ) ;
    static void calc_desired_camera_target_pos ( ) ;
    static void calc_desired_camera_origin_pos ( ) ;
    static void random_camera_origin_index ( so_called_type_platform_math_num_whole & ) ;
    static void random_camera_target_index ( so_called_type_platform_math_num_whole & ) ;
    static void camera_origin_index_is_duplicate ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_whole index ) ;
    static void camera_target_index_is_duplicate ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_whole index ) ;
    static void get_random_index
        ( so_called_type_platform_math_num_whole & result
        , so_called_type_platform_math_num_whole index_min
        , so_called_type_platform_math_num_whole index_max
        ) ;

    static so_called_type_platform_matrix_data camera_matrix ;
    static so_called_type_platform_math_num_whole camera_prepare_permitted ;
    static so_called_type_platform_math_num_whole frames_to_change_camera_target ;
    static so_called_type_platform_math_num_whole frames_to_change_camera_origin ;
    static so_called_type_platform_math_num_whole random_seed ;
    static so_called_type_platform_math_num_whole camera_created ;
    static so_called_type_platform_math_num_fract origin_rubber ;
    static so_called_type_platform_math_num_fract target_rubber ;
    
    static so_called_type_platform_math_num_whole entities_height_requested ;
    static so_called_type_platform_math_num_whole entities_height_replied ;
    static so_called_type_platform_math_num_fract entities_height ;
    
    static so_called_type_platform_math_num_whole entities_mesh_grid_requested ;
    static so_called_type_platform_math_num_whole entities_mesh_grid_replied ;
    static so_called_type_platform_math_num_whole entities_mesh_grid ;
    
    static so_called_type_platform_math_num_whole near_plane_distance_requested ;
    static so_called_type_platform_math_num_whole near_plane_distance_replied ;
    static so_called_type_platform_math_num_fract near_plane_distance ;
    
    static so_called_type_platform_math_num_whole filling_camera_schedules ;
    static so_called_type_platform_math_num_whole fill_camera_schedules_index ;
    
    static so_called_type_platform_math_num_whole fill_schedules_origin_requested ;
    static so_called_type_platform_math_num_whole fill_schedules_origin_replied ;
    static so_called_type_platform_math_num_whole fill_schedules_origin_index ;
    static so_called_type_platform_vector_data fill_schedules_origin ;
    
    static so_called_type_platform_math_num_whole fill_schedules_target_requested ;
    static so_called_type_platform_math_num_whole fill_schedules_target_replied ;
    static so_called_type_platform_math_num_whole fill_schedules_target_index ;
    static so_called_type_platform_vector_data fill_schedules_target ;
    
    static so_called_type_platform_math_num_whole desired_camera_origin_is_ready ;
    static so_called_type_platform_vector_data desired_camera_origin ;
    static so_called_type_platform_math_num_whole desired_camera_origin_new_requested ;
    static so_called_type_platform_math_num_whole desired_camera_origin_new_index ;
    static so_called_type_platform_vector_data desired_camera_origin_new_position ;
    
    static so_called_type_platform_math_num_whole desired_camera_target_is_ready ;
    static so_called_type_platform_vector_data desired_camera_target ;
    static so_called_type_platform_math_num_whole desired_camera_target_new_requested ;
    static so_called_type_platform_math_num_whole desired_camera_target_new_index ;
    static so_called_type_platform_vector_data desired_camera_target_new_position ;
    
    static so_called_type_platform_vector_data current_camera_origin ;
    static so_called_type_platform_vector_data current_camera_target ;
    
    static so_called_type_platform_math_num_whole render_aspect_requested ;
    static so_called_type_platform_math_num_fract render_aspect_height ;
    
    static so_called_type_platform_static_array_data < so_called_type_platform_math_num_whole , 4 > scheduled_camera_origin_indices ;
    static so_called_type_platform_static_array_data < so_called_type_platform_math_num_whole , 4 > scheduled_camera_target_indices ;
    static so_called_type_platform_static_array_data < so_called_type_platform_vector_data , 4 > scheduled_camera_origins ;
    static so_called_type_platform_static_array_data < so_called_type_platform_vector_data , 4 > scheduled_camera_targets ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_camera > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_update ( )
{
}

void shy_guts :: proceed_with_fill_camera_schedules ( )
{
}

void shy_guts :: proceed_with_camera_update ( )
{
}

void shy_guts :: proceed_with_update_desired_camera_target ( )
{
}

void shy_guts :: proceed_with_update_desired_camera_origin ( )
{
}

void shy_guts :: fill_next_camera_schedule ( )
{
}

void shy_guts :: reset_camera_rubber ( )
{
}

void shy_guts :: update_camera ( )
{
}

void shy_guts :: update_desired_camera_origin ( )
{
}

void shy_guts :: update_desired_camera_target ( )
{
}

void shy_guts :: update_current_camera_origin ( )
{
}

void shy_guts :: update_current_camera_target ( )
{
}

void shy_guts :: update_camera_matrix ( )
{
}

void shy_guts :: calc_desired_camera_target_pos ( )
{
}

void shy_guts :: calc_desired_camera_origin_pos ( )
{
}

void shy_guts :: random_camera_origin_index ( so_called_type_platform_math_num_whole & )
{
}

void shy_guts :: random_camera_target_index ( so_called_type_platform_math_num_whole & )
{
}

void shy_guts :: camera_origin_index_is_duplicate ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_whole index )
{
}

void shy_guts :: camera_target_index_is_duplicate ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_whole index )
{
}

void shy_guts :: get_random_index
    ( so_called_type_platform_math_num_whole & result
    , so_called_type_platform_math_num_whole index_min
    , so_called_type_platform_math_num_whole index_max
    )
{
}

void _shy_common_logic_camera :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_camera :: receive ( so_called_message_common_init )
{
    shy_guts :: origin_rubber = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: target_rubber = so_called_platform_math_consts :: fract_0 ;
    
    shy_guts :: camera_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: camera_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: entities_height_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: entities_height_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: entities_mesh_grid_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: entities_mesh_grid_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: near_plane_distance_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: near_plane_distance_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: random_seed = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: frames_to_change_camera_target = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: frames_to_change_camera_origin = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: filling_camera_schedules = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fill_camera_schedules_index = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: fill_schedules_origin_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fill_schedules_origin_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fill_schedules_target_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fill_schedules_target_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: desired_camera_origin_new_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: desired_camera_target_new_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , so_called_platform_math_consts :: whole_4 )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_vector_data origin_pos ;
        so_called_type_platform_vector_data target_pos ;
        so_called_type_platform_pointer_data < so_called_type_platform_math_num_whole > scheduled_origin_index ;
        so_called_type_platform_pointer_data < so_called_type_platform_math_num_whole > scheduled_target_index ;
        so_called_type_platform_pointer_data < so_called_type_platform_vector_data > scheduled_origin_pos ;
        so_called_type_platform_pointer_data < so_called_type_platform_vector_data > scheduled_target_pos ;
    
        so_called_platform_static_array :: element_ptr ( scheduled_origin_index , shy_guts :: scheduled_camera_origin_indices , i ) ;
        so_called_platform_static_array :: element_ptr ( scheduled_target_index , shy_guts :: scheduled_camera_target_indices , i ) ;
        so_called_platform_static_array :: element_ptr ( scheduled_origin_pos , shy_guts :: scheduled_camera_origins , i ) ;
        so_called_platform_static_array :: element_ptr ( scheduled_target_pos , shy_guts :: scheduled_camera_targets , i ) ;

        so_called_platform_vector :: xyz 
            ( scheduled_origin_pos . get ( )
            , so_called_platform_math_consts :: fract_0
            , so_called_platform_math_consts :: fract_0
            , so_called_platform_math_consts :: fract_0
            ) ;
        so_called_platform_vector :: xyz
            ( scheduled_target_pos . get ( )
            , so_called_platform_math_consts :: fract_0
            , so_called_platform_math_consts :: fract_0
            , so_called_platform_math_consts :: fract_0
            ) ;

        scheduled_origin_index . get ( ) = so_called_platform_math_consts :: whole_0 ;
        scheduled_target_index . get ( ) = so_called_platform_math_consts :: whole_0 ;
    }
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_camera_matrix_request )
{
    so_called_message_common_logic_camera_matrix_reply reply_msg ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: camera_created ) )
        reply_msg . matrix = shy_guts :: camera_matrix ;
    else
        so_called_platform_matrix :: identity ( reply_msg . matrix ) ;
    so_called_sender_common_logic_camera_matrix_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_camera_prepare_permit )
{
    shy_guts :: camera_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_camera_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: camera_prepare_permitted ) )
    {
        shy_guts :: entities_height_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: entities_mesh_grid_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: near_plane_distance_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_entities_height_request :: send ( so_called_message_common_logic_entities_height_request ( ) ) ;
        so_called_sender_common_logic_entities_mesh_grid_request :: send ( so_called_message_common_logic_entities_mesh_grid_request ( ) ) ;
        so_called_sender_common_logic_core_near_plane_distance_request :: send ( so_called_message_common_logic_core_near_plane_distance_request ( ) ) ;
    }
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_core_near_plane_distance_reply )
{
}
