namespace shy_guts
{
    static so_called_type_loadable_fsm_content_system * current_system = 0 ;
}

void shy_loadable_fsm_binder :: bind_system ( const so_called_std_char * name , so_called_type_loadable_fsm_content_system_binding binding )
{
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ; 
    ( * system_container ) [ name ] = so_called_type_loadable_fsm_content_system ( ) ;
    shy_guts :: current_system = & ( ( * system_container ) [ name ] ) ;
}

void shy_loadable_fsm_binder :: bind_input ( const so_called_std_char * name , so_called_type_loadable_fsm_content_input_binding binding )
{
    if ( shy_guts :: current_system )
        shy_guts :: current_system -> inputs [ name ] = binding ;
}

void shy_loadable_fsm_binder :: bind_action ( const so_called_std_char * name , so_called_type_loadable_fsm_content_action_binding binding )
{
    if ( shy_guts :: current_system )
        shy_guts :: current_system -> actions [ name ] = binding ;
}
