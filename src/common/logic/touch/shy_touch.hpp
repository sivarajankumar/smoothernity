namespace shy_guts
{
    namespace consts
    {
        static const so_called_platform_math_num_fract_type spot_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_platform_math_num_fract_type spot_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_platform_math_num_fract_type spot_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_platform_math_num_fract_type spot_pos_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
        static const so_called_platform_math_num_fract_type spot_size = so_called_platform_math :: init_num_fract ( 3 , 10 ) ;
        static const so_called_platform_math_num_whole_type spot_edges = so_called_platform_math :: init_num_whole ( 32 ) ;
        static const so_called_platform_math_num_whole_type spot_lifetime_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
    }

    static void update_spot ( ) ;
    static void decrease_spot_lifetime ( ) ;
    static void poll_touchscreen ( ) ;
    static void poll_mouse ( ) ;
    static void place_new_spot ( ) ;
    static void render_spot_mesh ( ) ;
    static void create_spot_mesh ( ) ;

    static so_called_platform_math_num_whole_type spot_frames_left ;
    static so_called_platform_math_num_whole_type spot_mesh_created ;
    static so_called_platform_math_num_whole_type spot_prepare_permitted ;
    static so_called_platform_math_num_whole_type should_place_new_spot ;
    static so_called_platform_math_num_whole_type mesh_create_requested ;
    static so_called_platform_math_num_fract_type spot_x ;
    static so_called_platform_math_num_fract_type spot_y ;
    static so_called_common_engine_render_mesh_id_type spot_mesh_id ;
    static so_called_platform_vector_data_type spot_position ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_touch > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: update_spot ( )
{
    shy_guts :: decrease_spot_lifetime ( ) ;
    shy_guts :: poll_touchscreen ( ) ;
    shy_guts :: poll_mouse ( ) ;
    shy_guts :: place_new_spot ( ) ;
}

void shy_guts :: decrease_spot_lifetime ( )
{
    if ( so_called_platform_conditions :: whole_greater_than_zero ( shy_guts :: spot_frames_left ) )
        so_called_platform_math :: dec_whole ( shy_guts :: spot_frames_left ) ;
}

void shy_guts :: poll_touchscreen ( )
{
    so_called_platform_math_num_whole_type touch ;
    so_called_platform_touch :: occured ( touch ) ;
    if ( so_called_platform_conditions :: whole_is_true ( touch ) )
    {
        so_called_platform_touch :: x ( shy_guts :: spot_x ) ;
        so_called_platform_touch :: y ( shy_guts :: spot_y ) ;
        shy_guts :: should_place_new_spot = so_called_platform_math_consts :: whole_true ;
    }
}

void shy_guts :: poll_mouse ( )
{
    so_called_platform_math_num_whole_type mouse_button ;
    so_called_platform_mouse :: left_button_down ( mouse_button ) ;
    if ( so_called_platform_conditions :: whole_is_true ( mouse_button ) )
    {
        so_called_platform_mouse :: x ( shy_guts :: spot_x ) ;
        so_called_platform_mouse :: y ( shy_guts :: spot_y ) ;
        shy_guts :: should_place_new_spot = so_called_platform_math_consts :: whole_true ;
    }
}

void shy_guts :: place_new_spot ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: should_place_new_spot ) )
    {
        so_called_platform_vector :: xyz ( shy_guts :: spot_position , shy_guts :: spot_x , shy_guts :: spot_y , shy_guts :: consts :: spot_pos_z ) ;
        shy_guts :: spot_frames_left = shy_guts :: consts :: spot_lifetime_in_frames ;
        shy_guts :: should_place_new_spot = so_called_platform_math_consts :: whole_false ;
    }
}

void shy_guts :: render_spot_mesh ( )
{
    so_called_platform_matrix_data_type matrix ;
    so_called_platform_math_num_fract_type fract_spot_frames_left ;
    so_called_platform_math_num_fract_type fract_spot_lifetime_in_frames ;
    so_called_platform_math_num_fract_type scale ;

    so_called_platform_math :: make_fract_from_whole ( fract_spot_frames_left , shy_guts :: spot_frames_left ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_spot_lifetime_in_frames , shy_guts :: consts :: spot_lifetime_in_frames ) ;
    so_called_platform_math :: div_fracts ( scale , fract_spot_frames_left , fract_spot_lifetime_in_frames ) ;
    so_called_platform_matrix :: set_axis_x ( matrix , scale , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_y ( matrix , so_called_platform_math_consts :: fract_0 , scale , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_z ( matrix , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , scale ) ;
    so_called_platform_matrix :: set_origin ( matrix , shy_guts :: spot_position ) ;
    so_called_common_engine_render_texture_unselect_sender :: send ( so_called_common_engine_render_texture_unselect_message ( ) ) ;
    {
        so_called_common_engine_render_mesh_set_transform_message mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = shy_guts :: spot_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_common_engine_render_mesh_set_transform_sender :: send ( mesh_set_transform_msg ) ;
    }
    {
        so_called_common_engine_render_mesh_render_message mesh_render_msg ;
        mesh_render_msg . mesh = shy_guts :: spot_mesh_id ;
        so_called_common_engine_render_mesh_render_sender :: send ( mesh_render_msg ) ;
    }
}

void shy_guts :: create_spot_mesh ( )
{
    so_called_platform_math_num_fract_type fract_spot_edges ;
    so_called_platform_math :: make_fract_from_whole ( fract_spot_edges , shy_guts :: consts :: spot_edges ) ;
            
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: consts :: spot_edges ) 
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_math_num_fract_type angle ;
        so_called_platform_math_num_fract_type fract_i ;
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
        so_called_platform_math :: div_fract_by ( angle , fract_spot_edges ) ;
        so_called_platform_math :: cos ( angle_cos , angle ) ;
        so_called_platform_math :: sin ( angle_sin , angle ) ;
        so_called_platform_math :: mul_fracts ( vertex_x , shy_guts :: consts :: spot_size , angle_cos ) ;
        so_called_platform_math :: mul_fracts ( vertex_y , shy_guts :: consts :: spot_size , angle_sin ) ;
        vertex_z = so_called_platform_math_consts :: fract_0 ;
        vertex_r = shy_guts :: consts :: spot_r ;
        vertex_g = shy_guts :: consts :: spot_g ;
        vertex_b = shy_guts :: consts :: spot_b ;
        vertex_a = so_called_platform_math_consts :: fract_1 ;

        so_called_common_engine_render_mesh_set_vertex_position_message set_pos_msg ;
        set_pos_msg . mesh = shy_guts :: spot_mesh_id ;
        set_pos_msg . offset = i ;
        set_pos_msg . x = vertex_x ;
        set_pos_msg . y = vertex_y ;
        set_pos_msg . z = vertex_z ;
        so_called_common_engine_render_mesh_set_vertex_position_sender :: send ( set_pos_msg ) ;

        so_called_common_engine_render_mesh_set_vertex_color_message set_col_msg ;
        set_col_msg . mesh = shy_guts :: spot_mesh_id ;
        set_col_msg . offset = i ;
        set_col_msg . r = vertex_r ;
        set_col_msg . g = vertex_g ;
        set_col_msg . b = vertex_b ;
        set_col_msg . a = vertex_a ;
        so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( set_col_msg ) ;
        
        so_called_common_engine_render_mesh_set_triangle_fan_index_value_message set_index_msg ;
        set_index_msg . mesh = shy_guts :: spot_mesh_id ;
        set_index_msg . offset = i ;
        set_index_msg . index = i ;
        so_called_common_engine_render_mesh_set_triangle_fan_index_value_sender :: send ( set_index_msg ) ;
    }
    
    so_called_common_engine_render_mesh_finalize_message mesh_finalize_msg ;
    mesh_finalize_msg . mesh = shy_guts :: spot_mesh_id ;
    so_called_common_engine_render_mesh_finalize_sender :: send ( mesh_finalize_msg ) ;
}

void _shy_common_logic_touch :: receive ( so_called_common_engine_render_mesh_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: spot_mesh_id = msg . mesh ;
        shy_guts :: create_spot_mesh ( ) ;
        shy_guts :: spot_mesh_created = so_called_platform_math_consts :: whole_true ;
        so_called_common_logic_touch_prepared_sender :: send ( so_called_common_logic_touch_prepared_message ( ) ) ;
    }
}

void _shy_common_logic_touch :: receive ( so_called_common_init_message )
{
    shy_guts :: spot_frames_left = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: spot_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: spot_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: should_place_new_spot = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_touch :: receive ( so_called_common_logic_touch_prepare_permit_message )
{
    shy_guts :: spot_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_touch :: receive ( so_called_common_logic_touch_render_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: spot_mesh_created ) && so_called_platform_conditions :: whole_greater_than_zero ( shy_guts :: spot_frames_left ) )
        shy_guts :: render_spot_mesh ( ) ;
}

void _shy_common_logic_touch :: receive ( so_called_common_logic_touch_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: spot_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: spot_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
            
            so_called_common_engine_render_mesh_create_request_message mesh_create_msg ;
            mesh_create_msg . vertices = shy_guts :: consts :: spot_edges ;
            mesh_create_msg . triangle_fan_indices = shy_guts :: consts :: spot_edges ;
            mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_common_engine_render_mesh_create_request_sender :: send ( mesh_create_msg ) ;
        }
        else
            shy_guts :: update_spot ( ) ;
    }
}

void _shy_common_logic_touch :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
