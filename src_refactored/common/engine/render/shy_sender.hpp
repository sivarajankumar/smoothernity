#include "shy_sender.h"

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

