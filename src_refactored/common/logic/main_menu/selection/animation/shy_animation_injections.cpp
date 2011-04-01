#include "./shy_animation_injections.h"

#include "./sender/appear_transform_request/shy_appear_transform_request_injections.h"
#include "./sender/disappear_transform_request/shy_disappear_transform_request_injections.h"
#include "./sender/idle_attention_transform_request/shy_idle_attention_transform_request_injections.h"
#include "./sender/idle_transform_request/shy_idle_transform_request_injections.h"
#include "./sender/push_attention_transform_request/shy_push_attention_transform_request_injections.h"
#include "./sender/push_transform_request/shy_push_transform_request_injections.h"
#include "./sender/push_weight_request/shy_push_weight_request_injections.h"
#include "./sender/select_transform_request/shy_select_transform_request_injections.h"
#include "./sender/transform_reply/shy_transform_reply_injections.h"
#include "./sender/unselect_transform_request/shy_unselect_transform_request_injections.h"

#include "../../../../engine/math/stateless/shy_stateless_injections.h"

#include "../../../../../injections/platform/conditions/shy_conditions.h"
#include "../../../../../injections/platform/math/consts/shy_consts.h"
#include "../../../../../injections/platform/math/shy_math.h"
#include "../../../../../injections/platform/matrix/shy_matrix.h"

#include "./shy_animation.hpp"
