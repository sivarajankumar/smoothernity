#include "tween.h"
#include "consts.h"
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

struct tweens_t
{
    int pool_len;
    struct tween_t *pool;
    struct tween_t *working;
    struct tween_t *sleeping;
};

static struct tweens_t g_tweens;

static void calc_value(struct tween_t *tween)
{
    if (tween->type == TWEEN_SINE)
    {
        tween->value = tween->shift +
            (tween->ampl * sin(tween->t * M_PI * 2.0f / tween->period));
    }
    else if (tween->type == TWEEN_SAW)
        tween->value = tween->shift + (tween->ampl * tween->t / tween->period);
}

static int api_tween_alloc(lua_State *lua)
{
    struct tween_t *tween;
    if (lua_gettop(lua) != 0)
    {
        lua_pushstring(lua, "api_tween_alloc: incorrect argument");
        lua_error(lua);
        return 0;
    }
    if (g_tweens.sleeping == 0)
    {
        lua_pushstring(lua, "api_tween_alloc: out of tweens");
        lua_error(lua);
        return 0;
    }
    tween = g_tweens.sleeping;
    tween->working = 1;
    g_tweens.sleeping = tween->next;

    if (tween->next)
        tween->next->prev = tween->prev;
    if (tween->prev)
        tween->prev->next = tween->next;

    if (g_tweens.working)
        g_tweens.working->prev = tween;
    tween->prev = 0;
    tween->next = g_tweens.working;
    g_tweens.working = tween;

    lua_pushinteger(lua, tween - g_tweens.pool);
    return 1;
}

static int api_tween_free(lua_State *lua)
{
    struct tween_t *tween;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_tween_free: incorrect argument");
        lua_error(lua);
        return 0;
    }

    tween = tween_get(lua_tointeger(lua, -1));
    lua_pop(lua, 1);
    
    if (tween == 0 || tween->working == 0)
    {
        lua_pushstring(lua, "api_tween_free: invalid tween");
        lua_error(lua);
        return 0;
    }
    tween->working = 0;

    if (g_tweens.working == tween)
        g_tweens.working = tween->next;

    if (tween->prev)
        tween->prev->next = tween->next;
    if (tween->next)
        tween->next->prev = tween->prev;

    if (g_tweens.sleeping)
        g_tweens.sleeping->prev = tween;
    tween->prev = 0;
    tween->next = g_tweens.sleeping;
    g_tweens.sleeping = tween;
    return 0;
}

static int api_tween_play_sine(lua_State *lua)
{
    struct tween_t *tween;
    float shift, ampl, period;
    if (lua_gettop(lua) != 4
     || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
     || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_tween_play_sine: incorrect argument");
        lua_error(lua);
        return 0;
    }
    tween = tween_get(lua_tointeger(lua, -4));
    shift = lua_tonumber(lua, -3);
    ampl = lua_tonumber(lua, -2);
    period = lua_tonumber(lua, -1);
    lua_pop(lua, 4);

    if (tween == 0)
    {
        lua_pushstring(lua, "api_tween_play_sine: invalid tween");
        lua_error(lua);
        return 0;
    }
    tween->type = TWEEN_SINE;
    tween->t = 0;
    tween->shift = shift;
    tween->ampl = ampl;
    tween->period = period;
    calc_value(tween);
    return 0;
}

static int api_tween_play_saw(lua_State *lua)
{
    struct tween_t *tween;
    float shift, ampl, period;
    if (lua_gettop(lua) != 4
     || !lua_isnumber(lua, -4) || !lua_isnumber(lua, -3)
     || !lua_isnumber(lua, -2) || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_tween_play_saw: incorrect argument");
        lua_error(lua);
        return 0;
    }
    tween = tween_get(lua_tointeger(lua, -4));
    shift = lua_tonumber(lua, -3);
    ampl = lua_tonumber(lua, -2);
    period = lua_tonumber(lua, -1);
    lua_pop(lua, 4);

    if (tween == 0)
    {
        lua_pushstring(lua, "api_tween_play_saw: invalid tween");
        lua_error(lua);
        return 0;
    }
    tween->type = TWEEN_SAW;
    tween->t = 0;
    tween->shift = shift;
    tween->ampl = ampl;
    tween->period = period;
    calc_value(tween);
    return 0;
}

int tween_init(lua_State *lua, int len)
{
    int i;
    g_tweens.pool = calloc(len, sizeof(struct tween_t));
    if (g_tweens.pool == 0)
        return 1;
    g_tweens.pool_len = len;
    for (i = 0; i < len; ++i)
    {
        if (i > 0)
            g_tweens.pool[i].prev = g_tweens.pool + i - 1;
        if (i < len - 1)
            g_tweens.pool[i].next = g_tweens.pool + i + 1;
    }
    g_tweens.sleeping = g_tweens.pool;

    lua_register(lua, "api_tween_alloc", api_tween_alloc);
    lua_register(lua, "api_tween_free", api_tween_free);
    lua_register(lua, "api_tween_play_sine", api_tween_play_sine);
    lua_register(lua, "api_tween_play_saw", api_tween_play_saw);
    
    return 0;
}

void tween_done(void)
{
    if (g_tweens.pool)
    {
        free(g_tweens.pool);
        g_tweens.pool = 0;
    }
}

struct tween_t * tween_get(int i)
{
    if (i >= 0 && i < g_tweens.pool_len)
        return g_tweens.pool + i;
    else
        return 0;
}

void tween_update(float dt)
{
    struct tween_t *tween;
    tween = g_tweens.working;
    while (tween)
    {
        tween->t += dt;
        if (tween->period > 0.0f)
        {
            while (tween->t > tween->period)
                tween->t -= tween->period;
        }
        calc_value(tween);
        tween = tween->next;
    }
}
