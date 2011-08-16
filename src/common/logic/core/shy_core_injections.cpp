#include "./shy_core_injections.h"

#include "./sender/near_plane_distance_reply/shy_near_plane_distance_reply_injections.h"
#include "./sender/use_ortho_projection_reply/shy_use_ortho_projection_reply_injections.h"
#include "./sender/use_perspective_projection_reply/shy_use_perspective_projection_reply_injections.h"

#include "../application/sender/render/shy_render_injections.h"
#include "../application/sender/update/shy_update_injections.h"
#include "../fidget/sender/prepare_permit/shy_prepare_permit_injections.h"
#include "../fidget/sender/update/shy_update_injections.h"

#include "../../engine/render/sender/aspect_request/shy_aspect_request_injections.h"
#include "../../engine/render/sender/blend_disable/shy_blend_disable_injections.h"
#include "../../engine/render/sender/enable_face_culling/shy_enable_face_culling_injections.h"
#include "../../engine/render/sender/matrix_identity/shy_matrix_identity_injections.h"
#include "../../engine/render/sender/projection_frustum/shy_projection_frustum_injections.h"
#include "../../engine/render/sender/projection_ortho/shy_projection_ortho_injections.h"
#include "../../engine/render/sender/texture_mode_modulate/shy_texture_mode_modulate_injections.h"

#include "../../../injections/platform/conditions/shy_conditions.h"
#include "../../../injections/platform/math/consts/shy_consts.h"
#include "../../../injections/platform/math/shy_math.h"

#include "./shy_core.hpp"

