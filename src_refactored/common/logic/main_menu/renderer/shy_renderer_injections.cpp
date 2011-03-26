#include "./shy_renderer_injections.h"

#include "../animation/sender/transform_request/shy_transform_request_injections.h"
#include "../letters/meshes/sender/render_request/shy_render_request_injections.h"

#include "../../fidget/sender/render_request/shy_render_request_injections.h"
#include "../../ortho/sender/planes_request/shy_planes_request_injections.h"
#include "../../text/sender/use_text_texture_request/shy_use_text_texture_request_injections.h"

#include "../../../engine/render/sender/blend_disable/shy_blend_disable_injections.h"
#include "../../../engine/render/sender/blend_src_alpha_dst_one_minus_alpha/shy_blend_src_alpha_dst_one_minus_alpha_injections.h"
#include "../../../engine/render/sender/clear_screen/shy_clear_screen_injections.h"
#include "../../../engine/render/sender/disable_depth_test/shy_disable_depth_test_injections.h"
#include "../../../engine/render/sender/fog_disable/shy_fog_disable_injections.h"
#include "../../../engine/render/sender/matrix_identity/shy_matrix_identity_injections.h"
#include "../../../engine/render/sender/matrix_load/shy_matrix_load_injections.h"
#include "../../../engine/render/sender/projection_ortho/shy_projection_ortho_injections.h"

#include "../../../../injections/platform/conditions/shy_conditions.h"
#include "../../../../injections/platform/math/consts/shy_consts.h"

#include "./shy_renderer.hpp"
