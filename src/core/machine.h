#pragma once

#include <lua.h>

struct machine_t;

void machine_init(lua_State*);
struct machine_t * machine_create(lua_State*, const char*);
int machine_step(struct machine_t*, float);
int machine_running(struct machine_t*);
void machine_destroy(struct machine_t*);
