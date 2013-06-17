#ifndef CVAO_H
#define CVAO_H

#include "lua.h"

int cvao_init(lua_State *lua, int count);
void cvao_done(void);
int cvao_bound(void);

#endif /* CVAO_H */

