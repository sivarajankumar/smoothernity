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
    INPUT_KEY_MINUS = 7,
    INPUT_KEY_EQUALS = 8,
    INPUT_KEY_SPACE = 9,
    INPUT_KEY_LSHIFT = 10,
    INPUT_KEY_RSHIFT = 11,
    INPUT_KEY_LALT = 12,
    INPUT_KEY_RALT = 13,
    INPUT_KEY_LCTRL = 14,
    INPUT_KEY_RCTRL = 15,
    INPUT_KEY_TAB = 16,
    INPUT_KEY_F1 = 17,
    INPUT_KEY_F2 = 18,
    INPUT_KEY_F3 = 19,
    INPUT_KEY_F4 = 20,
    INPUT_KEY_F5 = 21,
    INPUT_KEY_F6 = 22,
    INPUT_KEY_F7 = 23,
    INPUT_KEY_F8 = 24,
    INPUT_KEY_F9 = 25,
    INPUT_KEY_F10 = 26,
    INPUT_KEY_F11 = 27,
    INPUT_KEY_F12 = 28,
    INPUT_KEY_1 = 29,
    INPUT_KEY_2 = 30,
    INPUT_KEY_3 = 31,
    INPUT_KEY_4 = 32,
    INPUT_KEY_5 = 33,
    INPUT_KEY_6 = 34,
    INPUT_KEY_7 = 35,
    INPUT_KEY_8 = 36,
    INPUT_KEY_9 = 37,
    INPUT_KEY_0 = 38,
    INPUT_KEY_A = 39,
    INPUT_KEY_B = 40,
    INPUT_KEY_C = 41,
    INPUT_KEY_D = 42,
    INPUT_KEY_E = 43,
    INPUT_KEY_F = 44,
    INPUT_KEY_G = 45,
    INPUT_KEY_H = 46,
    INPUT_KEY_I = 47,
    INPUT_KEY_J = 48,
    INPUT_KEY_K = 49,
    INPUT_KEY_L = 50,
    INPUT_KEY_M = 51,
    INPUT_KEY_N = 52,
    INPUT_KEY_O = 53,
    INPUT_KEY_P = 54,
    INPUT_KEY_Q = 55,
    INPUT_KEY_R = 56,
    INPUT_KEY_S = 57,
    INPUT_KEY_T = 58,
    INPUT_KEY_U = 59,
    INPUT_KEY_V = 60,
    INPUT_KEY_W = 61,
    INPUT_KEY_X = 62,
    INPUT_KEY_Y = 63,
    INPUT_KEY_Z = 64,
    INPUT_KEYS_TOTAL = 65
};

struct input_t
{
    char keys[INPUT_KEYS_TOTAL];
};

static struct input_t g_input;

static int api_input_key(lua_State *lua)
{
    int key;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1))
    {
        lua_pushstring(lua, "api_input_key: incorrect argument");
        lua_error(lua);
        return 0;
    }
    key = lua_tointeger(lua, 1);
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

static int api_input_update(lua_State *lua)
{
    char value;
    SDL_Event event;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_input_update: incorrect argument");
        lua_error(lua);
        return 0;
    }
    while (SDL_PollEvent(&event))
    {
        if (event.type == SDL_KEYDOWN)
            value = 1;
        else
            value = 0;

        #define HANDLE_KEY(x, y) \
            if (event.key.keysym.sym == x) \
            { \
                g_input.keys[y] = value; \
                continue; \
            }

        HANDLE_KEY(SDLK_ESCAPE, INPUT_KEY_ESCAPE);
        HANDLE_KEY(SDLK_UP, INPUT_KEY_UP);
        HANDLE_KEY(SDLK_DOWN, INPUT_KEY_DOWN);
        HANDLE_KEY(SDLK_LEFT, INPUT_KEY_LEFT);
        HANDLE_KEY(SDLK_RIGHT, INPUT_KEY_RIGHT);
        HANDLE_KEY(SDLK_PAGEUP, INPUT_KEY_PAGEUP);
        HANDLE_KEY(SDLK_PAGEDOWN, INPUT_KEY_PAGEDOWN);
        HANDLE_KEY(SDLK_MINUS, INPUT_KEY_MINUS);
        HANDLE_KEY(SDLK_EQUALS, INPUT_KEY_EQUALS);
        HANDLE_KEY(SDLK_SPACE, INPUT_KEY_SPACE);
        HANDLE_KEY(SDLK_LSHIFT, INPUT_KEY_LSHIFT);
        HANDLE_KEY(SDLK_RSHIFT, INPUT_KEY_RSHIFT);
        HANDLE_KEY(SDLK_LALT, INPUT_KEY_LALT);
        HANDLE_KEY(SDLK_RALT, INPUT_KEY_RALT);
        HANDLE_KEY(SDLK_LCTRL, INPUT_KEY_LCTRL);
        HANDLE_KEY(SDLK_RCTRL, INPUT_KEY_RCTRL);
        HANDLE_KEY(SDLK_TAB, INPUT_KEY_TAB);
        HANDLE_KEY(SDLK_F1, INPUT_KEY_F1);
        HANDLE_KEY(SDLK_F2, INPUT_KEY_F2);
        HANDLE_KEY(SDLK_F3, INPUT_KEY_F3);
        HANDLE_KEY(SDLK_F4, INPUT_KEY_F4);
        HANDLE_KEY(SDLK_F5, INPUT_KEY_F5);
        HANDLE_KEY(SDLK_F6, INPUT_KEY_F6);
        HANDLE_KEY(SDLK_F7, INPUT_KEY_F7);
        HANDLE_KEY(SDLK_F8, INPUT_KEY_F8);
        HANDLE_KEY(SDLK_F9, INPUT_KEY_F9);
        HANDLE_KEY(SDLK_F10, INPUT_KEY_F10);
        HANDLE_KEY(SDLK_F11, INPUT_KEY_F11);
        HANDLE_KEY(SDLK_F12, INPUT_KEY_F12);
        HANDLE_KEY(SDLK_1, INPUT_KEY_1);
        HANDLE_KEY(SDLK_2, INPUT_KEY_2);
        HANDLE_KEY(SDLK_3, INPUT_KEY_3);
        HANDLE_KEY(SDLK_4, INPUT_KEY_4);
        HANDLE_KEY(SDLK_5, INPUT_KEY_5);
        HANDLE_KEY(SDLK_6, INPUT_KEY_6);
        HANDLE_KEY(SDLK_7, INPUT_KEY_7);
        HANDLE_KEY(SDLK_8, INPUT_KEY_8);
        HANDLE_KEY(SDLK_9, INPUT_KEY_9);
        HANDLE_KEY(SDLK_0, INPUT_KEY_0);
        HANDLE_KEY(SDLK_a, INPUT_KEY_A);
        HANDLE_KEY(SDLK_b, INPUT_KEY_B);
        HANDLE_KEY(SDLK_c, INPUT_KEY_C);
        HANDLE_KEY(SDLK_d, INPUT_KEY_D);
        HANDLE_KEY(SDLK_e, INPUT_KEY_E);
        HANDLE_KEY(SDLK_f, INPUT_KEY_F);
        HANDLE_KEY(SDLK_g, INPUT_KEY_G);
        HANDLE_KEY(SDLK_h, INPUT_KEY_H);
        HANDLE_KEY(SDLK_i, INPUT_KEY_I);
        HANDLE_KEY(SDLK_j, INPUT_KEY_J);
        HANDLE_KEY(SDLK_k, INPUT_KEY_K);
        HANDLE_KEY(SDLK_l, INPUT_KEY_L);
        HANDLE_KEY(SDLK_m, INPUT_KEY_M);
        HANDLE_KEY(SDLK_n, INPUT_KEY_N);
        HANDLE_KEY(SDLK_o, INPUT_KEY_O);
        HANDLE_KEY(SDLK_p, INPUT_KEY_P);
        HANDLE_KEY(SDLK_q, INPUT_KEY_Q);
        HANDLE_KEY(SDLK_r, INPUT_KEY_R);
        HANDLE_KEY(SDLK_s, INPUT_KEY_S);
        HANDLE_KEY(SDLK_t, INPUT_KEY_T);
        HANDLE_KEY(SDLK_u, INPUT_KEY_U);
        HANDLE_KEY(SDLK_v, INPUT_KEY_V);
        HANDLE_KEY(SDLK_w, INPUT_KEY_W);
        HANDLE_KEY(SDLK_x, INPUT_KEY_X);
        HANDLE_KEY(SDLK_y, INPUT_KEY_Y);
        HANDLE_KEY(SDLK_z, INPUT_KEY_Z);
    }
    return 0;
}

void input_init(lua_State *lua)
{
    lua_register(lua, "api_input_key", api_input_key);
    lua_register(lua, "api_input_update", api_input_update);

    #define LUA_PUBLISH(x) \
        lua_pushinteger(lua, x); \
        lua_setglobal(lua, "API_"#x);

    LUA_PUBLISH(INPUT_KEY_ESCAPE);
    LUA_PUBLISH(INPUT_KEY_UP);
    LUA_PUBLISH(INPUT_KEY_DOWN);
    LUA_PUBLISH(INPUT_KEY_LEFT);
    LUA_PUBLISH(INPUT_KEY_RIGHT);
    LUA_PUBLISH(INPUT_KEY_PAGEUP);
    LUA_PUBLISH(INPUT_KEY_PAGEDOWN);
    LUA_PUBLISH(INPUT_KEY_MINUS);
    LUA_PUBLISH(INPUT_KEY_EQUALS);
    LUA_PUBLISH(INPUT_KEY_SPACE);
    LUA_PUBLISH(INPUT_KEY_LSHIFT);
    LUA_PUBLISH(INPUT_KEY_RSHIFT);
    LUA_PUBLISH(INPUT_KEY_LALT);
    LUA_PUBLISH(INPUT_KEY_RALT);
    LUA_PUBLISH(INPUT_KEY_LCTRL);
    LUA_PUBLISH(INPUT_KEY_RCTRL);
    LUA_PUBLISH(INPUT_KEY_TAB);
    LUA_PUBLISH(INPUT_KEY_F1);
    LUA_PUBLISH(INPUT_KEY_F2);
    LUA_PUBLISH(INPUT_KEY_F3);
    LUA_PUBLISH(INPUT_KEY_F4);
    LUA_PUBLISH(INPUT_KEY_F5);
    LUA_PUBLISH(INPUT_KEY_F6);
    LUA_PUBLISH(INPUT_KEY_F7);
    LUA_PUBLISH(INPUT_KEY_F8);
    LUA_PUBLISH(INPUT_KEY_F9);
    LUA_PUBLISH(INPUT_KEY_F10);
    LUA_PUBLISH(INPUT_KEY_F11);
    LUA_PUBLISH(INPUT_KEY_F12);
    LUA_PUBLISH(INPUT_KEY_1);
    LUA_PUBLISH(INPUT_KEY_2);
    LUA_PUBLISH(INPUT_KEY_3);
    LUA_PUBLISH(INPUT_KEY_4);
    LUA_PUBLISH(INPUT_KEY_5);
    LUA_PUBLISH(INPUT_KEY_6);
    LUA_PUBLISH(INPUT_KEY_7);
    LUA_PUBLISH(INPUT_KEY_8);
    LUA_PUBLISH(INPUT_KEY_9);
    LUA_PUBLISH(INPUT_KEY_0);
    LUA_PUBLISH(INPUT_KEY_A);
    LUA_PUBLISH(INPUT_KEY_B);
    LUA_PUBLISH(INPUT_KEY_C);
    LUA_PUBLISH(INPUT_KEY_D);
    LUA_PUBLISH(INPUT_KEY_E);
    LUA_PUBLISH(INPUT_KEY_F);
    LUA_PUBLISH(INPUT_KEY_G);
    LUA_PUBLISH(INPUT_KEY_H);
    LUA_PUBLISH(INPUT_KEY_I);
    LUA_PUBLISH(INPUT_KEY_J);
    LUA_PUBLISH(INPUT_KEY_K);
    LUA_PUBLISH(INPUT_KEY_L);
    LUA_PUBLISH(INPUT_KEY_M);
    LUA_PUBLISH(INPUT_KEY_N);
    LUA_PUBLISH(INPUT_KEY_O);
    LUA_PUBLISH(INPUT_KEY_P);
    LUA_PUBLISH(INPUT_KEY_Q);
    LUA_PUBLISH(INPUT_KEY_R);
    LUA_PUBLISH(INPUT_KEY_S);
    LUA_PUBLISH(INPUT_KEY_T);
    LUA_PUBLISH(INPUT_KEY_U);
    LUA_PUBLISH(INPUT_KEY_V);
    LUA_PUBLISH(INPUT_KEY_W);
    LUA_PUBLISH(INPUT_KEY_X);
    LUA_PUBLISH(INPUT_KEY_Y);
    LUA_PUBLISH(INPUT_KEY_Z);
}
