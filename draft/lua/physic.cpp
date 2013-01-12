#include <iostream>
#include <lua.h>
#include <LinearMath/btAlignedAllocator.h>

struct physics_t
{
    struct mpool_t *mpool;
};

struct physics_t g_physics;

extern "C" int physic_init(lua_State *, struct mpool_t *mpool)
{
    std::cout << "physic_init" << std::endl;
    g_physics.mpool = mpool;
    return 0;
}

extern "C" void physic_done(void)
{
    std::cout << "physic_done" << std::endl;
}
