#pragma once

struct world_t;

int world_init(int count);
void world_done(void);
int world_update(float dt);
int world_alloc(int*);
world_t * world_get(int);
int world_free(world_t*);
int world_ddraw(world_t*);
void world_time_scale(world_t*, float);
int world_ddraw_mode(world_t*, int);
int world_move(world_t*, float*);
