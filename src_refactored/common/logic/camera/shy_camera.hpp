namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_whole change_origin_in_frames = so_called_platform_math :: init_num_whole ( 139 ) ;
        static const so_called_type_platform_math_num_whole change_target_in_frames = so_called_platform_math :: init_num_whole ( 181 ) ;
        static const so_called_type_platform_math_num_whole random_const_1 = so_called_platform_math :: init_num_whole ( 181 ) ;
        static const so_called_type_platform_math_num_whole random_const_2 = so_called_platform_math :: init_num_whole ( 139 ) ;
    }

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

void _shy_common_logic_camera :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_camera :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_camera_matrix_request )
{
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_camera_prepare_permit )
{
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_camera_update )
{
}

void _shy_common_logic_camera :: receive ( so_called_message_common_logic_core_near_plane_distance_reply )
{
}
