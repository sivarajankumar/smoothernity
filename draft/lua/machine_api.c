static int state_resume(struct machine_t *machine)
{
    int status;
    status = lua_resume(machine->thread, 1);
    if (status && status != LUA_YIELD)
    {
        fprintf(stderr, "Failed to resume thread: %s\n",
                lua_tostring(machine->thread, -1));
        return 1;
    }
    return 0;
}

static int api_yield(lua_State *lua)
{
    struct machine_t *machine;
    if (lua_gettop(lua) == 1 && lua_islightuserdata(lua, -1))
    {
        machine = lua_touserdata(lua, -1);
        lua_pop(lua, 1);
        machine->next_state = state_resume;
        return lua_yield(lua, 0);
    }
    else
    {
        lua_pushstring(lua, "api_yield: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_sleep(lua_State *lua)
{
    struct machine_t *machine;
    if (lua_gettop(lua) == 1 && lua_islightuserdata(lua, -1))
    {
        machine = lua_touserdata(lua, -1);
        lua_pop(lua, 1);
        machine->sleep = 1;
        machine->next_state = state_resume;
        return lua_yield(lua, 0);
    }
    else
    {
        lua_pushstring(lua, "api_sleep: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

static int api_time(lua_State *lua)
{
    struct machine_t *machine;
    if (lua_gettop(lua) == 1 && lua_islightuserdata(lua, -1))
    {
        machine = lua_touserdata(lua, -1);
        lua_pop(lua, 1);
        lua_pushinteger(lua, timer_passed(machine->run_timer));
        return 1;
    }
    else
    {
        lua_pushstring(lua, "api_time: incorrect argument");
        lua_error(lua);
        return 0;
    }
}

void machine_embrace(lua_State *lua)
{
    lua_register(lua, "api_yield", api_yield);
    lua_register(lua, "api_sleep", api_sleep);
    lua_register(lua, "api_time", api_time);
    lua_register(lua, "api_tween_alloc", api_tween_alloc);
    lua_register(lua, "api_tween_free", api_tween_free);
    lua_register(lua, "api_tween_play_sine", api_tween_play_sine);
    lua_register(lua, "api_ibuf_alloc", api_ibuf_alloc);
    lua_register(lua, "api_ibuf_free", api_ibuf_free);
    lua_register(lua, "api_ibuf_write", api_ibuf_write);
    lua_register(lua, "api_ibuf_bake", api_ibuf_bake);
    lua_register(lua, "api_ibuf_query", api_ibuf_query);
    lua_register(lua, "api_vbuf_alloc", api_vbuf_alloc);
    lua_register(lua, "api_vbuf_free", api_vbuf_free);
    lua_register(lua, "api_vbuf_write", api_vbuf_write);
    lua_register(lua, "api_vbuf_bake", api_vbuf_bake);
    lua_register(lua, "api_vbuf_query", api_vbuf_query);
    lua_register(lua, "api_space_alloc", api_space_alloc);
    lua_register(lua, "api_space_free", api_space_free);
    lua_register(lua, "api_space_query", api_space_query);
    lua_register(lua, "api_space_offset", api_space_offset);
    lua_register(lua, "api_space_offset_tween", api_space_offset_tween);
    lua_register(lua, "api_space_scale", api_space_scale);
    lua_register(lua, "api_space_scale_tween", api_space_scale_tween);
    lua_register(lua, "api_space_rotation", api_space_rotation);
    lua_register(lua, "api_space_rotation_tween", api_space_rotation_tween);
    lua_register(lua, "api_mesh_alloc", api_mesh_alloc);
    lua_register(lua, "api_mesh_free", api_mesh_free);
    lua_register(lua, "api_mesh_query", api_mesh_query);
    lua_register(lua, "api_text_alloc", api_text_alloc);
    lua_register(lua, "api_text_free", api_text_free);
    lua_register(lua, "api_text_query", api_text_query);
}
