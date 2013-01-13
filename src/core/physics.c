#include "physics.h"
#include "vector.h"
#include "mpool.h"
#include "../physics/physcpp.h"
#include "../physics/physres.h"

static int api_physics_set_gravity(lua_State *lua)
{
    struct vector_t *v;
    if (lua_gettop(lua) != 1 || !lua_isnumber(lua, -1))
    {
        lua_pushstring(lua, "api_physics_set_gravity: incorrect argument");
        lua_error(lua);
        return 0;
    }
    v = vector_get(lua_tointeger(lua, -1));
    lua_pop(lua, 1);
    if (v == 0)
    {
        lua_pushstring(lua, "api_physics_set_gravity: invalid vector");
        lua_error(lua);
        return 0;
    }
    physcpp_set_gravity(v->value);
    return 0;
}

int physics_init(lua_State *lua, int cs_count, int rb_count)
{
    if (physcpp_init(mpool_alloc, mpool_free, cs_count, rb_count)
     != PHYSRES_OK)
    {
        return 1;
    }
    lua_register(lua, "api_physics_set_gravity", api_physics_set_gravity);
    return 0;
}

void physics_done(void)
{
    physcpp_done();
}

void physics_update(float dt)
{
    physcpp_update(dt);
}

void physics_rb_get_new_matrix(int rbi, float *matrix)
{
    physcpp_rb_get_new_matrix(rbi, matrix);
}
