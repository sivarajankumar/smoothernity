namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_whole never = so_called_platform_math :: init_num_whole ( 9999 ) ;
        static so_called_type_platform_math_const_int_32 max_letters = 32 ;
    }
    
    class letter_state
    {
    public :
        so_called_type_platform_math_num_fract pos_radius ;
        so_called_type_platform_math_num_fract pos_angle ;
        so_called_type_platform_math_num_fract rot_angle ;
        so_called_type_platform_math_num_fract scale ;
        so_called_type_common_engine_render_mesh_id mesh ;
        so_called_type_common_logic_text_letter_id letter ;
    } ;

    static void title_create ( ) ;
    static void title_render ( ) ;
    static void title_update ( ) ;
    static void delete_all_meshes ( ) ;
    static void prepare_to_appear ( ) ;
    static void prepare_to_disappear ( ) ;
    static void animate_appear ( ) ;
    static void animate_disappear ( ) ;
    static void animate_lifecycle ( ) ;
    static void bake_next_letter ( ) ;
    static void proceed_with_render ( ) ;
    static void proceed_with_letter_creation ( ) ;
    static void add_letter 
        ( so_called_type_common_logic_text_letter_id 
        ) ;
    static void mesh_set_triangle_strip_index_value 
        ( so_called_type_common_engine_render_mesh_id mesh
        , so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_whole index 
        ) ;
    static void mesh_set_vertex_tex_coord 
        ( so_called_type_common_engine_render_mesh_id mesh 
        , so_called_type_platform_math_num_whole offset 
        , so_called_type_platform_math_num_fract u 
        , so_called_type_platform_math_num_fract v 
        ) ;
    static void mesh_set_vertex_position 
        ( so_called_type_common_engine_render_mesh_id mesh
        , so_called_type_platform_math_num_whole offset 
        , so_called_type_platform_math_num_fract x 
        , so_called_type_platform_math_num_fract y 
        , so_called_type_platform_math_num_fract z 
        ) ;
    static void mesh_set_vertex_color 
        ( so_called_type_common_engine_render_mesh_id mesh
        , so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract r
        , so_called_type_platform_math_num_fract g
        , so_called_type_platform_math_num_fract b
        , so_called_type_platform_math_num_fract a
        ) ;

    static so_called_type_platform_static_array_data < shy_guts :: letter_state , shy_guts :: consts :: max_letters > letters ;

    static so_called_type_platform_math_num_whole title_launch_permitted ;
    static so_called_type_platform_math_num_whole title_created ;
    static so_called_type_platform_math_num_whole title_finished ;
    static so_called_type_platform_math_num_whole title_frames ;
    static so_called_type_platform_math_num_whole title_appeared ;
    static so_called_type_platform_math_num_whole letters_count ;
    static so_called_type_platform_math_num_whole disappear_at_frames ;
    static so_called_type_platform_math_num_whole bake_letter_index ;

    static so_called_type_platform_math_num_whole render_started ;
    
    static so_called_type_platform_math_num_whole mesh_create_requested ;
    static so_called_type_platform_math_num_whole mesh_create_replied ;
    
    static so_called_type_platform_math_num_whole use_ortho_projection_requested ;
    static so_called_type_platform_math_num_whole use_ortho_projection_replied ;
    
    static so_called_type_platform_math_num_whole fidget_render_requested ;
    static so_called_type_platform_math_num_whole fidget_render_replied ;

    static so_called_type_platform_math_num_whole use_text_texture_requested ;
    static so_called_type_platform_math_num_whole use_text_texture_replied ;
    
    static so_called_type_platform_math_num_whole text_letter_big_tex_coords_requested ;
    static so_called_type_platform_math_num_whole text_letter_big_tex_coords_replied ;
    static so_called_type_common_logic_text_letter_id text_letter_big_tex_coords_letter ;
    
    static so_called_type_platform_math_num_whole render_aspect_requested ;
    static so_called_type_platform_math_num_fract render_aspect_width ;
    
    static so_called_type_platform_math_num_fract tex_coords_left ;
    static so_called_type_platform_math_num_fract tex_coords_right ;
    static so_called_type_platform_math_num_fract tex_coords_bottom ;
    static so_called_type_platform_math_num_fract tex_coords_top ;
    
    static so_called_type_platform_math_num_fract desired_pos_radius_coeff ;
    static so_called_type_platform_math_num_fract desired_pos_angle ;
    static so_called_type_platform_math_num_fract desired_rot_angle ;
    static so_called_type_platform_math_num_fract desired_scale ;
    static so_called_type_platform_math_num_fract scene_scale ;
    static so_called_type_platform_math_num_fract scene_scale_frames ;
    static so_called_type_platform_math_num_fract rubber_first ;
    static so_called_type_platform_math_num_fract rubber_last ;
} 
  
typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_title > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: title_create ( )
{
    typedef so_called_common_logic_text_consts :: alphabet_english eng ;
    shy_guts :: add_letter ( eng :: S ) ;
    shy_guts :: add_letter ( eng :: M ) ;
    shy_guts :: add_letter ( eng :: O ) ;
    shy_guts :: add_letter ( eng :: O ) ;
    shy_guts :: add_letter ( eng :: T ) ;
    shy_guts :: add_letter ( eng :: H ) ;
    shy_guts :: add_letter ( eng :: E ) ;
    shy_guts :: add_letter ( eng :: R ) ;
    shy_guts :: add_letter ( eng :: N ) ;
    shy_guts :: add_letter ( eng :: I ) ;
    shy_guts :: add_letter ( eng :: T ) ;
    shy_guts :: add_letter ( eng :: Y ) ;
    shy_guts :: bake_next_letter ( ) ;
}

void shy_guts :: title_render ( )
{
    so_called_type_platform_matrix_data scene_tm ;

    so_called_platform_matrix :: set_axis_x ( scene_tm , shy_guts :: scene_scale , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_y ( scene_tm , so_called_platform_math_consts :: fract_0 , shy_guts :: scene_scale , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_z ( scene_tm , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_1 ) ;
    so_called_platform_matrix :: set_origin ( scene_tm , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    
    so_called_sender_common_engine_render_blend_src_alpha_dst_one_minus_alpha :: send ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha ( ) ) ;
    
    so_called_message_common_engine_render_matrix_load matrix_load_msg ;
    matrix_load_msg . matrix = scene_tm ;
    so_called_sender_common_engine_render_matrix_load :: send ( matrix_load_msg ) ;
    
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: letters_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_pointer_data < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , i ) ;
        so_called_message_common_engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = letter . get ( ) . mesh ;
        so_called_sender_common_engine_render_mesh_render :: send ( mesh_render_msg ) ;
    }
    so_called_sender_common_engine_render_blend_disable :: send ( so_called_message_common_engine_render_blend_disable ( ) ) ;
}

void shy_guts :: title_update ( )
{
    so_called_type_platform_math_num_fract fract_letters_count ;
    so_called_type_platform_math_num_fract letter_size ;
    so_called_type_platform_math_num_fract desired_pos_radius ;
    so_called_type_platform_math_num_fract offset_y ;
    so_called_type_platform_math_num_fract fract_appear_duration_in_frames ;
    
    so_called_platform_math :: make_fract_from_whole ( fract_letters_count , shy_guts :: letters_count ) ;
    so_called_platform_math :: div_fracts ( letter_size , shy_guts :: render_aspect_width , fract_letters_count ) ;    
    so_called_platform_math :: mul_fracts ( desired_pos_radius , letter_size , shy_guts :: desired_pos_radius_coeff ) ;
    offset_y = so_called_common_logic_title_consts :: spin_radius_in_letters ;
    so_called_platform_math :: mul_fract_by ( offset_y , letter_size ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_appear_duration_in_frames , so_called_common_logic_title_consts :: appear_duration_in_frames ) ;

    so_called_common_engine_math_stateless :: lerp 
        ( shy_guts :: scene_scale 
        , shy_guts :: scene_scale_frames
        , so_called_common_logic_title_consts :: scene_scale_min
        , so_called_platform_math_consts :: fract_0 
        , so_called_common_logic_title_consts :: scene_scale_max 
        , fract_appear_duration_in_frames
        ) ;
    so_called_platform_math :: add_to_fract ( shy_guts :: scene_scale_frames , so_called_platform_math_consts :: fract_1 ) ;
                    
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: letters_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_math_num_fract offset_x ;
        so_called_type_platform_math_num_fract fract_i ;
        so_called_type_platform_math_num_fract rot_cos ;
        so_called_type_platform_math_num_fract rot_sin ;
        so_called_type_platform_math_num_fract rot_neg_sin ;
        so_called_type_platform_math_num_fract pos_cos ;
        so_called_type_platform_math_num_fract pos_sin ;
        so_called_type_platform_math_num_fract pos_neg_sin ;
        so_called_type_platform_math_num_fract rubber ;
        so_called_type_platform_math_num_fract pos_radius_old_part ;
        so_called_type_platform_math_num_fract pos_radius_new_part ;
        so_called_type_platform_math_num_fract pos_angle_old_part ;
        so_called_type_platform_math_num_fract pos_angle_new_part ;
        so_called_type_platform_math_num_fract rot_angle_old_part ;
        so_called_type_platform_math_num_fract rot_angle_new_part ;
        so_called_type_platform_math_num_fract scale_old_part ;
        so_called_type_platform_math_num_fract scale_new_part ;
        so_called_type_platform_math_num_whole starting_frame ;
        so_called_type_platform_math_num_whole finishing_frame ;
        so_called_type_platform_vector_data axis_x ;
        so_called_type_platform_vector_data axis_y ;
        so_called_type_platform_vector_data origin ;
        so_called_type_platform_vector_data offset ;
        so_called_type_platform_vector_data pos ;
        so_called_type_platform_matrix_data tm ;
        so_called_type_platform_pointer_data < shy_guts :: letter_state > letter ;
        
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , i ) ;
        
        so_called_platform_math :: make_fract_from_whole ( fract_i , i ) ;
        so_called_platform_math :: mul_fracts ( offset_x , shy_guts :: render_aspect_width , so_called_platform_math_consts :: fract_2 ) ;
        so_called_platform_math :: mul_fract_by ( offset_x , fract_i ) ;
        so_called_platform_math :: div_fract_by ( offset_x , fract_letters_count ) ;
        so_called_platform_math :: sub_from_fract ( offset_x , shy_guts :: render_aspect_width ) ;
        so_called_platform_math :: add_to_fract ( offset_x , letter_size ) ;
        so_called_platform_vector :: xyz ( offset , offset_x , offset_y , so_called_platform_math_consts :: fract_minus_3 ) ;        
        
        so_called_platform_math :: mul_wholes ( starting_frame , so_called_common_logic_title_consts :: frames_between_letters , i ) ;
        so_called_platform_math :: sub_wholes ( finishing_frame , shy_guts :: disappear_at_frames , starting_frame ) ;
        if ( so_called_platform_conditions :: whole_greater_than_whole ( shy_guts :: title_frames , starting_frame ) )
        {
            so_called_common_engine_math_stateless :: lerp ( rubber , fract_i , shy_guts :: rubber_first , so_called_platform_math_consts :: fract_0 , shy_guts :: rubber_last , fract_letters_count ) ;
            
            so_called_platform_math :: mul_fracts ( pos_angle_old_part , letter . get ( ) . pos_angle , rubber ) ;
            so_called_platform_math :: sub_fracts ( pos_angle_new_part , so_called_platform_math_consts :: fract_1 , rubber ) ;
            so_called_platform_math :: mul_fract_by ( pos_angle_new_part , shy_guts :: desired_pos_angle ) ;
            so_called_platform_math :: add_fracts ( letter . get ( ) . pos_angle , pos_angle_old_part , pos_angle_new_part ) ;
            
            so_called_platform_math :: mul_fracts ( pos_radius_old_part , letter . get ( ) . pos_radius , rubber ) ;
            so_called_platform_math :: sub_fracts ( pos_radius_new_part , so_called_platform_math_consts :: fract_1 , rubber ) ;
            so_called_platform_math :: mul_fract_by ( pos_radius_new_part , desired_pos_radius ) ;
            so_called_platform_math :: add_fracts ( letter . get ( ) . pos_radius , pos_radius_old_part , pos_radius_new_part ) ;
            
            so_called_platform_math :: mul_fracts ( rot_angle_old_part , letter . get ( ) . rot_angle , rubber ) ;
            so_called_platform_math :: sub_fracts ( rot_angle_new_part , so_called_platform_math_consts :: fract_1 , rubber ) ;
            so_called_platform_math :: mul_fract_by ( rot_angle_new_part , shy_guts :: desired_rot_angle ) ;
            so_called_platform_math :: add_fracts ( letter . get ( ) . rot_angle , rot_angle_old_part , rot_angle_new_part ) ;
            
            so_called_platform_math :: mul_fracts ( scale_old_part , letter . get ( ) . scale , rubber ) ;
            so_called_platform_math :: sub_fracts ( scale_new_part , so_called_platform_math_consts :: fract_1 , rubber ) ;
            so_called_platform_math :: mul_fract_by ( scale_new_part , shy_guts :: desired_scale ) ;
            so_called_platform_math :: add_fracts ( letter . get ( ) . scale , scale_old_part , scale_new_part ) ;
        }
        
        so_called_platform_math :: sin ( rot_sin , letter . get ( ) . rot_angle ) ;
        so_called_platform_math :: cos ( rot_cos , letter . get ( ) . rot_angle ) ;
        so_called_platform_math :: neg_fract ( rot_neg_sin , rot_sin ) ;
        
        so_called_platform_math :: sin ( pos_sin , letter . get ( ) . pos_angle ) ;
        so_called_platform_math :: cos ( pos_cos , letter . get ( ) . pos_angle ) ;
        so_called_platform_math :: neg_fract ( pos_neg_sin , pos_sin ) ;
        
        so_called_platform_vector :: xyz ( pos , pos_cos , pos_sin , so_called_platform_math_consts :: fract_0 ) ;
        so_called_platform_vector :: mul_by ( pos , letter . get ( ) . pos_radius ) ;
        
        if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: title_frames , finishing_frame ) )
        {
            so_called_platform_vector :: xyz ( axis_x , rot_cos , rot_sin , so_called_platform_math_consts :: fract_0 ) ;
            so_called_platform_vector :: xyz ( axis_y , rot_neg_sin , rot_cos , so_called_platform_math_consts :: fract_0 ) ;
            so_called_platform_vector :: mul_by ( axis_x , letter . get ( ) . scale ) ;
            so_called_platform_vector :: mul_by ( axis_y , letter . get ( ) . scale ) ;
            so_called_platform_vector :: mul_by ( axis_x , letter_size ) ;
            so_called_platform_vector :: mul_by ( axis_y , letter_size ) ;
        }
        else
        {
            so_called_platform_vector :: xyz ( axis_x , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
            so_called_platform_vector :: xyz ( axis_y , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
        }
        
        so_called_platform_vector :: add ( origin , pos , offset ) ;
        
        so_called_platform_matrix :: set_axis_x ( tm , axis_x ) ;
        so_called_platform_matrix :: set_axis_y ( tm , axis_y ) ;
        so_called_platform_matrix :: set_axis_z ( tm , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_1 ) ;
        so_called_platform_matrix :: set_origin ( tm , origin ) ;
        
        {
            so_called_message_common_engine_render_mesh_set_transform mesh_set_transform_msg ;
            mesh_set_transform_msg . mesh = letter . get ( ) . mesh ;
            mesh_set_transform_msg . transform = tm ;
            so_called_sender_common_engine_render_mesh_set_transform :: send ( mesh_set_transform_msg ) ;
        }
    }
}

void shy_guts :: delete_all_meshes ( )
{
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: letters_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_pointer_data < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , i ) ;
        so_called_message_common_engine_render_mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = letter . get ( ) . mesh ;
        so_called_sender_common_engine_render_mesh_delete :: send ( mesh_delete_msg ) ;
    }
}

void shy_guts :: prepare_to_appear ( )
{
    shy_guts :: desired_pos_angle = so_called_common_logic_title_consts :: appear_pos_angle_periods ;
    so_called_platform_math :: mul_fract_by ( shy_guts :: desired_pos_angle , so_called_platform_math_consts :: fract_pi ) ;
    so_called_platform_math :: mul_fracts ( shy_guts :: desired_rot_angle , so_called_platform_math_consts :: fract_2pi , so_called_platform_math_consts :: fract_3 ) ;
    shy_guts :: rubber_first = so_called_common_logic_title_consts :: appear_rubber_first ;
    shy_guts :: rubber_last = so_called_common_logic_title_consts :: appear_rubber_last ;
    shy_guts :: disappear_at_frames = shy_guts :: consts :: never ;
    shy_guts :: desired_scale = so_called_platform_math_consts :: fract_1 ;    
    shy_guts :: desired_pos_radius_coeff = so_called_common_logic_title_consts :: spin_radius_in_letters ;
}

void shy_guts :: prepare_to_disappear ( )
{
    shy_guts :: desired_pos_radius_coeff = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: desired_pos_angle = so_called_common_logic_title_consts :: disappear_pos_angle_periods ;
    so_called_platform_math :: mul_fract_by ( shy_guts :: desired_pos_angle , so_called_platform_math_consts :: fract_pi ) ;
    so_called_platform_math :: mul_fracts ( shy_guts :: desired_rot_angle , so_called_platform_math_consts :: fract_2pi , so_called_platform_math_consts :: fract_6 ) ;
    shy_guts :: rubber_first = so_called_common_logic_title_consts :: disappear_rubber_first ;
    shy_guts :: rubber_last = so_called_common_logic_title_consts :: disappear_rubber_last ;
    shy_guts :: desired_scale = so_called_platform_math_consts :: fract_0 ;    
    shy_guts :: title_appeared = so_called_platform_math_consts :: whole_true ;
    shy_guts :: disappear_at_frames = so_called_common_logic_title_consts :: disappear_duration_in_frames ;
}

void shy_guts :: animate_appear ( )
{
    so_called_platform_math :: inc_whole ( shy_guts :: title_frames ) ;
    if ( so_called_platform_conditions :: whole_greater_than_whole ( shy_guts :: title_frames , so_called_common_logic_title_consts :: appear_duration_in_frames ) )
    {
        shy_guts :: title_frames = so_called_platform_math_consts :: whole_0 ;
        shy_guts :: prepare_to_disappear ( ) ;
    }
    else
        shy_guts :: title_update ( ) ;
}

void shy_guts :: animate_disappear ( )
{
    so_called_platform_math :: inc_whole ( shy_guts :: title_frames ) ;
    if ( so_called_platform_conditions :: whole_greater_than_whole ( shy_guts :: title_frames , so_called_common_logic_title_consts :: disappear_duration_in_frames ) )
    {
        shy_guts :: title_finished = so_called_platform_math_consts :: whole_true ;
        shy_guts :: delete_all_meshes ( ) ;
        so_called_sender_common_logic_title_finished :: send ( so_called_message_common_logic_title_finished ( ) ) ;
    }
    else
        shy_guts :: title_update ( ) ;
}

void shy_guts :: animate_lifecycle ( )
{
    if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: title_appeared ) )
        shy_guts :: animate_appear ( ) ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: title_appeared ) )
        shy_guts :: animate_disappear ( ) ;
}

void shy_guts :: bake_next_letter ( )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: bake_letter_index , shy_guts :: letters_count ) )
    {
        so_called_type_platform_pointer_data < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , shy_guts :: bake_letter_index ) ;
        
        letter . get ( ) . scale = so_called_platform_math_consts :: fract_0 ;
        letter . get ( ) . pos_radius = so_called_platform_math_consts :: fract_0 ;
        letter . get ( ) . pos_angle = so_called_platform_math_consts :: fract_0 ;
        letter . get ( ) . rot_angle = so_called_platform_math_consts :: fract_0 ;
        
        shy_guts :: text_letter_big_tex_coords_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: text_letter_big_tex_coords_letter = letter . get ( ) . letter ;
        
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
        
        so_called_message_common_logic_text_letter_big_tex_coords_request text_letter_big_tex_coords_request_msg ;
        text_letter_big_tex_coords_request_msg . letter = letter . get ( ) . letter ;
        so_called_sender_common_logic_text_letter_big_tex_coords_request :: send ( text_letter_big_tex_coords_request_msg  ) ;        
        
        so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
        mesh_create_msg . vertices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
        so_called_sender_common_engine_render_mesh_create_request :: send ( mesh_create_msg ) ;
    }
    else
    {
        shy_guts :: title_created = so_called_platform_math_consts :: whole_true ;
        shy_guts :: prepare_to_appear ( ) ;
        shy_guts :: animate_lifecycle ( ) ;
        so_called_sender_common_logic_title_created :: send ( so_called_message_common_logic_title_created ( ) ) ;
    }
}

void shy_guts :: proceed_with_render ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_started ) )
    {
        shy_guts :: render_started = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_core_use_ortho_projection_request :: send ( so_called_message_common_logic_core_use_ortho_projection_request ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_ortho_projection_replied ) )
    {
        shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_false ;
        so_called_message_common_engine_render_clear_screen clear_screen_msg ;
        clear_screen_msg . r = so_called_platform_math_consts :: fract_0 ;
        clear_screen_msg . g = so_called_platform_math_consts :: fract_0 ;
        clear_screen_msg . b = so_called_platform_math_consts :: fract_0 ;
        so_called_sender_common_engine_render_clear_screen :: send ( clear_screen_msg ) ;
        so_called_sender_common_engine_render_disable_depth_test :: send ( so_called_message_common_engine_render_disable_depth_test ( ) ) ;
        so_called_sender_common_engine_render_fog_disable :: send ( so_called_message_common_engine_render_fog_disable ( ) ) ;

        shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_fidget_render_request :: send ( so_called_message_common_logic_fidget_render_request ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_render_replied ) )
    {
        shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_false ;
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: title_created ) && so_called_platform_conditions :: whole_is_false ( shy_guts :: title_finished ) )
        {
            shy_guts :: use_text_texture_requested = so_called_platform_math_consts :: whole_true ;
            so_called_sender_common_logic_text_use_text_texture_request :: send ( so_called_message_common_logic_text_use_text_texture_request ( ) ) ;
        }
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_text_texture_replied ) )
    {
        shy_guts :: use_text_texture_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: title_render ( ) ;
    }
}

void shy_guts :: proceed_with_letter_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: text_letter_big_tex_coords_replied )
       )
    {
        shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: text_letter_big_tex_coords_replied = so_called_platform_math_consts :: whole_false ;
                
        so_called_type_platform_math_num_fract title_r = so_called_platform_math_consts :: fract_0 ;
        so_called_type_platform_math_num_fract title_g = so_called_platform_math_consts :: fract_1 ;
        so_called_type_platform_math_num_fract title_b = so_called_platform_math_consts :: fract_0 ;
        so_called_type_platform_math_num_fract title_a = so_called_platform_math_consts :: fract_1 ;
        so_called_type_platform_math_num_fract x_left = so_called_platform_math_consts :: fract_minus_1 ;
        so_called_type_platform_math_num_fract x_right = so_called_platform_math_consts :: fract_1 ;
        so_called_type_platform_math_num_fract y_bottom = so_called_platform_math_consts :: fract_minus_1 ;
        so_called_type_platform_math_num_fract y_top = so_called_platform_math_consts :: fract_1 ;
        so_called_type_platform_math_num_fract z = so_called_platform_math_consts :: fract_0 ;
        
        so_called_type_platform_pointer_data < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , shy_guts :: bake_letter_index ) ;
        
        shy_guts :: mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 ) ;
        shy_guts :: mesh_set_vertex_color               ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_0 , title_r , title_g , title_b , title_a ) ;
        shy_guts :: mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_0 , shy_guts :: tex_coords_left , shy_guts :: tex_coords_top ) ;
        shy_guts :: mesh_set_vertex_position            ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_0 , x_left , y_top , z ) ;
        
        shy_guts :: mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_1 , so_called_platform_math_consts :: whole_1 ) ;
        shy_guts :: mesh_set_vertex_color               ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_1 , title_r , title_g , title_b , title_a ) ;
        shy_guts :: mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_1 , shy_guts :: tex_coords_left , shy_guts :: tex_coords_bottom ) ;
        shy_guts :: mesh_set_vertex_position            ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_1 , x_left , y_bottom , z ) ;
        
        shy_guts :: mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_2 , so_called_platform_math_consts :: whole_2 ) ;
        shy_guts :: mesh_set_vertex_color               ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_2 , title_r , title_g , title_b , title_a ) ;
        shy_guts :: mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_2 , shy_guts :: tex_coords_right , shy_guts :: tex_coords_top ) ;
        shy_guts :: mesh_set_vertex_position            ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_2 , x_right , y_top , z ) ;
        
        shy_guts :: mesh_set_triangle_strip_index_value ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_3 , so_called_platform_math_consts :: whole_3 ) ;
        shy_guts :: mesh_set_vertex_color               ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_3 , title_r , title_g , title_b , title_a ) ;
        shy_guts :: mesh_set_vertex_tex_coord           ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_3 , shy_guts :: tex_coords_right , shy_guts :: tex_coords_bottom ) ;
        shy_guts :: mesh_set_vertex_position            ( letter . get ( ) . mesh , so_called_platform_math_consts :: whole_3 , x_right , y_bottom , z ) ;
        
        so_called_message_common_engine_render_mesh_finalize mesh_finalize_msg ;
        mesh_finalize_msg . mesh = letter . get ( ) . mesh ;
        so_called_sender_common_engine_render_mesh_finalize :: send ( mesh_finalize_msg ) ;
        
        so_called_platform_math :: inc_whole ( shy_guts :: bake_letter_index ) ;
        shy_guts :: bake_next_letter ( ) ;
    }
}

void shy_guts :: add_letter ( so_called_type_common_logic_text_letter_id letter )
{
    so_called_type_platform_pointer_data < shy_guts :: letter_state > letter_state ;
    so_called_platform_static_array :: element_ptr ( letter_state , shy_guts :: letters , shy_guts :: letters_count ) ;
    letter_state . get ( ) . letter = letter ;
    so_called_platform_math :: inc_whole ( shy_guts :: letters_count ) ;
}

void shy_guts :: mesh_set_triangle_strip_index_value 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index 
    )
{
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_type_common_engine_render_mesh_id mesh 
    , so_called_type_platform_math_num_whole offset 
    , so_called_type_platform_math_num_fract u 
    , so_called_type_platform_math_num_fract v 
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_sender_common_engine_render_mesh_set_vertex_tex_coord :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_position msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_sender_common_engine_render_mesh_set_vertex_position :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_color 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract r
    , so_called_type_platform_math_num_fract g
    , so_called_type_platform_math_num_fract b
    , so_called_type_platform_math_num_fract a
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_color msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_sender_common_engine_render_mesh_set_vertex_color :: send ( msg ) ;
}

void _shy_common_logic_title :: receive ( so_called_message_common_engine_render_aspect_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_aspect_requested ) )
    {
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_aspect_width = msg . width ;
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: title_created ) )
            shy_guts :: title_create ( ) ;
        else if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: title_finished ) )
            shy_guts :: animate_lifecycle ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_true ;
        so_called_type_platform_pointer_data < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , shy_guts :: bake_letter_index ) ;
        letter . get ( ) . mesh = msg . mesh ;
        shy_guts :: proceed_with_letter_creation ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_message_common_init )
{
    shy_guts :: title_launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: title_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: title_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: title_appeared = so_called_platform_math_consts :: whole_false ;
    shy_guts :: disappear_at_frames = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: scene_scale = so_called_platform_math_consts :: fract_1 ;
    shy_guts :: scene_scale_frames = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: letters_count = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: title_frames = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: bake_letter_index = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: text_letter_big_tex_coords_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: text_letter_big_tex_coords_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_false;
    shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_text_texture_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: use_text_texture_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_started = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_core_use_ortho_projection_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_ortho_projection_requested ) )
    {
        shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_fidget_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_render_requested ) )
    {
        shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_text_letter_big_tex_coords_reply msg )
{
    so_called_type_platform_math_num_whole letters_are_equal ;
    so_called_common_logic_text_stateless :: are_letters_equal ( letters_are_equal , shy_guts :: text_letter_big_tex_coords_letter , msg . letter ) ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_letter_big_tex_coords_requested ) 
      && so_called_platform_conditions :: whole_is_true ( letters_are_equal )
       )
    {
        shy_guts :: text_letter_big_tex_coords_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: text_letter_big_tex_coords_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: tex_coords_left = msg . left ;
        shy_guts :: tex_coords_right = msg . right ;
        shy_guts :: tex_coords_bottom = msg . bottom ;
        shy_guts :: tex_coords_top = msg . top ;
        shy_guts :: proceed_with_letter_creation ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_text_use_text_texture_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_text_texture_requested ) )
    {
        shy_guts :: use_text_texture_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_text_texture_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_title_launch_permit )
{
    shy_guts :: title_launch_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_title_render )
{
    shy_guts :: render_started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_render ( ) ;
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_title_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: title_launch_permitted ) )
    {
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_engine_render_aspect_request :: send ( so_called_message_common_engine_render_aspect_request ( ) ) ;
    }
}
