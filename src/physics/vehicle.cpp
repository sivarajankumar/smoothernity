#include "physres.h"
#include "vehicle.hpp"
#include "world.hpp"
#include "colshape.hpp"
#include "../util/util.hpp"
#include <stdio.h>
#include <string.h>

static const size_t VEHICLE_SIZE = 256;

struct vehicles_t
{
    int left;
    int left_min;
    int count;
    int allocs;
    int frees;
    char *pool;
    vehicle_t *vacant;
};

static vehicles_t g_vehicles;

int vehicle_init(int count)
{
    int i;
    vehicle_t *veh;
    if (sizeof(vehicle_t) > VEHICLE_SIZE)
    {
        fprintf(stderr, "Invalid size:\nsizeof(vehicle_t) == %i\n",
                (int)sizeof(vehicle_t));
        return PHYSRES_CANNOT_INIT;
    }
    g_vehicles.pool = (char*)util_malloc(VEHICLE_SIZE, VEHICLE_SIZE * count);
    if (g_vehicles.pool == 0)
        return PHYSRES_CANNOT_INIT;
    memset(g_vehicles.pool, 0, VEHICLE_SIZE * count);
    g_vehicles.left = count;
    g_vehicles.left_min = count;
    g_vehicles.count = count;
    g_vehicles.vacant = vehicle_get(0);
    for (i = 0; i < count; ++i)
    {
        veh = vehicle_get(i);
        if (i < count - 1)
            veh->next = vehicle_get(i + 1);
        veh->vacant = 1;
        try {
            veh->chassis_data = (char*)util_malloc(alignof(btRigidBody),
                                                   sizeof(btRigidBody));
            veh->ray_data = (char*)util_malloc(alignof(btDefaultVehicleRaycaster),
                                               sizeof(btDefaultVehicleRaycaster));
            veh->veh_data = (char*)util_malloc(alignof(btRaycastVehicle),
                                               sizeof(btRaycastVehicle));
            veh->mstate = new mstate_c();
            veh->tuning = new btRaycastVehicle::btVehicleTuning();
        } catch (...) {
            goto cleanup;
        }
    }
    return PHYSRES_OK;
cleanup:
    for (i = 0; i < count; ++i)
    {
        veh = vehicle_get(i);
        if (veh->chassis_data)
            util_free(veh->chassis_data);
        if (veh->ray_data)
            util_free(veh->ray_data);
        if (veh->veh_data)
            util_free(veh->veh_data);
        if (veh->mstate)
            delete veh->mstate;
        if (veh->tuning)
            delete veh->tuning;
    }
    util_free(g_vehicles.pool);
    g_vehicles.pool = 0;
    return PHYSRES_CANNOT_INIT;
}

void vehicle_done(void)
{
    int i;
    vehicle_t *veh;
    if (g_vehicles.pool == 0)
        return;
    printf("Vehicles usage: %i/%i, allocs/frees: %i/%i\n",
           g_vehicles.count - g_vehicles.left_min, g_vehicles.count,
           g_vehicles.allocs, g_vehicles.frees);
    for (i = 0; i < g_vehicles.count; ++i)
    {
        veh = vehicle_get(i);
        vehicle_free(veh);
        try {
            util_free(veh->chassis_data);
            util_free(veh->ray_data);
            util_free(veh->veh_data);
            delete veh->mstate;
            delete veh->tuning;
        } catch (...) {
            fprintf(stderr, "vehicle_done: exception\n");
        }
    }
    util_free(g_vehicles.pool);
    g_vehicles.pool = 0;
}

int vehicle_left(void)
{
    return g_vehicles.left;
}

vehicle_t * vehicle_get(int vehi)
{
    if (vehi >= 0 && vehi < g_vehicles.count)
        return (vehicle_t*)(g_vehicles.pool + VEHICLE_SIZE * vehi);
    else
        return 0;
}

int vehicle_free(vehicle_t *veh)
{
    if (veh->vacant == 1)
        return PHYSRES_INVALID_VEH;
    ++g_vehicles.left;
    ++g_vehicles.frees;
    veh->vacant = 1;
    veh->next = g_vehicles.vacant;
    g_vehicles.vacant = veh;

    if (veh->shape->vehs == veh)
        veh->shape->vehs = veh->shape_next;
    if (veh->shape_next)
        veh->shape_next->shape_prev = veh->shape_prev;
    if (veh->shape_prev)
        veh->shape_prev->shape_next = veh->shape_next;
    veh->shape = 0;
    veh->shape_prev = 0;
    veh->shape_next = 0;

    if (veh->inert->vehs == veh)
        veh->inert->vehs = veh->inert_next;
    if (veh->inert_next)
        veh->inert_next->inert_prev = veh->inert_prev;
    if (veh->inert_prev)
        veh->inert_prev->inert_next = veh->inert_next;
    veh->inert = 0;
    veh->inert_prev = 0;
    veh->inert_next = 0;

    try
    {
        if (veh->wld)
        {
            if (veh->veh)
                veh->wld->world->removeAction(veh->veh);
            if (veh->chassis)
                veh->wld->world->removeRigidBody(veh->chassis);
        }
        if (veh->chassis)
            veh->chassis->~btRigidBody();
        if (veh->ray)
            veh->ray->~btDefaultVehicleRaycaster();
        if (veh->veh)
            veh->veh->~btRaycastVehicle();
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }

    veh->wld = 0;
    veh->chassis = 0;
    veh->ray = 0;
    veh->veh = 0;

    return PHYSRES_OK;
}

int vehicle_alloc(int *vehi, world_t *wld, colshape_t *shape,
                  colshape_t *inert, float *matrix, float mass, float ch_frict,
                  float ch_roll_frict, float sus_stif, float sus_comp,
                  float sus_damp, float sus_trav, float sus_force,
                  float slip_frict)
{
    vehicle_t *veh;
    if (g_vehicles.vacant == 0)
        return PHYSRES_OUT_OF_VEH;
    if (shape->shape == 0 || inert->shape == 0)
        return PHYSRES_INVALID_CS;
    ++g_vehicles.allocs;
    --g_vehicles.left;
    if (g_vehicles.left < g_vehicles.left_min)
        g_vehicles.left_min = g_vehicles.left;
    veh = g_vehicles.vacant;
    g_vehicles.vacant = g_vehicles.vacant->next;
    veh->vacant = 0;
    veh->next = 0;

    veh->shape = shape;
    if (shape->vehs)
        shape->vehs->shape_prev = veh;
    veh->shape_next = shape->vehs;
    veh->shape_prev = 0;
    shape->vehs = veh;

    veh->inert = inert;
    if (inert->vehs)
        inert->vehs->inert_prev = veh;
    veh->inert_next = inert->vehs;
    veh->inert_prev = 0;
    inert->vehs = veh;

    veh->tuning->m_suspensionStiffness = sus_stif;
    veh->tuning->m_suspensionCompression = sus_comp;
    veh->tuning->m_suspensionDamping = sus_damp;
    veh->tuning->m_maxSuspensionTravelCm = sus_trav;
    veh->tuning->m_maxSuspensionForce = sus_force;
    veh->tuning->m_frictionSlip = slip_frict;

    try
    {
        btVector3 vinert;
        veh->mstate->m.setFromOpenGLMatrix(matrix);
        inert->shape->calculateLocalInertia(mass, vinert);

        btRigidBody::btRigidBodyConstructionInfo info
                (mass, veh->mstate, shape->shape, vinert);
        info.m_friction = ch_frict;
        info.m_rollingFriction = ch_roll_frict;

        veh->chassis = new (veh->chassis_data) btRigidBody(info);
        veh->ray = new (veh->ray_data) btDefaultVehicleRaycaster(wld->world);
        veh->veh = new (veh->veh_data)
            btRaycastVehicle(*veh->tuning, veh->chassis, veh->ray);
        veh->veh->setCoordinateSystem(0, 1, 2);
        veh->chassis->setActivationState(DISABLE_DEACTIVATION);
        wld->world->addRigidBody(veh->chassis);
        wld->world->addAction(veh->veh);
        veh->wld = wld;
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }

    *vehi = ((char*)veh - g_vehicles.pool) / VEHICLE_SIZE;
    return PHYSRES_OK;
}

int vehicle_add_wheel(vehicle_t *veh, int *wheeli, float *pos, float *dir,
                      float *axl, float sus_rest, float roll, float radius,
                      int front)
{
    try
    {
        *wheeli = veh->veh->getNumWheels();
        veh->veh->addWheel(btVector3(pos[0], pos[1], pos[2]),
                           btVector3(dir[0], dir[1], dir[2]),
                           btVector3(axl[0], axl[1], axl[2]),
                           sus_rest, radius, *veh->tuning, front);
        veh->veh->getWheelInfo(*wheeli).m_rollInfluence = roll;
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int vehicle_set_wheel(vehicle_t *veh, int wheel, float engine,
                      float brake, float steer)
{
    try
    {
        if (wheel < 0 || wheel >= veh->veh->getNumWheels())
            return PHYSRES_INVALID_VEH_WHEEL;
        veh->veh->applyEngineForce(engine, wheel);
        veh->veh->setBrake(brake, wheel);
        veh->veh->setSteeringValue(steer, wheel);
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int vehicle_fetch_chassis_tm(vehicle_t *veh, float *matrix)
{
    try {
        veh->mstate->m.getOpenGLMatrix(matrix);
    } catch (...) {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int vehicle_fetch_wheel_tm(vehicle_t *veh, int wheel, float *matrix)
{
    try
    {
        if (wheel < 0 || wheel >= veh->veh->getNumWheels())
            return PHYSRES_INVALID_VEH_WHEEL;
        veh->veh->updateWheelTransform(wheel, true);
        veh->veh->getWheelInfo(wheel).m_worldTransform.getOpenGLMatrix(matrix);
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int vehicle_transform(vehicle_t *veh, float *matrix)
{
    try
    {
        btTransform tm;
        tm.setFromOpenGLMatrix(matrix);
        veh->chassis->setWorldTransform(tm);
        veh->chassis->setInterpolationWorldTransform(tm);
        veh->mstate->m = tm;
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}

int vehicle_wheel_contact(vehicle_t *veh, int wheel, int *in_contact)
{
    try
    {
        if (wheel < 0 || wheel >= veh->veh->getNumWheels())
            return PHYSRES_INVALID_VEH_WHEEL;
        *in_contact = veh->veh->getWheelInfo(wheel).m_raycastInfo.m_isInContact;
    }
    catch (...)
    {
        return PHYSRES_INTERNAL;
    }
    return PHYSRES_OK;
}
