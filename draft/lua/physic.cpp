#include <iostream>
#include <lua.h>

extern "C" int physic_init(lua_State *)
{
    std::cout << "physic_init" << std::endl;
    return 0;
}

extern "C" void physic_done(void)
{
    std::cout << "physic_done" << std::endl;
}
