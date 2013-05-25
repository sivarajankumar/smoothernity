#ifndef CORE_THREAD_H
#define CORE_THREAD_H

#include "lua.h"

int thread_init(lua_State *lua, int count, const int msizes[],
                const int mcounts[], int mlen);
void thread_done(void);

#endif /* CORE_THREAD_H */

