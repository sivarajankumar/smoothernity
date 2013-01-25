#pragma once

#include <lua.h>

int physics_init(lua_State *lua, int wld_count, int cs_count,
                 int rb_count, int veh_count);
void physics_done(void);
int physics_update(float dt);
int physics_wld_ddraw(int wldi);
int physics_rb_fetch_tm(int rbi, float *matrix);
int physics_veh_fetch_chassis_tm(int vehi, float *matrix);
int physics_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix);
