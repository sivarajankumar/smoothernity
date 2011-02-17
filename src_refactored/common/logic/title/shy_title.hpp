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
}

void shy_guts :: title_render ( )
{
}

void shy_guts :: title_update ( )
{
}

void shy_guts :: delete_all_meshes ( )
{
}

void shy_guts :: prepare_to_appear ( )
{
}

void shy_guts :: prepare_to_disappear ( )
{
}

void shy_guts :: animate_appear ( )
{
}

void shy_guts :: animate_disappear ( )
{
}

void shy_guts :: animate_lifecycle ( )
{
}

void shy_guts :: bake_next_letter ( )
{
}

void shy_guts :: proceed_with_render ( )
{
}

void shy_guts :: proceed_with_letter_creation ( )
{
}

void shy_guts :: add_letter ( so_called_type_common_logic_text_letter_id )
{
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
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
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
}

void _shy_common_logic_title :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_title :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
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
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_text_letter_big_tex_coords_reply )
{
}

void _shy_common_logic_title :: receive ( so_called_message_common_logic_text_use_text_texture_reply )
{
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
