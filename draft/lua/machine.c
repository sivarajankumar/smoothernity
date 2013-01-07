#include "machine.h"
#include "timer.h"
#include <stdio.h>
#include <stdlib.h>

typedef int (*state_t) (struct machine_t *);

struct machine_t
{
    lua_State *thread;
    state_t next_state;

    struct timer_t *step_timer;
    struct timer_t *sleep_timer;
    int sleep_timeout;
};

int state_resume(struct machine_t *machine)
{
    int status;
    status = lua_resume(machine->thread, 1);
    if (status && status != LUA_YIELD)
    {
        fprintf(stderr, "Failed to resume thread: %s\n",
                lua_tostring(machine->thread, -1));
        return 1;
    }
    return 0;
}

int state_sleep(struct machine_t *machine)
{
    if (timer_passed(machine->sleep_timer) < machine->sleep_timeout)
        machine->next_state = state_sleep;
    else
        machine->next_state = state_resume;
    return 0;
}

int api_yield(lua_State *lua)
{
    struct machine_t *machine;
    if (lua_isuserdata(lua, -1))
    {
        machine = lua_touserdata(lua, -1);
        lua_pop(lua, 1);
        machine->next_state = state_resume;
        return lua_yield(lua, 0);
    }
    else
    {
        lua_pushstring(lua, "myyield: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

int api_sleep(lua_State *lua)
{
    struct machine_t *machine;
    if (lua_islightuserdata(lua, -2) && lua_isnumber(lua, -1))
    {
        machine = lua_touserdata(lua, -2);
        machine->sleep_timeout = lua_tointeger(lua, -1);
        timer_reset(machine->sleep_timer);
        lua_pop(lua, 2);
        machine->next_state = state_sleep;
        return lua_yield(lua, 0);
    }
    else
    {
        lua_pushstring(lua, "mysleep: incorrect arguments");
        lua_error(lua);
        return 0;
    }
}

void machine_embrace(lua_State *lua)
{
    lua_register(lua, "api_yield", api_yield);
    lua_register(lua, "api_sleep", api_sleep);
}

int machine_step(struct machine_t *machine, int timeout)
{
    int status;
    state_t state;
    timer_reset(machine->step_timer);
    do
    {
        if (machine->next_state == 0)
            return 0;
        state = machine->next_state;
        machine->next_state = 0;
        status = (*state)(machine);
        if (status)
            return status;
    } while (timer_passed(machine->step_timer) < timeout);
    return 0;
}

struct machine_t * machine_create(lua_State *lua, const char *func)
{
    struct machine_t *machine;
    machine = calloc(1, sizeof(struct machine_t));
    if (machine == 0)
        return 0;
    machine->step_timer = timer_create();
    if (machine->step_timer == 0)
        goto cleanup;
    machine->sleep_timer = timer_create();
    if (machine->sleep_timer == 0)
        goto cleanup;
    machine->thread = lua_newthread(lua);
    if (machine->thread == 0)
        goto cleanup;
    lua_getglobal(machine->thread, func);
    lua_pushlightuserdata(machine->thread, machine);
    machine->next_state = state_resume;
    return machine;
cleanup:
    if (machine->step_timer)
        timer_destroy(machine->step_timer);
    if (machine->sleep_timer)
        timer_destroy(machine->sleep_timer);
    free(machine);
    return 0;
}

void machine_destroy(struct machine_t *machine)
{
    timer_destroy(machine->step_timer);
    timer_destroy(machine->sleep_timer);
    free(machine);
}

int machine_running(struct machine_t *machine)
{
    return machine->next_state != 0;
}
