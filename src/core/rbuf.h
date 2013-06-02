#ifndef CORE_RBUF_H
#define CORE_RBUF_H

#include "GL/glew.h"
#include "lua.h"

struct rbuf_t {
    GLuint buf_id;
    int size, mapped_ofs, mapped_len;
    GLvoid *mapped;
    GLenum target, item;
};

int rbuf_init(lua_State *lua, int count);
void rbuf_done(void);
void rbuf_reg_thread(lua_State *lua);
struct rbuf_t * rbuf_get(int);

#endif /* CORE_RBUF_H */

