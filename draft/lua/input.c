#include <SDL.h>
#include "input.h"

enum input_key_e
{
    INPUT_KEY_ESCAPE = 0,
    INPUT_KEY_UP = 1,
    INPUT_KEY_DOWN = 2,
    INPUT_KEY_LEFT = 3,
    INPUT_KEY_RIGHT = 4,
    INPUT_KEY_PAGEUP = 5,
    INPUT_KEY_PAGEDOWN = 6,
    INPUT_KEY_W = 7,
    INPUT_KEY_S = 8,
    INPUT_KEY_A = 9,
    INPUT_KEY_D = 10,
    INPUT_KEYS_TOTAL = 11
};

struct input_t
{
    char keys[INPUT_KEYS_TOTAL];
};

static struct input_t g_input;

static int api_input_key(lua_State *lua)
{
    int key;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_input_key: incorrect argument");
        lua_error(lua);
        return 0;
    }
    key = lua_tointeger(lua, -1);
    lua_pop(lua, 1);

    if (key < 0 || key >= (int)INPUT_KEYS_TOTAL)
    {
        lua_pushstring(lua, "api_input_key: invalid key code");
        lua_error(lua);
        return 0;
    }
    
    lua_pushinteger(lua, g_input.keys[key]);
    return 1;
}

void input_init(lua_State *lua)
{
    lua_register(lua, "api_input_key", api_input_key);
}

void input_update(void)
{
    SDL_Event event;
    memset(g_input.keys, 0, (size_t)INPUT_KEYS_TOTAL * sizeof(char));
    while (SDL_PollEvent(&event))
    {
        if (event.type == SDL_KEYDOWN)
        {
            if (event.key.keysym.sym == SDLK_ESCAPE)
                g_input.keys[INPUT_KEY_ESCAPE] = 1;
            else if (event.key.keysym.sym == SDLK_UP)
                g_input.keys[INPUT_KEY_UP] = 1;
            else if (event.key.keysym.sym == SDLK_DOWN)
                g_input.keys[INPUT_KEY_DOWN] = 1;
            else if (event.key.keysym.sym == SDLK_LEFT)
                g_input.keys[INPUT_KEY_LEFT] = 1;
            else if (event.key.keysym.sym == SDLK_RIGHT)
                g_input.keys[INPUT_KEY_RIGHT] = 1;
            else if (event.key.keysym.sym == SDLK_PAGEUP)
                g_input.keys[INPUT_KEY_PAGEUP] = 1;
            else if (event.key.keysym.sym == SDLK_PAGEDOWN)
                g_input.keys[INPUT_KEY_PAGEDOWN] = 1;
            else if (event.key.keysym.sym == SDLK_w)
                g_input.keys[INPUT_KEY_W] = 1;
            else if (event.key.keysym.sym == SDLK_s)
                g_input.keys[INPUT_KEY_S] = 1;
            else if (event.key.keysym.sym == SDLK_a)
                g_input.keys[INPUT_KEY_A] = 1;
            else if (event.key.keysym.sym == SDLK_d)
                g_input.keys[INPUT_KEY_D] = 1;
        }
    }
}
