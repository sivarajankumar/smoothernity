#ifndef _shy_common_engine_render_injections_included
#define _shy_common_engine_render_injections_included

#include "./message/aspect_request/shy_aspect_request_injections.h"
#include "./message/blend_disable/shy_blend_disable_injections.h"
#include "./message/blend_src_alpha_dst_one_minus_alpha/shy_blend_src_alpha_dst_one_minus_alpha_injections.h"
#include "./message/clear_screen/shy_clear_screen_injections.h"
#include "./message/disable_depth_test/shy_disable_depth_test_injections.h"
#include "./message/done/shy_done_injections.h"
#include "./message/enable_depth_test/shy_enable_depth_test_injections.h"
#include "./message/enable_face_culling/shy_enable_face_culling_injections.h"
#include "./message/fog_disable/shy_fog_disable_injections.h"
#include "./message/fog_linear/shy_fog_linear_injections.h"
#include "./message/frame_loss_request/shy_frame_loss_request_injections.h"
#include "./message/matrix_identity/shy_matrix_identity_injections.h"
#include "./message/matrix_load/shy_matrix_load_injections.h"
#include "./message/matrix_mult/shy_matrix_mult_injections.h"
#include "./message/mesh_create_request/shy_mesh_create_request_injections.h"
#include "./message/mesh_delete/shy_mesh_delete_injections.h"
#include "./message/mesh_finalize/shy_mesh_finalize_injections.h"
#include "./message/mesh_render/shy_mesh_render_injections.h"
#include "./message/mesh_set_transform/shy_mesh_set_transform_injections.h"
#include "./message/mesh_set_triangle_fan_index_value/shy_mesh_set_triangle_fan_index_value_injections.h"
#include "./message/mesh_set_triangle_strip_index_value/shy_mesh_set_triangle_strip_index_value_injections.h"
#include "./message/mesh_set_vertex_color/shy_mesh_set_vertex_color_injections.h"
#include "./message/mesh_set_vertex_position/shy_mesh_set_vertex_position_injections.h"
#include "./message/mesh_set_vertex_tex_coord/shy_mesh_set_vertex_tex_coord_injections.h"
#include "./message/projection_frustum/shy_projection_frustum_injections.h"
#include "./message/projection_ortho/shy_projection_ortho_injections.h"
#include "./message/texture_create_request/shy_texture_create_request_injections.h"
#include "./message/texture_finalize/shy_texture_finalize_injections.h"
#include "./message/texture_load_from_resource/shy_texture_load_from_resource_injections.h"
#include "./message/texture_loader_ready_request/shy_texture_loader_ready_request_injections.h"
#include "./message/texture_mode_modulate/shy_texture_mode_modulate_injections.h"
#include "./message/texture_select/shy_texture_select_injections.h"
#include "./message/texture_set_texel/shy_texture_set_texel_injections.h"
#include "./message/texture_set_texel_rgba/shy_texture_set_texel_rgba_injections.h"
#include "./message/texture_set_texels_rect/shy_texture_set_texels_rect_injections.h"
#include "./message/texture_unselect/shy_texture_unselect_injections.h"

#include "../../message/init/shy_init_injections.h"

#include "../../../injections/platform/scheduler/shy_scheduler.h"

#include "./shy_render.h"

typedef shy_common_engine_render_scheduled so_called_common_engine_render ;

#endif
