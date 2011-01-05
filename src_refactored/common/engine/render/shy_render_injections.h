#ifndef _shy_common_engine_render_injections_included
#define _shy_common_engine_render_injections_included

#include "shy_message_aspect_request_injections.h"
#include "shy_message_blend_disable_injections.h"
#include "shy_message_blend_src_alpha_dst_one_minus_alpha_injections.h"
#include "shy_message_clear_screen_injections.h"
#include "shy_message_disable_depth_test_injections.h"
#include "shy_message_enable_depth_test_injections.h"
#include "shy_message_enable_face_culling_injections.h"
#include "shy_message_fog_disable_injections.h"
#include "shy_message_fog_linear_injections.h"
#include "shy_message_frame_loss_request_injections.h"
#include "shy_message_matrix_identity_injections.h"
#include "shy_message_matrix_load_injections.h"
#include "shy_message_matrix_mult_injections.h"
#include "shy_message_mesh_create_request_injections.h"
#include "shy_message_mesh_delete_injections.h"
#include "shy_message_mesh_finalize_injections.h"
#include "shy_message_mesh_render_injections.h"
#include "shy_message_mesh_set_transform_injections.h"
#include "shy_message_mesh_set_triangle_fan_index_value_injections.h"
#include "shy_message_mesh_set_triangle_strip_index_value_injections.h"
#include "shy_message_mesh_set_vertex_color_injections.h"
#include "shy_message_mesh_set_vertex_position_injections.h"
#include "shy_message_mesh_set_vertex_tex_coord_injections.h"
#include "shy_message_projection_frustum_injections.h"
#include "shy_message_projection_ortho_injections.h"
#include "shy_message_texture_create_request_injections.h"
#include "shy_message_texture_finalize_injections.h"
#include "shy_message_texture_load_from_resource_injections.h"
#include "shy_message_texture_loader_ready_request_injections.h"
#include "shy_message_texture_mode_modulate_injections.h"
#include "shy_message_texture_select_injections.h"
#include "shy_message_texture_set_texel_injections.h"
#include "shy_message_texture_set_texel_rgba_injections.h"
#include "shy_message_texture_set_texels_rect_injections.h"
#include "shy_message_texture_unselect_injections.h"

#include "../../../injections/shy_platform_static_assert.h"
#include "../../../injections/shy_platform_scheduler.h"

#include "shy_render.h"

typedef shy_common_engine_render_scheduled so_called_common_engine_render ;

#endif
