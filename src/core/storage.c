#include "storage.h"
#include <pthread.h>

int storage_init(lua_State *lua, int size, int count)
{
    if (size <= 0 || count <= 0 || lua == 0)
        return -1;
    return 0;
}

void storage_done(void)
{
}
