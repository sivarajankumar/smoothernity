namespace shy_guts
{
    namespace consts
    {
        static void error_no_initial_state_in_machine_of_system ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
    }

    static so_called_lib_std_string error ;
}

void shy_guts :: consts :: error_no_initial_state_in_machine_of_system ( so_called_lib_std_string & error , so_called_lib_std_string fsm_machine , so_called_lib_std_string fsm_system )
{
    error . clear ( ) ;
    error += so_called_lib_std_string ( "no state '" ) ;
    error += so_called_loadable_fsm_consts :: state_initial ;
    error += so_called_lib_std_string ( "' in fsm machine '" ) ;
    error += fsm_machine ;
    error += so_called_lib_std_string ( "' of fsm system '" ) ;
    error += fsm_system ;
    error += so_called_lib_std_string ( "'" ) ;
}

void shy_loadable_fsm_assigner :: assign ( )
{
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_type_loadable_fsm_content_system_container :: const_iterator fsm_system_i = system_container -> begin ( )
        ; fsm_system_i != system_container -> end ( )
        ; ++ fsm_system_i
        )
    {
        so_called_lib_std_string fsm_system_name = fsm_system_i -> first ;
        const so_called_type_loadable_fsm_content_system & fsm_system = fsm_system_i -> second ;
        for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator fsm_machine_i = fsm_system . machines . begin ( )
            ; fsm_machine_i != fsm_system . machines . end ( )
            ; ++ fsm_machine_i
            )
        {
            so_called_lib_std_string fsm_machine_name = fsm_machine_i -> first ;
            const so_called_type_loadable_fsm_content_machine & fsm_machine = fsm_machine_i -> second ;
            if ( fsm_machine . states . find ( so_called_loadable_fsm_consts :: state_initial ) == fsm_machine . states . end ( ) )
                shy_guts :: consts :: error_no_initial_state_in_machine_of_system ( shy_guts :: error , fsm_machine_name , fsm_system_name ) ;
        }
    }
}

void shy_loadable_fsm_assigner :: get_error ( so_called_lib_std_string & arg_error )
{
    arg_error = shy_guts :: error ;
}