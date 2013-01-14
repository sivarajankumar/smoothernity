#include "vehicle.hpp"
#include "colshape.hpp"
#include <stdlib.h>

struct vehicles_t
{
    int left;
    int count;
    vehicle_t *pool;
    vehicle_t *vacant;
};

static vehicles_t g_vehicles;

int vehicle_init(int count)
{
    int i;
    vehicle_t *veh;
    g_vehicles.pool = (vehicle_t*)calloc(count, sizeof(vehicle_t));
    if (g_vehicles.pool == 0)
        return 1;
    g_vehicles.vacant = g_vehicles.pool;
    g_vehicles.left = count;
    g_vehicles.count = count;
    for (i = 0; i < count; ++i)
    {
        veh = g_vehicles.pool + i;
        if (i < count - 1)
            veh->next = g_vehicles.pool + i + 1;
        veh->vacant = 1;
        veh->mstate = new (veh->mstate_data) mstate_c();
    }
    return 0;
}

void vehicle_done(void)
{
    int i;
    if (g_vehicles.pool)
    {
        for (i = 0; i < g_vehicles.count; ++i)
        {
            vehicle_free(i, 0);
            g_vehicles.pool[i].mstate->~mstate_c();
            g_vehicles.pool[i].tuning.~btVehicleTuning();
        }
        free(g_vehicles.pool);
        g_vehicles.pool = 0;
    }
}

void vehicle_left(int *left)
{
    *left = g_vehicles.left;
}

vehicle_t * vehicle_get(int vehi)
{
    if (vehi >= 0 && vehi < g_vehicles.count)
        return g_vehicles.pool + vehi;
    else
        return 0;
}

void vehicle_free(int vehi, btDynamicsWorld *world)
{
    vehicle_t *veh;
    veh = vehicle_get(vehi);
    if (veh == 0 || veh->vacant == 1)
        return;
    ++g_vehicles.left;
    veh->vacant = 1;
    veh->next = g_vehicles.vacant;
    g_vehicles.vacant = veh;
    if (veh->veh && world)
        world->removeVehicle(veh->veh);
    if (veh->chassis)
    {
        veh->chassis->~btRigidBody();
        veh->chassis = 0;
    }
    if (veh->ray)
    {
        veh->ray->~btDefaultVehicleRaycaster();
        veh->ray = 0;
    }
    if (veh->veh)
    {
        veh->veh->~btRaycastVehicle();
        veh->veh = 0;
    }
}

int vehicle_alloc(btDynamicsWorld *world, colshape_t *cs, float *matrix,
                  float ch_frict, float ch_roll_frict,
                  float sus_stif, float sus_comp, float sus_damp,
                  float sus_trav, float sus_force, float slip_frict)
{
    vehicle_t *veh;
    if (g_vehicles.vacant == 0)
        return -1;
    --g_vehicles.left;
    veh = g_vehicles.vacant;
    g_vehicles.vacant = g_vehicles.vacant->next;
    veh->vacant = 0;
    veh->next = 0;

    veh->mstate->get.setFromOpenGLMatrix(matrix);
    veh->mstate->set = rb->mstate->get;
    veh->mstate->was_set = 1;

    veh->tuning.m_suspensionStiffness = sus_stif;
    veh->tuning.m_suspensionCompression = sus_comp;
    veh->tuning.m_suspensionDamping = sus_damp;
    veh->tuning.m_maxSuspensionTravelCm = sus_trav;
    veh->tuning.m_maxSuspensionForce = sus_force;
    veh->tuning.m_frictionSlip = slip_frict;

    btRigidBody::btRigidBodyConstructionInfo info
            (cs->mass, veh->mstate, cs->shape, cs->inertia);
    info.m_friction = ch_frict;
    info.m_rollingFriction = ch_roll_frict;

    veh->chassis = new (veh->chassis_data) btRigidBody(info);
    veh->ray = new (veh->ray_data) btDefaultVehicleRaycaster(world);
    veh->veh = new (veh->veh_data)
        btRaycastVehicle(veh->tuning, veh->chassis, veh->ray);
    veh->setCoordinateSystem(0, 1, 2);
    world->addVehicle(veh->veh);
    return veh - g_vehicles.pool;
}

int vehicle_add_wheel(vehicle_t*, float *pos, float *dir, float *axl,
                      float sus_rest, float roll, float radius, int front);
