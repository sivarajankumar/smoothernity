#include "yvehicle.hpp"
#include "yphysres.h"
#include "ymstate.hpp"
#include "world.hpp"
#include "ycolshape.hpp"
#include "pmem.hpp"
#include "vlog.hpp"

static const size_t YVEHICLE_SIZE = 256;

struct yvehicles_t {
    int count;
    char *pool;
};

static_assert(sizeof(yvehicle_t) <= YVEHICLE_SIZE, "Invalid yvehicle_t size");

static yvehicles_t g_yvehicles;

int yvehicle_init(int count) {
    yvehicle_t *veh;
    g_yvehicles.count = count;
    g_yvehicles.pool = (char*)pmem_alloc(PMEM_ALIGNOF(yvehicle_t),
                                        YVEHICLE_SIZE * count);
    if (!g_yvehicles.pool)
        return YPHYSRES_CANNOT_INIT;
    for (int i = 0; i < count; ++i) {
        veh = yvehicle_get(i);
        veh->vacant = 1;
        veh->chassis = 0;
        veh->mstate = 0;
        veh->ray = 0;
        veh->veh = 0;
        veh->tuning = 0;
        veh->chassis_data = veh->ray_data = veh->veh_data = 0;
        veh->wld = 0;
        veh->shape = veh->inert = 0;
        veh->shape_prev = veh->shape_next = 0;
        veh->inert_prev = veh->inert_next = 0;
    }
    for (int i = 0; i < count; ++i) {
        veh = yvehicle_get(i);
        try {
            veh->mstate = new ymstate_c();
            veh->tuning = new btRaycastVehicle::btVehicleTuning();
        } catch (...) {
            return YPHYSRES_CANNOT_INIT;
        }
        veh->chassis_data = (char*)pmem_alloc(PMEM_ALIGNOF(btRigidBody),
                                              sizeof(btRigidBody));
        veh->ray_data = (char*)pmem_alloc(PMEM_ALIGNOF(btDefaultVehicleRaycaster),
                                          sizeof(btDefaultVehicleRaycaster));
        veh->veh_data = (char*)pmem_alloc(PMEM_ALIGNOF(btRaycastVehicle),
                                          sizeof(btRaycastVehicle));
        if (!veh->chassis_data || !veh->ray_data || !veh->veh_data)
            return YPHYSRES_CANNOT_INIT;
    }
    return YPHYSRES_OK;
}

void yvehicle_done(void) {
    yvehicle_t *veh;
    if (!g_yvehicles.pool)
        return;
    for (int i = 0; i < g_yvehicles.count; ++i) {
        veh = yvehicle_get(i);
        yvehicle_free(veh);
        try {
            if (veh->mstate)
                delete veh->mstate;
            if (veh->tuning)
                delete veh->tuning;
        } catch (...) {
            VLOG_ERROR("exception");
        }
        if (veh->chassis_data)
            pmem_free(veh->chassis_data);
        if (veh->ray_data)
            pmem_free(veh->ray_data);
        if (veh->veh_data)
            pmem_free(veh->veh_data);
    }
    pmem_free(g_yvehicles.pool);
    g_yvehicles.pool = 0;
}

yvehicle_t * yvehicle_get(int vehi) {
    if (vehi >= 0 && vehi < g_yvehicles.count)
        return (yvehicle_t*)(g_yvehicles.pool + YVEHICLE_SIZE * vehi);
    else
        return 0;
}

int yvehicle_free(yvehicle_t *veh) {
    if (veh->vacant == 1)
        return YPHYSRES_INVALID_VEH;
    veh->vacant = 1;

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

    try {
        if (veh->wld) {
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
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    veh->wld = 0;
    veh->chassis = 0;
    veh->ray = 0;
    veh->veh = 0;

    return YPHYSRES_OK;
}

int yvehicle_alloc(yvehicle_t *veh, world_t *wld, ycolshape_t *shape,
ycolshape_t *inert, float *matrix, float mass, float ch_frict,
float ch_roll_frict, float sus_stif, float sus_comp, float sus_damp,
float sus_trav, float sus_force, float slip_frict) {
    if (!veh->vacant)
        return YPHYSRES_INVALID_VEH;
    if (!shape->shape || !inert->shape)
        return YPHYSRES_INVALID_CS;
    veh->vacant = 0;

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

    try {
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
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yvehicle_add_wheel(yvehicle_t *veh, int *wheeli, float *pos, float *dir,
float *axl, float sus_rest, float roll, float radius, int front) {
    try {
        *wheeli = veh->veh->getNumWheels();
        veh->veh->addWheel(btVector3(pos[0], pos[1], pos[2]),
                           btVector3(dir[0], dir[1], dir[2]),
                           btVector3(axl[0], axl[1], axl[2]),
                           sus_rest, radius, *veh->tuning, front);
        veh->veh->getWheelInfo(*wheeli).m_rollInfluence = roll;
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yvehicle_set_wheel(yvehicle_t *veh, int wheel,
float engine, float brake, float steer) {
    try {
        if (wheel < 0 || wheel >= veh->veh->getNumWheels())
            return YPHYSRES_INVALID_VEH_WHEEL;
        veh->veh->applyEngineForce(engine, wheel);
        veh->veh->setBrake(brake, wheel);
        veh->veh->setSteeringValue(steer, wheel);
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yvehicle_fetch_chassis_tm(yvehicle_t *veh, float *matrix) {
    try {
        veh->mstate->m.getOpenGLMatrix(matrix);
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yvehicle_fetch_wheel_tm(yvehicle_t *veh, int wheel, float *m) {
    try {
        if (wheel < 0 || wheel >= veh->veh->getNumWheels())
            return YPHYSRES_INVALID_VEH_WHEEL;
        veh->veh->updateWheelTransform(wheel, true);
        veh->veh->getWheelInfo(wheel).m_worldTransform.getOpenGLMatrix(m);
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yvehicle_transform(yvehicle_t *veh, float *matrix) {
    try {
        btTransform tm;
        tm.setFromOpenGLMatrix(matrix);
        veh->chassis->setWorldTransform(tm);
        veh->chassis->setInterpolationWorldTransform(tm);
        veh->mstate->m = tm;
    } catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}

int yvehicle_wheel_contact(yvehicle_t *veh, int wheel, int *in_cont) {
    try {
        if (wheel < 0 || wheel >= veh->veh->getNumWheels())
            return YPHYSRES_INVALID_VEH_WHEEL;
        *in_cont = veh->veh->getWheelInfo(wheel).m_raycastInfo.m_isInContact;
    }
    catch (...) {
        return YPHYSRES_INTERNAL;
    }
    return YPHYSRES_OK;
}
