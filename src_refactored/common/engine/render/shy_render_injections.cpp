#include "./shy_render_injections.h"

#include "./consts/shy_consts_injections.h"
#include "./sender/aspect_reply/shy_aspect_reply_injections.h"
#include "./sender/mesh_create_reply/shy_mesh_create_reply_injections.h"
#include "./sender/texture_create_reply/shy_texture_create_reply_injections.h"
#include "./sender/texture_loader_ready_reply/shy_texture_loader_ready_reply_injections.h"

#include "../../../injections/platform/conditions/shy_conditions.h"
#include "../../../injections/platform/math/shy_math.h"
#include "../../../injections/platform/math/consts/shy_consts.h"
#include "../../../injections/platform/math/type/const_int_32/shy_const_int_32.h"
#include "../../../injections/platform/matrix/shy_matrix.h"
#include "../../../injections/platform/render/shy_render.h"
#include "../../../injections/platform/render/type/texture_id/shy_texture_id.h"
#include "../../../injections/platform/render/type/index_buffer_id/shy_index_buffer_id.h"
#include "../../../injections/platform/render/type/index_buffer_mapped_data/shy_index_buffer_mapped_data.h"
#include "../../../injections/platform/render/type/vertex_buffer_id/shy_vertex_buffer_id.h"
#include "../../../injections/platform/render/type/vertex_buffer_mapped_data/shy_vertex_buffer_mapped_data.h"
#include "../../../injections/platform/static_array/type/data/shy_data.h"
#include "../../../injections/platform/static_array/shy_static_array.h"

#include "./shy_render.hpp"

