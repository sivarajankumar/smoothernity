#pragma once

#include "GL/glew.h"
#include "lua.h"

struct rbuf_t
{
    GLuint buf_id;
    int size;
    int mapped_ofs;
    int mapped_len;
    GLvoid *mapped;
    GLenum target;
    GLenum item;
};

int rbuf_init(lua_State *lua, int count);
void rbuf_done(void);
void rbuf_reg_thread(lua_State *lua);
struct rbuf_t * rbuf_get(int);

