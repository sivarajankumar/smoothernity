#include "input.h"
#include "SDL.h"

#define KEYS(op) \
    op(UP) op(DOWN) op(LEFT) op(RIGHT) op(PAGEUP) op(PAGEDOWN) \
    op(LCTRL) op(RCTRL) op(LSHIFT) op(RSHIFT) op(LALT) op(RALT) \
    op(ESCAPE) op(MINUS) op(EQUALS) op(SPACE) op(TAB) \
    op(F1) op(F2) op(F3) op(F4) op(F5) op(F6) \
    op(F7) op(F8) op(F9) op(F10) op(F11) op(F12) \
    op(1) op(2) op(3) op(4) op(5) op(6) op(7) op(8) op(9) op(0) \
    op(a) op(b) op(c) op(d) op(e) op(f) op(g) op(h) op(i) \
    op(j) op(k) op(l) op(m) op(n) op(o) op(p) op(q) op(r) \
    op(s) op(t) op(u) op(v) op(w) op(x) op(y) op(z)

enum input_key_e {
    #define DECL(x) INPUT_KEY_##x,
    KEYS(DECL)
    #undef DECL
    INPUT_KEYS_TOTAL
};

struct input_t {
    int keys[INPUT_KEYS_TOTAL];
};

static struct input_t g_input;

static int api_input_key(lua_State *lua) {
    int key;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, 1)) {
        lua_pushstring(lua, "api_input_key: incorrect argument");
        lua_error(lua);
        return 0;
    }
    key = lua_tointeger(lua, 1);
    lua_pop(lua, 1);

    if (key < 0 || key >= INPUT_KEYS_TOTAL) {
        lua_pushstring(lua, "api_input_key: invalid key code");
        lua_error(lua);
        return 0;
    }
    lua_pushinteger(lua, g_input.keys[key]);
    return 1;
}

static int api_input_update(lua_State *lua) {
    int value;
    SDL_Event event;
    if (lua_gettop(lua)) {
        lua_pushstring(lua, "api_input_update: incorrect argument");
        lua_error(lua);
        return 0;
    }
    while (SDL_PollEvent(&event)) {
        value = event.type == SDL_KEYDOWN;
        #define HANDLE(x) \
            if (event.key.keysym.sym == SDLK_##x) { \
                g_input.keys[INPUT_KEY_##x] = value; \
                continue; \
            }
        KEYS(HANDLE)
        #undef HANDLE
    }
    return 0;
}

void input_init(lua_State *lua) {
    lua_register(lua, "api_input_key", api_input_key);
    lua_register(lua, "api_input_update", api_input_update);
    #define REG(x) \
        lua_pushinteger(lua, INPUT_KEY_##x); \
        lua_setglobal(lua, "API_INPUT_KEY_"#x);
    KEYS(REG)
    #undef REG
}

