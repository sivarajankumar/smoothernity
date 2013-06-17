#ifndef PHYSICS_VEHICLE_HPP
#define PHYSICS_VEHICLE_HPP

#include "mstate.hpp"

struct world_t;
struct ycolshape_t;

struct vehicle_t {
    btRigidBody *chassis;
    mstate_c *mstate;
    btDefaultVehicleRaycaster *ray;
    btRaycastVehicle *veh;
    btRaycastVehicle::btVehicleTuning *tuning;
    char *chassis_data, *ray_data, *veh_data;
    int vacant;
    world_t *wld;
    ycolshape_t *shape, *inert;
    vehicle_t *shape_prev, *shape_next, *inert_prev, *inert_next;
};

int vehicle_init(int count);
void vehicle_done(void);
int vehicle_alloc(vehicle_t *veh, world_t*, ycolshape_t *shape,
                  ycolshape_t *inert, float *matrix, float mass,
                  float ch_frict, float ch_rfrict, float sus_stif,
                  float sus_comp, float sus_damp, float sus_trav,
                  float sus_force, float slip_frict);
int vehicle_free(vehicle_t*);
vehicle_t * vehicle_get(int);
int vehicle_add_wheel(vehicle_t*, int*, float *pos, float *dir, float *axl,
                      float sus_rest, float roll, float radius, int front);
int vehicle_set_wheel(vehicle_t*, int, float engine,
                      float brake, float steer);
int vehicle_fetch_chassis_tm(vehicle_t*, float*);
int vehicle_fetch_wheel_tm(vehicle_t*, int, float*);
int vehicle_transform(vehicle_t*, float*);
int vehicle_wheel_contact(vehicle_t*, int, int *in_contact);

#endif /* PHYSICS_VEHICLE_HPP */

