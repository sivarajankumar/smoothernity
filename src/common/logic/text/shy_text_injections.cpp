#include "./shy_text_injections.h"

#include "src/common/logic/text/consts/shy_consts_injections.h"
#include "src/common/logic/text/letter/big/tex/coords/reply/sender/shy_sender_injections.h"
#include "src/common/logic/text/letter/small/tex/coords/reply/sender/shy_sender_injections.h"
#include "src/common/logic/text/prepared/sender/shy_sender_injections.h"
#include "src/common/logic/text/render/reply/sender/shy_sender_injections.h"
#include "src/common/logic/text/use/text/texture/reply/sender/shy_sender_injections.h"
#include "src/common/logic/text/stateless/shy_stateless_injections.h"

#include "src/common/engine/math/stateless/shy_stateless_injections.h"
#include "src/common/engine/rasterizer/draw/ellipse/in/rect/sender/shy_sender_injections.h"
#include "src/common/engine/rasterizer/draw/rect/sender/shy_sender_injections.h"
#include "src/common/engine/rasterizer/draw/triangle/sender/shy_sender_injections.h"
#include "src/common/engine/rasterizer/finalize/request/sender/shy_sender_injections.h"
#include "src/common/engine/rasterizer/use/texel/sender/shy_sender_injections.h"
#include "src/common/engine/rasterizer/use/texture/sender/shy_sender_injections.h"
#include "src/common/engine/render/consts/shy_consts_injections.h"
#include "src/common/engine/render/blend/disable/sender/shy_sender_injections.h"
#include "src/common/engine/render/blend/src/alpha/dst/one/minus/alpha/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/create/request/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/finalize/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/render/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/transform/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/triangle/strip/index/value/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/vertex/color/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/vertex/position/sender/shy_sender_injections.h"
#include "src/common/engine/render/mesh/set/vertex/tex/coord/sender/shy_sender_injections.h"
#include "src/common/engine/render/texture/create/request/sender/shy_sender_injections.h"
#include "src/common/engine/render/texture/finalize/sender/shy_sender_injections.h"
#include "src/common/engine/render/texture/select/sender/shy_sender_injections.h"
#include "src/common/engine/render/texture/set/texels/rect/sender/shy_sender_injections.h"
#include "src/common/engine/render/stateless/shy_stateless_injections.h"

#include "src/injections/platform/conditions/shy_conditions.h"
#include "src/injections/platform/math/consts/shy_consts.h"
#include "src/injections/platform/math/shy_math.h"
#include "src/injections/platform/matrix/shy_matrix.h"
#include "src/injections/platform/pointer/data/type/shy_type.h"
#include "src/injections/platform/render/texel/data/type/shy_type.h"
#include "src/injections/platform/static/array/shy_array.h"
#include "src/injections/platform/static/array/data/type/shy_type.h"

#include "./shy_text.hpp"
