#include "physics.h"
#include "../physics/physcpp.h"
#include "mpool.h"

int physics_init(lua_State *lua)
{
    if (lua == 0)
        return 0;
    return physcpp_init(mpool_alloc, mpool_free);
}

void physics_done(void)
{
    physcpp_done();
}
