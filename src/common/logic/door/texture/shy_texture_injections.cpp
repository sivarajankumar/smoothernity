#include "./shy_texture_injections.h"

#include "common/logic/door/consts/shy_consts_injections.h"
#include "common/logic/door/sender/texture_creation_finished/shy_texture_creation_finished_injections.h"
#include "common/logic/door/sender/texture_select_reply/shy_texture_select_reply_injections.h"

#include "common/engine/rasterizer/sender/draw_rect/shy_draw_rect_injections.h"
#include "common/engine/rasterizer/sender/finalize_request/shy_finalize_request_injections.h"
#include "common/engine/rasterizer/sender/use_texel/shy_use_texel_injections.h"
#include "common/engine/rasterizer/sender/use_texture/shy_use_texture_injections.h"
#include "common/engine/render/consts/shy_consts_injections.h"
#include "common/engine/render/sender/texture_create_request/shy_texture_create_request_injections.h"
#include "common/engine/render/sender/texture_finalize/shy_texture_finalize_injections.h"
#include "common/engine/render/sender/texture_select/shy_texture_select_injections.h"
#include "common/engine/render/stateless/shy_stateless_injections.h"

#include "injections/platform/conditions/shy_conditions.h"
#include "injections/platform/math/consts/shy_consts.h"
#include "injections/platform/math/shy_math.h"
#include "injections/platform/render/type/texel_data/shy_texel_data.h"

#include "./shy_texture.hpp"

