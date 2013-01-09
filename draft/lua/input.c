#include <SDL.h>
#include "input.h"

struct input_t
{
    int key_escape;
};

static struct input_t g_input;

static int api_input_key_escape(lua_State *lua)
{
    if (lua_gettop(lua) == 0)
    {
        lua_pushinteger(lua, g_input.key_escape);
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_input_key_escape: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

void input_init(lua_State *lua)
{
    lua_register(lua, "api_input_key_escape", api_input_key_escape);
}

void input_update(void)
{
    SDL_Event event;
    g_input.key_escape = 0;
    while (SDL_PollEvent(&event))
    {
        if (event.type == SDL_KEYDOWN)
        {
            if (event.key.keysym.sym == SDLK_ESCAPE)
                g_input.key_escape = 1;
        }
    }
}
