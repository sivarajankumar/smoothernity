class _shy_common_engine_render
{
public :
    static void receive ( so_called_message_common_engine_render_aspect_request ) ;
    static void receive ( so_called_message_common_engine_render_blend_disable ) ;
    static void receive ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha ) ;
    static void receive ( so_called_message_common_engine_render_clear_screen ) ;
    static void receive ( so_called_message_common_engine_render_disable_depth_test ) ;
    static void receive ( so_called_message_common_engine_render_done ) ;
    static void receive ( so_called_message_common_engine_render_enable_depth_test ) ;
    static void receive ( so_called_message_common_engine_render_enable_face_culling ) ;
    static void receive ( so_called_message_common_engine_render_fog_disable ) ;
    static void receive ( so_called_message_common_engine_render_fog_linear ) ;
    static void receive ( so_called_message_common_engine_render_frame_loss_request ) ;
    static void receive ( so_called_message_common_engine_render_init ) ;
    static void receive ( so_called_message_common_engine_render_matrix_identity ) ;
    static void receive ( so_called_message_common_engine_render_matrix_load ) ;
    static void receive ( so_called_message_common_engine_render_matrix_mult ) ;
    static void receive ( so_called_message_common_engine_render_mesh_create_request ) ;
    static void receive ( so_called_message_common_engine_render_mesh_delete ) ;
    static void receive ( so_called_message_common_engine_render_mesh_finalize ) ;
    static void receive ( so_called_message_common_engine_render_mesh_render ) ;
    static void receive ( so_called_message_common_engine_render_mesh_set_transform ) ;
    static void receive ( so_called_message_common_engine_render_mesh_set_triangle_fan_index_value ) ;
    static void receive ( so_called_message_common_engine_render_mesh_set_triangle_strip_index_value ) ;
    static void receive ( so_called_message_common_engine_render_mesh_set_vertex_color ) ;
    static void receive ( so_called_message_common_engine_render_mesh_set_vertex_position ) ;
    static void receive ( so_called_message_common_engine_render_mesh_set_vertex_tex_coord ) ;
    static void receive ( so_called_message_common_engine_render_projection_frustum ) ;
    static void receive ( so_called_message_common_engine_render_projection_ortho ) ;
    static void receive ( so_called_message_common_engine_render_texture_create_request ) ;
    static void receive ( so_called_message_common_engine_render_texture_finalize ) ;
    static void receive ( so_called_message_common_engine_render_texture_load_from_resource ) ;
    static void receive ( so_called_message_common_engine_render_texture_loader_ready_request ) ;
    static void receive ( so_called_message_common_engine_render_texture_mode_modulate ) ;
    static void receive ( so_called_message_common_engine_render_texture_select ) ;
    static void receive ( so_called_message_common_engine_render_texture_set_texel ) ;
    static void receive ( so_called_message_common_engine_render_texture_set_texel_rgba ) ;
    static void receive ( so_called_message_common_engine_render_texture_set_texels_rect ) ;
    static void receive ( so_called_message_common_engine_render_texture_unselect ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_engine_render > :: module shy_common_engine_render_scheduled ;
