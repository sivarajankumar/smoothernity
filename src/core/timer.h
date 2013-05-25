#ifndef CORE_TIMER_H
#define CORE_TIMER_H

#include "lua.h"
int timer_init(lua_State*);
void timer_reg_thread(lua_State*);

#endif /* CORE_TIMER_H */

