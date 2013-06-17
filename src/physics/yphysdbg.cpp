#include "yphysdbg.h"
#include "LinearMath/btIDebugDraw.h"

#define DECL(x) const int YPHYSDBG_##x = btIDebugDraw::DBG_##x;
YPHYSDBG(DECL)
#undef DECL

