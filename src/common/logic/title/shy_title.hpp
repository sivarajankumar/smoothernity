namespace shy_guts
{
    namespace consts
    {
        static const so_called_platform_math_num_whole_type never = so_called_platform_math :: init_num_whole ( 9999 ) ;
        static so_called_platform_math_const_int_32_type max_letters = 32 ;
    }
    
    class letter_state
    {
    public :
        so_called_platform_math_num_fract_type pos_radius ;
        so_called_platform_math_num_fract_type pos_angle ;
        so_called_platform_math_num_fract_type rot_angle ;
        so_called_platform_math_num_fract_type scale ;
        so_called_common_engine_render_mesh_id_type mesh ;
        so_called_common_logic_text_letter_id_type letter ;
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
        ( so_called_common_logic_text_letter_id_type 
        ) ;
    static void mesh_set_triangle_strip_index_value 
        ( so_called_common_engine_render_mesh_id_type mesh
        , so_called_platform_math_num_whole_type offset
        , so_called_platform_math_num_whole_type index 
        ) ;
    static void mesh_set_vertex_tex_coord 
        ( so_called_common_engine_render_mesh_id_type mesh 
        , so_called_platform_math_num_whole_type offset 
        , so_called_platform_math_num_fract_type u 
        , so_called_platform_math_num_fract_type v 
        ) ;
    static void mesh_set_vertex_position 
        ( so_called_common_engine_render_mesh_id_type mesh
        , so_called_platform_math_num_whole_type offset 
        , so_called_platform_math_num_fract_type x 
        , so_called_platform_math_num_fract_type y 
        , so_called_platform_math_num_fract_type z 
        ) ;
    static void mesh_set_vertex_color 
        ( so_called_common_engine_render_mesh_id_type mesh
        , so_called_platform_math_num_whole_type offset
        , so_called_platform_math_num_fract_type r
        , so_called_platform_math_num_fract_type g
        , so_called_platform_math_num_fract_type b
        , so_called_platform_math_num_fract_type a
        ) ;

    static so_called_platform_static_array_data_type < shy_guts :: letter_state , shy_guts :: consts :: max_letters > letters ;

    static so_called_platform_math_num_whole_type title_launch_permitted ;
    static so_called_platform_math_num_whole_type title_created ;
    static so_called_platform_math_num_whole_type title_finished ;
    static so_called_platform_math_num_whole_type title_frames ;
    static so_called_platform_math_num_whole_type title_appeared ;
    static so_called_platform_math_num_whole_type letters_count ;
    static so_called_platform_math_num_whole_type disappear_at_frames ;
    static so_called_platform_math_num_whole_type bake_letter_index ;

    static so_called_platform_math_num_whole_type render_started ;
    
    static so_called_platform_math_num_whole_type mesh_create_requested ;
    static so_called_platform_math_num_whole_type mesh_create_replied ;
    
    static so_called_platform_math_num_whole_type use_ortho_projection_requested ;
    static so_called_platform_math_num_whole_type use_ortho_projection_replied ;
    
    static so_called_platform_math_num_whole_type fidget_render_requested ;
    static so_called_platform_math_num_whole_type fidget_render_replied ;

    static so_called_platform_math_num_whole_type use_text_texture_requested ;
    static so_called_platform_math_num_whole_type use_text_texture_replied ;
    
    static so_called_platform_math_num_whole_type text_letter_big_tex_coords_requested ;
    static so_called_platform_math_num_whole_type text_letter_big_tex_coords_replied ;
    static so_called_common_logic_text_letter_id_type text_letter_big_tex_coords_letter ;
    
    static so_called_platform_math_num_whole_type render_aspect_requested ;
    static so_called_platform_math_num_fract_type render_aspect_width ;
    
    static so_called_platform_math_num_fract_type tex_coords_left ;
    static so_called_platform_math_num_fract_type tex_coords_right ;
    static so_called_platform_math_num_fract_type tex_coords_bottom ;
    static so_called_platform_math_num_fract_type tex_coords_top ;
    
    static so_called_platform_math_num_fract_type desired_pos_radius_coeff ;
    static so_called_platform_math_num_fract_type desired_pos_angle ;
    static so_called_platform_math_num_fract_type desired_rot_angle ;
    static so_called_platform_math_num_fract_type desired_scale ;
    static so_called_platform_math_num_fract_type scene_scale ;
    static so_called_platform_math_num_fract_type scene_scale_frames ;
    static so_called_platform_math_num_fract_type rubber_first ;
    static so_called_platform_math_num_fract_type rubber_last ;
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
    so_called_platform_matrix_data_type scene_tm ;

    so_called_platform_matrix :: set_axis_x ( scene_tm , shy_guts :: scene_scale , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_y ( scene_tm , so_called_platform_math_consts :: fract_0 , shy_guts :: scene_scale , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_z ( scene_tm , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_1 ) ;
    so_called_platform_matrix :: set_origin ( scene_tm , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    
    so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_sender :: send ( so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_message ( ) ) ;
    
    so_called_common_engine_render_matrix_load_message matrix_load_msg ;
    matrix_load_msg . matrix = scene_tm ;
    so_called_common_engine_render_matrix_load_sender :: send ( matrix_load_msg ) ;
    
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: letters_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , i ) ;
        so_called_common_engine_render_mesh_render_message mesh_render_msg ;
        mesh_render_msg . mesh = letter . get ( ) . mesh ;
        so_called_common_engine_render_mesh_render_sender :: send ( mesh_render_msg ) ;
    }
    so_called_common_engine_render_blend_disable_sender :: send ( so_called_common_engine_render_blend_disable_message ( ) ) ;
}

void shy_guts :: title_update ( )
{
    so_called_platform_math_num_fract_type fract_letters_count ;
    so_called_platform_math_num_fract_type letter_size ;
    so_called_platform_math_num_fract_type desired_pos_radius ;
    so_called_platform_math_num_fract_type offset_y ;
    so_called_platform_math_num_fract_type fract_appear_duration_in_frames ;
    
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
                    
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: letters_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_math_num_fract_type offset_x ;
        so_called_platform_math_num_fract_type fract_i ;
        so_called_platform_math_num_fract_type rot_cos ;
        so_called_platform_math_num_fract_type rot_sin ;
        so_called_platform_math_num_fract_type rot_neg_sin ;
        so_called_platform_math_num_fract_type pos_cos ;
        so_called_platform_math_num_fract_type pos_sin ;
        so_called_platform_math_num_fract_type pos_neg_sin ;
        so_called_platform_math_num_fract_type rubber ;
        so_called_platform_math_num_fract_type pos_radius_old_part ;
        so_called_platform_math_num_fract_type pos_radius_new_part ;
        so_called_platform_math_num_fract_type pos_angle_old_part ;
        so_called_platform_math_num_fract_type pos_angle_new_part ;
        so_called_platform_math_num_fract_type rot_angle_old_part ;
        so_called_platform_math_num_fract_type rot_angle_new_part ;
        so_called_platform_math_num_fract_type scale_old_part ;
        so_called_platform_math_num_fract_type scale_new_part ;
        so_called_platform_math_num_whole_type starting_frame ;
        so_called_platform_math_num_whole_type finishing_frame ;
        so_called_platform_vector_data_type axis_x ;
        so_called_platform_vector_data_type axis_y ;
        so_called_platform_vector_data_type origin ;
        so_called_platform_vector_data_type offset ;
        so_called_platform_vector_data_type pos ;
        so_called_platform_matrix_data_type tm ;
        so_called_platform_pointer_data_type < shy_guts :: letter_state > letter ;
        
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
            so_called_common_engine_render_mesh_set_transform_message mesh_set_transform_msg ;
            mesh_set_transform_msg . mesh = letter . get ( ) . mesh ;
            mesh_set_transform_msg . transform = tm ;
            so_called_common_engine_render_mesh_set_transform_sender :: send ( mesh_set_transform_msg ) ;
        }
    }
}

void shy_guts :: delete_all_meshes ( )
{
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: letters_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , i ) ;
        so_called_common_engine_render_mesh_delete_message mesh_delete_msg ;
        mesh_delete_msg . mesh = letter . get ( ) . mesh ;
        so_called_common_engine_render_mesh_delete_sender :: send ( mesh_delete_msg ) ;
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
        so_called_common_logic_title_finished_sender :: send ( so_called_common_logic_title_finished_message ( ) ) ;
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
        so_called_platform_pointer_data_type < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , shy_guts :: bake_letter_index ) ;
        
        letter . get ( ) . scale = so_called_platform_math_consts :: fract_0 ;
        letter . get ( ) . pos_radius = so_called_platform_math_consts :: fract_0 ;
        letter . get ( ) . pos_angle = so_called_platform_math_consts :: fract_0 ;
        letter . get ( ) . rot_angle = so_called_platform_math_consts :: fract_0 ;
        
        shy_guts :: text_letter_big_tex_coords_requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: text_letter_big_tex_coords_letter = letter . get ( ) . letter ;
        
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
        
        so_called_common_logic_text_letter_big_tex_coords_request_message text_letter_big_tex_coords_request_msg ;
        text_letter_big_tex_coords_request_msg . letter = letter . get ( ) . letter ;
        so_called_common_logic_text_letter_big_tex_coords_request_sender :: send ( text_letter_big_tex_coords_request_msg  ) ;        
        
        so_called_common_engine_render_mesh_create_request_message mesh_create_msg ;
        mesh_create_msg . vertices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
        so_called_common_engine_render_mesh_create_request_sender :: send ( mesh_create_msg ) ;
    }
    else
    {
        shy_guts :: title_created = so_called_platform_math_consts :: whole_true ;
        shy_guts :: prepare_to_appear ( ) ;
        shy_guts :: animate_lifecycle ( ) ;
        so_called_common_logic_title_created_sender :: send ( so_called_common_logic_title_created_message ( ) ) ;
    }
}

void shy_guts :: proceed_with_render ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_started ) )
    {
        shy_guts :: render_started = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_true ;
        so_called_common_logic_core_use_ortho_projection_request_sender :: send ( so_called_common_logic_core_use_ortho_projection_request_message ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_ortho_projection_replied ) )
    {
        shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_false ;
        so_called_common_engine_render_clear_screen_message clear_screen_msg ;
        clear_screen_msg . r = so_called_platform_math_consts :: fract_0 ;
        clear_screen_msg . g = so_called_platform_math_consts :: fract_0 ;
        clear_screen_msg . b = so_called_platform_math_consts :: fract_0 ;
        so_called_common_engine_render_clear_screen_sender :: send ( clear_screen_msg ) ;
        so_called_common_engine_render_disable_depth_test_sender :: send ( so_called_common_engine_render_disable_depth_test_message ( ) ) ;
        so_called_common_engine_render_fog_disable_sender :: send ( so_called_common_engine_render_fog_disable_message ( ) ) ;

        shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_true ;
        so_called_common_logic_fidget_render_request_sender :: send ( so_called_common_logic_fidget_render_request_message ( ) ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_render_replied ) )
    {
        shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_false ;
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: title_created ) && so_called_platform_conditions :: whole_is_false ( shy_guts :: title_finished ) )
        {
            shy_guts :: use_text_texture_requested = so_called_platform_math_consts :: whole_true ;
            so_called_common_logic_text_use_text_texture_request_sender :: send ( so_called_common_logic_text_use_text_texture_request_message ( ) ) ;
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
                
        so_called_platform_math_num_fract_type title_r = so_called_platform_math_consts :: fract_0 ;
        so_called_platform_math_num_fract_type title_g = so_called_platform_math_consts :: fract_1 ;
        so_called_platform_math_num_fract_type title_b = so_called_platform_math_consts :: fract_0 ;
        so_called_platform_math_num_fract_type title_a = so_called_platform_math_consts :: fract_1 ;
        so_called_platform_math_num_fract_type x_left = so_called_platform_math_consts :: fract_minus_1 ;
        so_called_platform_math_num_fract_type x_right = so_called_platform_math_consts :: fract_1 ;
        so_called_platform_math_num_fract_type y_bottom = so_called_platform_math_consts :: fract_minus_1 ;
        so_called_platform_math_num_fract_type y_top = so_called_platform_math_consts :: fract_1 ;
        so_called_platform_math_num_fract_type z = so_called_platform_math_consts :: fract_0 ;
        
        so_called_platform_pointer_data_type < shy_guts :: letter_state > letter ;
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
        
        so_called_common_engine_render_mesh_finalize_message mesh_finalize_msg ;
        mesh_finalize_msg . mesh = letter . get ( ) . mesh ;
        so_called_common_engine_render_mesh_finalize_sender :: send ( mesh_finalize_msg ) ;
        
        so_called_platform_math :: inc_whole ( shy_guts :: bake_letter_index ) ;
        shy_guts :: bake_next_letter ( ) ;
    }
}

void shy_guts :: add_letter ( so_called_common_logic_text_letter_id_type letter )
{
    so_called_platform_pointer_data_type < shy_guts :: letter_state > letter_state ;
    so_called_platform_static_array :: element_ptr ( letter_state , shy_guts :: letters , shy_guts :: letters_count ) ;
    letter_state . get ( ) . letter = letter ;
    so_called_platform_math :: inc_whole ( shy_guts :: letters_count ) ;
}

void shy_guts :: mesh_set_triangle_strip_index_value 
    ( so_called_common_engine_render_mesh_id_type mesh
    , so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_whole_type index 
    )
{
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_sender :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_common_engine_render_mesh_id_type mesh 
    , so_called_platform_math_num_whole_type offset 
    , so_called_platform_math_num_fract_type u 
    , so_called_platform_math_num_fract_type v 
    )
{
    so_called_common_engine_render_mesh_set_vertex_tex_coord_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_common_engine_render_mesh_set_vertex_tex_coord_sender :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_common_engine_render_mesh_id_type mesh
    , so_called_platform_math_num_whole_type offset 
    , so_called_platform_math_num_fract_type x 
    , so_called_platform_math_num_fract_type y 
    , so_called_platform_math_num_fract_type z 
    )
{
    so_called_common_engine_render_mesh_set_vertex_position_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_common_engine_render_mesh_set_vertex_position_sender :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_color 
    ( so_called_common_engine_render_mesh_id_type mesh
    , so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_fract_type r
    , so_called_platform_math_num_fract_type g
    , so_called_platform_math_num_fract_type b
    , so_called_platform_math_num_fract_type a
    )
{
    so_called_common_engine_render_mesh_set_vertex_color_message msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( msg ) ;
}

void _shy_common_logic_title :: receive ( so_called_common_engine_render_aspect_reply_message msg )
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

void _shy_common_logic_title :: receive ( so_called_common_engine_render_mesh_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_true ;
        so_called_platform_pointer_data_type < shy_guts :: letter_state > letter ;
        so_called_platform_static_array :: element_ptr ( letter , shy_guts :: letters , shy_guts :: bake_letter_index ) ;
        letter . get ( ) . mesh = msg . mesh ;
        shy_guts :: proceed_with_letter_creation ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_common_init_message )
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

void _shy_common_logic_title :: receive ( so_called_common_logic_core_use_ortho_projection_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_ortho_projection_requested ) )
    {
        shy_guts :: use_ortho_projection_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_ortho_projection_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_common_logic_fidget_render_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_render_requested ) )
    {
        shy_guts :: fidget_render_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fidget_render_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_common_logic_text_letter_big_tex_coords_reply_message msg )
{
    so_called_platform_math_num_whole_type letters_are_equal ;
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

void _shy_common_logic_title :: receive ( so_called_common_logic_text_use_text_texture_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: use_text_texture_requested ) )
    {
        shy_guts :: use_text_texture_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: use_text_texture_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_title :: receive ( so_called_common_logic_title_launch_permit_message )
{
    shy_guts :: title_launch_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_title :: receive ( so_called_common_logic_title_render_message )
{
    shy_guts :: render_started = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_render ( ) ;
}

void _shy_common_logic_title :: receive ( so_called_common_logic_title_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: title_launch_permitted ) )
    {
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
        so_called_common_engine_render_aspect_request_sender :: send ( so_called_common_engine_render_aspect_request_message ( ) ) ;
    }
}

void _shy_common_logic_title :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

