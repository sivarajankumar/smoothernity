#include "./shy_mesh_injections.h"

#include "src/common/logic/blanket/consts/shy_consts_injections.h"
#include "src/common/logic/blanket/mesh/creation/finished/sender/shy_sender_injections.h"
#include "src/common/logic/blanket/mesh/render/reply/sender/shy_sender_injections.h"

#include "src/common/engine/render/mesh/create/request/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/finalize/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/render/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/transform/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/triangle/strip/index/value/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/vertex/color/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/vertex/position/sender/shy_sender_injections.h"

#include "src/injections/platform/conditions/shy_conditions.h"
#include "src/injections/platform/math/consts/shy_consts.h"
#include "src/injections/platform/math/shy_math.h"

#include "./shy_mesh.hpp"

