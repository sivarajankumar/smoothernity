namespace shy_guts
{
    namespace consts
    {
        static so_called_type_platform_math_num_whole create_rows_per_frame = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_type_platform_math_num_whole land_grid = so_called_platform_math :: init_num_whole ( 10 ) ;
        static so_called_type_platform_math_num_whole scale_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
        static so_called_type_platform_math_num_whole modulator_1 = so_called_platform_math :: init_num_whole ( 32 ) ;
        static so_called_type_platform_math_num_whole modulator_2 = so_called_platform_math :: init_num_whole ( 64 ) ;
        static so_called_type_platform_math_num_whole modulator_3 = so_called_platform_math :: init_num_whole ( 128 ) ;
        static so_called_type_platform_math_num_whole multiplier_1 = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_type_platform_math_num_whole multiplier_2 = so_called_platform_math :: init_num_whole ( 4 ) ;
        static so_called_type_platform_math_num_whole multiplier_3 = so_called_platform_math :: init_num_whole ( 2 ) ;
        static so_called_type_platform_math_num_fract color_scale = so_called_platform_math :: init_num_fract ( 255 , 1 ) ;
        static so_called_type_platform_math_num_fract land_radius = so_called_platform_math :: init_num_fract ( 10 , 1 ) ;
        static so_called_type_platform_math_num_fract land_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_type_platform_math_num_fract land_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_type_platform_math_num_fract land_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
    }

    static void render_land ( ) ;
    static void create_land_mesh ( ) ;
    static void create_land_texture ( ) ;
    static void mesh_set_triangle_strip_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index ) ;

    static so_called_type_platform_math_num_whole land_mesh_created ;
    static so_called_type_platform_math_num_whole land_texture_created ;
    static so_called_type_platform_math_num_whole land_prepare_permitted ;
    static so_called_type_platform_math_num_whole land_texture_creation_row ;
    static so_called_type_platform_math_num_fract land_scale ;
    static so_called_type_platform_math_num_whole texture_create_requested ;
    static so_called_type_platform_math_num_whole texture_create_replied ;
    static so_called_type_platform_math_num_whole mesh_create_requested ;
    static so_called_type_common_engine_render_mesh_id land_mesh_id ;
    static so_called_type_common_engine_render_texture_id land_texture_id ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_land > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: render_land ( )
{
    so_called_type_platform_matrix_data matrix ;
    so_called_type_platform_math_num_fract scale_step ;
    so_called_type_platform_math_num_fract increased_scale ;
    so_called_type_platform_math_num_fract fract_scale_in_frames ;
    
    {
        so_called_message_common_engine_render_texture_select texture_select_msg ;
        texture_select_msg . texture = shy_guts :: land_texture_id ;
        so_called_sender_common_engine_render_texture_select :: send ( texture_select_msg ) ;
    }
    so_called_platform_math :: make_fract_from_whole ( fract_scale_in_frames , shy_guts :: consts :: scale_in_frames ) ;
    so_called_platform_math :: div_fracts ( scale_step , so_called_platform_math_consts :: fract_1 , fract_scale_in_frames ) ;
    so_called_platform_math :: add_fracts ( increased_scale , shy_guts :: land_scale , scale_step ) ;
    if ( so_called_platform_conditions :: fract_less_than_fract ( increased_scale , so_called_platform_math_consts :: fract_1 ) )
        shy_guts :: land_scale = increased_scale ;
    else
        shy_guts :: land_scale = so_called_platform_math_consts :: fract_1 ;
    so_called_platform_matrix :: set_axis_x ( matrix , shy_guts :: land_scale , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_y ( matrix , so_called_platform_math_consts :: fract_0 , shy_guts :: land_scale , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_z ( matrix , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , shy_guts :: land_scale ) ;
    so_called_platform_matrix :: set_origin ( matrix , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    {
        so_called_message_common_engine_render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = shy_guts :: land_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_sender_common_engine_render_mesh_set_transform :: send ( mesh_set_transform_msg ) ;
    }
    {
        so_called_message_common_engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = shy_guts :: land_mesh_id ;
        so_called_sender_common_engine_render_mesh_render :: send ( mesh_render_msg ) ;
    }
}

void shy_guts :: create_land_mesh ( )
{
}

void shy_guts :: create_land_texture ( )
{
}

void shy_guts :: mesh_set_triangle_strip_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index )
{
}

void _shy_common_logic_land :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: land_mesh_id = msg . mesh ;
        shy_guts :: create_land_mesh ( ) ;
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_mesh_created ) )
            so_called_sender_common_logic_land_prepared :: send ( so_called_message_common_logic_land_prepared ( ) ) ;
    }
}

void _shy_common_logic_land :: receive ( so_called_message_common_engine_render_texture_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_create_requested ) )
    {
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: land_texture_id = msg . texture ;
    }
}

void _shy_common_logic_land :: receive ( so_called_message_common_init )
{
    shy_guts :: land_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_texture_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_texture_creation_row = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: land_scale = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_prepare_permit )
{
    shy_guts :: land_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_mesh_created ) && so_called_platform_conditions :: whole_is_true ( shy_guts :: land_texture_created ) )
        shy_guts :: render_land ( ) ;
    so_called_sender_common_logic_land_render_reply :: send ( so_called_message_common_logic_land_render_reply ( ) ) ;
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: land_texture_created ) )
        {
            if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: texture_create_replied ) )
            {
                shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_true ;
                so_called_sender_common_engine_render_texture_create_request :: send ( so_called_message_common_engine_render_texture_create_request ( ) ) ;
            }
            else
                shy_guts :: create_land_texture ( ) ;
        }
        else if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: land_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
        
            so_called_type_platform_math_num_whole total_vertices ;
            so_called_type_platform_math_num_whole total_indices ;
            
            so_called_platform_math :: add_wholes ( total_vertices , shy_guts :: consts :: land_grid , so_called_platform_math_consts :: whole_1 ) ;
            so_called_platform_math :: mul_whole_by ( total_vertices , total_vertices ) ;
            
            so_called_platform_math :: add_wholes ( total_indices , shy_guts :: consts :: land_grid , so_called_platform_math_consts :: whole_1 ) ;
            so_called_platform_math :: mul_whole_by ( total_indices , shy_guts :: consts :: land_grid ) ;
            so_called_platform_math :: mul_whole_by ( total_indices , so_called_platform_math_consts :: whole_2 ) ;
            
            so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = total_vertices ;
            mesh_create_msg . triangle_strip_indices = total_indices ;
            mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_sender_common_engine_render_mesh_create_request :: send ( mesh_create_msg ) ;
        }
    }
}
