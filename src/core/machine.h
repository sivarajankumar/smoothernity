#pragma once

#include <lua.h>

/* TODO: kill this */

struct machine_t;

typedef int (*state_t) (struct machine_t *);

struct machine_t
{
    lua_State *thread;
    state_t next_state;
    struct timer_t *step_timer;
    struct timer_t *run_timer;
    int sleep;
    float last_step_time;
};

void machine_init(lua_State*);
struct machine_t * machine_create(lua_State*, const char*);
int machine_step(struct machine_t*, float);
int machine_running(struct machine_t*);
void machine_destroy(struct machine_t*);
int machine_state_resume(struct machine_t*);
