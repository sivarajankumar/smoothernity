#ifndef CPROG_H
#define CPROG_H

#include "lua.h"
#include "GL/glew.h"

struct cprog_t {
    GLuint prog_id;
};

int cprog_init(lua_State *lua, int count);
void cprog_done(void);
struct cprog_t * cprog_get(int iprog);

#endif /* CPROG_H */

