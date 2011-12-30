namespace shy_guts
{
    static so_called_loadable_fsm_content_system_binding_container_type system_binding_container ;
    static so_called_loadable_fsm_content_system_container_type system_container ;
}

void shy_loadable_fsm_content :: get_system_binding_container ( so_called_loadable_fsm_content_system_binding_container_type * & pointer )
{
    pointer = & shy_guts :: system_binding_container ;
}

void shy_loadable_fsm_content :: get_system_container ( so_called_loadable_fsm_content_system_container_type * & pointer )
{
    pointer = & shy_guts :: system_container ;
}
