namespace shy_guts
{
    static so_called_loadable_consts_content_module_container_type module_container ;
}

void shy_loadable_consts_content :: get_module_container ( so_called_loadable_consts_content_module_container_type * & pointer )
{
    pointer = & shy_guts :: module_container ;
}
