class _shy_common_engine_render
{
public :
    static void receive ( so_called_common_done_message ) ;
    static void receive ( so_called_common_engine_render_aspect_request_message ) ;
    static void receive ( so_called_common_engine_render_blend_disable_message ) ;
    static void receive ( so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_message ) ;
    static void receive ( so_called_common_engine_render_clear_screen_message ) ;
    static void receive ( so_called_common_engine_render_disable_depth_test_message ) ;
    static void receive ( so_called_common_engine_render_enable_depth_test_message ) ;
    static void receive ( so_called_common_engine_render_enable_face_culling_message ) ;
    static void receive ( so_called_common_engine_render_fog_disable_message ) ;
    static void receive ( so_called_common_engine_render_fog_linear_message ) ;
    static void receive ( so_called_common_engine_render_frame_loss_request_message ) ;
    static void receive ( so_called_common_engine_render_matrix_identity_message ) ;
    static void receive ( so_called_common_engine_render_matrix_load_message ) ;
    static void receive ( so_called_common_engine_render_matrix_mult_message ) ;
    static void receive ( so_called_common_engine_render_mesh_create_request_message ) ;
    static void receive ( so_called_common_engine_render_mesh_delete_message ) ;
    static void receive ( so_called_common_engine_render_mesh_finalize_message ) ;
    static void receive ( so_called_common_engine_render_mesh_render_message ) ;
    static void receive ( so_called_common_engine_render_mesh_set_transform_message ) ;
    static void receive ( so_called_common_engine_render_mesh_set_triangle_fan_index_value_message ) ;
    static void receive ( so_called_common_engine_render_mesh_set_triangle_strip_index_value_message ) ;
    static void receive ( so_called_common_engine_render_mesh_set_vertex_color_message ) ;
    static void receive ( so_called_common_engine_render_mesh_set_vertex_position_message ) ;
    static void receive ( so_called_common_engine_render_mesh_set_vertex_tex_coord_message ) ;
    static void receive ( so_called_common_engine_render_projection_frustum_message ) ;
    static void receive ( so_called_common_engine_render_projection_ortho_message ) ;
    static void receive ( so_called_common_engine_render_texture_create_request_message ) ;
    static void receive ( so_called_common_engine_render_texture_finalize_message ) ;
    static void receive ( so_called_common_engine_render_texture_load_from_resource_message ) ;
    static void receive ( so_called_common_engine_render_texture_loader_ready_request_message ) ;
    static void receive ( so_called_common_engine_render_texture_mode_modulate_message ) ;
    static void receive ( so_called_common_engine_render_texture_select_message ) ;
    static void receive ( so_called_common_engine_render_texture_set_texel_message ) ;
    static void receive ( so_called_common_engine_render_texture_set_texel_rgba_message ) ;
    static void receive ( so_called_common_engine_render_texture_set_texels_rect_message ) ;
    static void receive ( so_called_common_engine_render_texture_unselect_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_engine_render 
    , so_called_common_engine_render_consts :: max_messages
    > :: module
    shy_common_engine_render_scheduled ;
