#include "timer.h"
#include "sys/time.h"

struct timer_t
{
    struct timeval time;
};

static struct timer_t g_timer;

static int api_timer(lua_State *lua)
{
    struct timeval cur;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_timer: incorrect argument");
        lua_error(lua);
        return 0;
    }
    gettimeofday(&cur, 0);
    lua_pushnumber(lua, 0.000001f *
        (float)(((cur.tv_sec - g_timer.time.tv_sec) * 1000000) +
                 (cur.tv_usec - g_timer.time.tv_usec)));
    return 1;
}

void timer_init(lua_State *lua)
{
    gettimeofday(&g_timer.time, 0);
    lua_register(lua, "api_timer", api_timer);
}
