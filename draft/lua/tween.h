#pragma once

#include <lua.h>

enum tween_e
{
    TWEEN_SINE = 0,
    TWEEN_SAW = 1
};

struct tween_t
{
    enum tween_e type;
    int working;
    float shift;
    float ampl;
    float period;
    float t;
    float value;
    struct tween_t *next;
    struct tween_t *prev;
};

int tween_init(lua_State *lua, int len);
void tween_done(void);
void tween_update(float dt);
struct tween_t * tween_get(int);
