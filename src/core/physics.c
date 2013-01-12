#include "physics.h"
#include "mpool.h"
#include "../physics/physcpp.h"

int physics_init(lua_State *lua, int cs_count, int rb_count)
{
    if (lua == 0) /* TODO: remove this check */
        return 1;
    return physcpp_init(mpool_alloc, mpool_free, cs_count, rb_count);
}

void physics_done(void)
{
    physcpp_done();
}
