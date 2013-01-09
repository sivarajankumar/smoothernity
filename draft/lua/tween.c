#include "tween.h"
#include "consts.h"
#include "scene.h"
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

int tween_init(int len)
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

int tween_alloc(void)
{
    struct tween_t *tween;
    if (g_tweens.sleeping)
    {
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
        return tween - g_tweens.pool;
    }
    else
        return -1;
}

void tween_free(int i)
{
    struct tween_t *tween;
    if (i < 0 || i >= g_tweens.pool_len)
        return;

    tween = g_tweens.pool + i;

    if (tween->working == 0)
        return;
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
}

struct tween_t * tween_get(int i)
{
    if (i >= 0 && i < g_tweens.pool_len)
        return g_tweens.pool + i;
    else
        return 0;
}

static void calc_value(struct tween_t *tween)
{
    if (tween->type == TWEEN_SINE)
    {
        tween->value = tween->shift +
            (tween->ampl * sin(tween->t * M_PI * 2.0f / tween->period));
    }
}

void tween_update(float dt)
{
    struct tween_t *tween;
    tween = g_tweens.working;
    while (tween)
    {
        tween->t += dt;
        calc_value(tween);
        tween = tween->next;
    }
}

void tween_play_sine(int i, float shift, float ampl, float period)
{
    struct tween_t *tween;
    if (i < 0 || i >= g_tweens.pool_len)
        return;
    tween = g_tweens.pool + i;
    tween->t = 0;
    tween->shift = shift;
    tween->ampl = ampl;
    tween->period = period;
    calc_value(tween);
}
