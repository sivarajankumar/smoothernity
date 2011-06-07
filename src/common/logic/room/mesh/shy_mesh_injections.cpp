#include "./shy_mesh_injections.h"

#include "../consts/shy_consts_injections.h"
#include "../sender/mesh_creation_finished/shy_mesh_creation_finished_injections.h"
#include "../sender/mesh_render_reply/shy_mesh_render_reply_injections.h"

#include "../../../engine/render/sender/mesh_create_request/shy_mesh_create_request_injections.h"
#include "../../../engine/render/sender/mesh_finalize/shy_mesh_finalize_injections.h"
#include "../../../engine/render/sender/mesh_render/shy_mesh_render_injections.h"
#include "../../../engine/render/sender/mesh_set_transform/shy_mesh_set_transform_injections.h"
#include "../../../engine/render/sender/mesh_set_triangle_strip_index_value/shy_mesh_set_triangle_strip_index_value_injections.h"
#include "../../../engine/render/sender/mesh_set_vertex_color/shy_mesh_set_vertex_color_injections.h"
#include "../../../engine/render/sender/mesh_set_vertex_position/shy_mesh_set_vertex_position_injections.h"
#include "../../../engine/render/sender/mesh_set_vertex_tex_coord/shy_mesh_set_vertex_tex_coord_injections.h"

#include "../../../../injections/platform/conditions/shy_conditions.h"
#include "../../../../injections/platform/math/consts/shy_consts.h"
#include "../../../../injections/platform/math/shy_math.h"
#include "../../../../injections/platform/matrix/shy_matrix.h"

#include "./shy_mesh.hpp"