#pragma once

#include <lua.h>

struct machine_t;

void machine_grasp(lua_State *);
struct machine_t * machine_create(lua_State *, const char *);
int machine_run(struct machine_t *);
void machine_destroy(struct machine_t *);
