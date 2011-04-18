void shy_loadable_fsm_reflection_logic_application :: prepare ( )
{
    so_called_loadable_fsm_binder :: bind_system ( "logic_application" ) ;
    
    so_called_loadable_fsm_binder :: bind_input ( "logic_amusement_created" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_amusement_finished" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_application_render" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_application_update" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_text_prepared" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_title_created" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_title_finished" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_main_menu_created" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "logic_main_menu_finished" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "stage_amusement_disabled" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "stage_amusement_enabled" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "stage_main_menu_disabled" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "stage_main_menu_enabled" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "stage_title_disabled" ) ;
    so_called_loadable_fsm_binder :: bind_input ( "stage_title_enabled" ) ;

    so_called_loadable_fsm_binder :: bind_action ( "logic_amusement_creation_permit" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_amusement_launch_permit" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_amusement_render" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_amusement_update" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_game_launch_permit" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_game_render" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_game_update" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_main_menu_creation_permit" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_main_menu_launch_permit" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_main_menu_render" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_main_menu_update" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_text_prepare_permit" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_text_update" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_title_launch_permit" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_title_render" ) ;
    so_called_loadable_fsm_binder :: bind_action ( "logic_title_update" ) ;
}
