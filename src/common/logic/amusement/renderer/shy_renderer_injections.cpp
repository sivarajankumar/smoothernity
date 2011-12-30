#include "./shy_renderer_injections.h"

#include "src/common/logic/amusement/consts/shy_consts_injections.h"

#include "src/common/logic/blanket/render/request/sender/shy_sender_injections.h"
#include "src/common/logic/door/render/request/sender/shy_sender_injections.h"
#include "src/common/logic/observer/animation/transform/request/sender/shy_sender_injections.h"
#include "src/common/logic/ortho/planes/request/sender/shy_sender_injections.h"
#include "src/common/logic/perspective/planes/request/sender/shy_sender_injections.h"
#include "src/common/logic/room/render/request/sender/shy_sender_injections.h"

#include "src/common/engine/math/stateless/shy_stateless_injections.h"
#include "src/common/engine/render/clear/screen/sender/shy_sender_injections.h"
#include "src/common/engine/render/disable/depth/test/sender/shy_sender_injections.h"
#include "src/common/engine/render/enable/depth/test/sender/shy_sender_injections.h"
#include "src/common/engine/render/matrix/identity/sender/shy_sender_injections.h"
#include "src/common/engine/render/matrix/load/sender/shy_sender_injections.h"
#include "src/common/engine/render/matrix/mult/sender/shy_sender_injections.h"
#include "src/common/engine/render/projection/frustum/sender/shy_sender_injections.h"
#include "src/common/engine/render/projection/ortho/sender/shy_sender_injections.h"

#include "src/injections/platform/conditions/shy_conditions.h"
#include "src/injections/platform/math/consts/shy_consts.h"

#include "./shy_renderer.hpp"
