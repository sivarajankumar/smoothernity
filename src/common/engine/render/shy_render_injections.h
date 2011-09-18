#ifndef _shy_common_engine_render_injections_included
#define _shy_common_engine_render_injections_included

#include "src/common/engine/render/consts/shy_consts_injections.h"
#include "src/common/engine/render/aspect/request/message/shy_message_injections.h"
#include "src/common/engine/render/blend/disable/message/shy_message_injections.h"
#include "src/common/engine/render/blend/src/alpha/dst/one/minus/alpha/message/shy_message_injections.h"
#include "src/common/engine/render/clear/screen/message/shy_message_injections.h"
#include "src/common/engine/render/disable/depth/test/message/shy_message_injections.h"
#include "src/common/engine/render/enable/depth/test/message/shy_message_injections.h"
#include "src/common/engine/render/enable/face/culling/message/shy_message_injections.h"
#include "src/common/engine/render/fog/disable/message/shy_message_injections.h"
#include "src/common/engine/render/fog/linear/message/shy_message_injections.h"
#include "src/common/engine/render/frame/loss/request/message/shy_message_injections.h"
#include "src/common/engine/render/matrix/identity/message/shy_message_injections.h"
#include "src/common/engine/render/matrix/load/message/shy_message_injections.h"
#include "src/common/engine/render/matrix/mult/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/create/request/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/delete/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/finalize/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/render/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/set/transform/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/set/triangle/fan/index/value/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/set/triangle/strip/index/value/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/set/vertex/color/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/set/vertex/position/message/shy_message_injections.h"
#include "src/common/engine/render/mesh/set/vertex/tex/coord/message/shy_message_injections.h"
#include "src/common/engine/render/projection/frustum/message/shy_message_injections.h"
#include "src/common/engine/render/projection/ortho/message/shy_message_injections.h"
#include "src/common/engine/render/texture/create/request/message/shy_message_injections.h"
#include "src/common/engine/render/texture/finalize/message/shy_message_injections.h"
#include "src/common/engine/render/texture/load/from/resource/message/shy_message_injections.h"
#include "src/common/engine/render/texture/loader/ready/request/message/shy_message_injections.h"
#include "src/common/engine/render/texture/mode/modulate/message/shy_message_injections.h"
#include "src/common/engine/render/texture/select/message/shy_message_injections.h"
#include "src/common/engine/render/texture/set/texel/message/shy_message_injections.h"
#include "src/common/engine/render/texture/set/texel/rgba/message/shy_message_injections.h"
#include "src/common/engine/render/texture/set/texels/rect/message/shy_message_injections.h"
#include "src/common/engine/render/texture/unselect/message/shy_message_injections.h"

#include "src/common/done/message/shy_message_injections.h"
#include "src/common/init/message/shy_message_injections.h"

#include "src/injections/platform/scheduler/shy_scheduler.h"

#include "./shy_render.h"

typedef shy_common_engine_render_scheduled so_called_common_engine_render ;

#endif
