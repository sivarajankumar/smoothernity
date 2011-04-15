namespace shy_guts
{
    static so_called_type_loadable_fsm_content_system_container system_container ;
}

void shy_loadable_fsm_content :: get_system_container ( so_called_type_loadable_fsm_content_system_container * & pointer )
{
    pointer = & shy_guts :: system_container ;
}
