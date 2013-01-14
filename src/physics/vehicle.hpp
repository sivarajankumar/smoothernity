#pragma once

#include "mstate.hpp"

struct colshape_t;

struct vehicle_t
{
    btRigidBody *chassis;
    mstate_c *mstate;
    btDefaultVehicleRaycaster *ray;
    btRaycastVehicle *veh;
    btRaycastVehicle::btVehicleTuning tuning;
    char chassis_data[sizeof(btRigidBody)];
    char mstate_data[sizeof(mstate_c)];
    char ray_data[sizeof(btDefaultVehicleRaycaster)];
    char veh_data[sizeof(btRaycastVehicle)];
    vehicle_t *next;
    int vacant;
};

int vehicle_init(int count);
void vehicle_done(void);
int vehicle_alloc(btDynamicsWorld*, colshape_t*, float *matrix,
                  float ch_frict, float ch_roll_frict,
                  float sus_stif, float sus_comp, float sus_damp,
                  float sus_trav, float sus_force, float slip_frict);
void vehicle_free(int, btDynamicsWorld*);
int vehicle_add_wheel(vehicle_t*, float *pos, float *dir, float *axl,
                      float sus_rest, float radius, int front);
vehicle_t * vehicle_get(int);
void vehicle_fetch_chassis_tm
