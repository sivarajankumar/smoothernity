#ifndef CRENDER_H
#define CRENDER_H

#include "lua.h"

int crender_init(lua_State *lua, int width, int height, int full_screen);
void crender_done(void);

#endif /* CRENDER_H */

