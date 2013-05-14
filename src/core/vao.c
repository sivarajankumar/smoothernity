#include "vao.h"

int vao_init(lua_State *lua, int count)
{
    if (lua == 0 || count == 0) /* TODO */
        return 0;
    return 1;
}

void vao_done(void)
{
}
