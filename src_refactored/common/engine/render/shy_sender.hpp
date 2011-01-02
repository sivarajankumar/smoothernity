#include "shy_sender.h"

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_blend_disable msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_clear_screen msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_disable_depth_test msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_enable_face_culling msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_enable_depth_test msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_fog_disable msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_fog_linear msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_matrix_load msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_matrix_mult msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_matrix_identity msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_projection_frustum msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_projection_ortho msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_mode_modulate msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_set_vertex_position msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_set_vertex_tex_coord msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_set_vertex_color msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_set_triangle_strip_index_value msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_set_triangle_fan_index_value msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_create_request msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    so_called_common_logic_blanket_mesh :: receive ( msg ) ;
    so_called_common_logic_door_mesh :: receive ( msg ) ;
    so_called_common_logic_entities :: receive ( msg ) ;
    so_called_common_logic_fidget :: receive ( msg ) ;
    so_called_common_logic_image :: receive ( msg ) ;
    so_called_common_logic_land :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_creator :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_mesh :: receive ( msg ) ;
    so_called_common_logic_room_mesh :: receive ( msg ) ;
    so_called_common_logic_text :: receive ( msg ) ;
    so_called_common_logic_title :: receive ( msg ) ;
    so_called_common_logic_touch :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_finalize msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_delete msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_render msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_mesh_set_transform msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_aspect_reply msg )
{
    so_called_common_logic_blanket_animation_fit :: receive ( msg ) ;
    so_called_common_logic_core :: receive ( msg ) ;
    so_called_common_logic_camera :: receive ( msg ) ;
    so_called_common_logic_fidget :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_layout_position :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_layout_row_rect :: receive ( msg ) ;
    so_called_common_logic_ortho :: receive ( msg ) ;
    so_called_common_logic_perspective :: receive ( msg ) ;
    so_called_common_logic_title :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_aspect_request msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_create_reply msg )
{
    so_called_common_logic_door_texture :: receive ( msg ) ;
    so_called_common_logic_image :: receive ( msg ) ;
    so_called_common_logic_land :: receive ( msg ) ;
    so_called_common_logic_room_texture :: receive ( msg ) ;
    so_called_common_logic_text :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_create_request msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_finalize msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_load_from_resource msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_loader_ready_reply msg )
{
    so_called_common_logic_image :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_loader_ready_request msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_select msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_set_texel msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_set_texel_rgba msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_set_texels_rect msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_texture_unselect msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_frame_loss_request msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

void shy_common_engine_render_sender :: send ( so_called_message_common_engine_render_frame_loss_reply msg )
{
    so_called_common_logic_fidget :: receive ( msg ) ;
}
