#include "./shy_renderer_injections.h"

#include "src/common/logic/main/menu/animation/transform/request/sender/shy_sender_injections.h"
#include "src/common/logic/main/menu/letters/meshes/render/request/sender/shy_sender_injections.h"
#include "src/common/logic/main/menu/selection/mesh/render/request/sender/shy_sender_injections.h"

#include "src/common/logic/fidget/render/request/sender/shy_sender_injections.h"
#include "src/common/logic/ortho/planes/request/sender/shy_sender_injections.h"
#include "src/common/logic/text/use/text/texture/request/sender/shy_sender_injections.h"

#include "src/common/engine/render/blend/disable/sender/shy_sender_injections.h"
#include "src/common/engine/render/blend/src/alpha/dst/one/minus/alpha/sender/shy_sender_injections.h"
#include "src/common/engine/render/clear/screen/sender/shy_sender_injections.h"
#include "src/common/engine/render/disable/depth/test/sender/shy_sender_injections.h"
#include "src/common/engine/render/fog/disable/sender/shy_sender_injections.h"
#include "src/common/engine/render/matrix/identity/sender/shy_sender_injections.h"
#include "src/common/engine/render/matrix/load/sender/shy_sender_injections.h"
#include "src/common/engine/render/projection/ortho/sender/shy_sender_injections.h"

#include "src/injections/platform/conditions/shy_conditions.h"
#include "src/injections/platform/math/consts/shy_consts.h"

#include "./shy_renderer.hpp"
