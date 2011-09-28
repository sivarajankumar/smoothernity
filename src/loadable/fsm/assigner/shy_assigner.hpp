namespace shy_guts
{
    static so_called_lib_std_bool error = so_called_lib_std_false ;
}

void shy_loadable_fsm_assigner :: get_error ( so_called_lib_std_bool & arg_error )
{
    arg_error = shy_guts :: error ;
}

void shy_loadable_fsm_assigner :: prepare ( )
{
    shy_guts :: error = so_called_lib_std_false ;
}

void shy_loadable_fsm_assigner :: assign ( )
{
    so_called_loadable_fsm_content_system_container_type * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_loadable_fsm_content_system_container_type :: iterator fsm_system_i = system_container -> begin ( )
        ; fsm_system_i != system_container -> end ( )
        ; ++ fsm_system_i
        )
    {
        so_called_lib_std_string fsm_system_name = fsm_system_i -> first ;
        so_called_loadable_fsm_content_system_type & fsm_system = fsm_system_i -> second ;
        for ( so_called_loadable_fsm_content_machine_container_type :: iterator fsm_machine_i = fsm_system . machines . begin ( )
            ; fsm_machine_i != fsm_system . machines . end ( )
            ; ++ fsm_machine_i
            )
        {
            so_called_lib_std_string fsm_machine_name = fsm_machine_i -> first ;
            so_called_loadable_fsm_content_machine_type & fsm_machine = fsm_machine_i -> second ;
            if ( fsm_machine . states . find ( so_called_loadable_fsm_consts :: state_initial ) == fsm_machine . states . end ( ) )
            {
                fsm_machine . states [ so_called_loadable_fsm_consts :: state_initial ] = so_called_loadable_fsm_content_state_type ( ) ;
                so_called_trace ( so_called_trace_loadable_fsm_assigner :: no_initial_state_in_machine_of_system_error ( fsm_machine_name . c_str ( ) , fsm_system_name . c_str ( ) ) ) ;
                shy_guts :: error = so_called_lib_std_true ;
            }
        }
    }
}
