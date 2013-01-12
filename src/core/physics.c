#include "physics.h"
#include "mpool.h"
#include "../physics/physcpp.h"

int physics_init(lua_State *lua, int colshape_count)
{
    if (lua == 0)
        return 1;
    return physcpp_init(mpool_alloc, mpool_free, colshape_count);
}

void physics_done(void)
{
    physcpp_done();
}
