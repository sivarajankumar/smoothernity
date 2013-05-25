#ifndef CORE_VAO_H
#define CORE_VAO_H

#include "lua.h"

int vao_init(lua_State *lua, int count);
void vao_done(void);
int vao_bound(void);

#endif /* CORE_VAO_H */

