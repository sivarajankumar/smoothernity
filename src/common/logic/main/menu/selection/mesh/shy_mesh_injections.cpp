#include "./shy_mesh_injections.h"

#include "common/logic/main/menu/selection/animation/transform/request/sender/shy_sender_injections.h"
#include "common/logic/main/menu/selection/consts/shy_consts_injections.h"
#include "common/logic/main/menu/selection/mesh/create/finished/sender/shy_sender_injections.h"
#include "common/logic/main/menu/selection/mesh/destroy/reply/sender/shy_sender_injections.h"
#include "common/logic/main/menu/selection/mesh/render/reply/sender/shy_sender_injections.h"

#include "common/engine/render/mesh/create/request/sender/shy_sender_injections.h"
#include "common/engine/render/mesh/delete/sender/shy_sender_injections.h"
#include "common/engine/render/mesh/finalize/sender/shy_sender_injections.h"
#include "common/engine/render/mesh/render/sender/shy_sender_injections.h"
#include "common/engine/render/mesh/set/transform/sender/shy_sender_injections.h"
#include "common/engine/render/mesh/set/triangle/strip/index/value/sender/shy_sender_injections.h"
#include "common/engine/render/mesh/set/vertex/color/sender/shy_sender_injections.h"
#include "common/engine/render/mesh/set/vertex/position/sender/shy_sender_injections.h"
#include "common/engine/render/texture/unselect/sender/shy_sender_injections.h"

#include "injections/platform/conditions/shy_conditions.h"
#include "injections/platform/math/consts/shy_consts.h"
#include "injections/platform/math/shy_math.h"
#include "injections/platform/matrix/shy_matrix.h"

#include "./shy_mesh.hpp"

