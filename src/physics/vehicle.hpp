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
    colshape_t *cs;
    vehicle_t *cs_prev;
    vehicle_t *cs_next;
};

int vehicle_init(int count);
void vehicle_done(void);
void vehicle_left(int *left); /* TODO: make "int vehicle_left(void);" */
int vehicle_alloc(btDynamicsWorld*, colshape_t*, float *matrix,
                  float ch_frict, float ch_roll_frict,
                  float sus_stif, float sus_comp, float sus_damp,
                  float sus_trav, float sus_force, float slip_frict);
void vehicle_free(vehicle_t*, btDynamicsWorld*);
vehicle_t * vehicle_get(int);
int vehicle_add_wheel(vehicle_t*, float *pos, float *dir, float *axl,
                      float sus_rest, float roll, float radius, int front);
int vehicle_set_wheel(vehicle_t*, int, float engine,
                      float brake, float steer);
void vehicle_fetch_chassis_tm(vehicle_t*, float*);
int vehicle_fetch_wheel_tm(vehicle_t*, int, float*);
void vehicle_transform(vehicle_t*, float*);
