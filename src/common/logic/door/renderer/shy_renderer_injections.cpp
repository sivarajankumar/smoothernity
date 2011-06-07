#include "./shy_renderer_injections.h"

#include "../sender/mesh_render_request/shy_mesh_render_request_injections.h"
#include "../sender/render_reply/shy_render_reply_injections.h"
#include "../sender/texture_select_request/shy_texture_select_request_injections.h"

#include "../../../engine/render/sender/blend_disable/shy_blend_disable_injections.h"
#include "../../../engine/render/sender/disable_depth_test/shy_disable_depth_test_injections.h"
#include "../../../engine/render/sender/texture_unselect/shy_texture_unselect_injections.h"

#include "../../../../injections/platform/conditions/shy_conditions.h"
#include "../../../../injections/platform/math/consts/shy_consts.h"

#include "./shy_renderer.hpp"