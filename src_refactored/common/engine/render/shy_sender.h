#ifndef _shy_common_engine_render_sender_included
#define _shy_common_engine_render_sender_included

class shy_common_engine_render_sender
{
public :
    static void send ( so_called_message_common_engine_render_aspect_reply ) ;
    static void send ( so_called_message_common_engine_render_aspect_request ) ;
    static void send ( so_called_message_common_engine_render_blend_disable ) ;
    static void send ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha ) ;
    static void send ( so_called_message_common_engine_render_clear_screen ) ;
    static void send ( so_called_message_common_engine_render_disable_depth_test ) ;
    static void send ( so_called_message_common_engine_render_enable_depth_test ) ;
    static void send ( so_called_message_common_engine_render_enable_face_culling ) ;
    static void send ( so_called_message_common_engine_render_fog_disable ) ;
    static void send ( so_called_message_common_engine_render_fog_linear ) ;
    static void send ( so_called_message_common_engine_render_frame_loss_reply ) ;
    static void send ( so_called_message_common_engine_render_frame_loss_request ) ;
    static void send ( so_called_message_common_engine_render_matrix_identity ) ;
    static void send ( so_called_message_common_engine_render_matrix_load ) ;
    static void send ( so_called_message_common_engine_render_matrix_mult ) ;
    static void send ( so_called_message_common_engine_render_mesh_create_reply ) ;
    static void send ( so_called_message_common_engine_render_mesh_create_request ) ;
    static void send ( so_called_message_common_engine_render_mesh_delete ) ;
    static void send ( so_called_message_common_engine_render_mesh_finalize ) ;
    static void send ( so_called_message_common_engine_render_mesh_render ) ;
    static void send ( so_called_message_common_engine_render_mesh_set_transform ) ;
    static void send ( so_called_message_common_engine_render_mesh_set_triangle_fan_index_value ) ;
    static void send ( so_called_message_common_engine_render_mesh_set_triangle_strip_index_value ) ;
    static void send ( so_called_message_common_engine_render_mesh_set_vertex_color ) ;
    static void send ( so_called_message_common_engine_render_mesh_set_vertex_position ) ;
    static void send ( so_called_message_common_engine_render_mesh_set_vertex_tex_coord ) ;
    static void send ( so_called_message_common_engine_render_projection_frustum ) ;
    static void send ( so_called_message_common_engine_render_projection_ortho ) ;
    static void send ( so_called_message_common_engine_render_texture_create_reply ) ;
    static void send ( so_called_message_common_engine_render_texture_create_request ) ;
    static void send ( so_called_message_common_engine_render_texture_finalize ) ;
    static void send ( so_called_message_common_engine_render_texture_load_from_resource ) ;
    static void send ( so_called_message_common_engine_render_texture_loader_ready_reply ) ;
    static void send ( so_called_message_common_engine_render_texture_loader_ready_request ) ;
    static void send ( so_called_message_common_engine_render_texture_mode_modulate ) ;
    static void send ( so_called_message_common_engine_render_texture_select ) ;
    static void send ( so_called_message_common_engine_render_texture_set_texel ) ;
    static void send ( so_called_message_common_engine_render_texture_set_texel_rgba ) ;
    static void send ( so_called_message_common_engine_render_texture_set_texels_rect ) ;
    static void send ( so_called_message_common_engine_render_texture_unselect ) ;
} ;

#endif
