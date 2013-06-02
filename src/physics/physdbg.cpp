#include "physdbg.h"
#include "LinearMath/btIDebugDraw.h"

#define DECL(x) const int PHYSDBG_##x = btIDebugDraw::DBG_##x;
PHYSDBG(DECL)
#undef DECL

