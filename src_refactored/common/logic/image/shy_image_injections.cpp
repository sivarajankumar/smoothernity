#include "./shy_image_injections.h"

#include "./sender/prepared/shy_prepared_injections.h"
#include "./sender/render_reply/shy_render_reply_injections.h"

#include "../../engine/math/stateless/shy_stateless_injections.h"
#include "../../engine/render/sender/blend_disable/shy_blend_disable_injections.h"
#include "../../engine/render/sender/blend_src_alpha_dst_one_minus_alpha/shy_blend_src_alpha_dst_one_minus_alpha_injections.h"
#include "../../engine/render/sender/mesh_create_request/shy_mesh_create_request_injections.h"
#include "../../engine/render/sender/mesh_finalize/shy_mesh_finalize_injections.h"
#include "../../engine/render/sender/mesh_render/shy_mesh_render_injections.h"
#include "../../engine/render/sender/mesh_set_transform/shy_mesh_set_transform_injections.h"
#include "../../engine/render/sender/mesh_set_vertex_position/shy_mesh_set_vertex_position_injections.h"
#include "../../engine/render/sender/mesh_set_vertex_tex_coord/shy_mesh_set_vertex_tex_coord_injections.h"
#include "../../engine/render/sender/texture_create_request/shy_texture_create_request_injections.h"
#include "../../engine/render/sender/texture_finalize/shy_texture_finalize_injections.h"
#include "../../engine/render/sender/texture_loader_ready_request/shy_texture_loader_ready_request_injections.h"
#include "../../engine/render/sender/texture_select/shy_texture_select_injections.h"

#include "../../../injections/platform/conditions/shy_conditions.h"
#include "../../../injections/platform/math/consts/shy_consts.h"
#include "../../../injections/platform/math/shy_math.h"
#include "../../../injections/platform/matrix/shy_matrix.h"

#include "./shy_image.hpp"

