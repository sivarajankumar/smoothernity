#include <lua.h>
#include <iostream>
#include <LinearMath/btAlignedAllocator.h>

extern "C"
int physic_init(lua_State *, void *(*memalloc)(size_t), void (*memfree)(void*))
{
    btAlignedAllocSetCustom(memalloc, memfree);
    return 0;
}

extern "C" void physic_done(void)
{
}
