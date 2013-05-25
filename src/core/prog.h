#pragma once

#include "lua.h"
#include "GL/glew.h"

struct prog_t
{
    GLuint prog_id;
};

int prog_init(lua_State *lua, int count);
void prog_done(void);
struct prog_t * prog_get(int iprog);

