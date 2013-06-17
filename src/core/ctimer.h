#ifndef CTIMER_H
#define CTIMER_H

#include "lua.h"
int ctimer_init(lua_State*);
void ctimer_reg_thread(lua_State*);

#endif /* CTIMER_H */

