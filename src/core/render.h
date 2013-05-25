#ifndef CORE_RENDER_H
#define CORE_RENDER_H

#include "lua.h"

int render_init(lua_State *lua, int width, int height, int full_screen);
void render_done(void);

#endif /* CORE_RENDER_H */

