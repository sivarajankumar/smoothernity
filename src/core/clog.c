#include "clog.h"
#include "cutil.h"
#include "vlog.h"

static int api_log_out(lua_State *lua) {
    int level, line;
    const char *src, *msg;
    if (lua_gettop(lua) != 4 || !cutil_isint(lua, 1) || !lua_isstring(lua, 2) ||
    !cutil_isint(lua, 3) || !lua_isstring(lua, 4)) {
        lua_pushstring(lua, "incorrect argument");
        lua_error(lua);
        return 0;
    }
    level = lua_tointeger(lua, 1);
    src = lua_tostring(lua, 2);
    line = lua_tointeger(lua, 3);
    msg = lua_tostring(lua, 4);
    if (level < 0 || level >= VLOG_LEVELS_TOTAL) {
        lua_pushstring(lua, "invalid log level");
        lua_error(lua);
        return 0;
    }
    vlog_out(level, src, line, msg);
    return 0;
}

void clog_reg_thread(lua_State *lua) {
    lua_register(lua, "api_log_out", api_log_out);
    #define REG(x) lua_pushinteger(lua, VLOG_LEVEL_##x); \
                   lua_setglobal(lua, "API_LOG_"#x);
    REG(INFO);
    REG(ERROR);
    #undef REG
}

