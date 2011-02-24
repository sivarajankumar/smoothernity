#include "./shy_renderer_injections.h"

#include "../consts/shy_consts_injections.h"

#include "../../observer/animation/sender/transform_request/shy_transform_request_injections.h"
#include "../../ortho/sender/planes_request/shy_planes_request_injections.h"
#include "../../perspective/sender/planes_request/shy_planes_request_injections.h"

#include "../../../engine/math/stateless/shy_stateless_injections.h"
#include "../../../engine/render/sender/clear_screen/shy_clear_screen_injections.h"
#include "../../../engine/render/sender/disable_depth_test/shy_disable_depth_test_injections.h"
#include "../../../engine/render/sender/enable_depth_test/shy_enable_depth_test_injections.h"
#include "../../../engine/render/sender/matrix_identity/shy_matrix_identity_injections.h"
#include "../../../engine/render/sender/matrix_load/shy_matrix_load_injections.h"
#include "../../../engine/render/sender/matrix_mult/shy_matrix_mult_injections.h"
#include "../../../engine/render/sender/projection_frustum/shy_projection_frustum_injections.h"
#include "../../../engine/render/sender/projection_ortho/shy_projection_ortho_injections.h"

#include "../../../../injections/platform/conditions/shy_conditions.h"
#include "../../../../injections/platform/math/consts/shy_consts.h"

#include "./shy_renderer.hpp"
