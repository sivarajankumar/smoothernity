#ifndef CTHREAD_H
#define CTHREAD_H

#include "lua.h"

int cthread_init(lua_State *lua, int count, const int msizes[],
                 const int mcounts[], int mlen);
void cthread_done(void);

#endif /* CTHREAD_H */

