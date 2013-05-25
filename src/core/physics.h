#pragma once

#include "lua.h"

int physics_init(lua_State *lua, int wld_count, int cs_count,
                 int rb_count, int veh_count,
                 const int msizes[], const int mcounts[], int mlen);
void physics_done(void);
int physics_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout);
int physics_rb_fetch_tm(int rbi, float *matrix);
int physics_veh_fetch_chassis_tm(int vehi, float *matrix);
int physics_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix);

