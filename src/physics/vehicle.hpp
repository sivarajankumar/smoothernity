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
    colshape_t *shape;
    colshape_t *inert;
    vehicle_t *shape_prev;
    vehicle_t *shape_next;
    vehicle_t *inert_prev;
    vehicle_t *inert_next;
};

int vehicle_init(int count);
void vehicle_done(void);
int vehicle_left(void);
int vehicle_alloc(int *vehi, btDynamicsWorld*, colshape_t *shape,
                  colshape_t *inert, float *matrix, float mass,
                  float ch_frict, float ch_rfrict, float sus_stif,
                  float sus_comp, float sus_damp, float sus_trav,
                  float sus_force, float slip_frict);
int vehicle_free(vehicle_t*, btDynamicsWorld*);
vehicle_t * vehicle_get(int);
int vehicle_add_wheel(vehicle_t*, int*, float *pos, float *dir, float *axl,
                      float sus_rest, float roll, float radius, int front);
int vehicle_set_wheel(vehicle_t*, int, float engine,
                      float brake, float steer);
int vehicle_fetch_chassis_tm(vehicle_t*, float*);
int vehicle_fetch_wheel_tm(vehicle_t*, int, float*);
int vehicle_transform(vehicle_t*, float*);
int vehicle_wheel_contact(vehicle_t*, int, int* in_contact);
