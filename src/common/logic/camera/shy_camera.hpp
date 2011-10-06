namespace shy_guts
{
    namespace consts
    {
        static const so_called_platform_math_num_whole_type change_origin_in_frames = so_called_platform_math :: init_num_whole ( 139 ) ;
        static const so_called_platform_math_num_whole_type change_target_in_frames = so_called_platform_math :: init_num_whole ( 181 ) ;
        static const so_called_platform_math_num_whole_type random_const_1 = so_called_platform_math :: init_num_whole ( 181 ) ;
        static const so_called_platform_math_num_whole_type random_const_2 = so_called_platform_math :: init_num_whole ( 139 ) ;
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
    static void random_camera_origin_index ( so_called_platform_math_num_whole_type & ) ;
    static void random_camera_target_index ( so_called_platform_math_num_whole_type & ) ;
    static void camera_origin_index_is_duplicate ( so_called_platform_math_num_whole_type & result , so_called_platform_math_num_whole_type index ) ;
    static void camera_target_index_is_duplicate ( so_called_platform_math_num_whole_type & result , so_called_platform_math_num_whole_type index ) ;
    static void get_random_index
        ( so_called_platform_math_num_whole_type & result
        , so_called_platform_math_num_whole_type index_min
        , so_called_platform_math_num_whole_type index_max
        ) ;

    static so_called_platform_matrix_data_type camera_matrix ;
    static so_called_platform_math_num_whole_type camera_prepare_permitted ;
    static so_called_platform_math_num_whole_type frames_to_change_camera_target ;
    static so_called_platform_math_num_whole_type frames_to_change_camera_origin ;
    static so_called_platform_math_num_whole_type random_seed ;
    static so_called_platform_math_num_whole_type camera_created ;
    static so_called_platform_math_num_fract_type origin_rubber ;
    static so_called_platform_math_num_fract_type target_rubber ;
    
    static so_called_platform_math_num_whole_type entities_height_requested ;
    static so_called_platform_math_num_whole_type entities_height_replied ;
    static so_called_platform_math_num_fract_type entities_height ;
    
    static so_called_platform_math_num_whole_type entities_mesh_grid_requested ;
    static so_called_platform_math_num_whole_type entities_mesh_grid_replied ;
    static so_called_platform_math_num_whole_type entities_mesh_grid ;
    
    static so_called_platform_math_num_whole_type near_plane_distance_requested ;
    static so_called_platform_math_num_whole_type near_plane_distance_replied ;
    static so_called_platform_math_num_fract_type near_plane_distance ;
    
    static so_called_platform_math_num_whole_type filling_camera_schedules ;
    static so_called_platform_math_num_whole_type fill_camera_schedules_index ;
    
    static so_called_platform_math_num_whole_type fill_schedules_origin_requested ;
    static so_called_platform_math_num_whole_type fill_schedules_origin_replied ;
    static so_called_platform_math_num_whole_type fill_schedules_origin_index ;
    static so_called_platform_vector_data_type fill_schedules_origin ;
    
    static so_called_platform_math_num_whole_type fill_schedules_target_requested ;
    static so_called_platform_math_num_whole_type fill_schedules_target_replied ;
    static so_called_platform_math_num_whole_type fill_schedules_target_index ;
    static so_called_platform_vector_data_type fill_schedules_target ;
    
    static so_called_platform_math_num_whole_type desired_camera_origin_is_ready ;
    static so_called_platform_vector_data_type desired_camera_origin ;
    static so_called_platform_math_num_whole_type desired_camera_origin_new_requested ;
    static so_called_platform_math_num_whole_type desired_camera_origin_new_index ;
    static so_called_platform_vector_data_type desired_camera_origin_new_position ;
    
    static so_called_platform_math_num_whole_type desired_camera_target_is_ready ;
    static so_called_platform_vector_data_type desired_camera_target ;
    static so_called_platform_math_num_whole_type desired_camera_target_new_requested ;
    static so_called_platform_math_num_whole_type desired_camera_target_new_index ;
    static so_called_platform_vector_data_type desired_camera_target_new_position ;
    
    static so_called_platform_vector_data_type current_camera_origin ;
    static so_called_platform_vector_data_type current_camera_target ;
    
    static so_called_platform_math_num_whole_type render_aspect_requested ;
    static so_called_platform_math_num_fract_type render_aspect_height ;
    
    static so_called_platform_static_array_data_type < so_called_platform_math_num_whole_type , 4 > scheduled_camera_origin_indices ;
    static so_called_platform_static_array_data_type < so_called_platform_math_num_whole_type , 4 > scheduled_camera_target_indices ;
    static so_called_platform_static_array_data_type < so_called_platform_vector_data_type , 4 > scheduled_camera_origins ;
    static so_called_platform_static_array_data_type < so_called_platform_vector_data_type , 4 > scheduled_camera_targets ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_camera > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_update ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entities_height_replied ) 
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: entities_mesh_grid_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: near_plane_distance_replied )
       )
    {
        shy_guts :: entities_height_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: entities_mesh_grid_replied = so_called_platform_math_consts :: whole_false ;
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: camera_created ) )
        {
            if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: filling_camera_schedules ) )
            {
                shy_guts :: filling_camera_schedules = so_called_platform_math_consts :: whole_true ;
                shy_guts :: fill_next_camera_schedule ( ) ;
            }
        }
        else
            shy_guts :: update_camera ( ) ;
    }
}

void shy_guts :: proceed_with_fill_camera_schedules ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fill_schedules_origin_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: fill_schedules_target_replied )
       )
    {
        shy_guts :: fill_schedules_origin_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fill_schedules_target_replied = so_called_platform_math_consts :: whole_false ;
        
        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_origin_index ;
        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_target_index ;
        so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_origin_pos ;
        so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_target_pos ;
        
        so_called_platform_static_array :: element_ptr ( scheduled_origin_index , shy_guts :: scheduled_camera_origin_indices , shy_guts :: fill_camera_schedules_index ) ;
        so_called_platform_static_array :: element_ptr ( scheduled_target_index , shy_guts :: scheduled_camera_target_indices , shy_guts :: fill_camera_schedules_index ) ;
        so_called_platform_static_array :: element_ptr ( scheduled_origin_pos , shy_guts :: scheduled_camera_origins , shy_guts :: fill_camera_schedules_index ) ;
        so_called_platform_static_array :: element_ptr ( scheduled_target_pos , shy_guts :: scheduled_camera_targets , shy_guts :: fill_camera_schedules_index ) ;

        scheduled_origin_index . get ( ) = shy_guts :: fill_schedules_origin_index ;
        scheduled_target_index . get ( ) = shy_guts :: fill_schedules_target_index ;
        scheduled_origin_pos . get ( ) = shy_guts :: fill_schedules_origin ;
        scheduled_target_pos . get ( ) = shy_guts :: fill_schedules_target ;
        
        so_called_platform_math :: inc_whole ( shy_guts :: fill_camera_schedules_index ) ;
        shy_guts :: fill_next_camera_schedule ( ) ;
    }
}

void shy_guts :: proceed_with_camera_update ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: desired_camera_origin_is_ready ) 
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: desired_camera_target_is_ready )
       )
    {
        shy_guts :: update_current_camera_origin ( ) ;
        shy_guts :: update_current_camera_target ( ) ;
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
        so_called_common_engine_render_aspect_request_sender :: send ( so_called_common_engine_render_aspect_request_message ( ) ) ;
    }
}

void shy_guts :: proceed_with_update_desired_camera_target ( )
{
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_0 ;
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_1 ;
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_2 ;
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_3 ;

    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_0 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_1 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_2 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_3 ;

    so_called_platform_static_array :: element_ptr ( scheduled_index_0 , shy_guts :: scheduled_camera_target_indices , so_called_platform_math_consts :: whole_0 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_index_1 , shy_guts :: scheduled_camera_target_indices , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_index_2 , shy_guts :: scheduled_camera_target_indices , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_index_3 , shy_guts :: scheduled_camera_target_indices , so_called_platform_math_consts :: whole_3 ) ;

    so_called_platform_static_array :: element_ptr ( scheduled_pos_0 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_0 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_pos_1 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_pos_2 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_pos_3 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_3 ) ;

    scheduled_index_0 . get ( ) = scheduled_index_1 . get ( ) ;
    scheduled_index_1 . get ( ) = scheduled_index_2 . get ( ) ;
    scheduled_index_2 . get ( ) = scheduled_index_3 . get ( ) ;
    scheduled_index_3 . get ( ) = shy_guts :: desired_camera_target_new_index ;

    scheduled_pos_0 . get ( ) = scheduled_pos_1 . get ( ) ;
    scheduled_pos_1 . get ( ) = scheduled_pos_2 . get ( ) ;
    scheduled_pos_2 . get ( ) = scheduled_pos_3 . get ( ) ;
    scheduled_pos_3 . get ( ) = shy_guts :: desired_camera_target_new_position ;

    shy_guts :: calc_desired_camera_target_pos ( ) ;
    shy_guts :: desired_camera_target_is_ready = so_called_platform_math_consts :: whole_true ;
    
    shy_guts :: proceed_with_camera_update ( ) ;
}

void shy_guts :: proceed_with_update_desired_camera_origin ( )
{
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_0 ;
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_1 ;
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_2 ;
    so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index_3 ;

    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_0 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_1 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_2 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_pos_3 ;

    so_called_platform_static_array :: element_ptr ( scheduled_index_0 , shy_guts :: scheduled_camera_origin_indices , so_called_platform_math_consts :: whole_0 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_index_1 , shy_guts :: scheduled_camera_origin_indices , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_index_2 , shy_guts :: scheduled_camera_origin_indices , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_index_3 , shy_guts :: scheduled_camera_origin_indices , so_called_platform_math_consts :: whole_3 ) ;

    so_called_platform_static_array :: element_ptr ( scheduled_pos_0 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_0 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_pos_1 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_pos_2 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_static_array :: element_ptr ( scheduled_pos_3 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_3 ) ;

    scheduled_index_0 . get ( ) = scheduled_index_1 . get ( ) ;
    scheduled_index_1 . get ( ) = scheduled_index_2 . get ( ) ;
    scheduled_index_2 . get ( ) = scheduled_index_3 . get ( ) ;
    scheduled_index_3 . get ( ) = shy_guts :: desired_camera_origin_new_index ;

    scheduled_pos_0 . get ( ) = scheduled_pos_1 . get ( ) ;
    scheduled_pos_1 . get ( ) = scheduled_pos_2 . get ( ) ;
    scheduled_pos_2 . get ( ) = scheduled_pos_3 . get ( ) ;
    scheduled_pos_3 . get ( ) = shy_guts :: desired_camera_origin_new_position ;

    shy_guts :: calc_desired_camera_origin_pos ( ) ;
    shy_guts :: desired_camera_origin_is_ready = so_called_platform_math_consts :: whole_true ;
    
    shy_guts :: proceed_with_camera_update ( ) ;
}

void shy_guts :: fill_next_camera_schedule ( )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: fill_camera_schedules_index , so_called_platform_math_consts :: whole_4 ) )
    {
        shy_guts :: random_camera_origin_index ( shy_guts :: fill_schedules_origin_index ) ;
        shy_guts :: random_camera_target_index ( shy_guts :: fill_schedules_target_index ) ;
        shy_guts :: fill_schedules_origin_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: fill_schedules_target_requested = so_called_platform_math_consts :: whole_true ;

        so_called_common_logic_entities_origin_request_message origin_request_msg ;
        so_called_common_logic_entities_origin_request_message target_request_msg ;
        origin_request_msg . index = shy_guts :: fill_schedules_origin_index ;
        target_request_msg . index = shy_guts :: fill_schedules_target_index ;
        so_called_common_logic_entities_origin_request_sender :: send ( origin_request_msg ) ;
        so_called_common_logic_entities_origin_request_sender :: send ( target_request_msg ) ;
    }
    else
    {
        shy_guts :: reset_camera_rubber ( ) ;
        shy_guts :: update_camera ( ) ;
        shy_guts :: camera_created = so_called_platform_math_consts :: whole_true ;
        so_called_common_logic_camera_prepared_sender :: send ( so_called_common_logic_camera_prepared_message ( ) ) ;
    }
}

void shy_guts :: reset_camera_rubber ( )
{
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > origin_ptr ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > target_ptr ;
    so_called_platform_static_array :: element_ptr ( origin_ptr , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_static_array :: element_ptr ( target_ptr , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: current_camera_origin = origin_ptr . get ( ) ;
    shy_guts :: current_camera_target = target_ptr . get ( ) ;
}

void shy_guts :: update_camera ( )
{
    shy_guts :: update_desired_camera_origin ( ) ;
    shy_guts :: update_desired_camera_target ( ) ;
    shy_guts :: proceed_with_camera_update ( ) ;
}

void shy_guts :: update_desired_camera_origin ( )
{
    shy_guts :: desired_camera_origin_is_ready = so_called_platform_math_consts :: whole_false ;
    so_called_platform_math :: dec_whole ( shy_guts :: frames_to_change_camera_origin ) ;
    if ( so_called_platform_conditions :: whole_less_or_equal_to_zero ( shy_guts :: frames_to_change_camera_origin ) )
    {
        shy_guts :: frames_to_change_camera_origin = shy_guts :: consts :: change_origin_in_frames ;
        shy_guts :: random_camera_origin_index ( shy_guts :: desired_camera_origin_new_index ) ;
        shy_guts :: desired_camera_origin_new_requested = so_called_platform_math_consts :: whole_true ;

        so_called_common_logic_entities_origin_request_message entities_origin_request_msg ;
        entities_origin_request_msg . index = shy_guts :: desired_camera_origin_new_index ;
        so_called_common_logic_entities_origin_request_sender :: send ( entities_origin_request_msg ) ;
    }
    else
    {
        shy_guts :: calc_desired_camera_origin_pos ( ) ;
        shy_guts :: desired_camera_origin_is_ready = so_called_platform_math_consts :: whole_true ;
    }
}

void shy_guts :: update_desired_camera_target ( )
{
    shy_guts :: desired_camera_target_is_ready = so_called_platform_math_consts :: whole_false ;
    so_called_platform_math :: dec_whole ( shy_guts :: frames_to_change_camera_target ) ;
    if ( so_called_platform_conditions :: whole_less_or_equal_to_zero ( shy_guts :: frames_to_change_camera_target ) )
    {
        shy_guts :: frames_to_change_camera_target = shy_guts :: consts :: change_target_in_frames ;
        shy_guts :: random_camera_target_index ( shy_guts :: desired_camera_target_new_index ) ;
        shy_guts :: desired_camera_target_new_requested = so_called_platform_math_consts :: whole_true ;

        so_called_common_logic_entities_origin_request_message entities_origin_request_msg ;
        entities_origin_request_msg . index = shy_guts :: desired_camera_target_new_index ;
        so_called_common_logic_entities_origin_request_sender :: send ( entities_origin_request_msg ) ;
    }
    else
    {
        shy_guts :: calc_desired_camera_target_pos ( ) ;
        shy_guts :: desired_camera_target_is_ready = so_called_platform_math_consts :: whole_true ;
    }
}

void shy_guts :: update_current_camera_origin ( )
{
    so_called_platform_math_num_fract_type rubber ;
    so_called_platform_math_num_fract_type inv_rubber ;
    so_called_platform_vector_data_type old_part ;
    so_called_platform_vector_data_type new_part ;

    so_called_platform_math :: sub_fracts ( inv_rubber , so_called_platform_math_consts :: fract_1 , shy_guts :: origin_rubber ) ;
    so_called_platform_vector :: mul ( old_part , shy_guts :: current_camera_origin , shy_guts :: origin_rubber ) ;
    so_called_platform_vector :: mul ( new_part , shy_guts :: desired_camera_origin , inv_rubber ) ;
    so_called_platform_vector :: add ( shy_guts :: current_camera_origin , old_part , new_part ) ;
}

void shy_guts :: update_current_camera_target ( )
{
    so_called_platform_math_num_fract_type rubber ;
    so_called_platform_math_num_fract_type inv_rubber ;
    so_called_platform_vector_data_type old_part ;
    so_called_platform_vector_data_type new_part ;

    so_called_platform_math :: sub_fracts ( inv_rubber , so_called_platform_math_consts :: fract_1 , shy_guts :: target_rubber ) ;
    so_called_platform_vector :: mul ( old_part , shy_guts :: current_camera_target , shy_guts :: target_rubber ) ;
    so_called_platform_vector :: mul ( new_part , shy_guts :: desired_camera_target , inv_rubber ) ;
    so_called_platform_vector :: add ( shy_guts :: current_camera_target , old_part , new_part ) ;
}

void shy_guts :: update_camera_matrix ( )
{
    so_called_platform_math_num_fract_type up_x ;
    so_called_platform_math_num_fract_type up_y ;
    so_called_platform_math_num_fract_type up_z ;
    so_called_platform_math_num_fract_type shift_x ;
    so_called_platform_math_num_fract_type shift_y ;
    so_called_platform_math_num_fract_type shift_z ;
    so_called_platform_vector_data_type up ;
    so_called_platform_vector_data_type shift ;
    so_called_platform_vector_data_type shifted_origin ;
    
    up_x = so_called_platform_math_consts :: fract_0 ;
    up_y = so_called_platform_math_consts :: fract_1 ;
    up_z = so_called_platform_math_consts :: fract_0 ;
    shift_x = so_called_platform_math_consts :: fract_0 ;
    shift_y = shy_guts :: entities_height ;
    so_called_platform_math :: add_to_fract ( shift_y , shy_guts :: render_aspect_height ) ;
    so_called_platform_math :: add_to_fract ( shift_y , shy_guts :: near_plane_distance ) ;
    shift_z = so_called_platform_math_consts :: fract_0 ;
    so_called_platform_vector :: xyz ( up , up_x , up_y , up_z ) ;
    so_called_platform_vector :: xyz ( shift , shift_x , shift_y , shift_z ) ;
    so_called_platform_vector :: add ( shifted_origin , shy_guts :: current_camera_origin , shift ) ;

    so_called_common_engine_camera_stateless :: matrix_look_at ( shy_guts :: camera_matrix , shifted_origin , shy_guts :: current_camera_target , up ) ;
}

void shy_guts :: calc_desired_camera_target_pos ( )
{
    so_called_platform_math_num_fract_type fract_frames_to_change_camera_target ;
    so_called_platform_math_num_fract_type fract_change_target_in_frames ;
    so_called_platform_math_num_fract_type spline_pos ;
    so_called_platform_math :: make_fract_from_whole ( fract_frames_to_change_camera_target , shy_guts :: frames_to_change_camera_target ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_change_target_in_frames , shy_guts :: consts :: change_target_in_frames ) ;
    so_called_platform_math :: div_fracts ( spline_pos , fract_frames_to_change_camera_target , fract_change_target_in_frames ) ;
    so_called_platform_math :: neg_fract ( spline_pos ) ;
    so_called_platform_math :: add_to_fract ( spline_pos , so_called_platform_math_consts :: fract_1 ) ;
    
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_0 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_1 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_2 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_3 ;
    
    so_called_platform_static_array :: element_ptr ( pos_0 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_0 ) ;
    so_called_platform_static_array :: element_ptr ( pos_1 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_static_array :: element_ptr ( pos_2 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_static_array :: element_ptr ( pos_3 , shy_guts :: scheduled_camera_targets , so_called_platform_math_consts :: whole_3 ) ;
    
    so_called_common_engine_math_stateless :: catmull_rom_spline ( shy_guts :: desired_camera_target , spline_pos , pos_0 . get ( ) , pos_1 . get ( ) , pos_2 . get ( ) , pos_3 . get ( ) ) ;
}

void shy_guts :: calc_desired_camera_origin_pos ( )
{
    so_called_platform_math_num_fract_type fract_frames_to_change_camera_origin ;
    so_called_platform_math_num_fract_type fract_change_origin_in_frames ;
    so_called_platform_math_num_fract_type spline_pos ;
    so_called_platform_math :: make_fract_from_whole ( fract_frames_to_change_camera_origin , shy_guts :: frames_to_change_camera_origin ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_change_origin_in_frames , shy_guts :: consts :: change_origin_in_frames ) ;
    so_called_platform_math :: div_fracts ( spline_pos , fract_frames_to_change_camera_origin , fract_change_origin_in_frames ) ;
    so_called_platform_math :: neg_fract ( spline_pos ) ;
    so_called_platform_math :: add_to_fract ( spline_pos , so_called_platform_math_consts :: fract_1 ) ;

    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_0 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_1 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_2 ;
    so_called_platform_pointer_data_type < so_called_platform_vector_data_type > pos_3 ;
    
    so_called_platform_static_array :: element_ptr ( pos_0 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_0 ) ;
    so_called_platform_static_array :: element_ptr ( pos_1 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_static_array :: element_ptr ( pos_2 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_static_array :: element_ptr ( pos_3 , shy_guts :: scheduled_camera_origins , so_called_platform_math_consts :: whole_3 ) ;
    
    so_called_common_engine_math_stateless :: catmull_rom_spline ( shy_guts :: desired_camera_origin , spline_pos , pos_0 . get ( ) , pos_1 . get ( ) , pos_2 . get ( ) , pos_3 . get ( ) ) ;
}

void shy_guts :: random_camera_origin_index ( so_called_platform_math_num_whole_type & result )
{
    so_called_platform_math_num_whole_type index ;
    so_called_platform_math_num_whole_type index_max ;
    so_called_platform_math_num_whole_type is_duplicate ;

    index = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( index_max , shy_guts :: entities_mesh_grid , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: mul_whole_by ( index_max , shy_guts :: entities_mesh_grid ) ;
    do
    {
        shy_guts :: get_random_index ( index , so_called_platform_math_consts :: whole_0 , index_max ) ;
        shy_guts :: camera_origin_index_is_duplicate ( is_duplicate , index ) ;
    } while ( so_called_platform_conditions :: whole_is_true ( is_duplicate ) ) ;
    result = index ;
}

void shy_guts :: random_camera_target_index ( so_called_platform_math_num_whole_type & result )
{
    so_called_platform_math_num_whole_type index ;
    so_called_platform_math_num_whole_type index_min ;
    so_called_platform_math_num_whole_type index_max ;
    so_called_platform_math_num_whole_type is_duplicate ;

    index = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( index_min , shy_guts :: entities_mesh_grid , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: mul_whole_by ( index_min , shy_guts :: entities_mesh_grid ) ;
    so_called_platform_math :: mul_wholes ( index_max , shy_guts :: entities_mesh_grid , shy_guts :: entities_mesh_grid ) ;
    do
    {
        shy_guts :: get_random_index ( index , index_min , index_max ) ;
        shy_guts :: camera_target_index_is_duplicate ( is_duplicate , index ) ;
    } while ( so_called_platform_conditions :: whole_is_true ( is_duplicate ) ) ;
    result = index ;
}

void shy_guts :: camera_origin_index_is_duplicate ( so_called_platform_math_num_whole_type & result , so_called_platform_math_num_whole_type index )
{
    result = so_called_platform_math_consts :: whole_false ;
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0 
        ; so_called_platform_conditions :: whole_less_than_whole ( i , so_called_platform_math_consts :: whole_4 ) 
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index ;
        so_called_platform_static_array :: element_ptr ( scheduled_index , shy_guts :: scheduled_camera_origin_indices , i ) ;
        if ( so_called_platform_conditions :: wholes_are_equal ( scheduled_index . get ( ) , index ) )
        {
            result = so_called_platform_math_consts :: whole_true ;
            break ;
        }
    }
}

void shy_guts :: camera_target_index_is_duplicate ( so_called_platform_math_num_whole_type & result , so_called_platform_math_num_whole_type index )
{
    result = so_called_platform_math_consts :: whole_false ;
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0 
        ; so_called_platform_conditions :: whole_less_than_whole ( i , so_called_platform_math_consts :: whole_4 ) 
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_index ;
        so_called_platform_static_array :: element_ptr ( scheduled_index , shy_guts :: scheduled_camera_target_indices , i ) ;
        if ( so_called_platform_conditions :: wholes_are_equal ( scheduled_index . get ( ) , index ) )
        {
            result = so_called_platform_math_consts :: whole_true ;
            break ;
        }
    }
}

void shy_guts :: get_random_index
    ( so_called_platform_math_num_whole_type & result
    , so_called_platform_math_num_whole_type index_min
    , so_called_platform_math_num_whole_type index_max
    )
{
    so_called_platform_math_num_whole_type index_diff ;
    so_called_platform_math :: add_to_whole ( shy_guts :: random_seed , shy_guts :: consts :: random_const_1 ) ;
    so_called_platform_math :: mod_whole_by ( shy_guts :: random_seed , shy_guts :: consts :: random_const_2 ) ;
    so_called_platform_math :: sub_wholes ( index_diff , index_max , index_min ) ;
    so_called_platform_math :: mod_wholes ( result , shy_guts :: random_seed , index_diff ) ;
    so_called_platform_math :: add_to_whole ( result , index_min ) ;
}

void _shy_common_logic_camera :: receive ( so_called_common_engine_render_aspect_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_aspect_requested ) )
    {
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_aspect_height = msg . height ;
        shy_guts :: update_camera_matrix ( ) ;
    }
}

void _shy_common_logic_camera :: receive ( so_called_common_init_message )
{
    shy_guts :: origin_rubber = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: target_rubber = so_called_platform_math_consts :: fract_0 ;
    
    shy_guts :: camera_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: camera_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: desired_camera_origin_is_ready = so_called_platform_math_consts :: whole_false ;
    shy_guts :: desired_camera_target_is_ready = so_called_platform_math_consts :: whole_false ;
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
    
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , so_called_platform_math_consts :: whole_4 )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_vector_data_type origin_pos ;
        so_called_platform_vector_data_type target_pos ;
        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_origin_index ;
        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > scheduled_target_index ;
        so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_origin_pos ;
        so_called_platform_pointer_data_type < so_called_platform_vector_data_type > scheduled_target_pos ;
    
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

void _shy_common_logic_camera :: receive ( so_called_common_logic_camera_matrix_request_message )
{
    so_called_common_logic_camera_matrix_reply_message reply_msg ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: camera_created ) )
        reply_msg . matrix = shy_guts :: camera_matrix ;
    else
        so_called_platform_matrix :: identity ( reply_msg . matrix ) ;
    so_called_common_logic_camera_matrix_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_camera :: receive ( so_called_common_logic_camera_prepare_permit_message )
{
    shy_guts :: camera_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_camera :: receive ( so_called_common_logic_camera_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: camera_prepare_permitted ) )
    {
        shy_guts :: entities_height_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: entities_mesh_grid_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: near_plane_distance_requested = so_called_platform_math_consts :: whole_true ;
        so_called_common_logic_entities_height_request_sender :: send ( so_called_common_logic_entities_height_request_message ( ) ) ;
        so_called_common_logic_entities_mesh_grid_request_sender :: send ( so_called_common_logic_entities_mesh_grid_request_message ( ) ) ;
        so_called_common_logic_core_near_plane_distance_request_sender :: send ( so_called_common_logic_core_near_plane_distance_request_message ( ) ) ;
    }
}

void _shy_common_logic_camera :: receive ( so_called_common_logic_core_near_plane_distance_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: near_plane_distance_requested ) )
    {
        shy_guts :: near_plane_distance_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: near_plane_distance_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: near_plane_distance = msg . distance ;
        shy_guts :: proceed_with_update ( ) ;
    }
}

void _shy_common_logic_camera :: receive ( so_called_common_logic_entities_height_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entities_height_requested ) )
    {
        shy_guts :: entities_height_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: entities_height_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: entities_height = msg . height ;
        shy_guts :: proceed_with_update ( ) ;
    }
}

void _shy_common_logic_camera :: receive ( so_called_common_logic_entities_mesh_grid_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entities_mesh_grid_requested ) )
    {
        shy_guts :: entities_mesh_grid_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: entities_mesh_grid_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: entities_mesh_grid = msg . grid ;
        shy_guts :: proceed_with_update ( ) ;
    }
}

void _shy_common_logic_camera :: receive ( so_called_common_logic_entities_origin_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fill_schedules_origin_requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: fill_schedules_origin_index , msg . index )
       )
    {
        shy_guts :: fill_schedules_origin_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fill_schedules_origin_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: fill_schedules_origin = msg . origin ;
        shy_guts :: proceed_with_fill_camera_schedules ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fill_schedules_target_requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: fill_schedules_target_index , msg . index )
       )
    {
        shy_guts :: fill_schedules_target_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fill_schedules_target_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: fill_schedules_target = msg . origin ;
        shy_guts :: proceed_with_fill_camera_schedules ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: desired_camera_origin_new_requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: desired_camera_origin_new_index , msg . index )
       )
    {
        shy_guts :: desired_camera_origin_new_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: desired_camera_origin_new_position = msg . origin ;
        shy_guts :: proceed_with_update_desired_camera_origin ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: desired_camera_target_new_requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: desired_camera_target_new_index , msg . index )
       )
    {
        shy_guts :: desired_camera_target_new_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: desired_camera_target_new_position = msg . origin ;
        shy_guts :: proceed_with_update_desired_camera_target ( ) ;
    }
}

void _shy_common_logic_camera :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
