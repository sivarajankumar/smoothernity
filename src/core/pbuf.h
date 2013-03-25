#pragma once

#include <lua.h>
#include <GL/glew.h>

enum pbuf_e
{
    PBUF_UNMAPPING,
    PBUF_UNMAPPED,
    PBUF_MAPPING,
    PBUF_MAPPED,
    PBUF_ERROR
};

struct pbuf_t
{
    GLuint buf_id;
    int size;
    int mapped_ofs;
    int mapped_len;
    GLvoid *mapped;
    enum pbuf_e state;
};

struct pbuf_data_t
{
    GLubyte color[4];
};

int pbuf_init(lua_State *lua, int *sizes, int count);
void pbuf_done(void);
void pbuf_reg_thread(lua_State *lua);
struct pbuf_t * pbuf_get(int);
int pbuf_thread(void);
