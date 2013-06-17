#ifndef YVEHICLE_HPP
#define YVEHICLE_HPP

#include "btBulletDynamicsCommon.h"

class ymstate_c;
struct yworld_t;
struct ycolshape_t;

struct yvehicle_t {
    btRigidBody *chassis;
    ymstate_c *mstate;
    btDefaultVehicleRaycaster *ray;
    btRaycastVehicle *veh;
    btRaycastVehicle::btVehicleTuning *tuning;
    char *chassis_data, *ray_data, *veh_data;
    int vacant;
    yworld_t *wld;
    ycolshape_t *shape, *inert;
    yvehicle_t *shape_prev, *shape_next, *inert_prev, *inert_next;
};

int yvehicle_init(int count);
void yvehicle_done(void);
int yvehicle_alloc(yvehicle_t *veh, yworld_t*, ycolshape_t *shape,
                  ycolshape_t *inert, float *matrix, float mass,
                  float ch_frict, float ch_rfrict, float sus_stif,
                  float sus_comp, float sus_damp, float sus_trav,
                  float sus_force, float slip_frict);
int yvehicle_free(yvehicle_t*);
yvehicle_t * yvehicle_get(int);
int yvehicle_add_wheel(yvehicle_t*, int*, float *pos, float *dir, float *axl,
                      float sus_rest, float roll, float radius, int front);
int yvehicle_set_wheel(yvehicle_t*, int, float engine,
                      float brake, float steer);
int yvehicle_fetch_chassis_tm(yvehicle_t*, float*);
int yvehicle_fetch_wheel_tm(yvehicle_t*, int, float*);
int yvehicle_transform(yvehicle_t*, float*);
int yvehicle_wheel_contact(yvehicle_t*, int, int *in_contact);

#endif /* YVEHICLE_HPP */

