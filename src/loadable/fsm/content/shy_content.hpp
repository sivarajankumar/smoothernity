namespace shy_guts
{
    static so_called_type_loadable_fsm_content_system_binding_container system_binding_container ;
    static so_called_type_loadable_fsm_content_system_container system_container ;
}

void shy_loadable_fsm_content :: get_system_binding_container ( so_called_type_loadable_fsm_content_system_binding_container * & pointer )
{
    pointer = & shy_guts :: system_binding_container ;
}

void shy_loadable_fsm_content :: get_system_container ( so_called_type_loadable_fsm_content_system_container * & pointer )
{
    pointer = & shy_guts :: system_container ;
}
