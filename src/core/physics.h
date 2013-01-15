#pragma once

#include <lua.h>

int physics_init(lua_State *lua, int cs_count, int rb_count, int veh_count);
void physics_done(void);
void physics_update(float dt);
void physics_ddraw(void);
int physics_rb_fetch_tm(int rbi, float *matrix);
int physics_veh_fetch_chassis_tm(int vehi, float *matrix);
int physics_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix);
