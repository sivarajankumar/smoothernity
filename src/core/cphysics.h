#ifndef CPHYSICS_H
#define CPHYSICS_H

#include "lua.h"

int cphysics_init(lua_State *lua, int wld_count, int cs_count,
                  int rb_count, int veh_count,
                  const int msizes[], const int mcounts[], int mlen);
void cphysics_done(void);
int cphysics_wld_cast(int wldi, int csi, float *mfrom, float *mto, float *vout);
int cphysics_rb_fetch_tm(int rbi, float *matrix);
int cphysics_veh_fetch_chassis_tm(int vehi, float *matrix);
int cphysics_veh_fetch_wheel_tm(int vehi, int wheel, float *matrix);

#endif /* CPHYSICS_H */

