namespace shy_guts
{
    static so_called_loadable_fsm_behaviour < so_called_common_logic_application_fsm_inputs_type > behaviour ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: determine_behaviour_inputs_change ( so_called_platform_math_num_whole_type & result )
{
    shy_guts :: behaviour . determine_behaviour_inputs_change ( result ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: init ( )
{
    shy_guts :: behaviour . set_system_binding ( so_called_common_logic_application_fsm_binding ) ;
    shy_guts :: behaviour . init ( ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: is_fsm_running ( so_called_platform_math_num_whole_type & result )
{
    shy_guts :: behaviour . is_fsm_running ( result ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: recalc_current_behaviour_inputs ( )
{
    shy_guts :: behaviour . recalc_current_behaviour_inputs ( ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: reset_behaviour_input_events ( )
{
    shy_guts :: behaviour . reset_behaviour_input_events ( ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: run_fsm_begin ( )
{
    shy_guts :: behaviour . run_fsm_begin ( ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: run_fsm_end ( )
{
    shy_guts :: behaviour . run_fsm_end ( ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: set_inputs 
    ( so_called_platform_pointer_data_type < so_called_common_logic_application_fsm_inputs_type > inputs_current
    , so_called_platform_pointer_data_type < so_called_common_logic_application_fsm_inputs_type > inputs_fixed
    )
{
    shy_guts :: behaviour . set_inputs ( inputs_current , inputs_fixed ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: tick_all_fsms ( )
{
    shy_guts :: behaviour . tick_all_fsms ( ) ;
}

void shy_common_logic_application_fsm_behaviour_loadable :: update_fixed_behaviour_inputs ( )
{
    shy_guts :: behaviour . update_fixed_behaviour_inputs ( ) ;
}

