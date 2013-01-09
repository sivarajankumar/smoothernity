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
    struct timer_t *run_timer;
    int sleep;
};

#include "machine_api_vbuf.c"
#include "machine_api_space.c"
#include "machine_api_mesh.c"
#include "machine_api_text.c"
#include "machine_api.c"

int machine_step(struct machine_t *machine, int timeout)
{
    int status;
    state_t state;
    timer_reset(machine->step_timer);
    machine->sleep = 0;
    while (1)
    {
        if (machine->next_state)
        {
            state = machine->next_state;
            machine->next_state = 0;
            status = (*state)(machine);
            if (status)
                return status;
        }
        if (machine->next_state == 0
         || machine->sleep == 1
         || timer_passed(machine->step_timer) > timeout)
            break;
    }
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
    machine->run_timer = timer_create();
    if (machine->run_timer == 0)
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
    if (machine->run_timer)
        timer_destroy(machine->run_timer);
    free(machine);
    return 0;
}

void machine_destroy(struct machine_t *machine)
{
    timer_destroy(machine->step_timer);
    timer_destroy(machine->run_timer);
    free(machine);
}

int machine_running(struct machine_t *machine)
{
    return machine->next_state != 0;
}
