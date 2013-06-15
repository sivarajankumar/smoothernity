#ifndef CRBUF_H
#define CRBUF_H

#include "GL/glew.h"
#include "lua.h"

struct crbuf_t {
    GLuint buf_id;
    int size, mapped_ofs, mapped_len;
    GLvoid *mapped;
    GLenum target, item;
};

int crbuf_init(lua_State *lua, int count);
void crbuf_done(void);
void crbuf_reg_thread(lua_State *lua);
struct crbuf_t * crbuf_get(int);

#endif /* CRBUF_H */

